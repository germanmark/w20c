from flask import Flask, Response, request
import json

app = Flask(__name__)

my_animals = ['Lion', 'Zebra', 'Panther', 'Donkey']

@app.get("/animals")
def animals_get():
    return Response(json.dumps(my_animals),
                    mimetype='application/json',
                    status=200)

@app.post("/animals")
def animals_post():
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
@app.patch("/animals")
def animals_patch():
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
@app.delete("/animals")
def animals_delete():
    my_animals.remove('Donkey')
    print(my_animals)
    return Response("Animal successfully deleted",
                    mimetype="text/plain",
                    status=200)

app.run(debug=True)
