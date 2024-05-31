from flask import Flask, render_template, request, jsonify

app=Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/profile',methods=['GET'])
def profile():
    return jsonify({'msg': 'This is Profile Page'})

@app.route('/portfolio',methods=['GET'])
def portfolio():
    return jsonify({'msg': 'This is Portfolio Page'})

@app.route('/contact',methods=['GET'])
def contact():
    return jsonify({'msg': 'This is Contact Page'})

if __name__ == '__main__':
  #DEBUG is SET to TRUE. CHANGE FOR PROD
  app.run(port=5000,debug=True)