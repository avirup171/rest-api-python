from flask import Flask, request
import operations

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/sum', methods=['GET'])
def sumCalculate():
    value_a=request.args.get('value_a')
    value_b=request.args.get('value_b')
    sum=operations.sum(value_a,value_b)
    return sum

@app.route('/queryparams',methods=['GET'])
def paramsDemo():
    print(request.url)
    print(request.query_string)
    return "Params Demo Route"

@app.route('/postparams', methods=['POST'])
def postParamsDemo():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        params= request.json
        print(params)
        return "Post demo"
    else:
        return "Invalid content type"

if __name__=='__main__':
    app.run()