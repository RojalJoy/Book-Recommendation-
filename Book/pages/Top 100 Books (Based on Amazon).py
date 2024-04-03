import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv('pages/Top-100.csv')
# Title and description

# Set page title and icon
st.set_page_config(page_title='Top 100 Books', page_icon=':books:')
st.title('Top Books in Each Category')
# Add a filter for genre selection
genres = df['genre'].unique().tolist()
selected_genre = st.selectbox('Select Genre', genres)
filtered_df = df[df['genre'] == selected_genre]

# Display filtered results
if not filtered_df.empty:
    st.markdown(f'### Top Books in {selected_genre}')
    st.write(filtered_df)
else:
    st.warning('No books found for the selected genre.')
# Title and description
st.title('Top 100 Books')
st.markdown('This is a curated list of the top 100 books based on various criteria.')

# Display the top 100 books in a table
st.write(df)



# Add a footer with credits or additional information
st.markdown('---')
st.markdown('Created by Rojal')
st.markdown('[Source Code](https://github.com/yourusername/top-books-app)')
