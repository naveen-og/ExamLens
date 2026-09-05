# ExamLens

ExamLens is a Python project that analyses past exam questions to find repeated and important questions.

The long-term goal is to build an AI/ML-powered study tool that can analyse many past papers, identify recurring topics, group similar questions, and help students focus on the concepts that appear most often.

## Current Features

At the moment, ExamLens can:

- Read questions from a text file
- Store questions in Python
- Ignore empty lines
- Count how many times each question appears
- Detect exact repeated questions

## Example

Input:

```text
What is photosynthesis?
Explain Ohm's Law.
What is photosynthesis?
Define refraction.
```

Output:

```text
What is photosynthesis? -> 2
Explain Ohm's law. -> 1
Define refraction. -> 1
```

## Why I am Building This

Students often have many years of past exam papers but no easy way to understand which questions and topics appear repeatedly

ExamLens aims to automatically analyse those papers and answer questions such as:

- Whcih questions are repeated the most?
- Which topics appear most frequently?
- Which chapters are the most important?
- Which questions are worded differently but test the same concept?
- What shuold a student prioritize while revising?

## Planned Features

### Stage 1 

- Read questions from text files
- Detect exact duplicate questions
- Count question frequency

### Stage 2

- Automatically read multiple exam papers from a folder
- Clean and normalize question text
- Improve question frequency analysis


Thats it for now!
