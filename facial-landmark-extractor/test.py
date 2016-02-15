import mooddeck
import cohnkanadedb as ckdb
import numpy

# mooddeck.get_landmark_extractor()
# sample_path = "/Users/i851474/Development/iot/mood-detector/facial-landmark-extractor/samples/"
# file_name = "hugh_laurie.jpeg"


db_path = "/Users/i851474/Development/iot/datasets/cohn-kanade-db"
emotions = ckdb.get_emotions(db_path)

extractor = mooddeck.get_landmark_extractor()
classifier = mooddeck.get_classifier()


# create a subset of emotions, only for testing purposes
emotions = emotions[0:10]
all_features = []

for e in emotions:
    print "Subject: {}, Sequence: {}, Emotion Label: {}".format(e[0], e[1], e[2])

def load_model():
    global classifier

    classifier.load()

def load_database_features():
    global all_features
    global emotions

    all_features = []
    for e in emotions:
        subject = e[0]
        sequence = e[1]
        img_path = ckdb.get_image_path(db_path, subject, sequence)
        features = extractor.extract(img_path)
        if len(all_features) == 0:
            all_features = features[0]
        else:
            all_features = numpy.vstack([all_features, features[0]])

def train_model():
    global all_features
    global classifier
    global emotions

    emotion_labels = numpy.array(emotions)[:,2]
    classifier.train(all_features, emotion_labels)
    classifier.save()

load_database_features()

# train_model()

load_model()

prediction = classifier.predict(all_features)

print prediction

"""
for e in all_features:
    img_path = ckdb.get_image_path(db_path, subject, sequence)
    features = extractor.extract(img_path)
    prediction = classifier.predict(features)
    print prediction
"""





