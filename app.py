from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/courses")
def courses():
    return render_template("courses.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/admission", methods=["GET", "POST"])
def admission():
    if request.method == "POST":
        name = request.form["name"]
        father = request.form["father"]
        mother = request.form["mother"]
        student_class = request.form["student_class"]
        mobile = request.form["mobile"]
        address = request.form["address"]

        return f"Thank You {name}! Your admission form has been submitted."

    return render_template("admission.html")


if __name__ == "_main_":
    app.run(debug=True)