from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split 
from sklearn.datasets import load_iris
#load dataset
irisData=load_iris()
#print(irisData)
#create feature and target arrays
x=irisData.data
y=irisData.target
#split into training and test set
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
knn=KNeighborsClassifier(n_neighbors=7)
knn.fit(x_train,y_train)
#predict on dataset which model has not seen before
y_pred=knn.predict(x_test)
from sklearn.metrics import confusion_matrix,accuracy_score
cm=confusion_matrix(y_test,y_pred)
print(cm)
a=accuracy_score(y_test,y_pred)
print(a)

# output:
# [[12  0  0]
#  [ 0  7  0]
#  [ 0  0 11]]
# 1.0