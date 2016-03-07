__author__ = 'Andre Pires'

from flask import Flask
from flask_restful import Resource, Api
from mood.service import PictureModelService, MoodService
from flask import request
import json
from flask_restful import reqparse

app = Flask(__name__)
api = Api(app)

class Mood(Resource):

    def __init__(self):
        self.mood_service = MoodService()

    def get(self, uid):
        mood_process = self.mood_service.get_mood(uid)
        return mood_process.to_json()

    def put(self, uid):
        mood_process = self.mood_service.perfom_mood_detection(uid)
        return mood_process.to_json()


class Picture(Resource):

    def __init__(self):
        self.picture_model_service = PictureModelService()

    def get(self, uid):
        picture = self.picture_model_service.find_by_key(uid)
        return picture.to_json()

class PictureList(Resource):

    def __init__(self):
        self.picture_model_service = PictureModelService()
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('limit', type=int)

    def post(self):
        args = self.parser.parse_args()
        limit = args['limit']
        query = json.loads(request.data)
        picture_list = self.picture_model_service.find_by_query(query, limit)
        ret = []
        for picture in picture_list:
            ret.append(picture.to_json())
        return ret


api.add_resource(Mood, '/moods/<string:uid>')
api.add_resource(Picture, '/pictures/<string:uid>')
api.add_resource(PictureList, '/pictures')

if __name__ == '__main__':
    app.run(debug=True)
