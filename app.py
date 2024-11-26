from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data for teachers
teachers = [
    {'name': 'Teacher A', 'rating': 0, 'votes': 0},
    {'name': 'Teacher B', 'rating': 0, 'votes': 0},
    {'name': 'Teacher C', 'rating': 0, 'votes': 0}
]

@app.route('/')
def home():
    return render_template('index.html', teachers=teachers)

@app.route('/vote/<teacher_name>', methods=['GET', 'POST'])
def vote(teacher_name):
    if request.method == 'POST':
        rating = int(request.form['rating'])
        for teacher in teachers:
            if teacher['name'] == teacher_name:
                teacher['rating'] = (teacher['rating'] * teacher['votes'] + rating) / (teacher['votes'] + 1)
                teacher['votes'] += 1
        return redirect(url_for('home'))
    return render_template('vote.html', teacher_name=teacher_name)

@app.route('/results')
def results():
    return render_template('results.html', teachers=teachers)

if __name__ == '__main__':
    app.run(debug=True)
