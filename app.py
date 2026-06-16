from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Sistema de Biblioteca"

@app.route("/sobre")
def sobre():
    return "Projeto desenvolvido na disciplina de Integração e Entrega Contínua"

if __name__ == "__main__":
    app.run(debug=True)
