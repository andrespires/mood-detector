__author__ = 'Andre Pires'

from jsonobject import *

class Point(JsonObject):
    x = DecimalProperty()
    y = DecimalProperty()

class Face(JsonObject):
    mood = StringProperty()
    points = ListProperty(Point)

    def add_point(self, point):
        self.points.append(point)

class MoodProcess(JsonObject):
    startDate = DateTimeProperty()
    endDate = DateTimeProperty()
    faces = ListProperty(Face)

    def add_face(self, face):
        self.faces.append(face)

class Picture(JsonObject):

    uid = StringProperty()
    device = StringProperty()
    location = StringProperty()
    image_path = StringProperty()
    date = DateTimeProperty()
    modified_date = DateTimeProperty()
    mood_process = ObjectProperty(MoodProcess)














