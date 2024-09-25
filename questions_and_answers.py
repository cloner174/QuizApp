#
questions = [
    # Easy Questions (20)
    {
        "id": 1,
        "question": "What is the output of `print(2 ** 3)`?",
        "options": ["5", "6", "8", "9"],
        "answer": "8",
        "difficulty": "easy"
    },
    {
        "id": 2,
        "question": "Which data type is immutable in Python?",
        "options": ["List", "Dictionary", "Set", "Tuple"],
        "answer": "Tuple",
        "difficulty": "easy"
    },
    {
        "id": 3,
        "question": "What keyword is used to define a function in Python?",
        "options": ["func", "define", "def", "function"],
        "answer": "def",
        "difficulty": "easy"
    },
    {
        "id": 4,
        "question": "Which method is used to add an element to a list?",
        "options": ["append()", "add()", "insert()", "push()"],
        "answer": "append()",
        "difficulty": "easy"
    },
    {
        "id": 5,
        "question": "How do you start a comment in Python?",
        "options": ["//", "#", "/*", "<!--"],
        "answer": "#",
        "difficulty": "easy"
    },
    {
        "id": 6,
        "question": "Which keyword is used for exception handling?",
        "options": ["try", "catch", "except", "handle"],
        "answer": "except",
        "difficulty": "easy"
    },
    {
        "id": 7,
        "question": "What is the output of `print(type([]))`?",
        "options": ["<class 'list'>", "<class 'tuple'>", "<class 'dict'>", "Error"],
        "answer": "<class 'list'>",
        "difficulty": "easy"
    },
    {
        "id": 8,
        "question": "Which operator is used for floor division?",
        "options": ["/", "//", "%", "**"],
        "answer": "//",
        "difficulty": "easy"
    },
    {
        "id": 9,
        "question": "Which keyword is used to create a class?",
        "options": ["class", "def", "object", "struct"],
        "answer": "class",
        "difficulty": "easy"
    },
    {
        "id": 10,
        "question": "What is the correct file extension for Python files?",
        "options": [".pyth", ".pt", ".pyt", ".py"],
        "answer": ".py",
        "difficulty": "easy"
    },
    {
        "id": 11,
        "question": "Which of the following is a Python tuple?",
        "options": ["[1, 2, 3]", "(1, 2, 3)", "{1, 2, 3}", "{'a':1, 'b':2}"],
        "answer": "(1, 2, 3)",
        "difficulty": "easy"
    },
    {
        "id": 12,
        "question": "How do you create a virtual environment in Python?",
        "options": ["python -m venv env", "virtualenv env", "Both A and B", "None of the above"],
        "answer": "Both A and B",
        "difficulty": "easy"
    },
    {
        "id": 13,
        "question": "What does PEP stand for in Python?",
        "options": ["Python Enhancement Proposal", "Python Executive Program", "Python Essential Package", "Python Extended Protocol"],
        "answer": "Python Enhancement Proposal",
        "difficulty": "easy"
    },
    {
        "id": 14,
        "question": "Which of the following is used to define a block of code in Python?",
        "options": ["Brackets", "Braces", "Indentation", "None of the above"],
        "answer": "Indentation",
        "difficulty": "easy"
    },
    {
        "id": 15,
        "question": "What is the method to convert a string to lowercase in Python?",
        "options": ["lower()", "toLowerCase()", "convert()", "None of the above"],
        "answer": "lower()",
        "difficulty": "easy"
    },
    {
        "id": 16,
        "question": "Which of the following is not a keyword in Python?",
        "options": ["lambda", "with", "async", "yielding"],
        "answer": "yielding",
        "difficulty": "easy"
    },
    {
        "id": 17,
        "question": "How do you start a loop that never ends in Python?",
        "options": ["for True:", "while True:", "loop:", "forever:"],
        "answer": "while True:",
        "difficulty": "easy"
    },
    {
        "id": 18,
        "question": "Which of the following is used to handle exceptions in Python?",
        "options": ["try-except", "catch-finally", "handle-error", "raise-try"],
        "answer": "try-except",
        "difficulty": "easy"
    },
    {
        "id": 19,
        "question": "What is the correct way to create a dictionary in Python?",
        "options": ["{1: 'a', 2: 'b'}", "[(1, 'a'), (2, 'b')]", "[1: 'a', 2: 'b']", "None of the above"],
        "answer": "{1: 'a', 2: 'b'}",
        "difficulty": "easy"
    },
    {
        "id": 20,
        "question": "Which function is used to read a line from standard input?",
        "options": ["readline()", "read()", "input()", "get()"],
        "answer": "input()",
        "difficulty": "easy"
    },
    
    # Medium Questions (10)
    {
        "id": 21,
        "question": "What is a lambda function in Python?",
        "options": [
            "A function defined with the lambda keyword",
            "A type of loop",
            "A built-in function for logging",
            "None of the above"
        ],
        "answer": "A function defined with the lambda keyword",
        "difficulty": "medium"
    },
    {
        "id": 22,
        "question": "Which of the following is not a valid way to declare a variable in Python?",
        "options": [
            "var1 = 10",
            "1var = 10",
            "_var = 10",
            "var_1 = 10"
        ],
        "answer": "1var = 10",
        "difficulty": "medium"
    },
    {
        "id": 23,
        "question": "How can you copy an object in Python?",
        "options": [
            "Using the copy() method",
            "Using the deepcopy() method",
            "Using the list() constructor",
            "All of the above"
        ],
        "answer": "All of the above",
        "difficulty": "medium"
    },
    {
        "id": 24,
        "question": "What is the purpose of the `__init__` method in a Python class?",
        "options": [
            "To initialize the class variables",
            "To create a new instance of the class",
            "Both A and B",
            "None of the above"
        ],
        "answer": "Both A and B",
        "difficulty": "medium"
    },
    {
        "id": 25,
        "question": "Which statement is used to handle exceptions in Python?",
        "options": [
            "try-except",
            "catch-finally",
            "handle-error",
            "raise-try"
        ],
        "answer": "try-except",
        "difficulty": "medium"
    },
    {
        "id": 26,
        "question": "What does the `*args` parameter do in a Python function?",
        "options": [
            "Accepts a variable number of keyword arguments",
            "Accepts a variable number of non-keyword arguments",
            "Unpacks a list",
            "None of the above"
        ],
        "answer": "Accepts a variable number of non-keyword arguments",
        "difficulty": "medium"
    },
    {
        "id": 27,
        "question": "Which method can be used to return the first element that matches a condition in a list?",
        "options": [
            "find()",
            "search()",
            "next(filter(...))",
            "match()"
        ],
        "answer": "next(filter(...))",
        "difficulty": "medium"
    },
    {
        "id": 28,
        "question": "What is the output of the following code?\n```python\ndef func(x, y=2, z=3):\n    return x + y + z\n\nprint(func(1, z=4))\n```",
        "options": ["6", "7", "5", "Error"],
        "answer": "7",
        "difficulty": "medium"
    },
    {
        "id": 29,
        "question": "Which built-in function can be used to determine the number of items in a list?",
        "options": ["count()", "length()", "len()", "size()"],
        "answer": "len()",
        "difficulty": "medium"
    },
    {
        "id": 30,
        "question": "How do you start a Python interactive debugger?",
        "options": [
            "import pdb; pdb.set_trace()",
            "import debugger; debugger.start()",
            "debugger.start()",
            "pdb.start()"
        ],
        "answer": "import pdb; pdb.set_trace()",
        "difficulty": "medium"
    },
    
    # Hard Questions (10)
    {
        "id": 31,
        "question": "What is a generator in Python?",
        "options": [
            "A function that returns a list",
            "A function that yields values one at a time",
            "A type of class",
            "None of the above"
        ],
        "answer": "A function that yields values one at a time",
        "difficulty": "hard"
    },
    {
        "id": 32,
        "question": "Which of the following best describes decorators in Python?",
        "options": [
            "Functions that modify the behavior of other functions",
            "Classes that inherit from other classes",
            "Modules that extend functionality",
            "None of the above"
        ],
        "answer": "Functions that modify the behavior of other functions",
        "difficulty": "hard"
    },
    {
        "id": 33,
        "question": "What is the purpose of the `__slots__` declaration in a Python class?",
        "options": [
            "To define private variables",
            "To prevent the dynamic creation of attributes",
            "To create multiple inheritance",
            "None of the above"
        ],
        "answer": "To prevent the dynamic creation of attributes",
        "difficulty": "hard"
    },
    {
        "id": 34,
        "question": "How can you achieve multithreading in Python?",
        "options": [
            "Using the `threading` module",
            "Using the `multiprocessing` module",
            "Using the `asyncio` module",
            "All of the above"
        ],
        "answer": "Using the `threading` module",
        "difficulty": "hard"
    },
    {
        "id": 35,
        "question": "What does the `@staticmethod` decorator do in a Python class?",
        "options": [
            "Defines a method that doesn't receive the instance as the first argument",
            "Defines a method that can only be accessed by the class itself",
            "Defines a method that can modify class state",
            "None of the above"
        ],
        "answer": "Defines a method that doesn't receive the instance as the first argument",
        "difficulty": "hard"
    },
    {
        "id": 36,
        "question": "Which of the following is true about the GIL (Global Interpreter Lock) in Python?",
        "options": [
            "It allows multiple native threads to execute Python bytecodes at once.",
            "It prevents multiple native threads from executing Python bytecodes simultaneously.",
            "It is specific to the `asyncio` module.",
            "None of the above."
        ],
        "answer": "It prevents multiple native threads from executing Python bytecodes simultaneously.",
        "difficulty": "hard"
    },
    {
        "id": 37,
        "question": "What is the difference between `@classmethod` and `@staticmethod` in Python?",
        "options": [
            "`@classmethod` receives the class as the first argument, while `@staticmethod` does not.",
            "`@staticmethod` receives the class as the first argument, while `@classmethod` does not.",
            "Both receive the class as the first argument.",
            "Neither receives the class as the first argument."
        ],
        "answer": "`@classmethod` receives the class as the first argument, while `@staticmethod` does not.",
        "difficulty": "hard"
    },
    {
        "id": 38,
        "question": "What is metaprogramming in Python?",
        "options": [
            "Writing programs that can modify themselves",
            "Using multiple inheritance in classes",
            "Creating decorators",
            "Using generators"
        ],
        "answer": "Writing programs that can modify themselves",
        "difficulty": "hard"
    },
    {
        "id": 39,
        "question": "How do you make a Python class iterable?",
        "options": [
            "Implement the `__iter__` and `__next__` methods",
            "Inherit from the `Iterator` class",
            "Use the `@iter` decorator",
            "None of the above"
        ],
        "answer": "Implement the `__iter__` and `__next__` methods",
        "difficulty": "hard"
    },
    {
        "id": 40,
        "question": "Which of the following is a correct way to create a context manager in Python?",
        "options": [
            "Using the `with` statement and implementing `__enter__` and `__exit__` methods",
            "Using the `async with` statement",
            "Using the `try-except` block",
            "Both A and B"
        ],
        "answer": "Using the `with` statement and implementing `__enter__` and `__exit__` methods",
        "difficulty": "hard"
    },
    {
        'id': 41,
        'question': 'What will be the output of the following code?',
        'code_snippet': 'print("Hello, World!")',
        'options': ['Hello, World!', 'hello, world!', 'Error', 'None'],
        'answer': 'Hello, World!',
        'difficulty': 'easy'
    },
    {
        'id': 42,
        'question': 'Which of the following is a mutable data type in Python?',
        'options': ['Tuple', 'String', 'List', 'Integer'],
        'answer': 'List',
        'difficulty': 'easy'
    },
    {
        'id': 43,
        'question': 'What does the "len()" function do in Python?',
        'options': ['Returns the length of an object', 'Calculates numerical expressions', 'Converts data types', 'Prints output to the console'],
        'answer': 'Returns the length of an object',
        'difficulty': 'medium'
    },
    {
        'id': 44,
        'question': 'What is the output of the following code?',
        'code_snippet': 'print(type( (1, 2, 3) ))',
        'options': ["<class 'list'>", "<class 'dict'>", "<class 'tuple'>", "<class 'set'>"],
        'answer': "<class 'tuple'>",
        'difficulty': 'medium'
    },
    {
        'id': 45,
        'question': 'Which keyword is used to create a function in Python?',
        'options': ['func', 'def', 'function', 'lambda'],
        'answer': 'def',
        'difficulty': 'hard'
    },
    {
        'id': 46,
        'question': 'What is the output of the following code?',
        'code_snippet': 'print(2 ** 3 ** 2)',
        'options': ['512', '64', '256', 'None of the above'],
        'answer': '512',
        'difficulty': 'hard'
    },
]