from flask import Flask, render_template, request
app=Flask(__name__)

SERVICES=[
    ("Preventive visits","Annual exams, screenings, vaccines, and health planning."),
    ("Same-week illness care","Respiratory symptoms, infections, rashes, minor injuries, and common acute concerns."),
    ("Pediatric primary care","Growth, development, preventive care, and everyday childhood illness."),
    ("Chronic-condition support","Longitudinal care for blood pressure, diabetes, asthma, and other ongoing needs."),
]

@app.get("/")
def home(): return render_template("home.html")
@app.get("/services")
def services(): return render_template("services.html", services=SERVICES)
@app.get("/providers")
def providers(): return render_template("providers.html")
@app.get("/patient-resources")
def patient_resources(): return render_template("patient-resources.html")
@app.route("/appointments", methods=["GET","POST"])
def appointments(): return render_template("appointments.html", submitted=request.method=="POST")

if __name__=="__main__": app.run(debug=True)
