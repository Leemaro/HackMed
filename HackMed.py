from flask import Flask, render_template, request
import nexmo

client = nexmo.Client(key="c9d92ff9", secret="KAsgFogaEQgcOu56")

app = Flask(__name__)

app.debug = True

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

    return render_template('your_results.html',replace_me=replace_me)

@app.route('/your_results_login',methods=["GET"])
def yourresultslogin():

    replace_me = "HERE I AM"

    return render_template('your_results_login.html',replace_me=replace_me)

@app.route('/contact',methods=["GET"])
def contact():

    replace_me = "HERE I AM"

    return render_template('contact.html',replace_me=replace_me)

@app.route('/technicians',methods=["GET"])
def technicians():

    replace_me = "HERE I AM"

    return render_template('technicians.html',replace_me=replace_me)

@app.route('/process_data',methods=["POST"])
def process_data():
    details = request.form["details"]
    name = request.form["name"]
    print(details)
    #nexmo python message api
    #need to add other inputs than name
    client.send_message({'from' : "ResultsRx", 'to' : details, "text" : name + ", your results are ready, you are not dead" })
    return render_template('hackmed_response.html',name=details)


if __name__ == '__main__':
    app.run()
