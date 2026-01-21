from flask import Flask, render_template, request

app = Flask(__name__)

# Route 1: Home page (GET request)
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# Route 2: Handle GET and POST requests
@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        return "<h2>This is a POST request</h2>"
    else:
        return "<h2>This is a GET request</h2>"

# Run the application
if __name__ == '__main__':
    app.run(debug=True)