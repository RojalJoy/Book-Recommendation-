import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('pages/dataset.csv')

# Remove whitespace from column names
df.columns = df.columns.str.strip()

# Bar chart colored by Sex
bar_chart_sex = px.bar(df, x='Reading frequency', y='Age', color='Gender', title='Age Distribution by Reading Frequency and Gender')
st.plotly_chart(bar_chart_sex)

# Pie chart
pie_chart = px.pie(df, names='Stream(MEDIICAL,ENGINEERING,DESIGNING,etc.)', title='Stream Distribution')
st.plotly_chart(pie_chart)

# 3D Scatter plot colored by Reading frequency
scatter_3d = px.scatter_3d(df, x='Gender', y='Average Reading Duration (minutes)', z='Age', color='Reading frequency', title='Reading Habits 3D Scatter Plot Colored by Reading Frequency')
st.plotly_chart(scatter_3d)

# Scatter plot
scatter_plot = px.scatter(df, x='Types of content (e.g., textbooks, research papers, fiction, technical articles)', y='Average Reading Duration (minutes)', color='Age', title='Reading Duration by Content Type Colored by Age')
st.plotly_chart(scatter_plot)
