import mysql.connector
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from chat import get_chatbot_response, save_chat_to_database


# Connect to MySQL database
def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="7>>HhNN6/fZ",
            database="dataset"
        )
        return conn
    except mysql.connector.Error as err:
        print("Error:", err)
        return None

# Fetch file contents from the database
def fetch_file_contents(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT file_content FROM information")
        file_contents = cursor.fetchall()
        cursor.close()
        return file_contents
    except mysql.connector.Error as err:
        print("Error:", err)
        return None


def load_data_from_files(file_contents):
    data = []
    for file_content in file_contents:
        try:
            # Extract the text content from the tuple
            content = file_content[0]  # Assuming the text is in the first element of the tuple
            data.append({'file_content': content})
        except FileNotFoundError:
            print("Error: File not found")
            continue
    return pd.DataFrame(data)


def preprocess_text(text):
    # If the input is a tuple, extract the text content
    if isinstance(text, tuple):
        text = text[0]  # Assuming the text is in the first element of the tuple
    # Perform the actual preprocessing
    # Add your preprocessing logic here
    return text.lower()  # Example: Convert text to lowercase


# Build and train the model
def build_model(data):
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(data['processed_content'])

    return data, tfidf_vectorizer, tfidf_matrix

# Generate response
def generate_response(user_input, data, tfidf_vectorizer, tfidf_matrix):
    user_input = preprocess_text(user_input)
    user_input_vector = tfidf_vectorizer.transform([user_input])

    similarities = cosine_similarity(user_input_vector, tfidf_matrix)
    closest_index = similarities.argmax()

    response = data.iloc[closest_index]['answer']
    return response

# Main function
def main():
    # Connect to the database
    conn = connect_to_database()
    if conn is None:
        return

    # Fetch file contents from the database
    file_contents = fetch_file_contents(conn)
    if file_contents is None:
        conn.close()
        return

    # Load data from files
    df = load_data_from_files(file_contents)

    # Preprocess text data
    df['processed_content'] = df['file_content'].apply(preprocess_text)

    # Build and train the model
    df, tfidf_vectorizer, tfidf_matrix = build_model(df)

    # Interaction loop
    print("Bot: Hello! How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Bot: Goodbye!")
            break
        response = generate_response(user_input, df, tfidf_vectorizer, tfidf_matrix)
        print("Bot:", response)
        # Save chat to database
        save_chat_to_database(user_input, response)

    # Close the database connection
    conn.close()

if __name__ == "__main__":
    main()
