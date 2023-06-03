import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import csv
import os.path

def inital():
    df_movies = pd.read_csv('Amdb_5000_movies.csv')
    tfidf = TfidfVectorizer(stop_words="english")
    df_movies['overview']=df_movies['overview'].fillna("")
    tfid_matrix = tfidf.fit_transform(df_movies['overview'])
    cosine_sim = linear_kernel(tfid_matrix, tfid_matrix)
    indices = pd.Series(df_movies.index, index = df_movies['id']).drop_duplicates()
    columna_lista = df_movies['vote_average'].astype(float).tolist()
    return indices, cosine_sim, columna_lista

def generate_overview_recomendations(id, cont = 0):
    indices, cosine_sim, columna_lista = inital()
    lis = []
    lista = []
    idx = indices[id]
    sim_scores = cosine_sim[idx]
    for i in sim_scores:
        #i = 10
        i=round(i*100)
        lista = [id,cont,i+columna_lista[cont]]
        if id == cont:
            cont += 1
            continue
        if i <= np.float64(7.0):
            cont +=1
            continue
        #validar que no se hagan relaciones cuando es 0.0
        cont += 1
        lis.append(lista)
        #print(i)
    return lis

def get_recomendations_overview():
    file = open("edges_list_overview.csv", "a", newline='')
    writer = csv.writer(file)
    headers = ["Source", "Target", "Weight"]
    writer.writerow(headers)
    for i in range(4801):
        liston = generate_overview_recomendations(i)
        writer.writerows(liston)
        
def file_is_empty():
    df = pd.read_csv("edges_list_overview.csv")
    return df.empty

def generate_overview():
    if os.path.exists("edges_list_overview.csv") is False:
        get_recomendations_overview()
    elif file_is_empty():
        get_recomendations_overview()