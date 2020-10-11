import numpy as np
import pandas as pd

#1.creating data set:
dataset=pd.read_csv('/home/deadman/DataSets/datasalary.csv')

#2.extracting column x:
x=dataset.iloc[:,:-1].values

#3.extracting column y:
y=dataset.iloc[:,1].values

h=0.2


#4.splitting dataset into training and test dataset by importing train_test_split from model_selection library of sklean module:
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)

#5.Scaling the model with standard scaler from preprocessing library of sklearn module:
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.fit_transform(x_test)

#6.Training the Model with training dataset by using k-nearest y importing neighbours library from sklearn module:
from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=5,metric='minkowski',p=2)
classifier.fit(x_train,y_train)

#7.Predicting the test set result:
y_pred=classifier.predict(x_test)
print(np.concatenate((y_pred.reshape(len(y_pred),1),y_test.reshape(len(y_test),1)),1))

#8.Makng confusion matrix:
from sklearn.metrics import confusion_matrix,accuracy_score
cm=confusion_matrix(y_test,y_pred)
print(cm)
accuracy_score(y_test,y_pred)

#9.Visaulising the training set results:
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt

x_set, y_set = x_train, y_train

x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1

#x_set,y_set=sc.inverse_transform(x_train),y_train
x1,x2=np.meshgrid(np.meshgrid(np.arange(x_min, x_max, h),np.arange(y_min, y_max, h))

# plt.contourf(x1,x2,classifier.predict(np.array([x1.ravel(),x2.ravel()]).T).reshape(x1.shape),aplha=0.75,cmap=ListedColormap(('red','green')))
# plt.xlim(x1.min(),x1.max())
# plt.ylim(x2.min(),x2.max())
# for i,j in enumerate(np.unique(y_set)):
#     plt.scatter(x_Set[y_set==j,0],x_set[y_set==j,1],c=ListedColormap(('red','green'))(i),label=j)

Z == classifier.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.figure()
plt.pcolormesh(xx, yy, Z, cmap=cmap_light)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold)
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title('K-NN Cluster (Training Set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()