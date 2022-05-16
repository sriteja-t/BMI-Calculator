from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = ''
    if request.method == 'POST' and 'weight' in request.form:
        w = float(request.form.get('weight'))
        h = float(request.form.get('height'))
        bmi = w/((h/100)**2)
    return render_template("index.html", bmi=bmi)

if __name__ == '__main__':
    app.run()