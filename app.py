from flask import Flask, render_template, request
import pycode
# import biopython


# Constructor; nodig om te runnen.
app = Flask(__name__)

# Mijn URL link http:127.0.0.1/
@app.route('/')
def googletranslate():
    dnaseq = request.args.get("dnaseq", "")
    protseq = pycode.translate(dnaseq)
    return render_template("translatepg.html", protseq=protseq)

@app.route('/hey')
def show_color():
    kleur = request.args.get("kleur", "white")
    return render_template("kleur.html", kleur=kleur)


if __name__ == '__main__':
    app.run()

#GET methode is uit de URL en niet veilig
#POST is veiliger, hij sluist het door naar request en response headers.