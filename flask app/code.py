from flask import Flask,jsonify,request

app = Flask(__name__)

List = [
    {
        "id":1,
        "name":"Raju",
        "contact":"9993598823",
        "done":False
    },
    {
        "id":2,
        "name":"Asma",
        "contact":"7777777777",
        "done":False
    }
]

@app.route("/")
def hello_world():
    return "Hello world"
@app.route("/add-data", methods=["POST"])

def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data."
                    }, 400)

    Contact = {
        "id":[-1]["id"]+1,
        "name":request.json["name"],
        "contact":request.json.get("contact", ""),
        "done":False
    }

    List.append(Contact)
    return jsonify({
        "status":"Success",
        "message":"Contact added successfully."
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":List
    })

if (__name__ == "__main__"):
    app.run(debug = True)