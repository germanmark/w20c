from flask import Flask, Response, request
import json

app = Flask(__name__)


@app.route("/animals",methods=['GET', 'POST', 'PATCH', 'DELETE'])
def animals():
    my_animals = ['Lion', 'Zebra', 'Panther', 'Donkey']
    if request.method == 'GET':
        return Response(json.dumps(my_animals),
                        mimetype='application/json',
                        status=200)
    elif request.method == 'POST':
        new_animal = request.json.get('animal')
        if (new_animal != None):
            my_animals.append(new_animal)
            print(my_animals)
            return Response("Animal successfully added",
                            mimetype="text/plain",
                            status=201)
        else:
            return Response("Error, no animal specified",
                            mimetype="text/plain",
                            status=400)

    elif request.method == 'PATCH':
        new_animal = request.json.get('animal')
        if (new_animal != None):
            my_animals[3] = new_animal
            print(my_animals)
            return Response("Animal successfully changed",
                            mimetype="text/plain",
                            status=200)
        else:
            return Response("Error, no animal specified",
                            mimetype="text/plain",
                            status=400)

    elif request.method == 'DELETE':
        my_animals.remove('Donkey')
        print(my_animals)
        return Response("Animal successfully deleted",
                        mimetype="text/plain",
                        status=200)

app.run(debug=True)