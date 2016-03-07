import datetime
import unittest

from mood.model.models import Picture, Face, Point, MoodProcess
from mood.service import PictureModelService, MoodService


class TestPictureModelService(unittest.TestCase):

    def save_picture(self):
        picture_model_service = PictureModelService()

        p1 = Point(x = 1, y = 1)
        p2 = Point(x = 2, y = 2)
        p3 = Point(x = 3, y = 3)
        p4 = Point(x = 4, y = 4)


        f1 = Face(
            mood = 'neutral', points = [p1, p2]
        )
        f2 = Face(
            mood = 'happy', points = [p3, p4]
        )
        moodProcess = MoodProcess(
            startDate = datetime.datetime.utcnow(),
            endDate = datetime.datetime.utcnow(),
            faces = [f1, f2]
        )
        pic = Picture(
            uid="12345",
            device="pi1",
            location="roomA",
            image_path = "/Users/i851474/Development/iot/mood-detector/mood/samples/hugh_laurie.jpeg",
            date=datetime.datetime.utcnow(),
            modified_date=datetime.datetime.utcnow(),
            mood_process = moodProcess
        )
        picture_model_service.save(pic)


    def test_get_mood_process(self):
        self.save_picture()

        mood_service = MoodService()
        mood_process = mood_service.get_mood("12345")
        self.assertEqual(2, len(mood_process.faces))


    def test_process_single_image(self):
        self.save_picture()
        mood_service = MoodService()
        mood_process = mood_service.perfom_mood_detection("12345")
        mood_process_get = mood_service.get_mood("12345")

        self.assertEqual(1, len(mood_process.faces))
        self.assertEqual(1, len(mood_process_get.faces))
        self.assertEqual(mood_process.faces[0].mood, mood_process_get.faces[0].mood)



if __name__ == '__main__':
    unittest.main()