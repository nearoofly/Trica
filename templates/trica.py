from flask import Flask, render_template, request

app = Flask(__name__)

# Page d'accueil demandant le consentement
@app.route('/')
def home():
    return render_template('index.html')

# Page pour afficher l'écran une fois le consentement donné
@app.route('/ecran')
def ecran():
    return render_template('ecran.html')

# Route pour gérer le consentement de l'utilisateur
@app.route('/autoriser', methods=['POST'])
def autoriser():
    # Traitement du consentement, enregistrement dans la base de données, etc.
    consentement_accorde = True

    if consentement_accorde:
        return render_template('ecran.html')
    else:
        return "Le consentement n'a pas été accordé."

if __name__ == '__main__':
    app.run(debug=True)