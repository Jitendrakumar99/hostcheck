import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score
data=pd.read_csv('sales_data.csv')
x=data[['week']]
y=data['sales']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
model=LinearRegression()
model.fit(x_train,y_train)
user_week=int(input("Enter the week number you want to predict sales for: "))
predicted_sales=model.predict([[user_week]])
print(f"Predicted sales for week {user_week}:{predicted_sales[0]}")
y_pred=model.predict(x_test)
mse=mean_squared_error(y_test,y_pred)
r2=r2_score(y_test,y_pred)
print(f"Mean Squared Error:{mse}")
print(f"R-squared:{r2}")
plt.scatter(x,y,color='blue')
plt.plot(x,model.predict(x),color='red')
plt.xlabel('Week')
plt.ylabel('Sales')
plt.title('Linear Regression - Sales Prediction')
plt.show()


