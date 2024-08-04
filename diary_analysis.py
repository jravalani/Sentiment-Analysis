import streamlit as st
import plotly.express as px
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import glob

filepaths = glob.glob('diary/*.txt')
analyzer = SentimentIntensityAnalyzer()

# print(round(score['pos'] * 10, 2))
positive_value = []
negative_value = []
for files in filepaths:
    with open(files, 'r') as file:
        content = file.read()
    score = analyzer.polarity_scores(content)
    positive_value.append(round(score['pos'] * 10, 2))
    negative_value.append(round(score['neg'] * 10, 2))

dates = [name.strip(".txt").strip("diary/") for name in filepaths]
dates = sorted(dates)
st.header("Diary Tone")

st.subheader("Positivity")
pos_figure = px.line(x=dates, y=positive_value, labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(pos_figure)

st.subheader("Negativity")
neg_figure = px.line(x=dates, y=negative_value, labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(neg_figure)


st.subheader("Content")
for index, files in enumerate(filepaths):
    with open(files, 'r') as file:
        content = file.read()
        st.write(f"{dates[index]}\n\n{content}")
