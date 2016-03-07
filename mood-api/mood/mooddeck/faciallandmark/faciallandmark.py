#!/usr/bin/python


import dlib
from skimage import io
import math
import numpy

__all__ = [
    'LandmarkExtractor', 'FeatureMatrix'
]


class LandmarkExtractor(object):
    """
        constructor
    """

    def __init__(self, predictor_path):
        """

        :rtype : LandmarkExtractor
        """
        self.predictor_path = predictor_path
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor(self.predictor_path)
        self.featureMatrix = FeatureMatrix()

    """
        extract
    """
    def extract(self, filePath):
        img = io.imread(filePath)
        dets = self.detector(img, 1)
        ## faces detected: len(dets)
        allFeatures = []
        for k, d in enumerate(dets):
            landmarkCoords = self.get_landmarks(img, d)
            features = self.featureMatrix.build(landmarkCoords)
            allFeatures.append(features)
        return allFeatures

    """
        extract features and landmark coords
    """
    def extract_with_landmark(self, filePath):
        img = io.imread(filePath)
        dets = self.detector(img, 1)
        allFeatureLandmarks = []
        for k, d in enumerate(dets):
            feature_landmark = FeatureLandmark()
            feature_landmark.landmark = self.get_landmarks(img, d)
            feature_landmark.features = [self.featureMatrix.build(feature_landmark.landmark)]
            allFeatureLandmarks.append(feature_landmark)
        return allFeatureLandmarks

    """
        getLandmarks
    """
    def get_landmarks(self, image, d):
        """
        :rtype : numpy.matrix
        """
        return numpy.matrix([[p.x, p.y] for p in self.predictor(image, d).parts()])


class FeatureLandmark(object):

    def __init__(self):
        self.features = None
        self.landmark = None

class FeatureMatrix(object):
    """
        constructor
    """
    # def __init__(self):
    #    self.foo

    """
        features
    """

    def build(self, landmarkCoords):
        pointIndices1 = [20, 20, 45, 45]
        pointIndices2 = [58, 9, 58, 58]
        pointIndices3 = [5, 7, 5, 32]
        pointIndices4 = [13, 13, 11, 36]

        size = landmarkCoords.shape
        features = []
        for x in range(0, size[0]):
            for i in range(0, len(pointIndices1)):
                p1 = landmarkCoords[(x + pointIndices1[i] - 1) % size[0]]
                p2 = landmarkCoords[(x + pointIndices2[i] - 1) % size[0]]
                p3 = landmarkCoords[(x + pointIndices3[i] - 1) % size[0]]
                p4 = landmarkCoords[(x + pointIndices4[i] - 1) % size[0]]

                points = [p1, p2, p3, p4]
                features.append(self.ratio(points))
        return features

    """
        ratio
    """

    def ratio(self, points):
        p1 = points[0];
        p2 = points[1];
        p3 = points[2];
        p4 = points[3];

        x1 = p1[0, 0]
        y1 = p1[0, 1]
        x2 = p2[0, 0]
        y2 = p2[0, 1]
        x3 = p3[0, 0]
        y3 = p3[0, 1]
        x4 = p4[0, 0]
        y4 = p4[0, 1]

        dist1 = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        dist2 = math.sqrt((x3 - x4) ** 2 + (y3 - y4) ** 2)
        if dist2 == 0:
            return 0

        ratio = dist1 / dist2
        return ratio

    def equal_point(self, p1, p2):
        x1 = p1[0, 0]
        y1 = p1[0, 1]
        x2 = p2[0, 0]
        y2 = p2[0, 1]

        return x1 == x2 and y1 == y2
