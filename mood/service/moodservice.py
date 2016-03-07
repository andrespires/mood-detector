__author__ = 'Andre Pires'

from picturemodelservice import PictureModelService
import mood.mooddeck as mooddeck
import datetime
from mood.model.models import MoodProcess, Face, Point
import mood.settings.const as const


class MoodService(object):

    def __init__(self):
        print const.landmark_predictor_path
        self.extractor = mooddeck.get_landmark_extractor(const.landmark_predictor_path)
        self.classifier = mooddeck.get_classifier()
        self.classifier.load()

    """
        Get mood process by picture uid
    """
    def get_mood(self, uid):
        picture_model_service = PictureModelService()
        picture = picture_model_service.find_by_key(uid)
        if picture is not None and picture.mood_process is not None:
            return picture.mood_process
        else:
            return []

    """
        Perform mood detection
    """
    def perfom_mood_detection(self, uid):
        picture_model_service = PictureModelService()
        picture = picture_model_service.find_by_key(uid)
        if picture is None or picture.image_path is None:
            return []

        mood_process = MoodProcess()
        mood_process.startDate = datetime.datetime.utcnow()
        # extract features and landmarks
        feature_landmarks = self.extractor.extract_with_landmark(picture.image_path)
        # for each feature/landmark predict mood and convert landmark to points
        for feature_landmark in feature_landmarks:
            face = Face()
            mood = self.classifier.predict(feature_landmark.features)
            face.mood = const.moods[int(mood[0])]
            face.points = self.convert2points(feature_landmark.landmark)
            mood_process.faces.append(face)
        mood_process.endDate = datetime.datetime.utcnow()

        picture.mood_process = mood_process
        # save picture model
        picture_model_service.save(picture)
        return picture.mood_process


    def convert2points(self, landmark):
        size = landmark.shape
        points = []
        for x in range(0, size[0]):
            point = Point()
            p = landmark[x]
            point.x = p[0, 0]
            point.y = p[0, 1]
            points.append(point)
        return points

