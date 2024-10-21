from transformers import AutoModelForCausalLM, AutoTokenizer
import sacrebleu
import Levenshtein
import json


def token_match(pred, target):
    pred_tokens = set(pred.split())
    target_tokens = set(target.split())
    return len(pred_tokens & target_tokens) / len(target_tokens) if target_tokens else 0

def is_runnable(code):
    try:
        exec(code)
        return True
    except Exception as e:
        return False


checkpoint = "bigcode/tiny_starcoder_py"
device = "cuda"

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint).to(device)

params = {
    'max_new_tokens': 30
}

with open("data.json", 'r') as file:
    data = json.load(file)

correct_full = 0
results = []

for i, element in enumerate(data):
    input = element["input"]
    output = element["output"]

    inputs = tokenizer.encode(input, return_tensors="pt").to(device)
    outputs = model.generate(inputs, pad_token_id=tokenizer.eos_token_id, **params)
    generated_output = tokenizer.decode(outputs[0])

    start = generated_output.find("<fim_middle>") + len("<fim_middle>")
    end = generated_output.find("<|endoftext|>")

    generated = generated_output[start:end]
    code = input.replace("<fim_prefix>", "").replace("<fim_suffix>", generated).replace("<fim_middle>", "")

    results.append({
        "correct": output,
        "generated": generated,
        "exact match": output == generated,
        "chrf": sacrebleu.corpus_chrf([generated], [[output]]).score,
        "levenshtein": Levenshtein.distance(generated, output),
        "token match": token_match(generated, output),
        "runnable": is_runnable(code)
    })

    if output == generated_output[start:end]:
        correct_full += 1

with open("results_generated.json", 'w') as file:
        json.dump(results, file, indent=4)

print(f"Exact matches -> {correct_full} out of {len(data)}")
