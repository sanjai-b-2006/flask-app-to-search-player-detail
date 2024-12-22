from flask import Flask, request, render_template, redirect, url_for
import requests

# Create a Flask application instance
app = Flask(__name__)

# Define the main route to render the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define the search route to handle form submissions
@app.route('/search', methods=['POST'])
def search():
    # Get the player name from the form
    player_name = request.form['player_name']
    # Construct the URL for the Transfermarkt search
    url = f'https://www.transfermarkt.com/schnellsuche/ergebnis/schnellsuche?query={player_name}'
    # Redirect to the constructed URL
    return redirect(url)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
