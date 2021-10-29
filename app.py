from flask import Flask , render_template , url_for ,request, redirect
from search import get_multi_search_results, get_search_results_by_birth_day, get_search_results_by_born, get_search_results_by_name

app = Flask(__name__)
#app._static_folder = ''

@app.route("/searchBy/name"  , methods = ['POST' , 'GET'] )
def search_by_name():
    if request.method == 'POST':
        task_content = request.form['content']
        print(task_content)
        es_response = get_search_results_by_name(task_content)
        hits = es_response['hits']['hits']
        num_results = len(hits)
        try:
            return render_template('index.html' , hits = hits , num_results = num_results , query = task_content)
        except:
            return 'There was an issue adding your task'
    else:
        return render_template('index.html')

@app.route("/searchBy/born"  , methods = ['POST' , 'GET'] )
def search_by_born():
    if request.method == 'POST':
        task_content = request.form['content']
        print(task_content)
        es_response = get_search_results_by_born(task_content)
        hits = es_response['hits']['hits']
        num_results = len(hits)
        try:
            return render_template('born.html' , hits = hits , num_results = num_results , query = task_content)
        except:
            return 'There was an issue adding your task'
    else:
        return render_template('born.html')

@app.route("/searchBy/bd"  , methods = ['POST' , 'GET'] )
def search_by_bd():
    if request.method == 'POST':
        to = request.form['to']
        from_d = request.form['from']
        print(to , from_d)
        es_response = get_search_results_by_birth_day(to ,from_d)
        hits = es_response['hits']['hits']
        num_results = len(hits)
        try:
            return render_template('bd.html' , hits = hits , num_results = num_results , query = from_d+" to "+to)
        except:
            return 'There was an issue adding your task'
    else:
        return render_template('bd.html')

@app.route("/search"  , methods = ['POST' , 'GET'] )
def advanced_search():
    if request.method == 'POST':
        task_content = request.form['content']
        print(task_content)
        es_response = get_multi_search_results(task_content)
        hits = es_response['hits']['hits']
        num_results = len(hits)
        try:
            return render_template('search.html' , hits = hits , num_results = num_results , query = task_content)
        except:
            return 'There was an issue adding your task'
    else:
        return render_template('search.html')

if __name__ == "__main__":
    app.run(debug=True)