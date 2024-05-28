from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def retorna_acessos():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)