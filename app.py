from flask import Flask, render_template, make_response

app = Flask(__name__)

@app.route("/")
def victim():
    response = make_response(render_template("victim.html"))
    # Modern clickjacking defense: only allow framing by same origin
    #response.headers["Content-Security-Policy"] = "frame-ancestors 'self'"
    # Backup header for older browsers
    #response.headers["X-Frame-Options"] = "DENY"
    return response

@app.route("/attacker")
def attacker():
    return render_template("attacker.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)
