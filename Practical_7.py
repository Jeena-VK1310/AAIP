import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score

# Importing the dataset
dataset = pd.read_csv('iris.csv')
dataset.describe()

# Splitting the dataset into the Training set and test set
x = dataset.iloc[:, [0, 1, 2, 3]].values
y = dataset.iloc[:, 4].values
print(x, y)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)
classifier = LogisticRegression(random_state=0, solver='lbfgs', multi_class='auto')
classifier.fit(x_train, y_train)

print("Jeena Vinod Kumar, 32")
y_pred = classifier.predict((x_test))
cm = confusion_matrix(y_test, y_pred)
print(cm)

acc = accuracy_score(y_test, y_pred)
print(acc)
