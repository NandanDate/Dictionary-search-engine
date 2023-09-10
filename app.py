from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Function to search for a word in the SQLite database
def search_word_in_database(word):
    conn = sqlite3.connect('dictionary2.db')
    cursor = conn.cursor()
    cursor.execute('SELECT definition FROM dictionary WHERE word LIKE ?', (word,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    word = request.form.get('word')
    definition = search_word_in_database(word)
    if definition:
        return render_template('results.html', query=word, definition=definition)
    else:
        return render_template('results.html', query=word, definition='Word not found')

if __name__ == '__main__':
    app.run(debug=True)
