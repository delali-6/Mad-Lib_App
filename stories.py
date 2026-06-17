STORIES = [

    # ─────────────────────────────────────────────────────────────────
    # EASY  (5 – 7 blanks)
    # ─────────────────────────────────────────────────────────────────
    {
        "id": 7,
        "title": "My Silly Pet",
        "description": "A short sweet story about the world's most ridiculous pet.",
        "emoji": "🐾",
        "category": "Animals",
        "difficulty": "easy",
        "blanks": [
            {"key": "pet",  "label": "A pet's name",    "hint": "e.g., Mr Fluffles"},
            {"key": "adj1", "label": "An adjective",    "hint": "e.g., dramatic"},
            {"key": "food", "label": "A type of food",  "hint": "e.g., pickles"},
            {"key": "verb", "label": "A verb (-ing)",   "hint": "e.g., howling"},
            {"key": "adj2", "label": "Another adjective", "hint": "e.g., magnificent"},
        ],
        "template": (
            "My pet {pet} is the most {adj1} animal in the whole world. "
            "Every single morning, {pet} wakes me up by {verb} until I bring them {food}. "
            "Yesterday, {pet} caused such a {adj1} scene at the park that everyone stopped to stare. "
            "Mum says keeping {pet} was a mistake, but I think {pet} is absolutely {adj2} "
            "and I would not swap them for anything in the world."
        ),
    },
    {
        "id": 8,
        "title": "The Magic Sandwich",
        "description": "One ordinary lunchtime. One extraordinary sandwich. Nothing will ever be the same.",
        "emoji": "🥪",
        "category": "Food",
        "difficulty": "easy",
        "blanks": [
            {"key": "name",  "label": "Your name",              "hint": "e.g., Jordan"},
            {"key": "ing1",  "label": "A sandwich filling",     "hint": "e.g., marshmallows"},
            {"key": "ing2",  "label": "Another filling",        "hint": "e.g., glitter"},
            {"key": "adj1",  "label": "An adjective",           "hint": "e.g., sparkling"},
            {"key": "verb1", "label": "A verb (past tense)",    "hint": "e.g., exploded"},
            {"key": "place", "label": "A place",                "hint": "e.g., the moon"},
        ],
        "template": (
            "One afternoon, {name} made the most unusual sandwich in history: "
            "{ing1} with {ing2} on top, covered in {adj1} sauce. "
            "The moment {name} took a bite, the sandwich {verb1} in a burst of rainbow light. "
            "Suddenly, {name} could fly! They soared all the way to {place} and back before dinner. "
            "The next day, {name} tried to make the sandwich again — but it just tasted like {ing1} and sadness."
        ),
    },
    {
        "id": 9,
        "title": "A Rainy Day Adventure",
        "description": "Sometimes the best adventures happen when you are stuck indoors.",
        "emoji": "🌧️",
        "category": "Adventure",
        "difficulty": "easy",
        "blanks": [
            {"key": "name",  "label": "A friend's name",        "hint": "e.g., Sam"},
            {"key": "game",  "label": "A game or activity",     "hint": "e.g., sock wrestling"},
            {"key": "adj1",  "label": "An adjective",           "hint": "e.g., gigantic"},
            {"key": "obj1",  "label": "A household object",     "hint": "e.g., laundry basket"},
            {"key": "sound", "label": "A funny sound",          "hint": "e.g., SPLOOOSH"},
            {"key": "adj2",  "label": "Another adjective",      "hint": "e.g., legendary"},
        ],
        "template": (
            "It was raining outside, so {name} invented a new game called {game}. "
            "First, {name} built a {adj1} fort out of every {obj1} in the house. "
            "Then things got completely out of control — there was a loud '{sound}' from the kitchen, "
            "and {name} discovered the cat had joined in the {game} tournament. "
            "By the end of the day, the living room looked {adj1} and {adj2}, "
            "and {name} declared it the best rainy day ever."
        ),
    },
    {
        "id": 10,
        "title": "The Birthday Party Surprise",
        "description": "A birthday party that nobody will forget — for better or for worse.",
        "emoji": "🎂",
        "category": "Celebrations",
        "difficulty": "easy",
        "blanks": [
            {"key": "bday",  "label": "The birthday person's name", "hint": "e.g., Priya"},
            {"key": "age",   "label": "An age (number)",            "hint": "e.g., 47"},
            {"key": "gift",  "label": "A weird gift",               "hint": "e.g., a pet crab"},
            {"key": "adj1",  "label": "An adjective",               "hint": "e.g., wobbly"},
            {"key": "food",  "label": "A cake flavour",             "hint": "e.g., cheese and onion"},
            {"key": "verb1", "label": "A verb (past tense)",        "hint": "e.g., somersaulted"},
            {"key": "adj2",  "label": "Another adjective",          "hint": "e.g., unforgettable"},
        ],
        "template": (
            "Today was {bday}'s {age}th birthday, and everyone was SO excited. "
            "The first guest arrived carrying a {adj1} {gift}, which immediately caused a commotion. "
            "The birthday cake was {adj1} and flavoured with {food}, which nobody expected. "
            "When {bday} blew out the candles, the whole cake {verb1} off the table. "
            "Everyone laughed until they cried, and {bday} declared it the most {adj2} birthday of all time. "
            "The {gift} seemed to enjoy the party too — especially the {food} cake crumbs."
        ),
    },

    # ─────────────────────────────────────────────────────────────────
    # MEDIUM  (10 blanks)
    # ─────────────────────────────────────────────────────────────────
    {
        "id": 1,
        "title": "The Wild Camping Trip",
        "description": "A hilariously unpredictable outdoor adventure that goes completely off the rails.",
        "emoji": "🏕️",
        "category": "Adventure",
        "difficulty": "medium",
        "blanks": [
            {"key": "name",   "label": "A person's name",           "hint": "e.g., Jessica"},
            {"key": "adj1",   "label": "An adjective",              "hint": "e.g., enormous"},
            {"key": "place",  "label": "A place name",              "hint": "e.g., Mount Doom"},
            {"key": "adj2",   "label": "Another adjective",         "hint": "e.g., sneaky"},
            {"key": "animal", "label": "An animal",                 "hint": "e.g., raccoon"},
            {"key": "food",   "label": "A type of food",            "hint": "e.g., spaghetti"},
            {"key": "verb1",  "label": "A verb (past tense)",       "hint": "e.g., screamed"},
            {"key": "noun1",  "label": "A random object",           "hint": "e.g., umbrella"},
            {"key": "verb2",  "label": "Another verb (past tense)", "hint": "e.g., danced"},
            {"key": "adj3",   "label": "An adjective",              "hint": "e.g., magnificent"},
        ],
        "template": (
            "Last weekend, {name} packed their {adj1} backpack and headed to {place} for a camping adventure. "
            "The moment they arrived, a {adj2} {animal} ran out of the bushes and stole their {food}! "
            "{name} {verb1} at the top of their lungs and grabbed a nearby {noun1}. "
            "They chased the {animal} through the forest until they {verb2} right into the river. "
            "Soaking wet but laughing, {name} decided it was the most {adj3} camping trip they'd ever had. "
            "They couldn't wait to tell everyone back home about their wild encounter with the {adj2} {animal}!"
        ),
    },
    {
        "id": 2,
        "title": "The Cooking Show Disaster",
        "description": "Lights, camera, kitchen chaos! This cooking show is about to go completely off the rails.",
        "emoji": "🍳",
        "category": "Food",
        "difficulty": "medium",
        "blanks": [
            {"key": "chef",   "label": "A celebrity chef's name",   "hint": "e.g., Gordon"},
            {"key": "dish",   "label": "A fancy dish",              "hint": "e.g., soufflé"},
            {"key": "ing1",   "label": "A weird ingredient",        "hint": "e.g., marshmallows"},
            {"key": "ing2",   "label": "Another weird ingredient",  "hint": "e.g., ketchup"},
            {"key": "adj1",   "label": "An adjective",              "hint": "e.g., explosive"},
            {"key": "verb1",  "label": "A verb (past tense)",       "hint": "e.g., exploded"},
            {"key": "liquid", "label": "A liquid",                  "hint": "e.g., pickle juice"},
            {"key": "body",   "label": "A body part",               "hint": "e.g., elbow"},
            {"key": "number", "label": "A number",                  "hint": "e.g., 47"},
            {"key": "adj2",   "label": "Another adjective",         "hint": "e.g., magnificent"},
        ],
        "template": (
            "Welcome to 'Cooking with {chef},' the show where culinary dreams come true! "
            "Today, {chef} attempted to make a world-famous {dish} using only {ing1} and {ing2}. "
            "The {adj1} mixture {verb1} all over the studio, covering the camera crew in {liquid}. "
            "{chef} burned their {body} on the oven and knocked over {number} bottles of hot sauce. "
            "Despite the chaos, the {adj2} {dish} somehow tasted incredible — or so {chef} claimed, "
            "while covered in {ing1} from head to toe. The audience gave a standing ovation anyway!"
        ),
    },
    {
        "id": 3,
        "title": "The Haunted Mansion Mystery",
        "description": "Dare to enter the spookiest house in town. What eerie secrets lurk inside?",
        "emoji": "👻",
        "category": "Spooky",
        "difficulty": "medium",
        "blanks": [
            {"key": "hero",     "label": "A hero's name",           "hint": "e.g., Sherlock"},
            {"key": "adj1",     "label": "A spooky adjective",      "hint": "e.g., creepy"},
            {"key": "room",     "label": "A room in a house",       "hint": "e.g., library"},
            {"key": "adj2",     "label": "Another adjective",       "hint": "e.g., ancient"},
            {"key": "object",   "label": "A household object",      "hint": "e.g., chandelier"},
            {"key": "creature", "label": "A spooky creature",       "hint": "e.g., vampire"},
            {"key": "verb1",    "label": "A verb (past tense)",     "hint": "e.g., shrieked"},
            {"key": "sound",    "label": "A scary sound",           "hint": "e.g., WOOOOOO"},
            {"key": "number",   "label": "A number",                "hint": "e.g., 13"},
            {"key": "adj3",     "label": "An adjective",            "hint": "e.g., terrified"},
        ],
        "template": (
            "On a dark and stormy night, {hero} crept through the {adj1} gates of the Haunted Mansion. "
            "Inside the {room}, a {adj2} {object} crashed to the floor and {hero} {verb1} in fright. "
            "Suddenly, a {creature} appeared from behind the curtains, screaming '{sound}!' "
            "The {creature} had been haunting this mansion for {number} years, waiting for someone brave to visit. "
            "{hero} felt {adj3} but stood their ground, demanding answers from the {creature}. "
            "Turns out, the {adj2} {creature} was just lonely and wanted someone to play board games with. "
            "What started as a {adj1} mystery ended with {hero} and the {creature} becoming the best of friends!"
        ),
    },
    {
        "id": 4,
        "title": "Space Explorer's Log",
        "description": "Houston, we have a problem — and it's absolutely, ridiculously hilarious.",
        "emoji": "🚀",
        "category": "Sci-Fi",
        "difficulty": "medium",
        "blanks": [
            {"key": "astro",  "label": "An astronaut's name",       "hint": "e.g., Commander Zara"},
            {"key": "planet", "label": "A made-up planet name",     "hint": "e.g., Zorbax"},
            {"key": "adj1",   "label": "A colour or adjective",     "hint": "e.g., purple"},
            {"key": "alien",  "label": "A type of alien",           "hint": "e.g., blob creature"},
            {"key": "number", "label": "A number",                  "hint": "e.g., 3,000"},
            {"key": "limb",   "label": "A body part (plural)",      "hint": "e.g., tentacles"},
            {"key": "verb1",  "label": "A verb (past tense)",       "hint": "e.g., wiggled"},
            {"key": "food",   "label": "A type of food",            "hint": "e.g., nachos"},
            {"key": "adj2",   "label": "Another adjective",         "hint": "e.g., glowing"},
            {"key": "verb2",  "label": "Another verb (past tense)", "hint": "e.g., zoomed"},
        ],
        "template": (
            "Stardate: Unknown. Commander {astro} reporting from the surface of planet {planet}. "
            "The sky here is a {adj1} colour, and the locals — a species of {alien} — have {number} {limb}. "
            "When I landed, the entire {alien} population {verb1} toward my spaceship in greeting. "
            "They offered me {food} as a welcome gift, which tasted surprisingly like {adj2} stardust. "
            "I tried to communicate using the universal translator, which kept saying '{food}' in reply to everything. "
            "The {alien} leader seemed offended, then {verb2} away on their {adj1} hovercraft. "
            "Note to mission control: next time, send someone who speaks {adj2} alien. {astro} out."
        ),
    },
    {
        "id": 5,
        "title": "The Big Sports Championship",
        "description": "The crowd goes wild as the most chaotic game in history unfolds before everyone's eyes.",
        "emoji": "🏆",
        "category": "Sports",
        "difficulty": "medium",
        "blanks": [
            {"key": "player",  "label": "A player's name",          "hint": "e.g., Thunderbolt"},
            {"key": "sport",   "label": "A sport",                  "hint": "e.g., underwater frisbee"},
            {"key": "team1",   "label": "A team name",              "hint": "e.g., The Flaming Pandas"},
            {"key": "team2",   "label": "Another team name",        "hint": "e.g., The Cosmic Wombats"},
            {"key": "adj1",    "label": "An adjective",             "hint": "e.g., unstoppable"},
            {"key": "verb1",   "label": "A verb (past tense)",      "hint": "e.g., somersaulted"},
            {"key": "score",   "label": "A score (number)",         "hint": "e.g., 47"},
            {"key": "object",  "label": "A random object",          "hint": "e.g., rubber duck"},
            {"key": "adj2",    "label": "Another adjective",        "hint": "e.g., legendary"},
            {"key": "cheer",   "label": "A crowd cheer sound",      "hint": "e.g., HOOOORAY"},
        ],
        "template": (
            "The {adj2} {sport} championship was finally here — {team1} versus {team2}! "
            "Star player {player} was famous for their {adj1} moves and their lucky {object}. "
            "In the first quarter, {player} {verb1} past three defenders and scored {score} points in one move! "
            "The crowd screamed '{cheer}!' so loudly that the entire stadium {adj1}ly shook. "
            "But {team2} wasn't giving up — their captain snatched the {object} right from {player}'s hands! "
            "With one second left on the clock, {player} {verb1} one final time and won it all for {team1}. "
            "The {adj2} victory was celebrated for weeks, and {player}'s {object} was put in the Hall of Fame!"
        ),
    },
    {
        "id": 6,
        "title": "A Very Weird Job Interview",
        "description": "Your dream job is on the line. Just try not to say anything too strange. Good luck.",
        "emoji": "💼",
        "category": "Workplace",
        "difficulty": "medium",
        "blanks": [
            {"key": "name",    "label": "Your name",                "hint": "e.g., Alex"},
            {"key": "job",     "label": "A job title",              "hint": "e.g., Professional Napper"},
            {"key": "company", "label": "A made-up company name",   "hint": "e.g., Wobble Corp"},
            {"key": "adj1",    "label": "An adjective",             "hint": "e.g., dynamic"},
            {"key": "years",   "label": "A number of years",        "hint": "e.g., 47"},
            {"key": "skill",   "label": "A weird skill",            "hint": "e.g., yodeling"},
            {"key": "verb1",   "label": "A verb (present tense)",   "hint": "e.g., juggle"},
            {"key": "object",  "label": "A random object",          "hint": "e.g., spatula"},
            {"key": "animal",  "label": "An animal",                "hint": "e.g., ferret"},
            {"key": "adj2",    "label": "Another adjective",        "hint": "e.g., passionate"},
        ],
        "template": (
            "{name} walked into {company} headquarters for their interview for the position of {job}. "
            "The interviewer asked, 'What makes you {adj1} enough for this role?' "
            "{name} replied, 'I have {years} years of experience and I can {verb1} a {object} with one hand.' "
            "The interviewer raised an eyebrow and said, 'Interesting. Can you also manage a {animal}?' "
            "{name} nodded confidently: 'My {skill} skills have prepared me for anything, including {animal} management.' "
            "The interviewer stood up, shook their hand, and said, 'You are the most {adj2} candidate we have ever met.' "
            "{name} got the job, and their very first task was teaching the office {animal} how to use the printer."
        ),
    },

    # ─────────────────────────────────────────────────────────────────
    # HARD  (12 – 14 blanks)
    # ─────────────────────────────────────────────────────────────────
    {
        "id": 11,
        "title": "The Grand Heist Plan",
        "description": "A daring crew. An impossible target. What could possibly go wrong? Everything.",
        "emoji": "🕵️",
        "category": "Crime Caper",
        "difficulty": "hard",
        "blanks": [
            {"key": "boss",   "label": "The mastermind's name",       "hint": "e.g., The Shadow"},
            {"key": "target", "label": "Something to steal",          "hint": "e.g., the world's largest cheese"},
            {"key": "place",  "label": "A fancy location",            "hint": "e.g., the Louvre"},
            {"key": "gadget", "label": "A made-up gadget",            "hint": "e.g., pocket jetpack"},
            {"key": "adj1",   "label": "An adjective",                "hint": "e.g., waterproof"},
            {"key": "hench1", "label": "A henchperson's name",        "hint": "e.g., Knuckles"},
            {"key": "hench2", "label": "Another henchperson's name",  "hint": "e.g., Sprockets"},
            {"key": "verb1",  "label": "A verb (past tense)",         "hint": "e.g., rappelled"},
            {"key": "verb2",  "label": "Another verb (past tense)",   "hint": "e.g., detonated"},
            {"key": "animal", "label": "An animal",                   "hint": "e.g., llama"},
            {"key": "number", "label": "A number",                    "hint": "e.g., 42"},
            {"key": "adj2",   "label": "Another adjective",           "hint": "e.g., catastrophic"},
            {"key": "escape", "label": "A mode of transport",         "hint": "e.g., unicycle"},
        ],
        "template": (
            "The legendary criminal mastermind {boss} had one final job: steal the {target} from {place}. "
            "The crew consisted of {hench1}, who specialised in {adj1} disguises, "
            "and {hench2}, whose only skill was operating a {gadget}. "
            "Phase One: {hench1} {verb1} through the ventilation shaft — directly into a guard's lunch. "
            "Phase Two: {hench2} {verb2} the alarm system, which accidentally also {verb2} {number} sprinklers. "
            "A rogue {animal} that had wandered into {place} chose this exact moment to cause chaos, "
            "chasing {hench1} through {number} corridors while {boss} watched on the security feed in horror. "
            "The {adj2} plan unravelled completely, and the crew escaped on a {escape} with nothing but wet socks. "
            "{boss} vowed that next time, they would not bring a {animal} as backup."
        ),
    },
    {
        "id": 12,
        "title": "The Intergalactic Travel Agency",
        "description": "Book your dream holiday — anywhere in the universe. Terms and conditions may apply.",
        "emoji": "🌌",
        "category": "Sci-Fi",
        "difficulty": "hard",
        "blanks": [
            {"key": "agent",    "label": "A travel agent's name",    "hint": "e.g., Zephyra"},
            {"key": "client",   "label": "A client's name",          "hint": "e.g., Dave"},
            {"key": "planet1",  "label": "A made-up planet",         "hint": "e.g., Glumtoria"},
            {"key": "planet2",  "label": "Another made-up planet",   "hint": "e.g., Squibble-9"},
            {"key": "adj1",     "label": "An adjective",             "hint": "e.g., bioluminescent"},
            {"key": "adj2",     "label": "Another adjective",        "hint": "e.g., soggy"},
            {"key": "food",     "label": "A food",                   "hint": "e.g., cornflakes"},
            {"key": "alien",    "label": "A type of alien",          "hint": "e.g., jelly cube"},
            {"key": "activity", "label": "A holiday activity",       "hint": "e.g., volcano surfing"},
            {"key": "price",    "label": "A made-up currency amount","hint": "e.g., 3 million space-bucks"},
            {"key": "verb1",    "label": "A verb (past tense)",      "hint": "e.g., evaporated"},
            {"key": "adj3",     "label": "A third adjective",        "hint": "e.g., non-refundable"},
        ],
        "template": (
            "Welcome to StarHop Travel! Agent {agent} beamed her best smile at client {client}. "
            "'I want something {adj1},' said {client}, 'but not too {adj2}.' "
            "{agent} immediately recommended {planet1}, famous for its {adj1} oceans of liquid {food}. "
            "'Alternatively,' she said, 'there is {planet2}, where the local {alien} population "
            "offers {activity} at a {adj2} discount of only {price}.' "
            "{client} asked about the weather on {planet1}. {agent} paused. "
            "'The atmosphere {verb1} every Tuesday,' she admitted, 'but the views are {adj1}.' "
            "{client} booked {planet2} instead, and two weeks later sent a postcard that read: "
            "'The {alien} took my luggage. The {activity} was {adj1}. The {food} buffet {verb1}. "
            "Sending more {price}. Do NOT tell my wife.' The booking was, of course, {adj3}."
        ),
    },
    {
        "id": 13,
        "title": "The Royal Wedding Disaster",
        "description": "The most anticipated royal event in history. What could go wrong in just one day?",
        "emoji": "👑",
        "category": "Romance",
        "difficulty": "hard",
        "blanks": [
            {"key": "royal1",  "label": "A royal's name",            "hint": "e.g., Prince Barnabas"},
            {"key": "royal2",  "label": "Another royal's name",      "hint": "e.g., Queen Doris"},
            {"key": "venue",   "label": "A wedding venue",           "hint": "e.g., the underwater palace"},
            {"key": "adj1",    "label": "An adjective",              "hint": "e.g., magnificent"},
            {"key": "dress",   "label": "An outfit description",     "hint": "e.g., made entirely of tinfoil"},
            {"key": "food1",   "label": "A wedding food",            "hint": "e.g., anchovy cake"},
            {"key": "animal",  "label": "An animal",                 "hint": "e.g., ostrich"},
            {"key": "verb1",   "label": "A verb (past tense)",       "hint": "e.g., avalanched"},
            {"key": "guest",   "label": "A famous guest's name",     "hint": "e.g., Lord Wobblington"},
            {"key": "number",  "label": "A number",                  "hint": "e.g., 300"},
            {"key": "adj2",    "label": "Another adjective",         "hint": "e.g., soggy"},
            {"key": "verb2",   "label": "Another verb (past tense)", "hint": "e.g., yodelled"},
            {"key": "adj3",    "label": "A third adjective",         "hint": "e.g., eternal"},
            {"key": "object",  "label": "A random object",           "hint": "e.g., a trampoline"},
        ],
        "template": (
            "The kingdom held its breath as {royal1} and {royal2} prepared to wed at {venue}. "
            "{royal1} arrived wearing a {adj1} gown {dress}, causing {number} photographers to faint. "
            "The ceremony began beautifully until a {animal} {verb1} through the main doors, "
            "scattering {number} guests and toppling the {adj1} {food1} tower. "
            "Distinguished guest {guest} tried to restore order by standing on {object} and {verb2} the national anthem, "
            "which only made the {animal} more {adj2} and frantic. "
            "{royal2} whispered to {royal1}: 'Is this normal?' "
            "{royal1} replied: 'I hired the {animal} for atmosphere.' "
            "Despite everything, when {royal1} and {royal2} exchanged rings the moment was {adj1} and {adj3}. "
            "The {adj2} {food1} was served anyway, and {guest} declared it the finest they had ever tasted — "
            "though they said so while still balanced on {object}."
        ),
    },
    {
        "id": 14,
        "title": "A Day at the Zoo Gone Wild",
        "description": "The animals are out. The visitors are panicking. The gift shop is on fire.",
        "emoji": "🦁",
        "category": "Adventure",
        "difficulty": "hard",
        "blanks": [
            {"key": "keeper",  "label": "A zookeeper's name",        "hint": "e.g., Maureen"},
            {"key": "animal1", "label": "A zoo animal",              "hint": "e.g., flamingo"},
            {"key": "animal2", "label": "Another zoo animal",        "hint": "e.g., capybara"},
            {"key": "animal3", "label": "A third zoo animal",        "hint": "e.g., warthog"},
            {"key": "adj1",    "label": "An adjective",              "hint": "e.g., frenzied"},
            {"key": "food",    "label": "A type of food",            "hint": "e.g., pretzels"},
            {"key": "verb1",   "label": "A verb (past tense)",       "hint": "e.g., galloped"},
            {"key": "verb2",   "label": "Another verb (past tense)", "hint": "e.g., commandeered"},
            {"key": "place",   "label": "A place inside a zoo",      "hint": "e.g., the reptile house"},
            {"key": "number",  "label": "A number",                  "hint": "e.g., 37"},
            {"key": "adj2",    "label": "Another adjective",         "hint": "e.g., thunderous"},
            {"key": "object",  "label": "A random object",           "hint": "e.g., a leaf blower"},
        ],
        "template": (
            "Zookeeper {keeper} had one rule: never leave the {animal1} enclosure unlocked. "
            "{keeper} left the {animal1} enclosure unlocked. "
            "Within minutes, the {adj1} {animal1} {verb1} through {place}, "
            "closely followed by {number} {animal2}s who had clearly been planning this for weeks. "
            "The {animal3} {verb2} a mobility scooter near the entrance and sped toward the {food} kiosk. "
            "{keeper} chased all {number} animals across the park armed only with {object}, "
            "shouting their names in a {adj2} voice that the visitors found more frightening than the animals. "
            "The {animal2}s gathered in the cafe and refused to move. "
            "The {animal3} ate every last piece of {food} and looked absolutely unapologetic. "
            "By closing time, {keeper} had retrieved {number} of the {number} animals. "
            "The {adj1} {animal1} was found the next morning in a {adj2} pose on the director's chair."
        ),
    },
    {
        "id": 15,
        "title": "The World's Worst Superhero",
        "description": "With great power comes great responsibility — and absolutely terrible aim.",
        "emoji": "🦸",
        "category": "Fantasy",
        "difficulty": "hard",
        "blanks": [
            {"key": "hero",     "label": "Your superhero name",       "hint": "e.g., Captain Wobble"},
            {"key": "power1",   "label": "A useless superpower",      "hint": "e.g., turning into a biscuit"},
            {"key": "power2",   "label": "Another useless power",     "hint": "e.g., summoning geese"},
            {"key": "villain",  "label": "A villain's name",          "hint": "e.g., Doctor Confusing"},
            {"key": "adj1",     "label": "An adjective",              "hint": "e.g., baffling"},
            {"key": "city",     "label": "A city name",               "hint": "e.g., Blobford"},
            {"key": "object",   "label": "A random object",           "hint": "e.g., a garden hose"},
            {"key": "verb1",    "label": "A verb (past tense)",       "hint": "e.g., ricocheted"},
            {"key": "verb2",    "label": "Another verb (past tense)", "hint": "e.g., waddled"},
            {"key": "number",   "label": "A number",                  "hint": "e.g., 14"},
            {"key": "adj2",     "label": "Another adjective",         "hint": "e.g., suspicious"},
            {"key": "sidekick", "label": "A sidekick's name",         "hint": "e.g., Biscuit Boy"},
            {"key": "adj3",     "label": "A third adjective",         "hint": "e.g., triumphant"},
        ],
        "template": (
            "{hero} was the mightiest hero in all of {city} — which admittedly had very low standards. "
            "Their greatest power was {power1}, which they had never once used successfully. "
            "Their second power, {power2}, only worked on Wednesdays and only if it was raining. "
            "When {villain} launched their {adj1} attack on {city}'s main roundabout, "
            "{hero} leapt into action, armed with {object} and a {adj1} battle cry. "
            "{hero} {verb1} off {number} parked cars trying to reach the scene. "
            "Sidekick {sidekick} {verb2} behind, offering {adj2} helpful advice like 'try not to do that.' "
            "In a flash of inspiration, {hero} activated {power2} — it was, miraculously, a Wednesday and raining. "
            "{number} summoned creatures descended on {villain} in a {adj2} frenzy. "
            "{villain} fled. {city} was saved. "
            "{hero} and {sidekick} posed for photos in front of the {adj1} roundabout looking {adj3}, "
            "trying not to mention the {number} dented cars."
        ),
    },
    {
        "id": 16,
        "title": "The School Play Catastrophe",
        "description": "Opening night at the school drama club. What could go wrong in front of 200 parents?",
        "emoji": "🎭",
        "category": "School",
        "difficulty": "hard",
        "blanks": [
            {"key": "teacher",  "label": "A drama teacher's name",   "hint": "e.g., Ms Dramsworth"},
            {"key": "play",     "label": "A famous play or musical", "hint": "e.g., Hamlet"},
            {"key": "student1", "label": "A student's name",         "hint": "e.g., Oliver"},
            {"key": "student2", "label": "Another student's name",   "hint": "e.g., Kezia"},
            {"key": "adj1",     "label": "An adjective",             "hint": "e.g., catastrophic"},
            {"key": "prop",     "label": "A stage prop",             "hint": "e.g., plastic sword"},
            {"key": "line",     "label": "A made-up dramatic line",  "hint": "e.g., The cheese is on fire!"},
            {"key": "verb1",    "label": "A verb (past tense)",      "hint": "e.g., somersaulted"},
            {"key": "verb2",    "label": "Another verb (past tense)","hint": "e.g., collapsed"},
            {"key": "number",   "label": "A number",                 "hint": "e.g., 12"},
            {"key": "animal",   "label": "An animal",                "hint": "e.g., ferret"},
            {"key": "adj2",     "label": "Another adjective",        "hint": "e.g., standing"},
        ],
        "template": (
            "{teacher} had spent {number} weeks preparing the school's production of {play}. "
            "Lead actor {student1} had memorised every line — or so everyone thought. "
            "The curtain rose to applause. {student1} stepped forward and said, '{line}' "
            "— a line that appears nowhere in {play}. "
            "{teacher} watched from the wings, {adj1}ly silent. "
            "{student2} entered carrying the {prop}, immediately {verb1} into the scenery, "
            "which {verb2} onto the stage in {number} pieces. "
            "From backstage came a crashing noise: a {animal} had somehow got into the costume room. "
            "The {animal} {verb1} onto the stage wearing a {adj1} costume meant for {student1}. "
            "The audience gave the {animal} a {adj2} ovation. "
            "{student1} improvised bravely, incorporating the {prop} and the {animal} into the final scene. "
            "{teacher} later described it as 'the most {adj1} and {adj2} performance of {play} ever staged.'"
        ),
    },
    {
        "id": 17,
        "title": "The Time Machine Mix-Up",
        "description": "You built a time machine. You pressed the wrong button. History will never be the same.",
        "emoji": "⏱️",
        "category": "Sci-Fi",
        "difficulty": "hard",
        "blanks": [
            {"key": "inventor", "label": "The inventor's name",        "hint": "e.g., Professor Blip"},
            {"key": "year1",    "label": "A year in the past",         "hint": "e.g., 1347"},
            {"key": "year2",    "label": "A year in the future",       "hint": "e.g., 3099"},
            {"key": "adj1",     "label": "An adjective",               "hint": "e.g., bewildered"},
            {"key": "figure",   "label": "A historical figure",        "hint": "e.g., Julius Caesar"},
            {"key": "object1",  "label": "A modern object",            "hint": "e.g., a selfie stick"},
            {"key": "verb1",    "label": "A verb (past tense)",        "hint": "e.g., texted"},
            {"key": "verb2",    "label": "Another verb (past tense)",  "hint": "e.g., challenged"},
            {"key": "food",     "label": "A type of food",             "hint": "e.g., a cheeseburger"},
            {"key": "number",   "label": "A number",                   "hint": "e.g., 6"},
            {"key": "creature", "label": "A creature from the future", "hint": "e.g., robot penguin"},
            {"key": "adj2",     "label": "Another adjective",          "hint": "e.g., glowing"},
            {"key": "adj3",     "label": "A third adjective",          "hint": "e.g., non-chronological"},
        ],
        "template": (
            "{inventor} had finally done it: a working time machine, built from {number} washing machines and hope. "
            "The plan was simple — visit {year1}, observe quietly, return home for tea. "
            "Instead, {inventor} pressed the wrong button and arrived in {year1} wearing a {adj1} expression "
            "and holding {object1}, which {figure} immediately {verb1} about on the royal scroll. "
            "{figure} {verb2} {inventor} to explain the strange device, described by {inventor} as "
            "'a {adj2} portal for {adj3} navigation.' "
            "{figure} demanded {number} of them immediately and offered payment in {food}. "
            "{inventor} panicked, hit the machine again, and skipped to {year2}, "
            "where {number} {creature}s were worshipping {object1} as a relic from a forgotten age. "
            "The {adj2} {creature}s bowed respectfully and offered {food} in tribute. "
            "It took {inventor} three more jumps and {number} accidental detours through {year1} "
            "to finally get home — arriving {adj3}, slightly {adj1}, and refusing to speak about {figure}."
        ),
    },
    {
        "id": 18,
        "title": "The Haunted Hotel Check-In",
        "description": "Five stars. Complimentary breakfast. Minor ghost situation. Read the reviews first.",
        "emoji": "🏨",
        "category": "Spooky",
        "difficulty": "hard",
        "blanks": [
            {"key": "guest",     "label": "The guest's name",          "hint": "e.g., Reginald"},
            {"key": "hotel",     "label": "A hotel name",              "hint": "e.g., Hotel Peculiar"},
            {"key": "room",      "label": "A room number",             "hint": "e.g., 666"},
            {"key": "adj1",      "label": "An adjective",              "hint": "e.g., eerily"},
            {"key": "ghost",     "label": "A ghost's name",            "hint": "e.g., Lord Wailsworth"},
            {"key": "adj2",      "label": "Another adjective",         "hint": "e.g., translucent"},
            {"key": "complaint", "label": "A petty complaint",         "hint": "e.g., the Wi-Fi is too slow"},
            {"key": "food",      "label": "A breakfast food",          "hint": "e.g., haunted porridge"},
            {"key": "verb1",     "label": "A verb (past tense)",       "hint": "e.g., levitated"},
            {"key": "verb2",     "label": "Another verb (past tense)", "hint": "e.g., rattled"},
            {"key": "object",    "label": "A random hotel object",     "hint": "e.g., the ironing board"},
            {"key": "number",    "label": "A number",                  "hint": "e.g., 47"},
            {"key": "adj3",      "label": "A third adjective",         "hint": "e.g., surprisingly comfortable"},
        ],
        "template": (
            "{guest} checked into {hotel} expecting a quiet night. Room {room} was {adj1} perfect — "
            "until the wardrobe {verb2} open at midnight to reveal {ghost}, a {adj2} ghost in a velvet jacket. "
            "{ghost} floated to the bedside and said, 'I have {number} complaints about your stay so far.' "
            "'{guest},' {ghost} continued solemnly, '{complaint}.' "
            "{guest} blinked. 'You are a ghost. Why do you care about {complaint}?' "
            "{ghost} {verb1} to the ceiling, offended. The {object} {verb2} across the room on its own. "
            "By 3am, {guest} and {ghost} were sitting in {adj2} armchairs eating {food} "
            "and arguing about the hotel's {adj1} {number}-star reviews online. "
            "{ghost} admitted they had written {number} of the reviews themselves. "
            "The bed, {guest} noted, was {adj3}. "
            "They left a glowing review: 'Outstanding stay. {ghost} is {adj2} but {adj3}. "
            "Would recommend to anyone who enjoys {food} and does not mind the {object} situation.'"
        ),
    },
]
