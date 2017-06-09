from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def hello():
    return render_template('indexnone.html')
@app.route('/ninja')
def ninja():
    return render_template('index.html')
@app.route('/ninja/<var>')
def color(var):
    print var
    if var == 'blue':
        return render_template('blue.html')
    if var == 'red':
        return render_template('red.html')
    if var == 'purple':
        return render_template('purple.html')
    if var == 'orange':
        return render_template('green.html')
    #for item in var:
        #if item == 'blue':
            #return render_template('blue.html')
        #if item == 'red':
            #return render_template('red.html')
        #if item == 'purple':
            #return render_template('green.html')

#@app.route('/ninja/red')
#def red():
    #return render_template('red.html')
#@app.route('/ninja/orange')
#def green():
    #return render_template('green.html')
#@app.route('/ninja/purple')
#def purple():
    #return render_template('purple.html')
app.run(debug=True)
