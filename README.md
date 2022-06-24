# API Development and Documentation Final Project

## Trivia App

Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a webpage to manage the trivia app and play the game, but their API experience is limited and still needs to be built out.

That's where you come in! Help them finish the trivia app so they can start holding trivia and seeing who's the most knowledgeable of the bunch. The application must:

1. Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer.
2. Delete questions.
3. Add questions and require that they include question and answer text.
4. Search for questions based on a text query string.
5. Play the quiz game, randomizing either all questions or within a specific category.

Completing this trivia app will give you the ability to structure plan, implement, and test an API - skills essential for enabling your future applications to communicate with others.

## Starting and Submitting the Project

[Fork](https://help.github.com/en/articles/fork-a-repo) the project repository and [clone](https://help.github.com/en/articles/cloning-a-repository) your forked repository to your machine. Work on the project locally and make sure to push all your changes to the remote repository before submitting the link to your repository in the Classroom.

## About the Stack

We started the full stack application for you. It is designed with some key functional areas:

### Backend

The [backend](./backend/README.md) directory contains a partially completed Flask and SQLAlchemy server. You will work primarily in `__init__.py` to define your endpoints and can reference models.py for DB and SQLAlchemy setup. These are the files you'd want to edit in the backend:

1. `backend/flaskr/__init__.py`
2. `backend/test_flaskr.py`

> View the [Backend README](./backend/README.md) for more details.

### Frontend

The [frontend](./frontend/README.md) directory contains a complete React frontend to consume the data from the Flask server. If you have prior experience building a frontend application, you should feel free to edit the endpoints as you see fit for the backend you design. If you do not have prior experience building a frontend application, you should read through the frontend code before starting and make notes regarding:

1. What are the end points and HTTP methods the frontend is expecting to consume?
2. How are the requests from the frontend formatted? Are they expecting certain parameters or payloads?

Pay special attention to what data the frontend is expecting from each API response to help guide how you format your API. The places where you may change the frontend behavior, and where you should be looking for the above information, are marked with `TODO`. These are the files you'd want to edit in the frontend:

1. `frontend/src/components/QuestionView.js`
2. `frontend/src/components/FormView.js`
3. `frontend/src/components/QuizView.js`

By making notes ahead of time, you will practice the core skill of being able to read and understand code and will have a simple plan to follow to build out the endpoints of your backend API.

## Running the server

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
export DB_USER=<username>
export DB_PASSWORD=<password>

flask run
```

## Running Your Frontend in Dev Mode

```bash
npm install
npm run start
```

## Endpoints

### GET /questions

Request:

A GET request is made and it fetches all questions and returns a json response.

Example: ```curl http://localhost:5000/questions```

Parameters: None

Response body

```json
{
    "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
    },
    "current_category": {
        "id": 1,
        "type": "Science"
    },
    "questions": [
        {
            "answer": "Maya Angelou",
            "category": 4,
            "difficulty": 2,
            "id": 5,
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        },
        {
            "answer": "Muhammad Ali",
            "category": 4,
            "difficulty": 1,
            "id": 9,
            "question": "What boxer's original name is Cassius Clay?"
        }
        .... #Data truncated
    ],
    "success": true,
    "total_questions": 24
}
```

### POST /questions

Request:
A POST request is made and it creates new question object and returns a json response of total number of questions.

Parameters: json Data

```json
data = {
    question = 'test question',
    answer = 'test answer',
    category = 1,
    difficulty = 1
}
```

Example: ```curl -X POST http://localhost:5000/questions -D data```

Response:

```json
{
    'success': True,
    'message': 'Question created'
    'total_questions': total_questions
}
```

### DELETE /questions/<question_id>

Request:

A DELETE request is made to delete a question object from database with question id as input.
Return number success message and number of questions remaining.

Example: ```curl -X DELETE http://localhost:5000/questions/<question_id>```

Response:

```json
{
    'success': True,
    'message': 'Question deleted'
    'total_questions': total_questions
}
```

### GET /categories

Request:

A GET request is made and it fetches all questions and returns a json response with all categories.

Example: ```curl http://localhost:5000/categories```

Response:

```json
{
    "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
    },
    "success": true
}
```

### GET /categories/<categories_id>/questions

Request:

A GET request is made and it fetches all questions, filtered by categories_id and returns a json response.

Example: ```curl http://localhost:5000/categories/<categories_id>/questions```

Response:

```json
{
    "questions": [
        {
            "answer": "Maya Angelou",
            "category": 4,
            "difficulty": 2,
            "id": 5,
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        },
        {
            "answer": "Muhammad Ali",
            "category": 4,
            "difficulty": 1,
            "id": 9,
            "question": "What boxer's original name is Cassius Clay?"
        },
    ],
    "success": true
}

```

### POST /quizzes

Request:

A POST request is made with categories_id and it fetches a random questions from the category and returns a json response the question.

```json
data = {
    "previous_questions": [],
    "category_id": 1
}
```

Example: ```curl -X POST http://localhost:5000/quizzes -D data```

Response:

```json
{
    'id': 27,
    'question': 'test question?',
    'answer': 'test answer',
    'category': 1,
    'difficulty': 3
}
```

### GET /categories/<category_id>/questions

Request

Example: ```curl http://localhost:5000/categories/<category_id>/questions```

### POST /search

Request:

A POST request is made with search term as a json data and it fetches all questions with search term as a substring in the question and returns a json response of all questions.

```json
data = {
    'searchTerm': 'test'
}
```

Example: ``` curl -X POST  http://localhost:5000/search -D data ```

## Error Handlers

When an error occurs, one of the following errors is returned as json.

- 400 Bad request
- 404 Resource not Found
- 405 Method Not Allowed
- 422 Unprocessable Entity

Response:

```json
{
    'sucess': False,
    'error': <error code>,
    'message': '<error message>'
}

```

## Testing

Running tests for the projects.

```bash

dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py

```
