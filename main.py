# Import
from flask import Flask, render_template


app = Flask(__name__)


# Pierwsza strona
@app.route('/')
def index():
    return render_template('index.html')

# Druga strona
@app.route('/<size>')
def lights(size):
    return render_template(
                            'lights.html', 
                            size=size
                           )

# Trzecia strona
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template(
                            'electronics.html',
                            size = size, 
                            lights = lights                           
                           )

# Obliczenia
@app.route('/<size>/<lights>/<device>' , methods = ['POST'])
def end(size, lights, device):
    projectpath = request.form['kontakt-tn']
    
    return render_template('end.html', 
                          
                            
                           
                                                    )

app.run(debug=True)
