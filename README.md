# Used-Vehicle-Price-Prediction-System
End-to end machine learning project with website built using flask framework.

# Work Flow
## 1. Data Acquisition 
On obtaining the dataset, read it using pandas and study the thus obtained pandas dataframe. 
>>>Link to dataset:https://www.kaggle.com/datasets/winky02/vehicles-csv

## 2. Data Cleaning 
This involved:
Removing duplicates 
Removing unnecessary features. For this purpose, ‘url’,’image_url’, ‘lat’, ‘long’, ‘city_url’, 
‘desc’, ‘city’, ‘VIN’ features were dropped totally.
Extreme values, that is, outliers were dropped because they inhibit prediction power of the 
model. 
Some missing values were dropped or filled with appropriate values.
