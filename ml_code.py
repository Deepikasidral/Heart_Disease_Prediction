import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

heart_data = pd.read_csv('/heart.csv')
heart_data.head()
heart_data.tail()   
heart_data.info()
heart_data.shape
heart_data.isnull().sum()
heart_data.describe()
heart_data['target'].value_counts()
#spliting the data and target
X=heart_data.drop(columns='target', axis=1)#while dropping a column axis=1 if we are removing column axis=0
Y=heart_data['target']
#splitting the data into training data and test data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y,test_size=0.2,stratify=Y,random_state=2)
print(X.shape,X_train.shape,X_test.shape)

model=LogisticRegression()
model.fit(X_train,Y_train)
X_train_prediction=model.predict(X_train)
training_data_accuracy =accuracy_score(X_train_prediction,Y_train)
print("Accuracy of training data=",training_data_accuracy)#Accuracy of training data= 0.8524390243902439
X_test_prediction=model.predict(X_test)
test_data_accuracy =accuracy_score(X_test_prediction,Y_test)
print("Accuracy of test data=",test_data_accuracy)#Accuracy of test data= 0.8048780487804879

#predictive model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
input_data = (41,0,1,130,204,0,0,172,0,1.4,2,0,2)
#change input data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

#reshape the numpy array as we are predicting for only on instances
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
prediction = model.predict(input_data_reshaped)
print(prediction)