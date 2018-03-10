from flask import Flask, render_template, request
import nexmo

client = nexmo.Client(key="c9d92ff9", secret="KAsgFogaEQgcOu56")

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hackmed',methods=["GET"])
def hackmed():

    replace_me = "HERE I AM"

    return render_template('hackmed.html',replace_me=replace_me)

@app.route('/about_us',methods=["GET"])
def aboutus():

    replace_me = "HERE I AM"

    return render_template('about_us.html',replace_me=replace_me)

@app.route('/lab_locations',methods=["GET"])
def maplocations():

    replace_me = "HERE I AM"

    return render_template('lab_locations.html',replace_me=replace_me)

@app.route('/your_results',methods=["GET"])
def yourresults():

    replace_me = "HERE I AM"

    return render_template('your_results',replace_me=replace_me)

@app.route('/process_data',methods=["POST"])
def process_data():
    name = request.form["name"]
    print(name)
    #nexmo python message api
    #need to add other inputs than name
    client.send_message({'from' : "ResultsRx", 'to' : '447805147698', "text" : name})
    return render_template('hackmed_response.html',name=name)


if __name__ == '__main__':
    app.run()
