#Preprocessing 
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

dataset=pd.read_csv('Position_Salaries.csv')

x=dataset.iloc[:,1:2].values
y=dataset.iloc[:,2:3].values

#Feature scaling
from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
sc_y=StandardScaler()
x=sc_x.fit_transform(x)
y=sc_y.fit_transform(y)

#Fitting the Model
from sklearn.svm import SVR
regressor=SVR(kernel='rbf')
regressor.fit(x,y)

#Predicting the value
y_pred=sc_y.inverse_transform(regressor.predict(sc_x.transform(np.array([[6.5]]))))

#Plotting the curve
plt.scatter(x,y, color='red')
plt.plot(x,regressor.predict(x),color='blue')
plt.show()