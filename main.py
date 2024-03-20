from flask import Flask,render_template,url_for,request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        name = data["name"]
        email = data["email"]
        message = data["message"]
        file = database.write(f'\n{email},{name},{message}')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        write_to_file(data)
        
        return 'form submitted'
    else:
        return 'something went wrong. Try again!'



