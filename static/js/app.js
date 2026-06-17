/**
 * Mad Libs World — client-side completion tracking + team mode.
 */

const STORAGE_KEY = 'madlibs_completed_v1';

/* ─── localStorage helpers ─────────────────────────────────── */

function getCompleted() {
    try { return JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]'); }
    catch { return []; }
}

function saveCompleted(ids) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(ids));
}

/* ─── Result page ──────────────────────────────────────────── */

function markStoryCompleted(storyId) {
    var completed = getCompleted();
    if (!completed.includes(storyId)) {
        completed.push(storyId);
        saveCompleted(completed);
    }
}

/* ─── Homepage ─────────────────────────────────────────────── */

/**
 * @param {number[]} storyIds  IDs of the featured stories shown on homepage.
 */
function initHomepage(storyIds) {
    var completed = getCompleted();
    var done = storyIds.filter(function (id) { return completed.includes(id); }).length;

    var countEl = document.getElementById('completed-count');
    if (countEl) countEl.textContent = done;

    completed.forEach(function (id) {
        var card = document.querySelector('[data-story-id="' + id + '"]');
        if (card) card.classList.add('is-completed');
    });
}

/* ─── Level story pages ────────────────────────────────────── */

/**
 * @param {number[]} storyIds  IDs of the stories shown on a levels/<difficulty> page.
 */
function initLevelPage(storyIds) {
    var completed = getCompleted();
    completed.forEach(function (id) {
        var card = document.querySelector('[data-story-id="' + id + '"]');
        if (card) card.classList.add('is-completed');
    });
}

/* ─── Play page — solo/team mode ───────────────────────────── */

var _blanks = [];          // [{key, label, hint}, ...]
var _teamAnswers = {};     // {key: value}
var _teamIndex = 0;
var _currentMode = 'solo';

/**
 * Called from play.html once DOM is ready.
 * @param {Array} blanks  The story.blanks array serialised from Jinja.
 */
function initPlayPage(blanks) {
    _blanks = blanks;
    document.getElementById('team-total').textContent = blanks.length;
    setPlayMode('solo');
}

function setPlayMode(mode) {
    _currentMode = mode;

    var isSolo = (mode === 'solo');
    document.getElementById('solo-instructions').style.display = isSolo ? '' : 'none';
    document.getElementById('team-instructions').style.display = isSolo ? 'none' : '';
    document.getElementById('solo-grid').style.display       = isSolo ? '' : 'none';
    document.getElementById('solo-submit').style.display     = isSolo ? '' : 'none';
    document.getElementById('team-panel').style.display      = isSolo ? 'none' : '';

    document.getElementById('btn-solo').classList.toggle('mode-btn--active', isSolo);
    document.getElementById('btn-team').classList.toggle('mode-btn--active', !isSolo);

    if (!isSolo) {
        // Reset team state
        _teamAnswers = {};
        _teamIndex = 0;
        // Remove required from all inputs (team mode manages submission itself)
        document.querySelectorAll('#solo-grid .blank-input').forEach(function (inp) {
            inp.removeAttribute('required');
            inp.value = '';
        });
        showTeamBlank(_teamIndex);
    } else {
        // Restore required on all inputs for solo mode
        document.querySelectorAll('#solo-grid .blank-input').forEach(function (inp) {
            inp.setAttribute('required', '');
        });
    }
}

function showTeamBlank(index) {
    var blank = _blanks[index];
    var isLast = (index === _blanks.length - 1);

    document.getElementById('team-player-num').textContent = index + 1;
    document.getElementById('team-field-num').textContent  = index + 1;
    document.getElementById('team-label-text').textContent = blank.label;
    document.getElementById('team-hint-text').textContent  = blank.hint;
    document.getElementById('team-current').textContent    = index + 1;
    document.getElementById('team-input').value            = '';
    document.getElementById('team-input').placeholder      = blank.hint;

    var nextBtn = document.getElementById('team-next-btn');
    nextBtn.textContent = isLast ? '🎲 Generate My Story!' : 'Next Player →';

    document.getElementById('team-input').focus();
}

function teamNext() {
    var input = document.getElementById('team-input');
    var value = input.value.trim();
    if (!value) {
        input.classList.add('input-error');
        input.focus();
        setTimeout(function () { input.classList.remove('input-error'); }, 600);
        return;
    }

    _teamAnswers[_blanks[_teamIndex].key] = value;

    if (_teamIndex < _blanks.length - 1) {
        _teamIndex++;
        showTeamBlank(_teamIndex);
    } else {
        // All blanks filled — populate form inputs and submit
        Object.keys(_teamAnswers).forEach(function (key) {
            var inp = document.getElementById(key);
            if (inp) inp.value = _teamAnswers[key];
        });
        document.getElementById('blanks-form').submit();
    }
}


