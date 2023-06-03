import csv

def return_weight(e):
  return e[1]

def compare_weight(e, a):
  if e[1] > a[1]:
    return True
  else:
    False

def addValue(lista, n, qty):
  if len(lista) < qty:
    lista.append(n)
  tmp = min(lista, key=return_weight)
  index = lista.index(tmp)
  if compare_weight(n, tmp) and len(lista) >= qty:
    lista.pop(index)
    lista.append(n)
  

def dls(G, s, L, qty): #añadir parametro
  n = len(G)
  visited = [False]*n
  path = [None]*n
  cost = [float('inf')]*n
  lista = []
  #Verificar si el número es mayor que los presentes en la lista y si es append, al final ordeno
  
  def _dls(u, L):
    if L > 0 and not visited[u]:
      visited[u] = True
      for v, w in G[u]:
        if not visited[v]:
          cost[v] = w
          path[v] = u
          tupla = (v, w)

          addValue(lista, tupla, qty)
          _dls(v, L - 1)

  _dls(s, L)
  return path, lista


def createGraphFromCSV(csv_file):
    with open(csv_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Saltar la primera línea (encabezados)
        graph = {}
        for row in reader:
            source = int(row[0])
            target = int(row[1])
            weight = float(row[2])

            if source not in graph:
                graph[source] = []
            graph[source].append((target, weight))

    return graph

def show_movies_titles(lista1, lista2):
  for i in lista1:
    print(lista2[i[0]])
    
G_overview = createGraphFromCSV("edges_list_overview.csv") #validar esto

def overview_recomendation(index, qty, movie_dataset):
    if index != -1:
        lista = dls(G_overview, index, 1, qty) #no retornar ni peso ni costo solo dejarlo como comentario para que se vea en la expo
        lista.sort(key=return_weight, reverse=True)
        show_movies_titles(lista, movie_dataset)
        return lista


def filter_selector(movieReference, movieSelectedFilter, movieRecommendationAmount, movie_dataset):
  try:
    index = movie_dataset.index(movieReference)
  except:
    index = -1
    return "Error, movie not found in the dataset"
  
  if movieSelectedFilter == "company":
    return -1
  elif movieSelectedFilter == "genre":
    return -1
  elif movieSelectedFilter == "overview":
    return overview_recomendation(index, movieRecommendationAmount, movie_dataset)
