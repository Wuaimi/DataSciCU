import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

"""
    ASSIGNMENT 2 (STUDENT VERSION):
    Using pandas to explore Titanic data from Kaggle (titanic.csv) and answer the questions.
"""

# Q1: Count the number of rows in the Titanic dataset
def Q1(df):
    """
        Problem 1:
            How many rows are there in the “titanic.csv”?
            Hint: In this function, you must load your data into memory before executing any operations. 
                  To access titanic.csv, use the path /data/titanic.csv.
    """
    # อ่านข้อมูลจากไฟล์ CSV
    df = pd.read_csv('/data/titanic.csv')
    # นับจำนวนแถวใน DataFrame
    rows = df.shape[0]
    return rows


# Q2: Drop unqualified variables
def Q2(df):
    """
        Problem 2:
            Drop variables with missing > 50%
            Drop categorical variables with flat values > 70% (variables with the same value in the same column)
            Return the number of remaining columns.
    """
    # คำนวณจำนวนแถวครึ่งหนึ่งของ DataFrame
    half = len(df) / 2
    # ลบคอลัมน์ที่มีค่า missing มากกว่า 50%
    half_df = df.dropna(thresh=half, axis=1)

    # ตรวจสอบแต่ละคอลัมน์ที่มีค่าประเภทเดียวกันเกิน 70%
    for column in half_df.columns:
        # คำนวณเปอร์เซ็นต์ของค่าที่พบมากที่สุดในคอลัมน์
        percent = half_df[column].value_counts().max() / len(half_df[column])
        # ลบคอลัมน์ถ้าเปอร์เซ็นต์เกิน 70%
        if percent > 0.7:
            half_df = half_df.drop(column, axis=1)

    # คืนค่าจำนวนคอลัมน์ที่เหลืออยู่
    return half_df.shape[1]


# Q3: Remove rows with missing targets ("Survived")
def Q3(df):
    """
        Problem 3:
            Remove all rows with missing targets (the variable "Survived")
            Return the number of remaining rows.
    """
    # ลบแถวที่ค่า "Survived" เป็น NaN
    df = df['Survived'].dropna(axis=0)
    # คืนค่าจำนวนแถวที่เหลืออยู่
    return df.shape[0]


# Q4: Handle outliers for the "Fare" column
def Q4(df):
    """
        Problem 4:
            For the variable “Fare”, replace outlier values with the boundary values.
            Return the mean of “Fare” after replacing the outliers, rounded to 2 decimal points.
    """
    # คำนวณเปอร์เซ็นไทล์ที่ 25 (Q1) และ 75 (Q3)
    q1 = np.percentile(df['Fare'].dropna(), 25)
    q3 = np.percentile(df['Fare'].dropna(), 75)
    # คำนวณขอบเขตล่างและบนของค่าที่ไม่ถือว่าเป็น outliers
    l_bound = q1 - 1.5 * (q3 - q1)
    u_bound = q3 + 1.5 * (q3 - q1)

    # แทนค่าที่น้อยกว่า l_bound ด้วย l_bound
    df['Fare'] = np.where(df['Fare'] < l_bound, l_bound, df['Fare'])
    # แทนค่าที่มากกว่า u_bound ด้วย u_bound
    df['Fare'] = np.where(df['Fare'] > u_bound, u_bound, df['Fare'])

    # คืนค่าค่าเฉลี่ยของ "Fare" หลังจากจัดการ outliers
    return round(df['Fare'].mean(), 2)


# Q5: Impute missing values for numeric columns
def Q5(df):
    """
        Problem 5:
            Impute missing values for numeric columns with the mean.
            Return the average of “Age” after imputing missing values, rounded to 2 decimal points.
    """
    # เติมค่าที่หายไป (NaN) ในคอลัมน์ตัวเลขด้วยค่าเฉลี่ยของคอลัมน์นั้น
    df = df.fillna(df.mean(numeric_only=True))
    # คืนค่าค่าเฉลี่ยของ "Age" หลังจากเติมค่าที่หายไป
    return round(df['Age'].mean(), 2)


# Q6: Perform dummy coding for the "Embarked" column
def Q6(df):
    """
        Problem 6:
            Convert the categorical variable “Embarked” to dummy variables.
            Return the average of “Embarked_Q” after dummy coding, rounded to 2 decimal points.
    """
    # สร้าง dummy variables สำหรับ "Embarked"
    A_df = pd.get_dummies(df['Embarked'], drop_first=True)
    # รวม dummy variables เข้ากับ DataFrame เดิม
    df = pd.concat([df, A_df], axis=1)
    # ลบคอลัมน์ "Embarked" ออกจาก DataFrame
    df = df.drop('Embarked', axis=1)
    # เปลี่ยนชื่อคอลัมน์ให้เข้าใจง่ายขึ้น
    df = df.rename(columns={'Q': 'Embarked_Q', 'S': 'Embarked_S'})
    # คืนค่าค่าเฉลี่ยของ "Embarked_Q"
    return round(df['Embarked_Q'].mean(), 2)


# Q7: Train/test split with stratification
def Q7(df):
    """
        Problem 7:
            Split the dataset into train and test sets using a 70%:30% split with stratification.
            Return the proportion of survivors in the training data, rounded to 2 decimal points.
    """
    # แยกคอลัมน์เป้าหมาย "Survived" ออกจากตัวแปรอิสระ
    y = df.pop('Survived')
    X = df
    # แบ่งข้อมูลเป็น train/test โดยใช้ stratification เพื่อให้การกระจายของ "Survived" สมดุลกัน
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.3, random_state=123)

    # คำนวณสัดส่วนของผู้รอดชีวิต (Survived = 1) ในชุดข้อมูล train
    return round((y_train == 1).sum() / y_train.shape[0], 2)
