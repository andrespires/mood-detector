"""

"""
from sklearn import decomposition
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib

import mood.settings.const as const


class Classifier(object):

    def __init__(self):
        self.pca = None
        self.classifier = None


    def train(self, features, ratings):
        self.pca = decomposition.PCA(n_components=20)
        self.pca.fit(features)
        features_train = self.pca.transform(features)

        # self.classifier = svm.SVC(gamma=0.001)
        self.classifier = RandomForestClassifier(n_estimators=10)

        self.classifier.fit(features_train, ratings)


    def predict(self, features):
        features_test = self.pca.transform(features)
        return self.classifier.predict(features_test)

    def save(self):
        joblib.dump(self.pca, const.pca_model_path)
        joblib.dump(self.classifier, const.classifier_model_path)

    def load(self):
        self.pca = joblib.load(const.pca_model_path)
        self.classifier = joblib.load(const.classifier_model_path)
