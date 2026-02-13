def generate_quiz(summary):
    sentences = summary.split(".")
    quiz = []

    for s in sentences[:5]:
        if len(s) > 40:
            quiz.append(f"What is meant by: {s.strip()}?")

    return quiz
