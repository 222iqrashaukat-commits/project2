from flask import Flask, jsonify, request

app = Flask(__name__)

# Student data
students = [
    {
        "id": 1,
        "name": "Ali",
        "department": "Computer Science",
        "age": 20
    },
    {
        "id": 2,
        "name": "Sara",
        "department": "Software Engineering",
        "age": 21
    }
]


# Home route
@app.route("/")
def home():
    return "Student API is running!"


# GET all students
@app.route("/api/students", methods=["GET"])
def get_students():
    return jsonify(students)


# POST - Add a new student
@app.route("/api/students", methods=["POST"])
def add_student():

    data = request.get_json()

    new_student = {
        "id": len(students) + 1,
        "name": data["name"],
        "department": data["department"],
        "age": data["age"]
    }

    students.append(new_student)

    return jsonify(new_student), 201

    # PUT - Update a student
@app.route("/api/students/<int:id>", methods=["PUT"])
def update_student(id):

    data = request.get_json()

    for student in students:
        if student["id"] == id:
            student["name"] = data["name"]
            student["department"] = data["department"]
            student["age"] = data["age"]

            return jsonify(student)

    return jsonify({"message": "Student not found"}), 404
    # DELETE - Delete a student
@app.route("/api/students/<int:id>", methods=["DELETE"])
def delete_student(id):

    for student in students:
        if student["id"] == id:
            students.remove(student)

            return jsonify({
                "message": "Student deleted successfully"
            })

    return jsonify({"message": "Student not found"}), 404
    # Run the application
if __name__ == "__main__":
    app.run(debug=True)