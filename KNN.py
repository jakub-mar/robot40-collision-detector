import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import cross_val_score

from sklearn.preprocessing import StandardScaler, scale
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix


data = pd.read_csv('data_100k.csv')

Y = data['isCollision'].values
Y = Y.astype('int')


X = data.drop(labels=['isCollision'], axis=1)

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.15, random_state=42)

print(X_train)
print(Y_train)

# scaler = StandardScaler()
# scaler.fit(X_train)

# X_train = scaler.transform(X_train)
# X_test = scaler.transform(X_test)

classifier = KNeighborsClassifier(n_neighbors=50)
classifier.fit(X_train, Y_train)

y_pred = classifier.predict(X_test)

print('Accuracy: ', metrics.accuracy_score(Y_test, y_pred))

# print(confusion_matrix(Y_test, y_pred))
# print(classification_report(Y_test, y_pred))
