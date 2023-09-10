import sqlite3

# Search for a word in the SQLite database and print its definition
def search_word_and_print_definition(word, database_name):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # Perform a case-insensitive search for the word in the database
    cursor.execute('SELECT definition FROM dictionary WHERE word LIKE ?', (word,))
    result = cursor.fetchone()

    conn.close()

    if result:
        definition = result[0]
        print(f"Word: {word}")
        print(f"Definition:\n{definition}")
    else:
        print(f"Word '{word}' not found in the dictionary.")

# Example usage:
database_name = 'dictionary2.db'  # Replace with the name of your SQLite database

# Take user input for the word to search
user_input = input("Enter a word to search: ")
search_word_and_print_definition(user_input, database_name)
