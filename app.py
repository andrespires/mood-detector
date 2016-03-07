__author__ = 'Andre Pires'

from flask import Flask
from flask_restful import Resource, Api
from mood.service import PictureModelService, MoodService

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



api.add_resource(Mood, '/mood/<string:uid>')
api.add_resource(Picture, '/picture/<string:uid>')

if __name__ == '__main__':
    app.run(debug=True)
