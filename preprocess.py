import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Feature Extractor, Dataset Creation Functions
max_pad_length = 86
def extract_features_cnn(file_name):
    try:
        audio,sample_rate = librosa.load(file_name)
        mfccs = librosa.feature.mfcc(y=audio,sr=sample_rate,n_mfcc=40)
        pad_width = max_pad_length - mfccs.shape[1]
        mfccs = np.pad(mfccs, pad_width=((0, 0), (0, pad_width)), mode='constant')

    except:
        print("Error encountered while parsing the file: ", file_name)
        return None

    return mfccs
    

def create_dataset(path,column_name):
    features=[]
    count=0
    for filename in tqdm(os.listdir(path)):
        data = extract_features_cnn(path+'/'+filename)
        features.append([data,column_name])
        
    featuresdf = pd.DataFrame(features, columns=['feature','class_label'])
    return featuresdf


def extract_feature(file_name): 
    try:
        audio,sample_rate = librosa.load(file_name)
        mfccs = librosa.feature.mfcc(y=audio,sr=sample_rate,n_mfcc=40)
        pad_width = max_pad_length - mfccs.shape[1]
        mfccs = np.pad(mfccs, pad_width=((0, 0), (0, pad_width)), mode='constant')
    except Exception as e:
        print("Error encountered while parsing file: ", file)
        return None, None
    return np.array([mfccs])

