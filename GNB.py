import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics


data = pd.read_csv('data_4.csv')

Y = data['isCollision'].values
Y = Y.astype('int')
# print(Y)

X = data.drop(labels=['isCollision'], axis=1)
# print(data.describe())
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.25, random_state=30)

# print(X_test)
# print(Y_test)

nb = GaussianNB()

nb.fit(X_train, Y_train)

print('Accuracy: ', nb.score(X_test, Y_test))

# prediction_test = nb.predict(X_test)
# print('Accuracy: ', metrics.accuracy_score(Y_test, prediction_test))

# # print(model.feature_importances_)
# feature_list = list(X.columns)
# feature_imp = pd.Series(nb.feature_importances_,
#                         index=feature_list).sort_values(ascending=False)

# print(feature_imp)
