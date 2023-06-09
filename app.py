from flask import Flask, render_template, url_for, request, redirect
import DLS
import generate_weights

formData = {}

app = Flask(__name__)

generate_weights.generar_csvs()
df_movies = generate_weights.pd.read_csv('Amdb_5000_movies.csv')
movie_dataset = df_movies['original_title'].astype(str).tolist()

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        formData['movieReference'] = request.form['movieref']
        formData['movieSelectedFilter'] = request.form['check']
        formData['movieRecommendationAmount'] = int(request.form['recamount'])

        return redirect(url_for('output'))
    
    else:
        return render_template('index.html')

@app.route('/output')
def output():
    result = DLS.filter_selector(formData['movieReference'], formData['movieSelectedFilter'], formData['movieRecommendationAmount'], movie_dataset)
    return render_template('output.html', movieRefName = formData['movieReference'], 
                           movieFilter = formData['movieSelectedFilter'],
                           movieRecAmount = formData['movieRecommendationAmount'],
                           recommendation_list = str(result))

if __name__ == '__main__':
    app.run(debug=True)

#flask --app app.py --debug run