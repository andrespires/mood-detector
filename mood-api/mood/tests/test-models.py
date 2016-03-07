import datetime
import unittest

from mood.model.models import Picture, Face, Point, MoodProcess

class TestModels(unittest.TestCase):

    def test_create_picture(self):
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
        self.assertEqual(pic.device, "pi1")
        json = pic.to_json()
        pic_from_json = Picture(json)
        self.assertEqual(pic.uid, pic_from_json.uid)
        self.assertEqual(pic.device, pic_from_json.device)
        self.assertEqual(pic.location, pic_from_json.location)
        self.assertEqual(pic.date, pic_from_json.date)
        self.assertEqual(pic.modified_date, pic_from_json.modified_date)
        self.assertEqual(len(pic.mood_process.faces), len(pic_from_json.mood_process.faces))


if __name__ == '__main__':
    unittest.main()