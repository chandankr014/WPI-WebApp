from tensorflow.keras.models import load_model
from flask import Flask, request, render_template

app = Flask(__name__)

model = load_model('model.h5')
print(model.summary())

# define endpoints  
@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/predict', methods=["GET","POST"])
def predict():
    if request.method=="POST":
        pH = float(request.form['pH'])
        DO = float(request.form['DO'])
        TDS = float(request.form['TDS'])
        Alkalinity = float(request.form['Alkalinity'])
        EC = float(request.form['EC'])
        Na = float(request.form['Na'])
        Ca = float(request.form['Ca'])
        Mg = float(request.form['Mg'])
        K = float(request.form['K'])
        F = float(request.form['F'])
        Cl = float(request.form['Cl'])
        Nitrate = float(request.form['Nitrate'])
        Sulphate = float(request.form['Sulphate'])
        Phosphate = float(request.form['Phosphate'])
        input_var= [pH, DO, TDS, Alkalinity, EC, Na, Ca, Mg, K, F, Cl,Nitrate, Sulphate, Phosphate]
        res = model.predict([input_var])
        return render_template('predict.html', pred="The Predicted value is :"+str(res[0][0]))
    return render_template('predict.html')

    #predict?pH=8.14&DO=8.7&TDS=84.0&Alkalinity=52.0&EC=147.0&Na=4.48&Ca=44.0&Mg=20.0&K=1.17&F=0.285&Cl=7.8&Nitrate=0.7&Sulphate=6.5&Phosphate=0.065

if __name__=="__main__":
    app.run(debug=True)