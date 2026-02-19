from flask import Flask, render_template, request

app = Flask(__name__)

# Student List
students = ["Rahul", "Priya", "Arun", "Sneha"]

# Student Profile (Dictionary)
student_profile = {
    "name": "Rahul",
    "age": 20,
    "course": "Computer Science",
    "marks": 75
}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/students/")
def student_list():
    return render_template("students.html", students=students)

@app.route("/result/", methods=["GET", "POST"])
def result():
    grade = ""
    if request.method == "POST":
        marks = int(request.form["marks"])
        if marks >= 50:
            grade = "Pass"
        else:
            grade = "Fail"
    return render_template("result.html", result=grade)

@app.route("/profile/")
def profile():
    return render_template("profile.html", student=student_profile)

@app.route("/about/")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
