**Video Game Sales Analysis | Data Analysis Project | Exploratory Data Analysis (EDA)**




Dataset Link - https://mavenanalytics.io/data-playground

Recommended Analysis

Which titles sold the most worldwide?

Which year had the highest sales? Has the industry grown over time?

Do any consoles seem to specialize in a particular genre?

What titles are popular in one region but flop in another?

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
import plotly.express as px

df = pd.read_csv('vgchartz-2024.csv')

df.shape

df.head()

Data Cleaning

# Deleting unwanted column

df.drop(columns = 'img', inplace = True)

df.columns

# checking null values

df.isna().sum()

df.info()

## Handling Null Values for numeric data type

num_cols = df.select_dtypes(include = np.number).columns.tolist()

num_cols

# Imputation

imputer = SimpleImputer(strategy = 'mean')
df[num_cols] = imputer.fit_transform(df[num_cols])

df.isna().sum()

## Handling Missing Values for date time column
## Coverting the datatype of date column

df['release_date'] = pd.to_datetime(df['release_date'])
df['last_update'] = pd.to_datetime(df['last_update'])



df.info()

df['release_date'].fillna(df['release_date'].median(), inplace = True)
df['last_update'].fillna(df['last_update'].median(), inplace = True)

df.isna().sum()

## Handling Missing values from remaining object data type

df.dropna(inplace = True)

df.isna().sum()

EDA

## 1. Which titles sold the most worldwide?


df.groupby('title')['total_sales'].sum().reset_index()

sales_by_title = df.groupby('title')['total_sales'].sum().reset_index()

sales_by_title.sort_values(by = 'total_sales', ascending= False)

sales_by_title_sorted = sales_by_title.sort_values(by = 'total_sales', ascending= False)

px.bar(sales_by_title_sorted.head(10), x = 'title', y = 'total_sales',
       title = 'Top 10 Titles by Worldwide sales')

Grand Theft Auto V, Call of Duty: Black Ops and Call of Duty: Modern Warfare 3 sold the most worldwide.

## Which year had the highest sales? Has the industry grown over time?


df['release_year']=df['release_date'].dt.year

sales_by_year = df.groupby('release_year')['total_sales'].sum().reset_index()

sales_by_year_sorted = sales_by_year.sort_values(by = 'total_sales', ascending = False)

px.bar(sales_by_year_sorted.head(10), x = 'release_year', y = 'total_sales',
       title = 'Top 10 years by Worldwide sales')

Year 2008 has made the highest sales worldwide.

px.line(sales_by_year, x = 'release_year', y = 'total_sales', title = 'Worldwide Sales Over Time')

Industry grew around 2008, However, it degraded somewhere around 2010 and is constant since then.

## Do any consoles seem to specialize in a particular genre?


console_vs_genre = df.groupby(['console','genre'])['total_sales'].sum().reset_index()

console_vs_genre_sorted = console_vs_genre.sort_values(by = 'total_sales', ascending= False)

px.sunburst(console_vs_genre_sorted, path = ['console', 'genre'], values = 'total_sales',
            title = 'Console Specialization in Genre')

PC console do seems to specialize in Adventure, Strategy and Misc Genre.

## What titles are popular in one region but flop in another?

df.head()

df['na_ratio']=df['na_sales']/df['total_sales']
df['jp_ratio']=df['jp_sales']/df['total_sales']
df['pal_ratio']=df['pal_sales']/df['total_sales']

**Titles that are popular in na but flop in other regions.**

na_popular = df[(df.na_ratio > 0.8) & (df.jp_ratio < 0.2) & (df.pal_ratio < 0.2 )]

na_popular

px.bar(na_popular.head(5), x = 'title', y = ['na_sales', 'jp_sales', 'pal_sales'],
       title = 'Most popular titles in NA Region but flop in other regions')

**Madden NFL 2004, Madden NFL 2005 and Madden NFL 06 titles are popular in NA Region but Flop in other regions.**

**Titles that are popular in jp region but flop in other regions.**

jp_popular = df[(df.jp_ratio > 0.8) & (df.na_ratio < 0.2) & (df.pal_ratio < 0.2 )]

jp_popular

px.bar(jp_popular.head(5), x = 'title', y = ['na_sales', 'jp_sales', 'pal_sales'],
       title = 'Most popular titles in JP Region but flop in other regions')

**Hot Shots Golf, Famista '89 - Kaimaku Han!! and R.B.I. Basebal titles are popular in JP Region but Flop in other regions.**

**Titles that are popular in pal region but flop in other regions**

pal_popular = df[(df.pal_ratio > 0.8) & (df.na_ratio < 0.2) & (df.jp_ratio < 0.2 )]

pal_popular

px.bar(pal_popular.head(5), x = 'title', y = ['na_sales', 'jp_sales', 'pal_sales'],
       title = 'Most popular titles in PAL Region but flop in other regions')

**The Sims 3 and Colin McRae Rallytitles are popular in PAL Region but Flop in other regions.**

