
from flask import Flask, jsonify, render_template, request 
import pandas as pd
import csv

app = Flask(__name__)

user_info = [ {'id':"1",
            'name':"John"},
            {'id':"2",
            'name':"Maya"},
            {'id':"3",
            'name':"Peter"}]
            

@app.route("/users", methods=['GET'])
def get():
    return  jsonify({'user_info':user_info})


@app.route('/users', methods=['GET', 'POST'])

def index():
   return render_template('index.html') 


@app.route('/data', methods=['POST'])

def data():

    if request.method=='POST':

        f = request.form['csvfile']

        data= []

        with open(f) as file:
            csvfile = csv.reader(file)
            for row in csvfile:
                data.append(row)
        data = pd.Dataframe(data)

        return render_template('data.html', data=data.to_html (header=False, index=False))

if __name__ == "__main__":
    app.run(debug=True)
