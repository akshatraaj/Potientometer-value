import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from flask import Flask , request , render_template , jsonify
cred = credentials.Certificate("potentiometer-akshat-firebase-adminsdk-xwfck-26f6eff0d1.json")
firebase_admin.initialize_app(cred)
db_client = firestore.client()
app = Flask(__name__)

@app.route('/' , methods = ['GET'])
def index():
    try:
        pot = db_client.collection('Display Meter').document('potentiometer values').get().to_dict()
        val = pot['pot val']
        return render_template('index.html' , value = val)
    except Exception as e:
        print(e)                        # printing error first
        return jsonify({'status' : 'failed'})

@app.route('/add' , methods = ['POST'])
def add():
    try:
        pot_val = request.json.get('potentiometer')
        db_client.collection('Display Meter').document('potentiometer values').set({'pot val' : pot_val})
        return jsonify({'status' : 'success'})
    except Exception as e:
        print(e)                        # printing error first
        return jsonify({'status' : 'failed'})

if __name__  ==  "__main__":
    app.run(host = '192.168.1.4' , port=5000, debug = True)
