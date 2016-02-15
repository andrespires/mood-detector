"""

"""
from sklearn import decomposition
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib


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
        joblib.dump(self.pca, 'pca.pkl')
        joblib.dump(self.classifier, 'classifier.pkl')

    def load(self):
        self.pca = joblib.load('pca.pkl')
        self.classifier = joblib.load('classifier.pkl')
