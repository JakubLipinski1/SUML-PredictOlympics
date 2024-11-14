from flask import Flask, jsonify, request
from flask_cors import CORS
import pyodbc

app = Flask(__name__)
CORS(app)

# Parametry połączenia z bazą danych
server = '(localdb)\\MSSQLLocalDB'
database = 'Test3'
username = ''
password = ''
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                      server+';DATABASE='+database+';UID='+username+';PWD='+ password)


@app.route('/elementy', methods=['GET'])
def get_element():
        return jsonify({'nazwa': 'elementTestowy', 'opis': 'taki o to element'})


if __name__ == '__main__':
    app.run(debug=True)
