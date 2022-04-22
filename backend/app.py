from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from routine import get_simplified_routine


app = Flask(__name__)
CORS(app)
api = Api(app)

parser = reqparse.RequestParser()


class Routine(Resource):

    def post(self):

        parser.add_argument("courses", type=str)
        args = parser.parse_args()
        courses = args["courses"]

        if not courses:
            return {}

        courses = courses.replace(" ", "")
        courses = courses.upper()
        courses = courses.split(sep=",")

        # TODO IMPORTANT need to change the sheet if they change it in xlsx file
        routine = get_simplified_routine(course_codes=courses, sheet="ROUTINE")
        return routine


api.add_resource(Routine, '/')

if __name__ == '__main__':
    app.run(debug=True)

# if __name__ == '__main__':
#     app.run()
