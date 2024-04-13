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

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

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


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)

