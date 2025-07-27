# app.py - Main Flask application file
# Location: Root directory of the application

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Main index route that renders the home page"""
    return render_template('index.html')


@app.route('/about')
def about():
    """About page route"""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Contact page route"""
    return render_template('contact.html')


if __name__ == '__main__':
    # Use a more compatible configuration to avoid watchdog issues
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False) 