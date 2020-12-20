# Synthetic-Voice-Detection



## Dataset

Dataset -  http://bil.eecs.yorku.ca/datasets/

* Total of 17,870 utterances.
* Training Set - Contains 77.3% of the dataset, used to train the ML model. Gender and class balanced.
* Validation Set - Contains 15.58% of the dataset, used to validate the accuracy of the ML model. Gender and class balanced.
* Generalization Testing - Contains 6.68% of the dataset. Contains only voices from one unseen algorithm(Google TTS Wavenet) and unseen real voices. Gender and        class balanced. Used to check if the model has successfully learnt to generalize.

## Network Architecture

<img src="img/network.png">

Resources  - https://arxiv.org/pdf/1812.00149.pdf
