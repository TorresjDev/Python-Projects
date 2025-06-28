import csv
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import requests
import os


cvs_file = "socialmediapostdata.csv"
cvs_url = "https://raw.githubusercontent.com/BuffTechTalk/CIDM6311/main/socialmediapostdata.csv"

if not os.path.exists(cvs_file):
    response = requests.get(cvs_url)
    with open(cvs_file, "wb") as csv_file:
        csv_file.write(response.content)

# Load the dataset
