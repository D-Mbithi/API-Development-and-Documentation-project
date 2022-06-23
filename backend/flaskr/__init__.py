from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category, db

QUESTIONS_PER_PAGE = 10


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    """
    @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    """

    CORS(app)

    """
    @DONE TODO: Use the after_request decorator to set Access-Control-Allow
    """

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS"
        )
        return response

    """
    @DONE TODO:
    Create an endpoint to handle GET requests
    for all available categories.
    """

    @app.route('/categories')
    def get_categories():
        categories = {category.id:category.type for category in Category.query.all()}

        return jsonify({
            'success': True,
            'categories': categories
        })

    """
    @DONE TODO:
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories.

    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions.
    """

    @app.route('/questions')
    def get_questions():
        page = request.args.get('page', 1, type=int)
        category_id = request.args.get('category_id')

        if category_id == None:
            category_id = 1

        start = (page - 1) * QUESTIONS_PER_PAGE
        end = start + QUESTIONS_PER_PAGE

        questions = [question.format() for question in Question.query.all()[start:end]]
        categories = {category.id:category.type for category in Category.query.all()}

        current_category = Category.query.all()[0]
        current_category = current_category.format()

        total_questions = len(Question.query.all())

        return jsonify({
            'success': True,
            'questions': questions,
            'categories': categories,
            'current_category': current_category,
            'total_questions': total_questions
        })

    """
    @DONE TODO:
    Create an endpoint to DELETE question using a question ID.

    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page.
    """

    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_questions(question_id):
        question = Question.query.get_or_404(question_id)
        question.delete()

        return jsonify({
            'success': True,
            'message': 'Question  deleted'
        })

    """
    @DONE TODO:
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab,
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.
    """

    @app.route('/questions', methods=['POST'])
    def create_question():
        json_data = request.get_json()

        print(json_data)

        question = Question(
            question = json_data['question'],
            answer = json_data['answer'],
            category = json_data['category'],
            difficulty = json_data['difficulty']
        )

        question.insert()

        return jsonify({
            'success': True,
            'message': 'Question created'
        })

    """
    @DONE TODO:
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.

    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    """

    @app.route('/search', methods=['POST'])
    def search_question():
        json_data = request.get_json()
        search_term = json_data['searchTerm']

        questions = [
            question.format() for question in Question.query.filter(
                Question.question.ilike(f'%{search_term}%')
            ).all()
        ]

        return jsonify({
            'success': True,
            'questions': questions
        })

    """
    @DONE TODO:
    Create a GET endpoint to get questions based on category.

    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    """

    @app.route('/categories/<category_id>/questions')
    def get_questions_by_category(category_id):
        questions = [
            question.format() for question in Question.query.filter_by(
                category=category_id
            ).all()
        ]

        return jsonify({
            'success': True,
            'questions': questions
        })

    """
    @TODO:
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    """

    @app.route('/quizzes', methods=['POST'])
    def quizzes():
        json_data = request.get_json()

        previous_question = json_data['previous_questions']
        category = json_data['quiz_category']

        previous_questions = []
        questions = [
            question.id for question in Question.query.filter_by(
                category=category['id']
            ).all()
        ]
        selection = random.choice(questions)

        question = Question.query.get_or_404(selection)

        question = question.format()

        return jsonify({
            'success': True,
            'question': question
        })

    """
    @DONE TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    """

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Resource Not Found'
        }), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': 'Method Not Allowed'
        }), 405

    @app.errorhandler(422)
    def unprocessable_entity(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'Unprocessable Entity'
        }), 422

    return app
