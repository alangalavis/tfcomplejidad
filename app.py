from flask import Flask, render_template, url_for, request, redirect
import overview_weights
import DLS

overview_weights.generate_overview()

app = Flask(__name__)

formData = {}

movie_index = 0


df_movies = overview_weights.pd.read_csv('Amdb_5000_movies.csv')

peliculas_lista = df_movies['original_title'].astype(str).tolist()

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        if peliculas_lista.index(request.form['movieref']) is ValueError:
            movie_index = -1
            return render_template('index.html')
        else:
            movie_index = peliculas_lista.index(request.form['movieref'])
            formData['movieReference'] = request.form['movieref']
            formData['movieSelectedFilter'] = request.form['check']
            formData['movieRecommendationAmount'] = request.form['recamount']
            return redirect(url_for('output'))
    else:
        return render_template('index.html')

DLS.overview_recomendation(0, 5, peliculas_lista)

@app.route('/output')
def output():

    DLS.overview_recomendation(peliculas_lista.index(formData['movieReference']), int(formData['movieRecommendationAmount']), peliculas_lista)

    return render_template('output.html', movieRefName = formData['movieReference'], 
                           movieFilter = formData['movieSelectedFilter'],
                           movieRecAmount = formData['movieRecommendationAmount'])


if __name__ == '__main__':
    app.run(debug=True)

#flask --app app.py --debug run