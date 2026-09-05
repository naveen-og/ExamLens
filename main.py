from pathlib import Path
import string

questions = []

papers_folder = Path("papers")

for paper in papers_folder.glob("*.txt"):
    with open(paper) as file:
        for line in file:
            question = line.lower().strip()
            for punctuation in string.punctuation:
                question = question.replace(punctuation, "")
            if question:
                questions.append(question)

shown_questions = []

for question in questions:
    if question not in shown_questions:
        count = questions.count(question)
        print(f"{question} --> {count}")
        shown_questions.append(question)

total_questions = len(questions)

print(f"\nTotal questions: {total_questions}")
