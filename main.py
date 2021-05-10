from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)

api = Api(app)

class HelloWorld(Resource):
    def get(self, x):
        return {"val": x*x}




api.add_resource(HelloWorld, "/helloworld/<int:x>")


if __name__ == "__main__":
    app.run(debug=True)
