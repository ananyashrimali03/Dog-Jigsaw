from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests
import json
import os

app = Flask(__name__)

# Dog API base URL (Template: Claude Opus 4.6)
DOG_API_URL = "https://dog.ceo/api"

FAVORITES_FILE = os.path.join(os.path.dirname(__file__), 'favorites.json')
SCORE_FILE = os.path.join(os.path.dirname(__file__), 'score.json')

def load_score():
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, 'r') as f:
            return json.load(f)
    return {'puzzles_solved': 0, 'total_points': 0}

def save_score(score):
    with open(SCORE_FILE, 'w') as f:
        json.dump(score, f)

def load_favorites():
    if os.path.exists(FAVORITES_FILE):
        with open(FAVORITES_FILE, 'r') as f:
            return json.load(f)
    return []

def save_favorites(favorites):
    with open(FAVORITES_FILE, 'w') as f:
        json.dump(favorites, f)

def get_all_breeds():
    """Fetch all available dog breeds from the API"""
    response = requests.get(f"{DOG_API_URL}/breeds/list/all")
    if response.status_code == 200:
        breeds_data = response.json()
        return breeds_data['message']
    return {}

def get_random_dog_image(breed=None):
    """Fetch a random dog image, optionally by breed"""
    if breed:
        url = f"{DOG_API_URL}/breed/{breed}/images/random"
    else:
        url = f"{DOG_API_URL}/breeds/image/random"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['message']
    return None

@app.route('/')
def home():
    """Main page - shows a random dog image"""
    breeds = get_all_breeds()
    selected_breed = request.args.get('breed', '')

    if selected_breed:
        dog_image = get_random_dog_image(selected_breed)
    else:
        dog_image = get_random_dog_image()

    return render_template('index.html',
                         dog_image=dog_image,
                         breeds=breeds,
                         selected_breed=selected_breed,
                         favorites_count=len(load_favorites()),
                         score=load_score())

@app.route('/favorite', methods=['POST'])
def add_favorite():
    image_url = request.form.get('image_url')
    breed = request.form.get('breed', '')
    favorites = load_favorites()
    if image_url and not any(f['url'] == image_url for f in favorites):
        favorites.append({'url': image_url, 'breed': breed})
        save_favorites(favorites)
    return redirect(request.form.get('next', url_for('home')))

@app.route('/favorite/remove', methods=['POST'])
def remove_favorite():
    image_url = request.form.get('image_url')
    favorites = load_favorites()
    favorites = [f for f in favorites if f['url'] != image_url]
    save_favorites(favorites)
    return redirect(request.form.get('next', url_for('favorites')))

@app.route('/favorites')
def favorites():
    fav_list = load_favorites()
    return render_template('favorites.html', favorites=fav_list, score=load_score())

@app.route('/puzzle')
def puzzle():
    image_url = request.args.get('image_url', '')
    score = load_score()
    return render_template('puzzle.html', image_url=image_url, score=score)

@app.route('/puzzle/solved', methods=['POST'])
def puzzle_solved():
    moves = request.json.get('moves', 0)
    # Fewer moves = more points (max 100 for 0 extra moves on a 3x3) (Updates: Claude Opus 4.6)
    points = max(10, 100 - (moves * 5))
    score = load_score()
    score['puzzles_solved'] += 1
    score['total_points'] += points
    save_score(score)
    return jsonify({'points_earned': points, 'total_points': score['total_points'], 'puzzles_solved': score['puzzles_solved']})

if __name__ == '__main__':
    app.run(debug=True)
# (All updates: Claude Opus 4.6, no manual coding, debugging)