from flask import Flask, render_template, request, redirect, session

app= Flask(__name__)
app.secret_key = 'holamundo'


@app.route('/')
def index():
    return render_template( 'index.html')

@app.route('/process', methods=['POST'])
def process():   
    
    session['name'] = request.form['name']
    session['label1']  = request.form['label1']
    session['label2']  = request.form['label2']
    session['coment']  = request.form['coment']
    print(request.form)
    return redirect('/results')

@app.route('/results')
def results():
    return render_template( 'results.html')    








if __name__=="__main__":
    app.run(debug=True)
