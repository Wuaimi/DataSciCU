import pandas as pd
import json
from datetime import datetime, timezone

"""
    ASSIGNMENT 1 (STUDENT VERSION):
    Using pandas to explore YouTube trending data from GB (GBvideos.csv and GB_category_id.json) and answer the questions.
"""


def Q1():
    """
        1. How many rows are there in the GBvideos.csv after removing duplications?
        - To access 'GBvideos.csv', use the path '/data/GBvideos.csv'.
    """
    # Load the dataset
    file_path = '/data/GBvideos.csv'
    df = pd.read_csv(file_path)
    # Remove duplicate rows
    buffer = df.drop_duplicates()
    # Return the number of rows after removing duplicates
    return buffer.shape[0]


def Q2(vdo_df):
    '''
        2. How many videos have "dislikes" more than "likes"? 
           Make sure that you count only unique titles!
        - GBvideos.csv has been loaded into memory and is ready to be utilized as vdo_df
        - The duplicate rows of vdo_df have been removed.
    '''
    # Filter rows where 'dislikes' > 'likes'
    filtered_df = vdo_df[vdo_df['dislikes'] > vdo_df['likes']]
    # Count the number of unique titles
    unique_titles = filtered_df['title'].nunique()
    return unique_titles


def Q3(vdo_df):
    '''
        3. How many videos are trending on 22 Jan 2018 with more than 10,000 comments?
        - GBvideos.csv has been loaded into memory and is ready to be utilized as vdo_df
        - The duplicate rows of vdo_df have been removed.
        - The trending date of vdo_df is represented as 'YY.DD.MM'. For example, January 22, 2018, is represented as '18.22.01'.
    '''
    # Filter rows for the specified date and comment count > 10,000
    filtered_df = vdo_df[(vdo_df['trending_date'] == '18.22.01') & (vdo_df['comment_count'] > 10000)]
    # Count the number of videos meeting the criteria
    num_videos = filtered_df.shape[0]
    return num_videos


def Q4(vdo_df):
    '''
        4. Which trending date has the minimum average number of comments per video?
        - GBvideos.csv has been loaded into memory and is ready to be utilized as vdo_df
        - The duplicate rows of vdo_df have been removed.
    '''
    # Group by 'trending_date' and calculate the mean number of comments
    avg_comments_per_date = vdo_df.groupby('trending_date')['comment_count'].mean()
    # Find the date with the minimum average number of comments
    min_avg_comments_date = avg_comments_per_date.idxmin()
    return min_avg_comments_date


def Q5(vdo_df):
    '''
        5. Compare "Sports" and "Comedy": 
           How many days have more total daily views for "Sports" than for "Comedy"?
        - GBvideos.csv has been loaded into memory and is ready to be utilized as vdo_df
        - The duplicate rows of vdo_df have been removed.
        - Load additional data from 'GB_category_id.json' for category mapping.
        - To access 'GB_category_id.json', use the path '/data/GB_category_id.json'.
    '''
    # Load the category mapping from the JSON file
    with open('/data/GB_category_id.json', 'r') as f:
        category_data = json.load(f)
    # Create a mapping from category_id to category_name
    category_mapping = {int(item['id']): item['snippet']['title'] for item in category_data['items']}
    # Map the category names to the dataset
    vdo_df['category_name'] = vdo_df['category_id'].map(category_mapping)
    
    # Filter data for "Sports" and "Comedy"
    sports_df = vdo_df[vdo_df['category_name'] == 'Sports']
    comedy_df = vdo_df[vdo_df['category_name'] == 'Comedy']
    
    # Group by 'trending_date' and sum the views for each category
    sports_daily_views = sports_df.groupby('trending_date')['views'].sum()
    comedy_daily_views = comedy_df.groupby('trending_date')['views'].sum()
    
    # Compare daily views and count the number of days where "Sports" has more views than "Comedy"
    comparison = sports_daily_views > comedy_daily_views
    days_more_sports_views = comparison.sum()
    
    return days_more_sports_views


# Example usage and testing
"""
file_path = '/data/GBvideos.csv'
df = pd.read_csv(file_path)
vdo_df = df.drop_duplicates()

print(Q1()) # Returns the number of rows after deduplication
print(Q2(vdo_df)) # Returns the count of unique titles with more dislikes than likes
print(Q3(vdo_df)) # Returns the count of videos trending on 22 Jan 2018 with > 10,000 comments
print(Q4(vdo_df)) # Returns the trending date with the minimum average comments
print(Q5(vdo_df)) # Returns the number of days where "Sports" has more views than "Comedy"
"""
