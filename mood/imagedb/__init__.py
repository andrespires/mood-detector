__author__ = 'Andre Pires'

import os

def get_emotions(dbpath):
    labels_path = dbpath + "/emotion-labels"
    dataset_path = dbpath + "/dataset"

    emotions = []
    for subject in os.listdir(os.path.join(labels_path)):
        seq_path = os.path.join(labels_path, subject)
        if os.path.isdir(seq_path):
            for sequence in os.listdir(seq_path):
                emo_path = os.path.join(seq_path, sequence)
                if os.path.isdir(emo_path):
                    emo_files = os.listdir(emo_path)
                    if len(emo_files) > 0 and emo_files[0].endswith("txt"):
                        f = open(emo_path + "/" + emo_files[0])
                        line = f.readline().strip()
                        emotion = int(float(line))
                        emotions.append([subject, sequence, emotion])

    return emotions


def get_image_path(dbpath, subject, sequence):
    dataset_path = dbpath + "/dataset"
    path = dataset_path + "/" + subject + "/" + sequence
    files = os.listdir(path)
    files = sorted(files)
    return path + "/" + files[len(files) - 1]



