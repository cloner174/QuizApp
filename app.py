import sqlite3
import random
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session
from config import Config
from questions_and_answers import questions


app = Flask(__name__)
app.config.from_object(Config)


def get_db_connection():
    try:
        conn = sqlite3.connect(app.config['DATABASE'])
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        app.logger.error(f'Database connection error: {e}')
        return None


def init_db():
    conn = get_db_connection()
    if conn:
        with app.open_resource('schema.sql') as f:
            conn.executescript(f.read().decode('utf8'))
        conn.close()


@app.route('/', methods=['GET', 'POST'])
def quiz_form():
    if 'score' in session:
        return redirect(url_for('result_already_submitted'))
    if request.method == 'POST':
        session.clear()
        session['name'] = request.form['name']
        session['email'] = request.form['email']
        session['difficulty'] = request.form['difficulty']
        return redirect(url_for('quiz'))
    return render_template('quiz_form.html')


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if 'score' in session:
        return redirect(url_for('result_already_submitted'))
    if 'name' not in session:
        return redirect(url_for('quiz_form'))
    if request.method == 'POST':
        session['answers'] = request.form.to_dict()
        return redirect(url_for('submit'))
    difficulty = session['difficulty'].lower()
    filtered_questions = [q for q in questions if q['difficulty'] == difficulty]
    # Ensure there are enough questions
    num_questions = min(10, len(filtered_questions))
    session['quiz_questions'] = random.sample(filtered_questions, num_questions)
    return render_template('quiz.html', questions=session['quiz_questions'])


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if 'answers' not in session:
        return redirect(url_for('quiz'))
    user_answers = session['answers']
    correct = 0
    wrong_answers = []
    for q in session['quiz_questions']:
        qid = str(q['id'])
        if user_answers.get(qid) == q['answer']:
            correct += 1
        else:
            wrong_answers.append({
                'question': q['question'],
                'code_snippet': q.get('code_snippet'),
                'options': q['options'],
                'your_answer': user_answers.get(qid),
                'correct_answer': q['answer']
            })
    score = correct
    conn = get_db_connection()
    if conn:
        conn.execute(
            'INSERT INTO scores (name, email, score, difficulty, timestamp) VALUES (?, ?, ?, ?, ?)',
            (session['name'], session['email'], score, session['difficulty'], datetime.now())
        )
        conn.commit()
        conn.close()
    session['score'] = score
    session['total'] = len(session['quiz_questions'])
    session['wrong_answers'] = wrong_answers
    return render_template('result.html', score=score, total=session['total'])


@app.route('/leaderboard')
def leaderboard():
    conn = get_db_connection()
    if conn:
        scores = conn.execute(
            'SELECT * FROM scores ORDER BY score DESC, timestamp ASC LIMIT 10'
        ).fetchall()
        conn.close()
    else:
        scores = []
    return render_template('leaderboard.html', scores=scores)


@app.route('/wrong_answers')
def wrong_answers():
    if 'wrong_answers' not in session:
        return redirect(url_for('quiz_form'))
    return render_template('wrong_answers.html', wrong_answers=session['wrong_answers'])


@app.route('/result_already_submitted')
def result_already_submitted():
    return render_template('result_already_submitted.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error_code=404, error_message='Page Not Found'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html', error_code=500, error_message='Internal Server Error'), 500


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
    
#cloner174