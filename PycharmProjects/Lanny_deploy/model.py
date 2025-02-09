import pandas as pd
import numpy as np
import pickle
import joblib
import sklearn.preprocessing
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

with open(r"C:\Users\MODUPE\data.pkl", "rb") as file:
    x,y = pickle.load(file)

# print(x)
# print(y)

print(x.columns)
scaler = sklearn.preprocessing.StandardScaler()
x = scaler.fit_transform(x)
xtrain,xtest,ytrain,ytest = train_test_split(x,y,
                                             test_size = 0.2,
                                             random_state = 42)

model = RandomForestRegressor()
model.fit(xtrain,ytrain)

print(model.score(xtest,ytest))

with open("model.pkl", "wb") as file:
    joblib.dump(model,file)

with open("scaler.pkl", "wb") as file:
    pickle.dump(scaler, file)



print( "g".upper() )

