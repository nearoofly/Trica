from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/ecran')
def ecran():
    return render_template('ecran.html')


@app.route('/autoriser', methods=['POST'])
def autoriser():
    
    consentement_accorde = True

    if consentement_accorde:
        return render_template('ecran.html')
    else:
        return "Le consentement n'a pas été accordé."

if __name__ == '__main__':
    app.run(debug=True)
