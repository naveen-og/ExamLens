from pathlib import Path
from text_utils import normalise_question

questions = []

papers_folder = Path("papers")

for paper in papers_folder.glob("*.txt"):
    with open(paper) as file:
        for line in file:
            question = normalise_question(line)
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
