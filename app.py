from flask import Flask, render_template, 

app = Flask(__name__)

@app.route("/")
def base():
    return render_template("forma. html")

@app.route("/forma")
def froma():
    return render_template("forma. html")

@app.route("/re")
def re():
    return render_template("re. html")


if __name__ == "__main__"
    app.run(debug=True)
