from flask import Flask
import pymysql

app = Flask(__name__)

@app.route('/')
def index():
    try:
        connection - pymysql.connect(
            host= 'db',
            user= 'root',
            password= '1234',
            database= 'test_db'
        )

        return "Connect"
    except:
        return "Can't Conenct"
    
if __name__ == '__main__':
    app.run(hopst= '0.0.0.0')