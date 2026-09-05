import string

def normalise_question(question):
    question = question.strip().lower()

    for punctuation in string.punctuation:
        question = question.replace(punctuation, "")

    question = " ".join(question.split())

    return question
