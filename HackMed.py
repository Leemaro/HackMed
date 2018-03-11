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
    return render_template('hackmed.html')

@app.route('/about_us',methods=["GET"])
def aboutus():
    return render_template('about_us.html')

@app.route('/lab_locations',methods=["GET"])
def maplocations():
    return render_template('lab_locations.html')

@app.route('/your_results',methods=["GET"])
def yourresults():
    return render_template('your_results.html')

@app.route('/your_results_login',methods=["GET"])
def yourresultslogin():
    #code to make table progromatic

    return render_template('your_results_login.html')

@app.route('/contact',methods=["GET"])
def contact():
    return render_template('contact.html')

@app.route('/technicians',methods=["GET"])
def technicians():
    return render_template('technicians.html')

@app.route('/process_data',methods=["POST"])
def process_data():
    details = request.form["details"]
    name = request.form["name"]
    type = request.form["type"]
    #nexmo python message api
    #need to add other inputs than name
    client.send_message({'from' : "ResultsRx", 'to' : details, "text" : name + ", your " + type + " test results are ready, action is required, contact your GP." + \
                         " View online at: www.domain.com/hackmed/your_results"})
    return render_template('hackmed_response.html',name=name, details=details)

@app.route('/calling')
def call_doctor():
    print("Calling Doctor")
    return 'Calling Doctor'
    client.create_call({
        'to' : [{'type': 'phone', 'number': 447923978877}],
        'from': {'type': 'phone', 'number': 447520660907},
        'answer_url': ['https://developer.nexmo.com/ncco/tts.json']
    })




if __name__ == '__main__':
    app.run()
