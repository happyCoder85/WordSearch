"""
Description: MyMath Web Application
Author: Jonathan Spurling
Section Number: ADEV-3005 (251409)
Date Created: February 20, 2024

Updates: None
"""
from flask import Flask, render_template, request
from Search import Search

app = Flask(__name__)

@app.route('/')
def index():
    """Loads the index.html page"""
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def do_word_search():
    """
        Does the task of search a phrase and returning the letters found from letters either supplied or regular vowels.
    """
    letters = request.form['letters']
    phrase = request.form['phrase']
    title = "Here are your results:"

    search = Search()

    result = search.search_for_letters(phrase, letters)

    return render_template('results.html',
                        letters=letters,
                        phrase=phrase,
                        result=result,
                        title=title,)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
    