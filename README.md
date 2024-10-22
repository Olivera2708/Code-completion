# Code Completion Example Generation and Evaluation

This project demonstrates how I generated a dataset of code completion examples from a personal repository, evaluated an open-source code completion model, and analyzed the model's predictions against actual code.

## Project Overview

The main objectives of this project were to:

1. **Generate a dataset** of code completion examples by splitting code into three parts: 
   - **Prefix**: Code before the cursor.
   - **Middle**: Code that should be typed next (missing code).
   - **Suffix**: Code after the cursor.

2. **Run a code completion model** (`tiny_starcoder`) on the generated examples to obtain the model's completions.

3. **Manually review and analyze** the differences between the model's predicted completions and the actual missing code.

4. **Evaluate the model's quality** using both automatic metrics and manual labeling.

## Dataset Generation

I wrote a script to generate code completion examples by splitting Python files from one of my repositories into three parts simulating a user's cursor position:

- **Prefix**: The code before the cursor.
- **Middle**: The code that is missing and assumed to be typed next.
- **Suffix**: The code after the cursor.

The script generated examples by selecting random positions within the code files. This created realistic scenarios for code completion.

## Model Evaluation

I used the open-source `tiny_starcoder` model to generate code completions for each example. The model predicted the **middle** part of the code, while the **prefix** and **suffix** were provided as context.

### Manual Review

After running the model on the dataset, I manually reviewed the generated completions and assigned labels based on the following criteria:
- **Correct**: The generated code matched the expected missing code.
- **Partially Correct**: The generated code was close, but contained errors or inaccuracies.
- **Incorrect**: The generated code was wrong or irrelevant.
- **Runnable**: The generated code could be executed without errors.
- **Not Runnable**: The generated code would fail if executed.

This manual review provided a deeper understanding of common model errors, such as incorrect indentation, over-generation of code, or unnecessary empty lines.

## Automatic Metrics

To complement manual labeling, I calculated the following metrics to evaluate the model's performance:

1. **Exact Match**: Measures whether the model's generated code matches the actual missing code exactly.
2. **chrF (Character F-score)**: A metric based on character-level n-grams that balances precision and recall.
3. **Levenshtein Distance**: Measures the number of edits (insertions, deletions, substitutions) needed to transform the model's output into the correct code.
4. **Token Match**: Compares token-level matches between the model's predictions and the actual missing code.
5. **Runnable Metric**: Evaluates whether the generated code is syntactically correct and can be executed without errors.

## Results

- **Top Performers**: The model performed well in cases where the missing code was simple and directly predictable from the context.
- **Common Mistakes**: The most frequent mistakes involved incorrect indentation, generating too much code, and unnecessary empty lines.

## How to Run

To reproduce this project, you can clone this repository, but I suggest using the provided [notebook](https://github.com/Olivera2708/Code-completion/blob/main/AI_Code_Completion.ipynb). It contains all relevant code with detailed descriptions and explains the thought process behind each step.