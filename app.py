from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>My First Website</h1>
    <p>Website created by me using Python Flask.</p>
    <p><b>Name:</b> Boss kv</p>
    <p><b>Age:</b> 18</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
