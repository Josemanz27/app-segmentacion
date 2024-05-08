from flask import Flask,request,render_template
import numpy as np
import pandas
import sklearn
import pickle

# Importar los modelos
model = pickle.load(open('model.pkl','rb'))
sc = pickle.load(open('standscaler.pkl','rb'))
ct = pickle.load(open('encoder.pkl','rb'))

# crear flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/predict",methods=['POST'])
def predict():
    G = request.form['Gender']
    A = request.form['Age']
    AI = request.form['AnualIncome']
    SS = request.form['SpendingScore']

    def prediction(G,A,Ai,SS):
      features = ([[G,A,Ai,SS]])
      transformed_features = ct.transform(features)
      transformed_features[:,2:] = sc.transform(transformed_features[:,2:])
      prediction = kmeansmodel.predict(transformed_features).reshape(1,-1)
      return prediction[0]
      
    single_pred = prediction(G,A,AI,SS)

    result =(f"La prediccion es: {single_pred[0]}")
    return render_template('index.html',result = result)




# python main
if __name__ == "__main__":
    app.run(debug=True)