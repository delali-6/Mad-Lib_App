import re
from flask import Flask, render_template, request, redirect, url_for
from stories import STORIES

app = Flask(__name__)

# The six original homepage stories
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
        parts.append({"type": "fill", "content": answers.get(key, "___")})
        last_end = end
    if template[last_end:]:
        parts.append({"type": "text", "content": template[last_end:]})
    return parts


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


if __name__ == "__main__":
    app.run(debug=True)

