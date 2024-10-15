import pandas as pd
import json
from datetime import datetime,timezone

"""
    ASSIGNMENT 1 (STUDENT VERSION):
    Using pandas to explore youtube trending data from GB (GBvideos.csv and GB_category_id.json) and answer the questions.
"""


def Q1():
    """
        1. How many rows are there in the GBvideos.csv after removing duplications?
        - To access 'GBvideos.csv', use the path '/data/GBvideos.csv'.
    """
    # TODO: Paste your code here
    file_path = '/data/GBvideos.csv'
    df = pd.read_csv(file_path)
    buffer = df.drop_duplicates()
    return buffer.shape[0]

def Q2(vdo_df):
    '''
        2. How many VDO that have "dislikes" more than "likes"? Make sure that you count only unique title!
            - GBvideos.csv has been loaded into memory and is ready to be utilized as vdo_df
            - The duplicate rows of vdo_df have been removed.
    '''
    # TODO: Paste your code here
    filtered_df = vdo_df[vdo_df['dislikes'] > vdo_df['likes']]
    unique_titles = filtered_df['title'].nunique()
    
    return unique_titles

def Q3(vdo_df):
    '''
        3. How many VDO that are trending on 22 Jan 2018 with comments more than 10,000 comments?
            - GBvideos.csv has been loaded into memory and is ready to be utilized as vdo_df
            - The duplicate rows of vdo_df have been removed.
            - The trending date of vdo_df is represented as 'YY.DD.MM'. For example, January 22, 2018, is represented as '18.22.01'.
    '''
    # TODO: Paste your code here
    filtered_df = vdo_df[(vdo_df['trending_date'] == '18.22.01') & (vdo_df['comment_count'] > 10000)]
    num_videos = filtered_df.shape[0]
    
    return num_videos

def Q4(vdo_df):
    '''
        4. Which trending date that has the minimum average number of comments per VDO?
            - GBvideos.csv has been loaded into memory and is ready to be utilized as vdo_df
            - The duplicate rows of vdo_df have been removed.
    '''

    # TODO:  Paste your code here
    avg_comments_per_date = vdo_df.groupby('trending_date')['comment_count'].mean()
    min_avg_comments_date = avg_comments_per_date.idxmin()
    
    return min_avg_comments_date

def Q5(vdo_df):
    '''
        5. Compare "Sports" and "Comedy", how many days that there are more total daily views of VDO in "Sports" category than in "Comedy" category?
            - GBvideos.csv has been loaded into memory and is ready to be utilized as vdo_df
            - The duplicate rows of vdo_df have been removed.
            - You must load the additional data from 'GB_category_id.json' into memory before executing any operations.
            - To access 'GB_category_id.json', use the path '/data/GB_category_id.json'.
    '''
    # TODO:  Paste your code here
    with open('/data/GB_category_id.json', 'r') as f:
        category_data = json.load(f)
    category_mapping = {int(item['id']): item['snippet']['title'] for item in category_data['items']}
    vdo_df['category_name'] = vdo_df['category_id'].map(category_mapping)
    sports_df = vdo_df[vdo_df['category_name'] == 'Sports']
    comedy_df = vdo_df[vdo_df['category_name'] == 'Comedy']
    sports_daily_views = sports_df.groupby('trending_date')['views'].sum()
    comedy_daily_views = comedy_df.groupby('trending_date')['views'].sum()
    comparison = sports_daily_views > comedy_daily_views
    days_more_sports_views = comparison.sum()
    
    return days_more_sports_views

""" file_path = 'HW/week1/data/USvideos.csv'
df = pd.read_csv(file_path)
vdo_df = df.drop_duplicates()
print(Q1()) #Passed
print(Q2(vdo_df)) #passed
print(Q3(vdo_df)) #passed
print(Q4(vdo_df))
print(Q5(vdo_df)) """