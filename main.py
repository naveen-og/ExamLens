
## This is a list assigned to a variable called questions, this list stores the available questions
questions = []
## The below line opens the file paper1.txt in the folder named papers, and stores the data in the file as a variable named file.
#
with open("papers/paper1.txt") as file:
    for line in file: # for each line in the file
        question = line.strip() # question is assigned to the line stripped of extra lines and spaces
## if question exists! meaning that the paper1.txt isnt empty then the if block runs
        if question:
            questions.append(question)
## the if block appends the questions list according to the variable question
shown_questions = []
# new variable named shown_questions = []
for question in questions:
    if question not in shown_questions:
        count = questions.count(question)

        print(f"{question} --> {count}")

        shown_questions.append(question)
