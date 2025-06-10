from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        # Aqui você pode adicionar autenticação
        if email == 'admin@example.com' and senha == '1234':
            return f'Bem-vindo, {email}!'
        else:
            return 'Login inválido. Tente novamente.'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
