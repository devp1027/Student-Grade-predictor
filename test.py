import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style

data = pd.read_csv("student-mat.csv", sep=";")
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]
predict = "G3"

X = np.array(data.drop([predict], 1))
y = np.array(data[predict])
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.1)
best = 0
"""""
for _ in range(30):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.1)

    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    print(acc)
    if acc > best:
        best  = acc
        with open("Studentmodel.pickle","wb") as f:
            pickle.dump(linear, f)
"""

pickle_in = open("Studentmodel.pickle","rb")
linear = pickle.load(pickle_in)
print ("Co: ", linear.coef_)
print ("inter: ", linear.intercept_)

preditions = linear.predict(x_test)

for i in range(len(preditions)):
    print (preditions[i],x_test[i], y_test[i])

p = "G2"

style.use("ggplot")
pyplot.scatter(data[p], data["G3"])
pyplot.xlabel(p)
pyplot.ylabel("Fianl Grade")
pyplot.show()