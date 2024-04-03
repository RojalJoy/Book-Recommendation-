import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv('https://github.com/RojalJoy/Book-Recommendation-/blob/main/Book/pages/data.csv')

# Title of the web app
st.title('Book Recommendation System')

# Add a search bar for book title and author name
search_query = st.text_input("Search by Book Title or Author Name")

# Add a slider for average rating filter
min_rating, max_rating = st.slider("Select Average Rating Range", float(df['average_rating'].min()), float(df['average_rating'].max()), (float(df['average_rating'].min()), float(df['average_rating'].max())))

# Add a select box for selecting genre
genres = df['categories'].unique().tolist()
selected_genre = st.selectbox('Select Genre', genres)

# Filter books based on user input
if search_query:
    filtered_books = df[df['title'].str.contains(search_query, case=False) | df['authors'].str.contains(search_query, case=False)]
else:
    filtered_books = df

# Filter books based on selected genre and average rating range
filtered_books = filtered_books[(filtered_books['categories'] == selected_genre) & (filtered_books['average_rating'] >= min_rating) & (filtered_books['average_rating'] <= max_rating)]

# Display filtered books in a grid layout with social sharing buttons and "View Details" button below each book
st.subheader('Recommended Books:')
num_books = len(filtered_books)
books_per_row = 4
num_rows = (num_books - 1) // books_per_row + 1

for row in range(num_rows):
    cols = st.columns(books_per_row)
    for col in range(books_per_row):
        book_index = row * books_per_row + col
        if book_index < num_books:
            book = filtered_books.iloc[book_index]
            if pd.isnull(book['thumbnail']):
                cols[col].write("No image available")
            else:
                cols[col].image(book['thumbnail'], caption='Thumbnail Image', width=150)
            cols[col].write(f"**Title:** {book['title']}")
            cols[col].write(f"**Author:** {book['authors']}")
            cols[col].write(f"**Average Rating:** {book['average_rating']}")
            cols[col].write(f"**Genre:** {book['categories']}")

            # Add share button with icons using Markdown and HTML
            share_html = f"""
                <a href="https://twitter.com/intent/tweet?url=&text=Check out this book: {book['title']} by {book['authors']}" target="_blank">
                    <img src="https://simplesharebuttons.com/images/somacro/twitter.png" alt="Twitter" style="width: 30px;"/>
                </a>
                <a href="https://www.facebook.com/sharer/sharer.php?u=&title=Check out this book: {book['title']} by {book['authors']}" target="_blank">
                    <img src="https://simplesharebuttons.com/images/somacro/facebook.png" alt="Facebook" style="width: 30px;"/>
                </a>
                <a href="https://www.linkedin.com/shareArticle?url=&title=Check out this book: {book['title']} by {book['authors']}" target="_blank">
                    <img src="https://simplesharebuttons.com/images/somacro/linkedin.png" alt="LinkedIn" style="width: 30px;"/>
                </a>
                <a href="mailto:?subject=Check out this book: {book['title']} by {book['authors']}&body=I thought you might like this book: {book['title']} by {book['authors']}. Check it out: [Book Link]" target="_blank">
                    <img src="https://simplesharebuttons.com/images/somacro/email.png" alt="Email" style="width: 30px;"/>
                </a>
                """
            cols[col].markdown(share_html, unsafe_allow_html=True)

            # Add "View Details" button below each book with a unique key
            button_key = f"details_button_{book_index}"
            if st.button(f"View Details of {book['title']}", key=button_key):
                st.write(f"**Title:** {book['title']}")
                st.write(f"**Author:** {book['authors']}")
                st.write(f"**Average Rating:** {book['average_rating']}")
                st.write(f"**Genre:** {book['categories']}")
                st.write(f"**Year Published:** {book['published_year']}")
                st.write(f"**Description:** {book['description']}")
                st.write(f"**Number of Pages:** {book['num_pages']}")
                st.write("---")
