from __future__ import division
import mooddeck
import cohnkanadedb as ckdb
import numpy

db_path = "/Users/i851474/Development/iot/datasets/cohn-kanade-db"
emotions = ckdb.get_emotions(db_path)
# emotions = numpy.array(emotions)[0:20]

extractor = mooddeck.get_landmark_extractor()
classifier = mooddeck.get_classifier()
all_features = []

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


def predict_test_db():
    load_database_features()
    prediction = classifier.predict(all_features)
    print prediction


def predict_hugh_laurie_mood():
    mood = ["neutral", "angry", "showing contempt", "disgusted", "afraid", "happy", "sad", "surprised"]
    features = extractor.extract("./samples/hugh_laurie.jpeg")
    hugh_laurie_mood = classifier.predict(features)
    print "Hugh Laurie is {}".format(mood[int(hugh_laurie_mood[0])])


def predict_happy_neutral_people():
    mood = ["neutral", "angry", "showing contempt", "disgusted", "afraid", "happy", "sad", "surprised"]
    features = extractor.extract("./samples/2008_001322.jpg")
    happy_people = classifier.predict(features)
    print "Person 1 is {}".format(mood[int(happy_people[0])])
    print "Person 2 is {}".format(mood[int(happy_people[1])])
    print "Person 3 is {}".format(mood[int(happy_people[2])])


def perform_cross_validation():
    global all_features
    global emotions
    emotion_labels = numpy.array(emotions)[:,2]

    n = len(all_features)
    jump = int(numpy.floor(n/10))
    array = numpy.arange(0,n - jump, jump)
    means = []
    for x in array:
        idx = numpy.concatenate((numpy.arange(0,x), numpy.arange(x+jump,n)), axis=0).tolist()
        features = all_features[idx,:]
        labels = emotion_labels[idx]
        classifier.train(features, labels)

        idx = numpy.arange(x, x+jump)
        test = all_features[idx, :]
        labels = emotion_labels[idx]
        predictions = classifier.predict(test)
        means.append(sum(labels == predictions) / len(idx))

    print sum(means) / len(array)




# To train the model, uncomment these lines
# load_database_features()
# train_model()

# To load the model already saved, uncomment these lines
# load_database_features()
# load_model()

# Predictions after you have the model in memory, load or train the model first
# predict_happy_neutral_people()
# predict_hugh_laurie_mood()

# Performing cross validations
load_database_features()
perform_cross_validation()








