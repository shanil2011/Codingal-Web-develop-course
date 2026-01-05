from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def leap_year():
    result = None

    if request.method == "POST":
        year = int(request.form["year"])

        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            result = f"{year} is a Leap Year ✅"
        else:
            result = f"{year} is NOT a Leap Year ❌"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
