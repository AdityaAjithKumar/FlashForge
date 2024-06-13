from flask import Flask, render_template, request, redirect, url_for
import google.generativeai as genai
import os
import json

app = Flask(__name__)

# Configure the Gemini API
API_KEY = "AIzaSyB2sxsKb7ZiiLWlRIImu_wBJxy2ZvrsQus"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def get_quiz(topic, num_questions):
    response = model.generate_content(f"""
    You are an API. Your work is to make quizzes about various {topic}. Remember, you can only answer in the given format and you can't talk. If you talk, the app crashes. Give your response in this format only:
    dont add json or ``` in the answer.
    {{
        "title": "Python Programming Quiz",
        "questions": [
            {{
                "question": "What is the keyword to define a function in Python?",
                "options": ["def", "function", "fun", "define"],
                "answer": "def"
            }},
            {{
                "question": "What does the 'len' function do in Python?",
                "options": ["Returns the length of an object", "Converts a string to lowercase", "Sorts the elements of a list", "None of the above"],
                "answer": "Returns the length of an object"
            }}
            # Add more questions as needed
        ]
    }}
    """)

    print(response.text)

    # Parse the JSON response
    quiz = json.loads(response.text)
    return quiz

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        topic = request.form['topic']
        num_questions = int(request.form['num_questions'])
        quiz = get_quiz(topic, num_questions)
        return render_template('quiz.html', quiz=quiz, enumerate=enumerate)
    return redirect(url_for('index'))

@app.route('/submit', methods=['POST'])
def submit():
    topic = request.form['topic']
    num_questions = int(request.form['num_questions'])
    quiz = get_quiz(topic, num_questions)
    user_answers = {key: value for key, value in request.form.items() if key.startswith('q')}
    correct_answers = {f"q{i}": q["answer"] for i, q in enumerate(quiz["questions"])}
    score = sum(1 for i in range(len(quiz["questions"])) if user_answers.get(f"q{i}") == correct_answers[f"q{i}"])
    return render_template('result.html', score=score, total=len(quiz["questions"]))

if __name__ == '__main__':
    app.run(debug=True)