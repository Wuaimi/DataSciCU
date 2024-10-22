import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

"""
    ASSIGNMENT 2 (STUDENT VERSION):
    Using pandas to explore Titanic data from Kaggle (titanic.csv) and answer the questions.
"""


def Q1(df):
    """
        Problem 1:
            How many rows are there in the “titanic.csv?
            Hint: In this function, you must load your data into memory before executing any operations. To access titanic.csv,
              use the path /data/titanic.csv.
    """
    # TODO: Code 
    df = pd.read_csv('/data/titanic.csv')
    rows = df.shape[0]
    return rows


def Q2(df):
    '''
        Problem 2:
            Drop unqualified variables
            Drop variables with missing > 50%
            Drop categorical variables with flat values > 70% (variables with the same value in the same column)
            How many columns do we have left?
    '''
    # TODO: Code here

    half = len(df)/2
    half_df = df.dropna(thresh=half, axis=1)
    for column in half_df.columns:
        percent = half_df[column].value_counts().max() / len(half_df[column])
        if (percent > 0.7):
            half_df = half_df.drop(column, axis=1)

    return half_df.shape[1]

def Q3(df):
    '''
       Problem 3:
            Remove all rows with missing targets (the variable "Survived")
            How many rows do we have left?
    '''
    # TODO: Code here
    df = df['Survived'].dropna(axis=0)
    return df.shape[0]


def Q4(df):
    '''
       Problem 4:
            Handle outliers
            For the variable “Fare”, replace outlier values with the boundary values
            If value < (Q1 - 1.5IQR), replace with (Q1 - 1.5IQR)
            If value > (Q3 + 1.5IQR), replace with (Q3 + 1.5IQR)
            What is the mean of “Fare” after replacing the outliers (round 2 decimal points)?
            Hint: Use function round(_, 2)
    '''
    # TODO: Code here
    q1 = np.percentile(df['Fare'].dropna(),25)
    q3 = np.percentile(df['Fare'].dropna(),75)
    l_bound = q1 - ((q3-q1)*1.5)
    u_bound = q3 + ((q3-q1)*1.5)
    df['Fare'] = np.where(df['Fare'] < l_bound, l_bound, df['Fare'])
    df['Fare'] = np.where(df['Fare'] > u_bound, u_bound, df['Fare'])

    return round(df['Fare'].mean(),2)

def Q5(df):
    '''
       Problem 5:
            Impute missing value
            For number type column, impute missing values with mean
            What is the average (mean) of “Age” after imputing the missing values (round 2 decimal points)?
            Hint: Use function round(_, 2)
    '''
    # TODO: Code here
    df = df.fillna(df.mean(numeric_only=True))
    return round(df['Age'].mean(), 2)


def Q6(df):
    '''
        Problem 6:
            Convert categorical to numeric values
            For the variable “Embarked”, perform the dummy coding.
            What is the average (mean) of “Embarked_Q” after performing dummy coding (round 2 decimal points)?
            Hint: Use function round(_, 2)
    '''
    # TODO: Code here
    A_df = pd.get_dummies(df['Embarked'], drop_first=True)
    df = pd.concat([df, A_df], axis=1)
    df = df.drop('Embarked', axis=1)
    df = df.rename(columns={
        'Q': 'Embarked_Q',
        'S': 'Embarked_S'
    })
    return round(df['Embarked_Q'].mean(), 2)


def Q7(df):
    '''
        Problem 7:
            Split train/test split with stratification using 70%:30% and random seed with 123
            Show a proportion between survived (1) and died (0) in all data sets (total data, train, test)
            What is the proportion of survivors (survived = 1) in the training data (round 2 decimal points)?
            Hint: Use function round(_, 2), and train_test_split() from sklearn.model_selection
    '''
    # TODO: Code here
    y = df.pop('Survived')
    X = df

    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.3, random_state=123)
    # print("train")
    # print(f"1   {(y_train == 1).sum()/y_train.shape[0]}")
    # print(f"0   {(y_train == 0).sum()/y_train.shape[0]}")
    # print("test")
    # print(f"1   {(y_test == 1).sum()/y_test.shape[0]}")
    # print(f"0   {(y_test == 0).sum()/y_test.shape[0]}")

    mean = round((y_train == 1).sum()/y_train.shape[0], 2)