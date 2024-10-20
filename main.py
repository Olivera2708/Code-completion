from transformers import AutoModelForCausalLM, AutoTokenizer
import json

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
    results.append({
        "correct": output,
        "generated": generated_output[start:end]
    })

    if output == generated_output[start:end]:
        correct_full += 1

with open("results.json", 'w') as file:
        json.dump(results, file, indent=4)

print(f"Accuracy full -> {correct_full/len(data)*100}")
