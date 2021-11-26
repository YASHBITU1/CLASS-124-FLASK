from logging import error
from flask import Flask,jsonify,request

app = Flask(__name__)
@app.route("/")
def welcome():
    return "welcome to class 124 project"

Data = [{
    "id":1,
    "contact":"7639749209",
    "Name":"Krish",
    "done":False
},
{
    "id":2,
    "contact":"1263889208",
    "Name":"T.V Bill = -/1890",
    "done":False
}]
@app.route("/adddata",methods = ["POST"])
def addcontact():
    if(not request.json):
        return jsonify({
            "status":"error",
            "message":"plz provide the data"
        },400)
    contact = {
        "id":Data[-1]["id"]+1,
        "contact":request.json["contact"],
        "Name":request.json.get("Name",""),
        "done":False 
    }      
    Data.append(contact)
    return jsonify({
        "status":"success",
        "message":"contact added succesfully"

    })
@app.route("/getdata")
def getcontact():
    return jsonify({"data":Data})   

if(__name__ == "__main__"):
    app.run(debug=True) 