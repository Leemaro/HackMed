from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hackmed',methods=["GET"])
def hackmed():

    replace_me = "HERE I AM"

    return render_template('hackmed.html',replace_me=replace_me)

@app.route('/process_data',methods=["POST"])
def process_data():
    name = request.form["name"]

    #nexmo python message api

    return render_template('hackmed_response.html',name=name)


if __name__ == '__main__':
    app.run()
