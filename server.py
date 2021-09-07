from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
import random
app.secret_key = 'omar comin!'

@app.route('/')
def render_page():
    if 'number' not in session:
        session['number'] = random.randint(1,100)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def show_result():
    session['guess']= int(request.form['guess'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)