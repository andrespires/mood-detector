"""Facial Landmark Extractor

"""
import faciallandmark


def get_landmark_extractor(predictor_path):
    return faciallandmark.LandmarkExtractor(predictor_path)
