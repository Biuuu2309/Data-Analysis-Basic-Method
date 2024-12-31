# %% [markdown]
# CLONE DATASET

# %%
# import kagglehub

# # Download latest version
# path = kagglehub.dataset_download("thedevastator/youtube-trending-videos-dataset")

# print("Path to dataset files:", path)

# %% [markdown]
# DATA CLEANING

# %%
import pandas as pd
import numpy as np
import csv
import random

YT_Table = pd.read_csv('E:\Data Analysis Basic Method\Project\Data-Analysis-Basic-Method\Dataset5\Youtube_Test.csv')
YT_Table
DF = pd.DataFrame(YT_Table)
DF

# %% [markdown]
# KIEM TRA DU LIEU NULL

# %%
DF.isnull()

# %% [markdown]
# CHU DONG XOA DU LIEU TREN CAC FIELDS

# %% [markdown]
# 1. TAGS

# %%
DF.loc[[i for i in range(0,5)], 'tags'] = np.nan
DF


# %% [markdown]
# 2. VIEWS

# %%
DF.loc[[i for i in range(5,9)], 'views'] = np.nan
DF

# %% [markdown]
# 3. LIKES

# %%
DF.loc[[i for i in range(9, 15)], 'likes'] = np.nan
DF

# %% [markdown]
# 4. DISLIKES

# %%
DF.loc[[i for i in range(15, 20)], 'dislikes'] = np.nan
DF

# %% [markdown]
# 5. COMMENT COUNTS

# %%
DF.loc[[i for i in range(20, 25)], 'comment_count'] = np.nan

# %% [markdown]
# 6. COMMENTS DISABLED

# %%
DF.loc[[i for i in range(25, 30)], 'comments_disabled'] = np.nan
DF

# %% [markdown]
# 7. RATINGS DISABLED

# %%
DF.loc[[i for i in range(30, 35)], 'ratings_disabled'] = np.nan


# %% [markdown]
# 8. VIDEO ERROR OR REMOVED

# %%
DF.loc[[i for i in range(35, 40)], 'video_error_or_removed'] = np.nan


# %% [markdown]
# DIEN GIA TRI CON THIEU

# %% [markdown]
# VIEWS

# %%
MMM = [int(DF['views'].mean()), int(DF['views'].mode()[0]), int(DF['views'].median())]
DF['views'].fillna(min(MMM), inplace=True)
DF

# %% [markdown]
# LIKES

# %%
MMM = [int(DF['likes'].mean()), int(DF['likes'].mode()[0]), int(DF['likes'].median())]
DF['likes'].fillna(min(MMM), inplace=True)
DF

# %% [markdown]
# DISLIKES

# %%
MMM = [int(DF['dislikes'].mean()), int(DF['dislikes'].mode()[0]), int(DF['dislikes'].median())]
DF['dislikes'].fillna(min(MMM), inplace=True)
DF

# %% [markdown]
# COMMENT COUNT

# %%
MMM = [int(DF['comment_count'].mean()), int(DF['comment_count'].mode()[0]), int(DF['comment_count'].median())]
DF['comment_count'].fillna(min(MMM), inplace=True)
DF

# %% [markdown]
# COMMENTS DISABLED

# %% [markdown]
# Random by percent

# %%
true_ratio = len(DF[DF['comments_disabled'] == True]) / len(DF)

random_fill = np.random.choice([True, False], size=len(DF), p=[true_ratio, 1 - true_ratio])

DF['comments_disabled'] = DF['comments_disabled'].fillna(pd.Series(random_fill))

# %% [markdown]
# RATINGS DISABLED

# %%
true_ratio = len(DF[DF['ratings_disabled'] == True]) / len(DF)

random_fill = np.random.choice([True, False], size=len(DF), p=[true_ratio, 1 - true_ratio])

DF['ratings_disabled'] = DF['ratings_disabled'].fillna(pd.Series(random_fill))

# %% [markdown]
# VIDEO ERROR OR REMOVED

# %%
true_ratio = len(DF[DF['video_error_or_removed'] == True]) / len(DF)

random_fill = np.random.choice([True, False], size=len(DF), p=[true_ratio, 1 - true_ratio])

DF['video_error_or_removed'] = DF['video_error_or_removed'].fillna(pd.Series(random_fill))

# %% [markdown]
# TAGS

# %%
def create_tags(row):
    tags = ''
    lst = row['title'].split()
    for j, word in enumerate(lst):
        if j == 0:
            tags += str(word) + '|"'  
        elif j == len(lst) - 1:
            tags += str(word) + '"""'  
        else:
            tags += str(word) + '""|""'  
    tags = tags.strip()

    tags = tags.translate(str.maketrans('', '', ":()?!"))
    return tags

DF['tags'] = DF.apply(lambda row: create_tags(row) if pd.isna(row['tags']) else row['tags'], axis=1)

# %% [markdown]
# TAGS [none]

# %%
DF_2 = DF[DF['tags'] == '[none]']

DF_2.reset_index(drop=True, inplace=True)

for i in range(len(DF_2)):  
    lst = DF_2.loc[i, 'title'].split()  
    tags_list = []
    for j in range(len(lst)):  
        if j == 0:
            tags_list.append(str(lst[j]) + '|"')  
        elif j == len(lst) - 1:
            tags_list.append(str(lst[j]) + '"""')  
        else:
            tags_list.append(str(lst[j]) + '""|""')  
    
    tags = ''.join(tags_list).strip()
    for char in ":()?!":
        tags = tags.replace(char, "")
    
    DF_2.loc[i, 'tags'] = tags
DF.loc[DF['tags'] == '[none]', ['title', 'tags']] = DF_2[['title', 'tags']].values


# %% [markdown]
# LAM MIN DU LIEU THEO 3 CACH DE DE DANG SO SANH

# %% [markdown]
# VIEWS - MEAN - 5 NHOM

# %%
DFS = DF.sort_values(by='views', ascending=True)
DF1 = DFS[:int(len(DFS)/5)]
DF2 = DFS[int(len(DFS)/5):int(len(DFS)/5)*2]
DF3 = DFS[int(len(DFS)/5)*2:int(len(DFS)/5)*3]
DF4 = DFS[int(len(DFS)/5)*3:int(len(DFS)/5)*4]
DF5 = DFS[int(len(DFS)/5)*4:]

DFS.loc[[i for i in range(0,int(len(DFS)/5))], 'views'] = int(DF1['views'].mean())
DFS.loc[[i for i in range(int(len(DFS)/5),int(len(DFS)/5)*2)], 'views'] = int(DF2['views'].mean())
DFS.loc[[i for i in range(int(len(DFS)/5)*2,int(len(DFS)/5)*3)], 'views'] = int(DF3['views'].mean())
DFS.loc[[i for i in range(int(len(DFS)/5)*3,int(len(DFS)/5)*4)], 'views'] = int(DF4['views'].mean())
DFS.loc[[i for i in range(int(len(DFS)/5)*4,len(DFS))], 'views'] = int(DF5['views'].mean())
DFS

# %% [markdown]
# UPDATE CHO DF

# %%
DF = DF.sort_values(by='views', ascending=True)
DF1 = DF[:int(len(DF)/5)]
DF2 = DF[int(len(DF)/5):int(len(DF)/5)*2]
DF3 = DF[int(len(DF)/5)*2:int(len(DF)/5)*3]
DF4 = DF[int(len(DF)/5)*3:int(len(DF)/5)*4]
DF5 = DF[int(len(DF)/5)*4:]

DF.loc[[i for i in range(0,int(len(DF)/5))], 'views'] = int(DF1['views'].mean())
DF.loc[[i for i in range(int(len(DF)/5),int(len(DF)/5)*2)], 'views'] = int(DF2['views'].mean())
DF.loc[[i for i in range(int(len(DF)/5)*2,int(len(DF)/5)*3)], 'views'] = int(DF3['views'].mean())
DF.loc[[i for i in range(int(len(DF)/5)*3,int(len(DF)/5)*4)], 'views'] = int(DF4['views'].mean())
DF.loc[[i for i in range(int(len(DF)/5)*4,len(DF))], 'views'] = int(DF5['views'].mean())
DF

# %% [markdown]
# LIKES - MEDIAN - 5 NHOM

# %%
DFS2 = DFS.sort_values(by='likes', ascending=True)
DF1 = DFS2[:int(len(DFS2)/5)]
DF2 = DFS2[int(len(DFS2)/5):int(len(DFS2)/5)*2]
DF3 = DFS2[int(len(DFS2)/5)*2:int(len(DFS2)/5)*3]
DF4 = DFS2[int(len(DFS2)/5)*3:int(len(DFS2)/5)*4]
DF5 = DFS2[int(len(DFS2)/5)*4:]

DFS2.loc[[i for i in range(0,int(len(DFS2)/5))], 'likes'] = int(DF1['likes'].median())
DFS2.loc[[i for i in range(int(len(DFS2)/5),int(len(DFS2)/5)*2)], 'likes'] = int(DF2['likes'].median())
DFS2.loc[[i for i in range(int(len(DFS2)/5)*2,int(len(DFS2)/5)*3)], 'likes'] = int(DF3['likes'].median())
DFS2.loc[[i for i in range(int(len(DFS2)/5)*3,int(len(DFS2)/5)*4)], 'likes'] = int(DF4['likes'].median())
DFS2.loc[[i for i in range(int(len(DFS2)/5)*4,len(DFS2))], 'likes'] = int(DF5['likes'].median())
DFS2

# %% [markdown]
# UPDATE CHO DF

# %%
DF = DF.sort_values(by='likes', ascending=True)
DF1 = DF[:int(len(DF)/5)]
DF2 = DF[int(len(DF)/5):int(len(DF)/5)*2]
DF3 = DF[int(len(DF)/5)*2:int(len(DF)/5)*3]
DF4 = DF[int(len(DF)/5)*3:int(len(DF)/5)*4]
DF5 = DF[int(len(DF)/5)*4:]

DF.loc[[i for i in range(0,int(len(DF)/5))], 'likes'] = int(DF1['likes'].median())
DF.loc[[i for i in range(int(len(DF)/5),int(len(DF)/5)*2)], 'likes'] = int(DF2['likes'].median())
DF.loc[[i for i in range(int(len(DF)/5)*2,int(len(DF)/5)*3)], 'likes'] = int(DF3['likes'].median())
DF.loc[[i for i in range(int(len(DF)/5)*3,int(len(DF)/5)*4)], 'likes'] = int(DF4['likes'].median())
DF.loc[[i for i in range(int(len(DF)/5)*4,len(DF))], 'likes'] = int(DF5['likes'].median())
DF

# %% [markdown]
# DISLIKE - BOUNDARIES - 5 NHOM

# %%
DFS3 = DFS.sort_values(by='dislikes', ascending=True)
DF1 = DFS3[:int(len(DFS3)/5)]
DF2 = DFS3[int(len(DFS3)/5):int(len(DFS3)/5)*2]
DF3 = DFS3[int(len(DFS3)/5)*2:int(len(DFS3)/5)*3]
DF4 = DFS3[int(len(DFS3)/5)*3:int(len(DFS3)/5)*4]
DF5 = DFS3[int(len(DFS3)/5)*4:]

for i in range(0,int(len(DFS3)/5)):
    if i - int(DF1['dislikes'].min()) < int(DF1['dislikes'].max()) - i:
        DFS3.loc[i, 'dislikes'] = int(DF1['dislikes'].min())
    else:
        DFS3.loc[i, 'dislikes'] = int(DF1['dislikes'].max())
for i in range(int(len(DFS3)/5),int(len(DFS3)/5)*2):
    if i - int(DF2['dislikes'].min()) < int(DF2['dislikes'].max()) - i:
        DFS3.loc[i, 'dislikes'] = int(DF2['dislikes'].min())
    else:
        DFS3.loc[i, 'dislikes'] = int(DF2['dislikes'].max())
for i in range(int(len(DFS3)/5)*2,int(len(DFS3)/5)*3):
    if i - int(DF3['dislikes'].min()) < int(DF3['dislikes'].max()) - i:
        DFS3.loc[i, 'dislikes'] = int(DF3['dislikes'].min())
    else:
        DFS3.loc[i, 'dislikes'] = int(DF3['dislikes'].max())
for i in range(int(len(DFS3)/5)*3,int(len(DFS3)/5)*4):
    if i - int(DF4['dislikes'].min()) < int(DF4['dislikes'].max()) - i:
        DFS3.loc[i, 'dislikes'] = int(DF4['dislikes'].min())
    else:
        DFS3.loc[i, 'dislikes'] = int(DF4['dislikes'].max())
for i in range(int(len(DFS3)/5)*4,len(DFS3)):
    if i - int(DF5['dislikes'].min()) < int(DF5['dislikes'].max()) - i:
        DFS3.loc[i, 'dislikes'] = int(DF5['dislikes'].min())
    else:
        DFS3.loc[i, 'dislikes'] = int(DF5['dislikes'].max())
DFS3

# %% [markdown]
# UPDATE CHO DF

# %%
DF = DF.sort_values(by='dislikes', ascending=True)
DF1 = DF[:int(len(DF)/5)]
DF2 = DF[int(len(DF)/5):int(len(DF)/5)*2]
DF3 = DF[int(len(DF)/5)*2:int(len(DF)/5)*3]
DF4 = DF[int(len(DF)/5)*3:int(len(DF)/5)*4]
DF5 = DF[int(len(DF)/5)*4:]

for i in range(0,int(len(DF)/5)):
    if i - int(DF1['dislikes'].min()) < int(DF1['dislikes'].max()) - i:
        DF.loc[i, 'dislikes'] = int(DF1['dislikes'].min())
    else:
        DF.loc[i, 'dislikes'] = int(DF1['dislikes'].max())
for i in range(int(len(DF)/5),int(len(DF)/5)*2):
    if i - int(DF2['dislikes'].min()) < int(DF2['dislikes'].max()) - i:
        DF.loc[i, 'dislikes'] = int(DF2['dislikes'].min())
    else:
        DF.loc[i, 'dislikes'] = int(DF2['dislikes'].max())
for i in range(int(len(DF)/5)*2,int(len(DF)/5)*3):
    if i - int(DF3['dislikes'].min()) < int(DF3['dislikes'].max()) - i:
        DF.loc[i, 'dislikes'] = int(DF3['dislikes'].min())
    else:
        DF.loc[i, 'dislikes'] = int(DF3['dislikes'].max())
for i in range(int(len(DF)/5)*3,int(len(DF)/5)*4):
    if i - int(DF4['dislikes'].min()) < int(DF4['dislikes'].max()) - i:
        DF.loc[i, 'dislikes'] = int(DF4['dislikes'].min())
    else:
        DF.loc[i, 'dislikes'] = int(DF4['dislikes'].max())
for i in range(int(len(DF)/5)*4,len(DF)):
    if i - int(DF5['dislikes'].min()) < int(DF5['dislikes'].max()) - i:
        DF.loc[i, 'dislikes'] = int(DF5['dislikes'].min())
    else:
        DF.loc[i, 'dislikes'] = int(DF5['dislikes'].max())
DF

# %%
DF

# %% [markdown]
# TIM DO LECH CHUAN LON NHAT

# %%
S2 = (DF['likes']**2).sum()
S3 = (DF['dislikes']**2).sum()
S4 = (DF['comment_count']**2).sum()

y = S2 / len(DF) - DF['likes'].mean()**2
z = S3 / len(DF) - DF['dislikes'].mean()**2
t = S4 / len(DF) - DF['comment_count'].mean()**2

variance = sum((DF['views'] - DF['views'].mean())**2) / len(DF)

std_views = variance**0.5
std_likes = y**0.5
std_dislikes = z**0.5
std_comment_count = t**0.5

print(std_views, std_likes, std_dislikes, std_comment_count)

DFS_SORT = DF.sort_values(by='views', ascending=True)

DFS_SORT.iloc[:5, DFS_SORT.columns.get_loc('views')] *= 1.1

DFS_SORT.iloc[-5:, DFS_SORT.columns.get_loc('views')] *= 0.9

DF = DFS_SORT


# %% [markdown]
# XAC DINH GIA TRI NGOAI LE

# %% [markdown]
# VIEWS

# %%
DFSV = DF.sort_values(by='views', ascending=True)
Q1 = DFSV.iloc[int(len(DF)*0.25)]['views']
Q3 = DFSV.iloc[int(len(DF)*0.75)]['views']

OL_Views = DFSV[(DFSV['views'] < Q1 - (1.5 * (Q3 - Q1))) | (DFSV['views'] > Q3 + (1.5 * (Q3 - Q1)))]
OL_Views

# %% [markdown]
# LIKES

# %%
DFSL = DF.sort_values(by='likes', ascending=True)
Q1 = DFSL.iloc[int(len(DF)*0.25)]['likes']
Q3 = DFSL.iloc[int(len(DF)*0.75)]['likes']

OL_Likes = DFSL[(DFSL['likes'] < Q1 - (1.5 * (Q3 - Q1))) | (DFSL['likes'] > Q3 + (1.5 * (Q3 - Q1)))]
OL_Likes

# %% [markdown]
# DISLIKES

# %%
DFSDL = DF.sort_values(by='dislikes', ascending=True)
Q1 = DFSDL.iloc[int(len(DF)*0.25)]['dislikes']
Q3 = DFSDL.iloc[int(len(DF)*0.75)]['dislikes']

OL_DL = DFSDL[(DFSDL['dislikes'] < Q1 - (1.5 * (Q3 - Q1))) | (DFSDL['dislikes'] > Q3 + (1.5 * (Q3 - Q1)))]
OL_DL

# %% [markdown]
# COMMENT_COUNT

# %%
DFSCC = DF.sort_values(by='comment_count', ascending=True)
Q1 = DFSCC.iloc[int(len(DF)*0.25)]['comment_count']
Q3 = DFSCC.iloc[int(len(DF)*0.75)]['comment_count']

OL_CC = DFSCC[(DFSCC['comment_count'] < Q1 - (1.5 * (Q3 - Q1))) | (DFSCC['comment_count'] > Q3 + (1.5 * (Q3 - Q1)))]
OL_CC

# %% [markdown]
# XU LY DU LIEU KHONG NHAT QUAN

# %% [markdown]
# NGAY THANG NAM

# %% [markdown]
# CHU DONG DIEN LOI KHONG NHAT QUAN - trending_date

# %%
DF = DF.sort_values(by='index', ascending=True)
DF.loc[[i for i in range(0,5)], 'trending_date'] = '17.14.111'
DF.loc[[i for i in range(5,10)], 'trending_date'] = '17.144.11'
DF.loc[[i for i in range(10,15)], 'trending_date'] = '177.14.11'
DF.loc[[i for i in range(15,20)], 'trending_date'] = '11.14.17'
DF.loc[[i for i in range(20,25)], 'trending_date'] = '14.11.17'
DF

# %% [markdown]
# 17.14.111 | 17.144.11 | 177.14.11 | 11.14.17 | 14.11.17 -> 17.14.11

# %%
DF.loc[(DF['trending_date'] == '17.14.111') | (DF['trending_date'] == '17.144.11') | (DF['trending_date'] == '177.14.11') | (DF['trending_date'] == '11.14.17') | (DF['trending_date'] == '14.11.17'), 'trending_date'] = '17.14.11'
DF

# %% [markdown]
# DONG BO trending_date (yy.dd.mm) -> publish_date(dd/mm/yyyy)

# %%
def convert_date(date_str):
    year, day, month = date_str.split('.')
    year = '20' + year  
    return f'{day}/{month}/{year}'

DF['trending_date'] = DF['trending_date'].apply(convert_date)
DF

# %% [markdown]
# FIELD DANH NGHIA

# %% [markdown]
# published_day_of_week, publish_country

# %%
DF.loc[[i for i in range(8,13)], 'published_day_of_week'] = 'MONDAYY'
DF.loc[[i for i in range(0,5)], 'publish_country'] = 'uss'

# %% [markdown]
# MONDAYY -> Monday, uss -> US

# %%
valid_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

DF.loc[~DF['published_day_of_week'].isin(valid_days), 'published_day_of_week'] = DF['published_day_of_week'].str.title()
    
import re

def correct_day(day):
    if day in valid_days:
        return day
    corrected_day = re.sub(r'(\w)\1+', r'\1', day)
    return corrected_day if corrected_day in valid_days else day.lower()

DF['published_day_of_week'] = DF['published_day_of_week'].apply(correct_day)
DF

# %%
valid_countrys = ['US', 'FRANCE', 'CANADA', 'GB']

DF.loc[~DF['publish_country'].isin(valid_days), 'publish_country'] = DF['publish_country'].str.upper()
    
def correct_country(country):
    if country in valid_countrys:
        return country
    corrected_country = re.sub(r'(\w)\1+', r'\1', country)
    return corrected_country if corrected_country in valid_countrys else country.lower()

DF['publish_country'] = DF['publish_country'].apply(correct_country)
DF

# %% [markdown]
# CHUYEN DOI VA PHAN TACH DU LIEU

# %% [markdown]
# published_day_of_week

# %%
ordered_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

DF['published_day_of_week'] = pd.Categorical(DF['published_day_of_week'], categories=ordered_days, ordered=True)
sorted_days = DF['published_day_of_week'].drop_duplicates().sort_values()

dict_day = {day: i + 1 for i, day in enumerate(sorted_days, start=1)}

print(dict_day)


# %%
DF['published_day_of_week'] = DF['published_day_of_week'].map(dict_day)

# %% [markdown]
# publish_country

# %%
country = DF['publish_country'].drop_duplicates()
dict_country = {country: i for i, country in enumerate(country, start=1)}
DF['publish_country'] = DF['publish_country'].map(dict_country)

# %% [markdown]
# time_frame

# %%
times = [f'{i}:00 to {i}:59' for i in range(0, 24)]

DF['time_frame'] = pd.Categorical(DF['time_frame'], categories=times, ordered=True)
time_frame = DF['time_frame'].drop_duplicates().sort_values()
dict_time_frame = {time: i for i, time in enumerate(time_frame, start=1)}
DF['time_frame'] = DF['time_frame'].map(dict_time_frame)

# %%
DF

# %% [markdown]
# comments_disabled, ratings_disabled, video_error_or_removed

# %%
dict_bool = {True: 1, False: 0}
DF['comments_disabled'] = DF['comments_disabled'].map(dict_bool)
DF['ratings_disabled'] = DF['ratings_disabled'].map(dict_bool)
DF['video_error_or_removed'] = DF['video_error_or_removed'].map(dict_bool)
DF

# %% [markdown]
# Gop thanh 1 field

# %% [markdown]
# Tao cot moi co gia tri NaN

# %%
DF.insert(column= 'bool_field', loc= len(DF.columns), value=np.nan)
DF

# %% [markdown]
# Gan gia tri vao cot vua tao

# %%
unique_combinations = DF[['comments_disabled', 'ratings_disabled', 'video_error_or_removed']].drop_duplicates()

DF['bool_field'] = DF.apply(lambda row: f"{row['comments_disabled']}{row['ratings_disabled']}{row['video_error_or_removed']}" if pd.isna(row['bool_field']) else row['bool_field'], axis=1)

# %% [markdown]
# POP comments_disabled

# %%
DFT = DF
DFT = DFT.pop('comments_disabled')
DFT

# %% [markdown]
# POP ratings_disabled

# %%
DFT = DF
DFT = DFT.pop('ratings_disabled')
DFT

# %% [markdown]
# POP video_error_or_removed

# %%
DFT = DF
DFT = DFT.pop('video_error_or_removed')
DFT

# %% [markdown]
# Du lieu sau khi gom va xoa cot 

# %%
DFT = DF
DF

# %% [markdown]
# THONG KE

# %% [markdown]
# 1. MODE

# %% [markdown]
# trending_date, channel_title, category_id, publish_date, time_frame, published_day_of_week, publish_country, views, likes, dislikes, comment_count

# %%
DF[['trending_date', 'channel_title', 'category_id', 'publish_date', 'time_frame', 'published_day_of_week', 'publish_country', 'views', 'likes', 'dislikes', 'comment_count']].mode()

# %% [markdown]
# views, likes, dislikes, comment_count -> describle

# %%
DF[['views', 'likes', 'dislikes', 'comment_count']].describe()

# %% [markdown]
# DATA REDUCTION

# %% [markdown]
# PCA - Giam so chieu tu 4(views, likes, dislikes, comment_count) -> 3 | 2 | 1

# %%
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
data_scaled = scaler.fit_transform(DF[['views', 'likes', 'dislikes', 'comment_count']])

pca = PCA(n_components=2)  
data_pca = pca.fit_transform(data_scaled)

print("Dữ liệu sau khi PCA:", data_pca)
print("Tỷ lệ phương sai giải thích:", pca.explained_variance_ratio_)
data_pca

# %% [markdown]
# views, likes - Phan cum

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

plt.scatter(DF['views'], DF['likes'], c='gray', edgecolor='k')
plt.title("Dữ liệu trước khi phân cụm")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


# %%
from sklearn.cluster import KMeans

# Khởi tạo mô hình K-Means với 3 cụm
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(DF[['views', 'likes']])

# Lấy nhãn cụm
DF['Cluster'] = kmeans.labels_

print("\nDữ liệu sau phân cụm:")
print(DF.head())

# Vẽ các cụm
plt.scatter(DF['views'], DF['likes'], c=DF['Cluster'], cmap='viridis', edgecolor='k')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red')  # Tâm cụm
plt.title("Kết quả phân cụm với K-Means")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


# %% [markdown]
# Export to CSV

# %%
DF.to_csv(r'E:\Data Analysis Basic Method\Project\Data-Analysis-Basic-Method\NguyenMinhVu_PTDLCB_24\File CSV Sau chinh sua\Python\DataCleaningPython.csv')

# %%
YT_Tablee = pd.read_csv(r'E:\Data Analysis Basic Method\Project\Data-Analysis-Basic-Method\NguyenMinhVu_PTDLCB_24\File CSV Sau chinh sua\Python\DataCleaningPython.csv')
YT_Tablee


