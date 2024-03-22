import csv
import urllib.parse
from flask import Flask,request, jsonify

app = Flask(__name__)
i=0
@app.route('/search/<string:term>')
def get_topic(term):
    try:
        
        with open('books.txt', 'r') as file:
            data = csv.reader(file)  # Read the entire file
        
            #headers = next(data)
            rows = [row for row in data]
            term = urllib.parse.unquote(term)
            # Return the extracted data as a JSON response
            if not term:
                return jsonify(error='Search value not provided'), 400
            #print(topic)
            for i in rows:
                if term in i:
                    return jsonify(book=i)
        return jsonify(data=rows)
    except FileNotFoundError:
        return jsonify(error='File not found'), 404
    return jsonify()
@app.route('/hello')
def hello():
    global i
    i+=1
    
    return jsonify(message="Hello, World!", number=str(i))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
