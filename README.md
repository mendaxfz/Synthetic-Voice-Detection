# Synthetic-Voice-Detection



## Dataset

Dataset -  http://bil.eecs.yorku.ca/datasets/

* Total of 17,870 utterances.
* Training Set - Contains 77.3% of the dataset, used to train the ML model. Gender and class balanced.
* Validation Set - Contains 15.58% of the dataset, used to validate the accuracy of the ML model. Gender and class balanced.
* Generalization Testing - Contains 6.68% of the dataset. Contains only voices from one unseen algorithm(Google TTS Wavenet) and unseen real voices. Gender and        class balanced. Used to check if the model has successfully learnt to generalize.


## Feature Extraction

Extracting MFCCs essentially summarises the frequency distribution across a window size, this makes it possible to analyse both frequency and temporal characteristics of a sound wave. I have used the Librosa library, alongside a custom script to extract the MFCCs of all the audio files in the dataset and saved the processed dataset as a HDF5 file. This downsized the dataset by about 5 times.

<img src="img/audio.png" width="1000" height="300"> <img src="img/mfcc.png" width="1000" height="300">


## Network Architecture

<img src="img/network.png">

Resources  - https://arxiv.org/pdf/1812.00149.pdf
