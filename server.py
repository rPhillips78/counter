from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'Standing to be the coldest'

@app.route('/')
def get_count():
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += 1
    return render_template("index.html", count=session['count'])


@app.route('/destroy_session')
def destroy_session():
    if session['count']:
        session.clear()
    return redirect('/') 

@app.route('/add_two')
def add_two():
    session['count'] += 1
    return redirect('/')

@app.route('/add_num', methods=['POST'])
def add_num():
    num = request.form['number']
    if num:
        session['count'] += (int(num))
    session['count'] -= 1
    return redirect('/')



app.run(debug=True)