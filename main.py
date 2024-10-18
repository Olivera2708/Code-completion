from transformers import AutoModelForCausalLM, AutoTokenizer
import json

checkpoint = "bigcode/tiny_starcoder_py"
device = "cuda"

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint).to(device)

params = {
    'max_new_tokens': 50
}

with open("data.json", 'r') as file:
    data = json.load(file)

correct_full = 0

for i, element in enumerate(data):
    input = element["input"]
    output = element["output"]

    inputs = tokenizer.encode(input, return_tensors="pt").to(device)
    outputs = model.generate(inputs, pad_token_id=tokenizer.eos_token_id, **params)
    generated_output = tokenizer.decode(outputs[0])

    start = generated_output.find("<fim_middle>") + len("<fim_middle>")
    end = generated_output.find("<|endoftext|>")
    print(f"--- Example {i} ---")
    print(f"Correct -> {output}")
    print(f"Model generated -> {generated_output[start:end]}")

    if output == generated_output[start:end]:
        correct_full += 1

print(f"Accuracy full -> {correct_full/i*100}")
