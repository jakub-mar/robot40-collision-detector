import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics


data = pd.read_csv('data_100k.csv')

Y = data['isCollision'].values
Y = Y.astype('int')
# print(Y)

X = data.drop(labels=['isCollision'], axis=1)
print(data.describe())
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.1, random_state=30)

print(X_train)
print(Y_train)

model = RandomForestClassifier(n_estimators=10, random_state=11)

model.fit(X_train, Y_train)

prediction_test = model.predict(X_test)
print('Accuracy: ', metrics.accuracy_score(Y_test, prediction_test))

# print(model.feature_importances_)
feature_list = list(X.columns)
feature_imp = pd.Series(model.feature_importances_,
                        index=feature_list).sort_values(ascending=False)

# print(feature_imp)
