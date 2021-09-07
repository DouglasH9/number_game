from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = 'omar comin!'

@app.route('/')
def render_page():
    return render_template('index.html')

@app.route('/render', methods=['POST'])
def show_result():
    session['number']=request.form['number']
    
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)