import json
import os
import random


def tokenize(code):
    lines = [line for line in code.splitlines(keepends=True) if line.replace("\n", "").replace("\t", "").strip() != ""]
    return lines

def split_code(lines):
    cursor = random.randint(1, len(lines)-3)
    middle_length = random.randint(1, 1)

    prefix = ""
    for val in lines[:cursor]:
        prefix += val
    suffix = ""
    for val in lines[cursor+middle_length:]:
        suffix += val
    middle = ""
    for val in lines[cursor]:
        middle += val

    return prefix, suffix, middle

def generate(directory_path):
    data = []
    for counter, filename in enumerate(os.listdir(directory_path)):
        if counter == 50:
            break
        file_path = os.path.join(directory_path, filename)
        with open(file_path, 'r') as file:
            code = file.read()
            lines = tokenize(code)
            prefix, suffix, middle = split_code(lines)
            data.append({
                "input": f"<fim_prefix>{prefix}<fim_suffix>{suffix}<fim_middle>",
                "output": middle
                })

    with open("data.json", 'w') as json_file:
        json.dump(data, json_file, indent=4)

generate("data")