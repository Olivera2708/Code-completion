import json


with open("data.json", 'r') as file:
    data = json.load(file)

with open("results.json", 'r') as file:
    results = json.load(file)

for i, example in enumerate(data):
    input = example["input"].replace("<fim_prefix>", "").replace("<fim_middle>", "").replace("<fim_suffix>", "MISSING\n")
    print(f"----- Example {i+1} -----\n")
    print(input)
    print(f"--- Generated ---\n")
    print(results[i]["generated"])
    print(f"---  Correct  ---\n")
    print(results[i]["correct"])
    print()