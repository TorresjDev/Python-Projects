from wordcloud import WordCloud, STOPWORDS
import csv
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import plotly.express as px
import requests
import os

load_dotenv()
cvs_file = "socialmediapostdata.csv"
cvs_url_key = "CVS_URL"

# welcome message
print("Welcome to the Social Media Analyzer!")
print("-" * 75)
print("This program will analyze social media posts data and visualize the number of posts per author per day.")
print("Please follow the instructions to enter the URL of the CSV file containing the social media posts data.")
print("-" * 75)

# prompt user for the URL of the CSV file if not use env default
cvs_url = input(
    "Please enter the URL to the CSV file (or press Enter to use the default): ") or os.getenv(cvs_url_key)

# Check if the CSV file exists, if not download it from the provided URL
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
# print(post_data)

# calculate the daily number of posts created by each user using to_datetime method to convert the 'date_time' column to datetime format
post_data['date_time'] = pd.to_datetime(
    post_data['date_time'], format='%d/%m/%Y %H:%M').dt.date
print(post_data)

# Calculate the daily number of posts created by each user
content_counts = post_data.groupby(['author', 'date_time'])[
    'content'].count().reset_index(name='content_count')
print(content_counts)

# Show few rows of the content_counts DataFrame to verify the grouping and counting
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

# Plot the number of posts per author per day using Plotly Express
fig = px.line(
    content_counts,
    x='date_time',
    y='content_count',
    color='author',
    markers=True,
    labels={'content_count': 'Number of Posts', 'date_time': 'Date'},
    title='Number of Posts per Author per Day')
fig.show()

# Filter the DataFrame prompt user for input author
author_name = input(
    "Please enter the author name to filter (e.g., 'jimmyfallon'): ")
author_data = content_counts[content_counts['author'] == author_name].copy()

# Ensure that 'date_time' is in datetime format for plotting
author_data['date_time'] = pd.to_datetime(author_data['date_time'])

# Plot the number of posts by the selected author per day using matplotlib
plt.figure(figsize=(12, 6))
plt.plot(author_data['date_time'], author_data['content_count'],
         label=author_name, linestyle='-', color='blue')
plt.title('Number of Posts per Author per Day')
plt.xlabel('Date')
plt.ylabel('Number of Posts')
plt.grid(axis='y', linestyle='--')
plt.tight_layout()
plt.show()

# Filter the DataFrame for the selected author's posts
author_posts = post_data[post_data['author'] == author_name].copy()

# Ensure that 'date_time' is in datetime format for plotting
author_posts['date_time'] = pd.to_datetime(
    author_posts['date_time'])

# Extract the content of the selected author's posts
author_content = author_posts['content']

print(author_content)

# Generate a word cloud from the selected author's posts content
all_content = ' '.join(author_content.astype(str))
# Update the stop words to include common words that may not be useful in the word cloud
updated_stop_words = STOPWORDS.update(["https", "co", "t"])
# Generate the word cloud using WordCloud from wordcloud library
wordcloud = WordCloud(stopwords=updated_stop_words, width=800,
                      height=400, background_color="white").generate(all_content)

# Display the generated word cloud using matplotlib
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

# Convert 'date_time' to datetime format for accurate plotting
author_posts['date_time'] = pd.to_datetime(
    author_posts['date_time'])

print(author_posts)

# Plot the daily number of likes and shares for the selected author using matplotlib
plt.figure(figsize=(12, 6))
plt.plot(author_posts['date_time'], author_posts['number_of_likes'],
         label='Daily Likes', linestyle='-', color='blue')
plt.plot(author_posts['date_time'], author_posts['number_of_shares'],
         label='Daily Shares', linestyle='-', color='orange')
plt.title(f'Daily Likes and Shares for {author_name}')
plt.xlabel('Date')
plt.ylabel('Count of Likes/Shares')
plt.legend()
plt.grid(axis='y', linestyle='--')
plt.tight_layout()
plt.show()


# Plot the daily number of likes and shares for the selected author using Plotly Express
fig = px.line(
    author_posts,
    x='date_time',
    y=['number_of_likes', 'number_of_shares'],
    labels={'date_time': 'Date', 'value': 'Count'},
    title=f'Daily Likes and Shares for {author_name}',
    markers=True,
    color_discrete_map={'number_of_likes': 'blue',
                        'number_of_shares': 'orange'}
)
fig.update_layout(
    xaxis_title='Date',
    yaxis_title='Count of Likes/Shares',
    legend_title='Metrics'
)
fig.show()


# ending message
print("Thank you for using the Social Media Analyzer!")
print("-" * 75)
print("We hope you found the analysis and visualizations helpful.")
print("Feel free to explore the data further or modify the code for your own analysis.")
print("-" * 75)
print("Goodbye!")
print("-" * 75)
