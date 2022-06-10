import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import cross_val_score


data = pd.read_csv('data_4.csv')

Y = data['isCollision'].values
Y = Y.astype('int')
# print(Y)

X = data.drop(labels=['isCollision'], axis=1)
# print(data.describe())
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.1, random_state=30)

# print(X_test)
# print(Y_test)

model = LinearDiscriminantAnalysis()
model.fit(X_train, Y_train)

cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)

scores = cross_val_score(model, X_test, Y_test, scoring='accuracy', cv=cv, n_jobs=-1)
print(np.mean(scores))
