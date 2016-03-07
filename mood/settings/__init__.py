__author__ = 'Andre Pires'

from pymongo import MongoClient
import const

DATABASES = {
    'default' : {
        'ENGINE': 'django_mongodb_engine',
        'NAME': 'picture_db'
    }
}

INSTALLED_APPS = (

)

const.mongodb_client = MongoClient('localhost', 27017)
const.db = const.mongodb_client.picture_db

# classifier
const.moods = ["neutral", "angry", "showing contempt", "disgusted", "afraid", "happy", "sad", "surprised"]

const.app_root = "/Users/i851474/Development/iot/mood-detector"
const.landmark_predictor_path = const.app_root + "/mood/config/shape_predictor_68_face_landmarks.dat"
const.pca_model_path = const.app_root + "/../ml-model/pca.pkl"
const.classifier_model_path = const.app_root + "/../ml-model/classifier.pkl"


