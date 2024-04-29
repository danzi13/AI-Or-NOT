from flask import Flask, render_template, Response, request, jsonify
from datetime import datetime

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
    {"id":0, "answer": "B", "reason":"This is real beacuse there are no repeated items, inconsitencies in background, weird fingers, or seemingly perfect skin or hair."},
    {"id":1, "answer": "A", "reason":"This is fake because the finger are very off/odd"},
    {"id":2, "answer": "B", "reason":"AI generated images have trouble blending foreground and background and also highly detailed textures is not necessarily indicative of AI gen images. So, duplication of objects is the correct answer as AI gen images lack diversity/organic variation."},
    {"id":3, "answer": "B", "reason":"As like weird fingers, AI images generate things with imperfect symmetry and irregular patterns. Nothing was ever disccussed about lighting/shadows or color saturation."},
    {"id":4, "answer": "A", "reason":"Fingers are often miss generated as they typically do not have realistic anatomy and appropriate proportions. Neither eyes nor feet were discussed about."},
    {"id":5, "answer": "B", "reason":"Uniform texture and lack of pores is the same as smooth skin that is indicative of excessive manipulation or synthesis."},
    {"id":6, "answer": "A", "reason":"The left images lack diversity and has visible repitition with two orange and two yellow fish and also has trouble blending foreground and background"},
    {"id":7, "answer": "B", "reason":"The right image visible duplicates/repeats the archway multiple times over seemingly perfectly which is strongly indicative of AI generation"}
]

user_answers = [
    {"id":0, "answer": ""},
    {"id":1, "answer": ""},
    {"id":2, "answer": ""},
    {"id":3, "answer": ""},
    {"id":4, "answer": ""},
    {"id":5, "answer": ""},
    {"id":6, "answer": ""},
    {"id":7, "answer": ""}
]

learn_amt = [
    {"id":0, "times_visited": 0},
    {"id":1, "times_visited": 0},
    {"id":2, "times_visited": 0},
    {"id":3, "times_visited": 0},
    {"id":4, "times_visited": 0},
    {"id":5, "times_visited": 0}
]

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/quiz_home')
def quiz_home():
    print(learn_amt)
    return render_template('quiz_home.html')

@app.route('/learn/<int:id>')
def learn(id):
    global data
    global learn_amt
    learn_amt[id]['times_visited'] += 1
    item = get_item_by_id(id)
    prev_id = (id - 1)
    next_id = (id + 1)
    if (item["id"] == len(data)-1):
        return render_template('learn.html', item=item, prev_id=prev_id, next_id=next_id, quiz_time = True)
    return render_template('learn.html', item=item, prev_id=prev_id, next_id=next_id, quiz_time = False)

def get_item_by_id(id):
    for item in data:
        if item["id"] == id:
            return item
    return None

@app.route('/update_userans', methods=['POST'])
def update_variable():
    global user_answers
    data = request.get_json()
    user_answers = data.get('user_answers')
    return jsonify({'message': 'Variable updated on the server.'})

@app.route('/quiz/<int:id>', methods=['GET'])
def quiz(id):
    global quiz_data
    global user_answers

    item = get_item_by_i(id)
    next_id = (id + 1) % len(quiz_data)

    if next_id == 0:
        # Calculate the score
        score = calculate_score(user_answers)
        # Redirect to the score page with the calculated score
        return render_template('score.html', score=score)
    
    return render_template('quiz.html', item=item, next_id=next_id, correct_answers=correct_answers, user_answers=user_answers)

def get_item_by_i(id):
    for item in quiz_data:
        if item["id"] == id:
            return item
    return None

def calculate_score(user_answers):
    total_questions = len(user_answers) 
    correct_answers_count = 0


    for i in range(total_questions):

        if user_answers[i].get('answer') == correct_answers[i]['answer']:
            correct_answers_count += 1

    percentage_score = (correct_answers_count / (total_questions - 1)) * 100
    return percentage_score

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)

