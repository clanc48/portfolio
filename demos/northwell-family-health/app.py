from flask import Flask, render_template

app = Flask(__name__)

@app.get('/')
def home(): return render_template('home.html')
@app.get('/services')
def services(): return render_template('services.html')
@app.get('/providers')
def providers(): return render_template('providers.html')
@app.get('/patient-resources')
def patient_resources(): return render_template('patient-resources.html')
@app.get('/appointments')
def appointments(): return render_template('appointments.html')

if __name__ == '__main__': app.run(debug=True)
