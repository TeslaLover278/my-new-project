from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data for teachers
teachers = [
    {'name': 'Teacher A', 'photo': 'teacher_a.jpg', 'bio': 'Teacher A is passionate about science and loves to experiment.', 'rating': 0, 'votes': 0},
    {'name': 'Teacher B', 'photo': 'teacher_b.jpg', 'bio': 'Teacher B excels in mathematics and makes complex concepts easy to understand.', 'rating': 0, 'votes': 0},
    {'name': 'Teacher C', 'photo': 'teacher_c.jpg', 'bio': 'Teacher C has a deep knowledge of history and brings the past to life in class.', 'rating': 0, 'votes': 0}
]

@app.route('/')
def home():
    return render_template('index.html', teachers=teachers)

@app.route('/vote/<teacher_name>', methods=['GET', 'POST'])
def vote(teacher_name):
    teacher = next((teacher for teacher in teachers if teacher['name'] == teacher_name), None)
    if request.method == 'POST' and teacher:
        rating = int(request.form['rating'])
        teacher['rating'] = (teacher['rating'] * teacher['votes'] + rating) / (teacher['votes'] + 1)
        teacher['votes'] += 1
        return redirect(url_for('home'))
    return render_template('vote.html', teacher=teacher)

@app.route('/results')
def results():
    sorted_teachers = sorted(teachers, key=lambda x: (x['rating'], x['votes']), reverse=True)
    return render_template('results.html', teachers=sorted_teachers)

if __name__ == '__main__':
    app.run(debug=True)
