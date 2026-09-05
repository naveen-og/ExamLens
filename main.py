from pathlib import Path

questions = []

papers_folder = Path("papers")

for paper in papers_folder.glob("*.txt"):
    with open(paper) as file:
        for lines in file:
            question = lines.strip()
            if question:
                questions.append(question)

shown_questions = []

for question in questions:
    if question not in shown_questions:
        count = questions.count(question)
        print(f"{question} --> {count}")
        shown_questions.append(question)

total_questions = 0
print(questions)
for question in questions:
    count = questions.count(question)
    total_questions += count

print(total_questions)
