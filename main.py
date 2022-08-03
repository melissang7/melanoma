from flask import Flask, render_template

app = Flask(__name__)

#criar a 1° página do site
#route -> melanoma.com.br/
#função -> o que será exibido na página

@app.route("/")  #atribuir uma nova funcionalidade para a função abaixo
def DiagnosticoMelanoma():
    return render_template("DiagnosticoMelanoma.html")

#colocar o site no ar
if __name__ == "__main__":   #executar o código quando rodar diretamente
    app.run(debug=True)

    # servidor Vercel