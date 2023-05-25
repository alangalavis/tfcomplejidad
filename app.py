from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

#flask --app app.py --debug run

#En el terminal hacer lo siguiente:
"""
pip install pipenv
pipenv --python 3.8
pipenv install -r requirements.txt
pipenv shell
python app.py
"""