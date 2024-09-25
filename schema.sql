DROP TABLE IF EXISTS scores;
CREATE TABLE scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    score INTEGER NOT NULL,
    difficulty TEXT NOT NULL,
    timestamp TEXT NOT NULL
);

DROP TABLE IF EXISTS wrong_answers;
CREATE TABLE wrong_answers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    question TEXT NOT NULL,
    your_answer TEXT NOT NULL,
    correct_answer TEXT NOT NULL
);
