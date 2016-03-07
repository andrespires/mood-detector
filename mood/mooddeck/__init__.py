import os
import glob

import classifier
import faciallandmark

faciallandmark_dft = None
classifier_dft = None

def get_landmark_extractor(predictor_path="./config/shape_predictor_68_face_landmarks.dat"):
    global faciallandmark_dft

    if faciallandmark_dft is None:
        faciallandmark_dft = faciallandmark.get_landmark_extractor(predictor_path)
    return faciallandmark_dft


def get_classifier():
    global classifier_dft
    if classifier_dft is None:
        classifier_dft = classifier.get_classifier()
    return classifier_dft

def train(self, image_path):
    print "Start training procedure"
    allFeatures = []
    for f in glob.glob(os.path.join(image_path, "*")):
        allFeatures.append(faciallandmark_dft.extract(f))