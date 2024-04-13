from flask import Flask, render_template, Response, request, jsonify

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

data = []
current_id = 11

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/learn')
def learn():
    return render_template('learn.html')

@app.route('/game')
def game():
    return render_template('game.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)

