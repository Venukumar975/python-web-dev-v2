from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    # Configure for Replit environment - must use 0.0.0.0 for host and port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)