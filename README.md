# 📖 Mad Libs World

A fun, interactive Mad Lib web app built with Python and Flask. Choose from **18 stories** across three difficulty levels, fill in the blanks, and watch hilariously silly stories come to life!

---

## 🌐 View the App

Once the server is running, open your browser and go to:

**[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## ✨ Features

- **18 unique stories** across 3 difficulty levels:
  - 🟢 **Easy** — 4 stories, 5–7 fill-ins (Animals, Food, Adventure, Celebrations)
  - 🟡 **Medium** — 6 stories, 10 fill-ins (Adventure, Food, Spooky, Sci-Fi, Sports, Workplace)
  - 🔴 **Hard** — 8 stories, 12–14 fill-ins (Crime Caper, Sci-Fi, Romance, Adventure, Fantasy, School)
- **Story dashboard** — three colour-coded sections, each with its own progress counter
- **Fill-in form** — labelled fields with helpful hints for every blank
- **Highlighted result** — your words appear colour-highlighted inside the finished story
- **Completion tracking** — finished stories get a green ✓ badge on the dashboard (saved in your browser so it persists across page reloads)
- **Progress counter** — see how many of the 6 stories you've completed
- **Print-friendly** — print your finished story with one click
- **Responsive** — works on mobile and desktop

---

## 🚀 Getting Started

### 1. Clone or download the project

```bash
git clone <https://github.com/delali-6/Mad-Lib_App.git>
cd Mad-Lib_App
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
python main.py
```

### 4. Open in your browser

**[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 📁 Project Structure

```
Mad-Lib_App/
├── main.py            ← Flask app and routes
├── stories.py         ← All 6 Mad Lib story definitions
├── requirements.txt   ← Python dependencies
├── README.md
├── templates/
│   ├── base.html      ← Shared page layout
│   ├── index.html     ← Homepage / story dashboard
│   ├── play.html      ← Fill-in-the-blanks form
│   └── result.html    ← Completed story display
└── static/
    ├── css/style.css  ← Styles
    └── js/app.js      ← Completion tracking (localStorage)
```

---

## 🛠️ Tech Stack

| Layer     | Technology          |
|-----------|---------------------|
| Backend   | Python 3, Flask     |
| Frontend  | HTML, CSS, JavaScript |
| Storage   | Browser localStorage (no database needed) |

---

## ➕ Adding More Stories

Open `stories.py` and add a new entry to the `STORIES` list following the same structure as the existing ones. Each story needs:

- `id` — unique integer
- `title`, `description`, `emoji`, `category`
- `blanks` — list of `{ key, label, hint }` dicts
- `template` — story string using `{key}` placeholders matching the blank keys
