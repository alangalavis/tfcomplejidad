from flask import Flask, render_template, url_for, request, redirect


app = Flask(__name__)

formData = {}

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        formData['movieReference'] = request.form['movieref']
        formData['movieSelectedFilter'] = request.form['check']
        formData['movieRecommendationAmount'] = request.form['recamount']
        return redirect(url_for('output'))
    else:
        return render_template('index.html')

@app.route('/output')
def output():
    return render_template('output.html', movieRefName = formData['movieReference'], 
                           movieFilter = formData['movieSelectedFilter'],
                           movieRecAmount = formData['movieRecommendationAmount'])


if __name__ == '__main__':
    app.run(debug=True)

#flask --app app.py --debug run