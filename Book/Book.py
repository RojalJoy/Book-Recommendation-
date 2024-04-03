import streamlit as st

def run():
    # Set page configuration
    st.set_page_config(
        page_title="Book Recommendation Site",
        page_icon="📚",  # Set app icon to a book emoji
        layout="wide"  # Set wide layout for dashboard
    )

    # Display website description
    st.header("Welcome to our Book Recommendation Site!")
    st.write("""
        Our platform is designed to help book enthusiasts discover new and exciting reads based on their interests and preferences. Whether you're a fiction fanatic, a non-fiction aficionado, or someone in between, we've got you covered with a curated list of the top 100 books sourced from Amazon's vast collection.

        What sets us apart is our focus on data-driven recommendations and insightful analysis of reading habits. We dive deep into book statistics, analyzing trends, genres, authorship, and reader preferences to provide you with personalized suggestions that match your reading style.
    """)

    # Create a two-column layout for dashboard sections
    col1, col2 = st.columns(2)

    # Display key features in the left column
    with col1:
        st.subheader("Key Features:")
        st.write("- Top 100 Books: Explore the best books across various genres...")
        st.write("- Data Visualization: Dive into interactive charts...")
        # ... List other features

    # Add a placeholder for future "User Input" section in right column
    with col2:
        st.subheader("More Features")
        st.write("- Personalized Recommendations: Enter your preferences for a tailored reading list.")
        st.write("- Insightful Analysis: Explore trends, popular authors, and hidden gems.")
        st.write("- Clean and intuitive interface for easy navigation.")

    # Display image and caption at the bottom (optional)
    st.empty()
    st.image("pages/books.jpg", use_column_width=True, caption="Happy Reading!")

if __name__ == "__main__":
    run()
