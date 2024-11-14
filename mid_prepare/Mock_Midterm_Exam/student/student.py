import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.preprocessing import StandardScaler

class exam:
    def __init__(self, data: pd.DataFrame): # DO NOT modify this line
        self.data = data
        self.X_train = None
        self.X_test = None 
        self.y_train = None 
        self.y_test = None 

    def Q1(self): # DO NOT modify this line
        """
        1. Data Preparation and Feature Selection
           In this step, select and prepare a subset of relevant features for predicting Titanic survival outcomes. 
           Specifically:
           - Select the target variable 'survived' and the following features:
             'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked', 'class', 'adult_male', and 'alone'.
           - Handle missing values by filling them appropriately (e.g., median for numerical columns like 'age' and 'fare',
             and mode for categorical columns like 'embarked').
           - Convert categorical variables to numerical values using one-hot encoding with "drop the first category in each feature" so that they can be used in the model.

           This step ensures the data is complete, properly formatted, and ready for machine learning.

           **Remarks:**
           1. You must return the shape of the modified dataset to confirm changes were made correctly (return `self.data.shape`).
           2. Remember to update `self.data` as it will be used in subsequent methods.
        """
        cols = ['survived','pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked', 'class', 'adult_male', 'alone']
        self.df = self.df[cols]

        
        self.df.fillna(self.df.mean(numeric_only=True), inplace=True)
        self.df.fillna(self.df.mode().iloc[0], inplace=True)

    def Q2(self): # DO NOT modify this line
        """
        2. Splitting and Standardizing the Data
           Now that the data is ready, split it into training and testing sets to evaluate the model’s performance later:
           - Separate the target variable ('survived') from the selected features.
           - Use a 70-30 split for training and testing data, setting `random_state=2024` for reproducibility, 
             and enable stratification to maintain class distribution in the split.
           - Calculate and return the proportion of survivors in the training set as a quick metric to check data balance.
           
           By the end of this step, you will have the datasets ready for model training and evaluation.

           **Remarks:**
           1. Return the survivability rate in the training set, rounded to two decimal places (`round(y_train.mean(), 2)`), 
          which shows the proportion of survivors.
           2. Update `self.X_train`, `self.X_test`, `self.y_train`, and `self.y_test` for use in the final question.
           **Hint**
           You can use a try-except statement.
        """

    def Q3(self):
        """
        3. Model Training and Prediction
        Using logistic regression, train a predictive model to determine if a passenger survived:
        - Initialize a Logistic Regression model with `max_iter=10000` to ensure the model converges.
        - Train (fit) the model on the training dataset.
        - Use the trained model to make predictions on the test dataset and return the first prediction to verify output format.

        This step completes the machine learning pipeline, allowing you to assess model accuracy by comparing predictions 
        to actual test outcomes.

        **Remarks:**
        1. Return the first element of the prediction array (`y_pred[0]`) to verify that the model outputs correctly.
        """


import pandas as pd
import numpy as np
from student import *

class Checker:
    def __init__(self, exam):
        # Assuming model is an instance of a class with methods Q1, Q2, Q3, and attributes like y_test
        self.exam = exam

    def Q1(self):
        y = self.exam.Q1()
        print(y)

    def Q2(self):
        self.exam.Q1()
        y1 = self.exam.Q2()
        print(f"{y1:.2f}")

    def Q3(self):
        self.exam.Q1()
        self.exam.Q2()
        y = self.exam.Q3()
        print(y)

def main():
    data = pd.read_csv('/titanic.csv')
    exam_titanic = exam(data)
    checker = Checker(exam_titanic)
    eval(f"checker.{input().strip()}()")


if __name__ == "__main__":
    main()