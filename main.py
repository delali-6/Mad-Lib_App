import re
import secrets
import string
import time
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from stories import STORIES

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)

# ── Story helpers ────────────────────────────────────────────────────────────

FEATURED_IDS = {1, 2, 3, 4, 5, 6}
FEATURED_STORIES = [s for s in STORIES if s["id"] in FEATURED_IDS]

DIFFICULTY_LABELS = {
    "easy":   {"icon": "🟢", "title": "Easy",   "blanks": "5–7 fill-ins",   "desc": "Perfect for getting started"},
    "medium": {"icon": "🟡", "title": "Medium", "blanks": "10 fill-ins",    "desc": "A proper creative workout"},
    "hard":   {"icon": "🔴", "title": "Hard",   "blanks": "12–14 fill-ins", "desc": "Longer stories, best as a team"},
}


def get_story(story_id):
    return next((s for s in STORIES if s["id"] == story_id), None)


def build_story_parts(template, answers):
    """Split a story template into alternating text and highlighted fill-in parts."""
    parts = []
    last_end = 0
    for match in re.finditer(r"\{(\w+)\}", template):
        key = match.group(1)
        start, end = match.span()
        if template[last_end:start]:
            parts.append({"type": "text", "content": template[last_end:start]})
        parts.append({"type": "fill", "content": answers.get(key, "___"), "key": key})
        last_end = end
    if template[last_end:]:
        parts.append({"type": "text", "content": template[last_end:]})
    return parts


# ── Standard routes ──────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html", stories=FEATURED_STORIES)


@app.route("/levels")
def levels():
    counts = {d: len([s for s in STORIES if s["difficulty"] == d])
              for d in ("easy", "medium", "hard")}
    return render_template("levels.html", labels=DIFFICULTY_LABELS, counts=counts)


@app.route("/levels/<difficulty>")
def levels_difficulty(difficulty):
    if difficulty not in DIFFICULTY_LABELS:
        return redirect(url_for("levels"))
    level_stories = [s for s in STORIES if s["difficulty"] == difficulty]
    label = DIFFICULTY_LABELS[difficulty]
    return render_template("levels_stories.html",
                           stories=level_stories,
                           difficulty=difficulty,
                           label=label)


@app.route("/play/<int:story_id>")
def play(story_id):
    story = get_story(story_id)
    if not story:
        return redirect(url_for("index"))
    ref = request.args.get("ref", "")
    if ref in DIFFICULTY_LABELS:
        back_url = url_for("levels_difficulty", difficulty=ref)
        back_label = f"← Back to {DIFFICULTY_LABELS[ref]['title']} Stories"
    else:
        back_url = url_for("index")
        back_label = "← Back to Stories"
    return render_template("play.html", story=story,
                           back_url=back_url, back_label=back_label)


@app.route("/result/<int:story_id>", methods=["POST"])
def result(story_id):
    story = get_story(story_id)
    if not story:
        return redirect(url_for("index"))
    answers = {
        blank["key"]: request.form.get(blank["key"], "").strip() or "___"
        for blank in story["blanks"]
    }
    story_parts = build_story_parts(story["template"], answers)
    ref = request.args.get("ref", "")
    if ref in DIFFICULTY_LABELS:
        back_url = url_for("levels_difficulty", difficulty=ref)
        back_label = f"← Back to {DIFFICULTY_LABELS[ref]['title']} Stories"
    else:
        back_url = url_for("index")
        back_label = "← Back to Stories"
    return render_template("result.html", story=story, story_parts=story_parts,
                           back_url=back_url, back_label=back_label)


# ── Team game — invite-code multiplayer ──────────────────────────────────────

GAMES = {}          # { code: game_dict }
GAME_TTL = 1200     # 20 minutes in seconds


def _make_code():
    chars = string.ascii_uppercase + string.digits
    while True:
        code = "".join(secrets.choice(chars) for _ in range(6))
        if code not in GAMES:
            return code


def _cleanup_games():
    now = time.time()
    for code in [c for c, g in list(GAMES.items()) if now - g["created_at"] > GAME_TTL]:
        del GAMES[code]


@app.route("/join", methods=["GET", "POST"])
def join_game():
    """Landing page where players type in a code to join a team game."""
    error = None
    if request.method == "POST":
        code = request.form.get("code", "").strip().upper()
        if not code:
            error = "Please enter a game code."
        elif code not in GAMES:
            error = f'Code "{code}" not found. Check the code and try again.'
        else:
            return redirect(url_for("game_join", code=code))
    return render_template("join_game.html", error=error)


@app.route("/game/start/<int:story_id>")
def game_start(story_id):
    """Host creates a new team game. Returns the lobby with the invite code."""
    _cleanup_games()
    story = get_story(story_id)
    if not story:
        return redirect(url_for("levels"))
    code = _make_code()
    GAMES[code] = {
        "story_id":   story_id,
        "answers":    {b["key"]: None for b in story["blanks"]},
        "assignments": {},      # blank_key -> player_name
        "next_blank":  0,
        "created_at":  time.time(),
    }
    join_path = url_for("game_join", code=code)
    return render_template("game_lobby.html", code=code, story=story, join_path=join_path)


@app.route("/game/<code>", methods=["GET", "POST"])
def game_join(code):
    """Player enters their name and is assigned the next available blank."""
    code = code.upper()
    game = GAMES.get(code)
    if not game:
        return render_template("game_error.html",
                               msg="Game not found. The invite code may have expired.")
    story = get_story(game["story_id"])
    blanks = story["blanks"]

    # If this browser already has an assignment for this game, send them to play
    existing_key = session.get(f"game_{code}_key")
    if existing_key and existing_key in game["answers"]:
        return redirect(url_for("game_play", code=code))

    if request.method == "POST":
        name = request.form.get("name", "").strip()[:30] or "Player"
        idx = game["next_blank"]
        if idx >= len(blanks):
            return render_template("game_error.html",
                                   msg="All blanks are taken — this game is full!")
        blank = blanks[idx]
        game["next_blank"] += 1
        game["assignments"][blank["key"]] = name
        session[f"game_{code}_key"] = blank["key"]
        session[f"game_{code}_name"] = name
        return redirect(url_for("game_play", code=code))

    spots_left = len(blanks) - game["next_blank"]
    return render_template("game_join.html", code=code, story=story,
                           spots_left=spots_left, total=len(blanks),
                           filled=game["next_blank"])


@app.route("/game/<code>/play", methods=["GET", "POST"])
def game_play(code):
    """Player fills in their assigned blank."""
    code = code.upper()
    game = GAMES.get(code)
    if not game:
        return redirect(url_for("index"))
    blank_key = session.get(f"game_{code}_key")
    player_name = session.get(f"game_{code}_name", "Player")
    if not blank_key:
        return redirect(url_for("game_join", code=code))
    story = get_story(game["story_id"])
    blank = next((b for b in story["blanks"] if b["key"] == blank_key), None)
    blank_num = next((i + 1 for i, b in enumerate(story["blanks"])
                      if b["key"] == blank_key), "?")
    already_answered = game["answers"].get(blank_key) is not None

    if request.method == "POST":
        if not already_answered:
            answer = request.form.get("answer", "").strip()[:60] or "___"
            game["answers"][blank_key] = answer
        return redirect(url_for("game_wait", code=code))

    return render_template("game_play.html", code=code, story=story, blank=blank,
                           blank_num=blank_num, player_name=player_name,
                           already_answered=already_answered,
                           total=len(story["blanks"]))


@app.route("/game/<code>/wait")
def game_wait(code):
    """Waiting room — polls until all blanks are filled, then shows result."""
    code = code.upper()
    game = GAMES.get(code)
    if not game:
        return redirect(url_for("index"))
    story = get_story(game["story_id"])
    filled = sum(1 for v in game["answers"].values() if v is not None)
    total = len(story["blanks"])
    if filled >= total:
        return redirect(url_for("game_result", code=code))
    return render_template("game_wait.html", code=code, story=story,
                           filled=filled, total=total)


@app.route("/game/<code>/status")
def game_status(code):
    """JSON endpoint polled by the wait page."""
    code = code.upper()
    game = GAMES.get(code)
    if not game:
        return jsonify({"error": "not found"}), 404
    story = get_story(game["story_id"])
    filled = sum(1 for v in game["answers"].values() if v is not None)
    total = len(story["blanks"])
    return jsonify({"ready": filled >= total, "filled": filled, "total": total})


@app.route("/game/<code>/result")
def game_result(code):
    """Final story reveal — shows who answered what."""
    code = code.upper()
    game = GAMES.get(code)
    if not game:
        return redirect(url_for("index"))
    story = get_story(game["story_id"])
    answers = {k: (v or "___") for k, v in game["answers"].items()}
    story_parts = build_story_parts(story["template"], answers)
    return render_template("game_result.html", code=code, story=story,
                           story_parts=story_parts,
                           assignments=game["assignments"])


if __name__ == "__main__":
    app.run(debug=True)
