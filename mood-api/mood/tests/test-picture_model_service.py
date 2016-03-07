import datetime
import unittest

from mood.model.models import Picture, Face, Point, MoodProcess
from mood.service import PictureModelService


class TestPictureModelService(unittest.TestCase):

    def test_save_picture(self):
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
            date=datetime.datetime.utcnow(),
            modified_date=datetime.datetime.utcnow(),
            mood_process = moodProcess
        )
        modified_count = picture_model_service.save(pic)
        self.assertEqual(1, modified_count)


    def test_update_picture(self):
        picture_model_service = PictureModelService()

        pic = Picture(
            uid="12345",
            device="pi2",
            location="roomA",
            date=datetime.datetime.utcnow(),
            modified_date=datetime.datetime.utcnow(),
        )
        picture_model_service.save(pic)
        same_pic = picture_model_service.find_by_key(pic.uid)

        self.assertEqual(same_pic.uid, pic.uid)
        self.assertEqual("pi2", same_pic.device)


    def test_delete_picture(self):
        picture_model_service = PictureModelService()

        pic = Picture(
            uid="abc",
            device="pi1",
            location="roomA",
            date=datetime.datetime.utcnow(),
            modified_date=datetime.datetime.utcnow()
        )

        picture_model_service.save(pic)
        deleted_count = picture_model_service.delete(pic.uid)
        self.assertEqual(1, deleted_count)


if __name__ == '__main__':
    unittest.main()