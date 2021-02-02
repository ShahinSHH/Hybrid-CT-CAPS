# -*- coding: utf-8 -*-
"""
Implementation of the Hybrid-CT-CAPS framework

@authors: Parnian Afshar, Shahin Heidarian
"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import seaborn as sn
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report



df = pd.read_csv('Hybrid_CT_Data_Numeric.csv')

df_train = df[df['train-test'].isin(['Train'])]
df_test=  df[df['train-test'].isin(['Test'])]

X_train= df_train[['Patient Sex', 'Patient Age','Weight','Dyspnea', 'Cough', 'Fever', 'Flu-like symptoms',
                   'Fatigue', 'Myalgia', 'Nausea', 'Chest pain', 'Headache', 'Loss of appetite', 'Asthma history', 'Anosmia',
                   'Abdominal pain', 'Prob']]

X_test= df_test[['Patient Sex', 'Patient Age','Weight','Dyspnea', 'Cough', 'Fever', 'Flu-like symptoms',
                   'Fatigue', 'Myalgia', 'Nausea', 'Chest pain', 'Headache', 'Loss of appetite', 'Asthma history', 'Anosmia',
                   'Abdominal pain', 'Prob']]

y_train= df_train[['Diagnosis']]

y_test= df_test[['Diagnosis']]

clf = RandomForestClassifier(n_estimators=1000)
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)

print('Accuracy: ',metrics.accuracy_score(y_test, y_pred))


target_names = ['class 0', 'class 1']
print(classification_report(y_test, y_pred, target_names=target_names))
             

