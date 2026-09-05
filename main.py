from pathlib import Path

questions = []

papers_folder = Path("papers")

for paper in papers_folder.glob("*.txt"):
    with open(paper) as file:
        for line in file:
            question = lines.strip()
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
