# Dog Jigsaw (Template: Claude Opus 4.6)

A Flask web app that lets you browse random dog photos, save your favorites, and solve jigsaw puzzles made from them.

## Features (Updates: Claude Opus 4.6)

- **Browse Dogs** — View random dog images from the [Dog CEO API](https://dog.ceo/dog-api/), optionally filtered by breed
- **Save Favorites** — Star photos to add them to your favorites collection
- **Jigsaw Puzzles** — Play a 3x3 tile-swap puzzle using any favorited photo
- **Score Tracking** — Earn points for solving puzzles (fewer moves = more points), tracked across sessions

## How to Run (Updates: Claude Opus 4.6)

1. Install the required packages:
```bash
pip install -r requirements.txt
```

2. Run the app:
```bash
python app.py
```

3. Open your browser and go to:
```
http://127.0.0.1:5000
```

## Project Structure 

```
app.py              # Flask routes and API logic
favorites.json      # Saved favorite images (auto-created)
score.json          # Puzzle score data (auto-created)
requirements.txt    # Python dependencies
templates/
  index.html        # Home page - browse and star dogs
  favorites.html    # Favorites gallery with puzzle links
  puzzle.html       # Jigsaw puzzle game
```

## How It Works

- Browse random dog images on the home page, filter by breed with the dropdown
- Click the star button to save a photo to your favorites
- Go to Favorites and click the puzzle icon on any saved photo to play a jigsaw puzzle
- Swap tiles by clicking two of them — solve the puzzle to earn points
- Fewer moves = more points (max 100, min 10 per puzzle)
- Your total score is shown in the nav bar across all pages

## API Details (Updates: Claude Opus 4.6)

This app uses the free [Dog CEO API](https://dog.ceo/dog-api/). API calls are made using Python's `requests` module via simple GET requests to `https://dog.ceo/api`. The two main endpoints used are `/breeds/list/all` (returns a JSON object mapping breed names to sub-breed arrays) and `/breed/{breed}/images/random` (returns a JSON object with a `message` field containing a single image URL string and a `status` field). All responses are JSON with a 200 status code on success. No API key or authentication is required — the API is completely open and free to use.

## Prompt Log (Updates: Claude Opus 4.6)

See [PROMPT_HISTORY.txt](PROMPT_HISTORY.txt) for the AI prompts used during development.
