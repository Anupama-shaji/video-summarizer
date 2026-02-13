from flask import Flask, render_template, request

app = Flask(__name__)

# Sample quiz questions
quiz_questions = [
    {
        "question": "What does AI stand for?",
        "options": ["Artificial Intelligence", "Automated Internet", "Active Input"],
        "answer": "Artificial Intelligence"
    },
    {
        "question": "Which language is used for AI?",
        "options": ["Python", "HTML", "CSS"],
        "answer": "Python"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5"],
        "answer": "4"
    }
]

# ------------------ ROUTES ------------------

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/summarize", methods=["POST"])
def summarize():
    youtube_link = request.form.get("youtube_link")

    # Temporary placeholder summary
    summary = f"This is a generated summary for the video: {youtube_link}"

    key_points = [
    "Concepts are explained step-by-step",
    "Examples help in better understanding",
    "Important formula: F = m × a",
    "Useful for quick revision"
]


    # Extract video ID for embedding
    import re
    match = re.search(r"(?:v=|youtu\.be/)([\w-]+)", youtube_link)
    video_id = match.group(1) if match else ""

    
    return render_template("summary.html", summary=summary, video_id=video_id,key_points=key_points)

@app.route("/quiz")
def quiz():
    # Send indexed quiz to template
    indexed_quiz = list(enumerate(quiz_questions))
    return render_template("quiz.html", quiz=indexed_quiz)

@app.route("/submit_quiz", methods=["POST"])
def submit_quiz():
    user_answers = request.form
    score = 0
    results = []

    for i, q in enumerate(quiz_questions):
        user_ans = user_answers.get(f"q{i}")
        correct_ans = q["answer"]
        is_correct = user_ans == correct_ans
        if is_correct:
            score += 1

        results.append({
            "question": q["question"],
            "selected": user_ans,
            "correct": correct_ans,
            "is_correct": is_correct
        })

    total = len(quiz_questions)
    return render_template("score.html", results=results, score=score, total=total)

# ------------------ MAIN ------------------
if __name__ == "__main__":
    app.run(debug=True)