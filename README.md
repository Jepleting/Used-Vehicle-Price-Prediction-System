# Used-Vehicle-Price-Prediction-System
End-to end machine learning project with website built using flask framework.

# Work Flow
## 1. Data Acquisition 
On obtaining the dataset, read it using pandas and study the thus obtained pandas dataframe. 
>>>Link to dataset:https://www.kaggle.com/datasets/winky02/vehicles-csv

## 2. Data Cleaning 
This involved:
Removing duplicates.

Removing unnecessary features. For this purpose, ‘url’,’image_url’, ‘lat’, ‘long’, ‘city_url’, 
‘desc’, ‘city’, ‘VIN’ features were dropped totally.

Extreme values, that is, outliers were dropped because they inhibit prediction power of the 
model. 

Some missing values were dropped or filled with appropriate values.

## 3. Explanatory Data Analysis 

Involves taking a look at some of the variables and their distribution. 

Price is the feature that we are predicting in this study. Before applying any models, taking a 
look at price data may give us some ideas. 

There is a positive correlation between year and price and a negative correlation 
between mileage and price. This makes sense, since newer cars are generally more expensive and 
cars with more mileage are relatively cheaper. There is also  a negative correlation between 
mileage and year - the newer a car is the less miles it is likely to have travelled.

## 4. Feature Engineering 

To distinguish older cars from newer ones. Create two new columns: age of cars by year, and 
average mileage of car per year. 

## 5. Modelling

Splitting the dataset- the data is divided into training and test data in an 80-20 split. 
Fitting the model- using LabelEncoder to convert categorical values to assign numerical values or the 
model first before fitting the Random Forest Regressor

## 6. Performance Evaluation
The loaded model has an estimate of the accuracy of 88.1% on unseen data. 




