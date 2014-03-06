from flask import Flask, render_template
from trends import TrendFinder
from credentials import CREDS

app = Flask(__name__)
trendfinder = TrendFinder(CREDS)

@app.route('/')
def hello_world():
    return render_template('index.html', trends=trendfinder.find_trends())

if __name__ == '__main__':
    app.run(debug=True)