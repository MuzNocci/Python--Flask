from flask import Flask, render_template

app = Flask(__name__)

title = 'Site em Flask'

@app.route('/')
def Homepage():
    return render_template('homepage.html', title = title, divteste = 'body da página')

@app.route('/contato')
def Contatos():
    return render_template('contatos.html', title = title, subtitle = 'Contato')
    
if __name__ == '__main__':
    app.run(debug=True)