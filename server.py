from flask import Flask, request
app = Flask ("__main__")
"""
prove code, let´s suppose it comes from some DB
"""
device ={
    "matricula":"65184532",
    "code":"112233",
    "descrip":"somesensor",
    "value":69
}
#server user
@app.route("/users", methods=["POST"])
def save_user():
    user = request.json
    print (user)
    return(user)
@app.route ("/users", methods=["GET"])
def go_home():
    users = request.json
    print(users)
    return (users)
@app.route("/devices", methods=["POST"])
def save_edvices():
    devices = request.json
    print (devices)
    return(devices)
@app.route ("/devices", methods=["GET"])
def go_home():
    devices = request.json
    print(devices)
    return (devices)
if __name__ == "__main__":
    app.run(debug=True, port=5000)
