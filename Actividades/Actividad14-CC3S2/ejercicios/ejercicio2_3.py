from iac_patterns.prototype import ResourcePrototype
from iac_patterns.factory import NullResourceFactory
import json
import os

def add_welcome_file(block: dict):
    block["resource"][0]["null_resource"][0]["app_ej23"][0]["triggers"]["welcome"] = "¡Hola!"
    block["resource"][0]["local_file"] = [{
        "welcome_txt": [{
            "content": "Bienvenido",
            "filename": "${path.module}/bienvenida.txt"
        }]
    }]

res = NullResourceFactory.create("app_ej23")
path = os.path.join("output", "ejercicio2_3")
os.makedirs(path, exist_ok=True)
prototype = ResourcePrototype(res)
cloned_res = prototype.clone(mutator=add_welcome_file)
with open(os.path.join(path, "main.tf.json"), "w") as f:
    json.dump(cloned_res.data,f,indent=4)