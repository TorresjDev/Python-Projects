# required for generating word clouds
from wordcloud import WordCloud, STOPWORDS
import csv  # required for reading and writing CSV files for python
import pandas as pd  # required for data evaluation and analysis
import matplotlib.pyplot as plt  # required for plotting data using matplotlib
# required for creating interactive plots using Plotly Express
# required for loading environment variables from a .env file
from dotenv import load_dotenv
import plotly.express as px
import requests  # required for making HTTP requests to fetch data from URLs
import os  # required for interacting with the operating system, such as checking file existence


# Load environment variables from .env file
load_dotenv()
cvs_file = "socialmediapostdata.csv"
cvs_url_key = "CVS_URL"  # Environment variable key for the CSV URL

# welcome message
print("Welcome to the Social Media Analyzer!")
print("-" * 50)
print("This program will analyze social media posts data and visualize the number of posts per author per day.")
print("Please follow the instructions to enter the URL of the CSV file containing the social media posts data.")
print("-" * 50)

# prompt user for the URL of the CSV file if not use env default
cvs_url = input(
    "Please enter the URL to the CSV file (or press Enter to use the default): ") or os.getenv(cvs_url_key)

if not os.path.exists(cvs_file):
    response = requests.get(cvs_url)
    with open(cvs_file, "wb") as csv_file:
        csv_file.write(response.content)

# Load the dataset using pandas as pd
post_data = pd.read_csv(cvs_file, encoding='utf-8')
print(post_data)

# Clean the dataset by removing unnecessary columns using the drop method from pandas
post_data = post_data.drop(
    ['country', 'id', 'language', 'latitude', 'longitude'], axis=1)
print(post_data)

# calculate the daily number of posts created by each user using to_datetime method to convert the 'date_time' column to datetime format
post_data['date_time'] = pd.to_datetime(
    post_data['date_time'], format='%d/%m/%Y %H:%M').dt.date
print(post_data)

# Calculate the daily number of posts created by each user
content_counts = post_data.groupby(['author', 'date_time'])[
    'content'].count().reset_index(name='content_count')

print(content_counts)

content_counts['date_time'] = pd.to_datetime(content_counts['date_time'])

#  Plot the number of posts per author per day calculated above using matplotlib.pyplot
plt.figure(figsize=(12, 6))

for author in content_counts['author'].unique():
    author_data = content_counts[content_counts['author'] == author]
    plt.plot(author_data['date_time'],
             author_data['content_count'], marker='o', label=author)
plt.title('Number of Posts for Author per Day')
plt.xlabel('Date')
plt.ylabel('Number of Posts')
plt.legend(title='Author')
plt.tight_layout()
plt.show()

#  Plot the number of posts per author per day calculated above using or plotly express.
fig = px.line(
    content_counts,
    x='date_time',
    y='content_count',
    color='author',
    markers=True,
    labels={'content_count': 'Number of Posts', 'date_time': 'Date'},
    title='Number of Posts per Author per Day')
fig.show()

# Create a chart to show the number of daily posts of author jimmyfallon
