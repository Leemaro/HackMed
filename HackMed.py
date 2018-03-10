from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hackmed',methods=["GET"])
def hackmed():

    replace_me = "HERE I AM"

    return render_template('hackmed.html',replace_me=replace_me)

if __name__ == '__main__':
    app.run()
