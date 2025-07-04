# -*- coding: utf-8 -*-
"""placement_model.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uVJlKk23La9OzPeyPnxum9HC00_CE9No
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/placement.csv')
df = df.iloc[:, 1:]
df.head()

"""Steps <br/>
0) <strong>Preprocessing + EDA + Feature Selection <strong/> <br/>
1) <strong>Extract input and output cols<strong/> <br/>
2) <strong>Scale the values<strong/><br/>
3) <strong>Train test split<strong/><br/>
4) <strong>Train the model<strong/><br/>
5) <strong>Evaluate the model/model selection<strong/><br/>
6) <strong>Deploy the model<strong/>

EDA
"""

plt.scatter(df['cgpa'], df['iq'], c=df['placement']) # differentiating on the basis of df['placement']
plt.xlabel('CGPA')
plt.ylabel('IQ')

"""Step-1"""

x = df.iloc[:, 0:2] #input
y = df.iloc[:, -1] #output

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_train

x_test = scaler.transform(x_test)
x_test

from sklearn.linear_model import LinearRegression
# model = LinearRegression()
model = LogisticRegression()

#model training
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_pred)

from mlxtend.plotting import plot_decision_regions
plot_decision_regions(x_train, y_train.values, clf=model, legend=2)