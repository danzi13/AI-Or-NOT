from flask import Flask, render_template, Response, request, jsonify

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

data = [
    {"id": 0, "Title": "Background Information", "Description": "Check for inconsistencies or blending of various backgrounds that might appear unnatural or out of place", "image_path": "learn1"},
    {"id": 1, "Title": "Repeating Items", "Description": "Identify any duplicated or cloned objects within the image that may indicate a lack of diversity or organic variation.", "image_path": "learn2"},
    {"id": 2, "Title": "Weird Fingers", "Description": "Weird Fingers: Pay attention to the appearance of fingers, they typically do not have realistic anatomy and appropriate proportions.", "image_path": "learn3"},
    {"id": 3, "Title": "Smooth Skin", "Description": " Assess the skin texture for any overly smooth or artificial appearance, which could indicate excessive manipulation or synthesis.", "image_path": "learn4"},
    {"id": 4, "Title": "Garbled Text", "Description": " Jumbled Text: Look for any nonsensical or randomly placed text within the image that doesn't fit with the overall context.", "image_path": "learn5"},
    {"id": 5, "Title": "Helpful tip!: Zoom in", "Description": "Zooming in allows for a closer inspection of details, revealing potential flaws or inconsistencies that may not be immediately apparent at first glance.", "image_path": "learn6"}
]

quiz_data = [
    {"id": 0, "Question": "Is this image real or AI?", "choice":[{"option":"A","selection":"AI"},{"option":"B","selection":"Real"}], "image_path": "quiz1"},
    {"id": 1, "Question": "Is this image real or AI?", "choice":[{"option":"A","selection":"AI"},{"option":"B","selection":"Real"}], "image_path": "quiz2"}, 
    {"id": 2, "Question": "When analyzing an image for AI-generated elements, what might indicate its artificial origin?", "choice":[{"option":"A","selection":"Seamless blending of foreground and background"},{"option":"B","selection":"Anomalous placement or duplication of objects"}, {"option":"C","selection":"Highly detailed textures with no imperfections"}]}, 
    {"id": 3, "Question": "Which of the following characteristics might suggest an AI-generated image?", "choice":[{"option":"A","selection":"Perfectly aligned shadows and lighting"},{"option":"B","selection":"Imperfect symmetry and irregular patterns"}, {"option":"C","selection":"Inconsistent color saturation"}]}, 
    {"id": 4, "Question": "When examining an AI-generated image for inconsistencies, which specific body part is often scrutinized for anomalies?", "choice":[{"option":"A","selection":"Fingers"},{"option":"B","selection":"Eyes"}, {"option":"C","selection":"Feet"}]},
    {"id": 5, "Question": "In AI-generated images, what visual trait might suggest the use of artificial intelligence when it comes to depicting skin?", "choice":[{"option":"A","selection":"Fine wrinkles and imperfections"},{"option":"B","selection":"Uniform texture and lack of pores"}, {"option":"C","selection":"Variable shading and lighting effects"}]},
    {"id": 6, "Question": "Which image is AI?", "choice":[{"option":"A","selection":"Left"},{"option":"B","selection":"Right"}], "image_path": "quiz3"},
    {"id": 7, "Question": "Which image is AI?", "choice":[{"option":"A","selection":"Left"},{"option":"B","selection":"Right"}], "image_path": "quiz4"},
    {"id": 8, "Question": "Is this image real of AI?", "choice":[{"option":"A","selection":"Real"},{"option":"B","selection":"AI"}], "image_path": "quiz5"}

]

correct_answers = [
    {"id":0, "answer": "B"},
    {"id":1, "answer": "A"},
    {"id":2, "answer": "B"},
    {"id":3, "answer": "B"},
    {"id":4, "answer": "A"},
    {"id":5, "answer": "B"},
    {"id":6, "answer": "A"},
    {"id":7, "answer": "B"},
    {"id":8, "answer": "B"},
]

user_answers = [
    {"id":0, "answer": ""},
    {"id":1, "answer": ""},
    {"id":2, "answer": ""},
    {"id":3, "answer": ""},
    {"id":4, "answer": ""},
    {"id":5, "answer": ""},
    {"id":6, "answer": ""},
    {"id":7, "answer": ""},
    {"id":8, "answer": ""},
]

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/learn/<int:id>')
def learn(id):
    global data
    item = get_item_by_id(id)
    prev_id = (id - 1) % len(data)  
    next_id = (id + 1) % len(data) 
    return render_template('learn.html', item=item, prev_id=prev_id, next_id=next_id)

def get_item_by_id(id):
    for item in data:
        if item["id"] == id:
            return item
    return None

@app.route('/quiz/<int:id>', methods=['GET', 'POST'])
def quiz(id):
    global quiz_data
    global user_answers
    
    # Handle POST request to update user's answer
    if request.method == 'POST':
        user_answer = request.form.get('answer')
        user_answers[id]['answer'] = user_answer
    
    item = get_item_by_i(id)
    prev_id = (id - 1) % len(quiz_data)
    next_id = (id + 1) % len(quiz_data)

    if next_id == 0:
        # Calculate the score
        score = calculate_score(user_answers)
        # Redirect to the score page with the calculated score
        return render_template('score.html', score=score)
    
    return render_template('quiz.html', item=item, prev_id=prev_id, next_id=next_id)


def get_item_by_i(id):
    for item in quiz_data:
        if item["id"] == id:
            return item
    return None

def calculate_score(user_answers):
    total_questions = len(user_answers)
    correct_answers_count = 0
    for user_answer in user_answers:
        if user_answer.get('userA') == correct_answers[user_answer.get('id')]:
            correct_answers_count += 1
    percentage_score = (correct_answers_count / total_questions) * 100
    return percentage_score


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)

