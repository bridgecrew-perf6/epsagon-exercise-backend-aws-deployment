from flask import Flask, request
from flask_restful import Api, Resource
import json
from models.span.get_span import get_span
app = Flask(__name__)

api = Api(app)

def create_new_key(arg, key):
    new_key = []
    for i in arg:
        if key not in ["spanId", "parentSpanId"]:
            try:
                if "." in i:
                    i = float(i)
                else:
                    i = int(i)
            except:
                pass
        new_key.append(i)
    return new_key

class Span(Resource):
    def get(self):
        filters = []
        if request.args is None:
            return get_span()
        else:
            args = dict(request.args)
            for key in args:
                arg = json.loads(args[key])
                new_key = create_new_key(arg, key)
                filters.append((key, new_key[0], new_key[1], new_key[2]))
            return get_span(*filters)

api.add_resource(Span, '/spans')

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80) #BAD PRACTICE, but had to do it in time