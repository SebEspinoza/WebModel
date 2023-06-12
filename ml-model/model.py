import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv("df2020limpio.csv")

features = [
    "MinTemp",
    "MaxTemp",
    "Rainfall",
    "Humidity9am",
    "Humidity3pm",
    "Pressure9am",
    "Pressure3pm",
    "Temp9am",
    "Temp3pm",
]
check_rows = features[:]
check_rows.append("RainTomorrow")

X = df[features]
y = df["RainTomorrow"]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

from sklearn.neighbors import KNeighborsClassifier

clf = KNeighborsClassifier(n_neighbors=3)

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

y_pred

accuracy = clf.score(X_test, y_test)

print("Precisión del modelo:", accuracy)

scores = []

for n in range(1, 5):
    clf = KNeighborsClassifier(n_neighbors=n)
    clf.fit(X_train, y_train)
    scores.append(clf.score(X_test, y_test))

plt.plot(range(1, 5), scores)

plt.xlabel("Neighbors")
plt.ylabel("Precision del modelo (%)")

plt.show()
