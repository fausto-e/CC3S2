import os, json
from shutil import copyfile

# Parámetros de ejemplo para N entornos
ENVS = [
    {"name": f"app{i}", "network": f"net{i}"} for i in range(1, 11)
]

MODULE_DIR = "modules/simulated_app"
OUT_DIR    = "environments"

def render_and_write(env):
    env_dir = os.path.join(OUT_DIR, env["name"])
    os.makedirs(env_dir, exist_ok=True)

    # 2) Genera network.tf.json
    config = {
        "variable": [
            {
                "name": [
                    {
                        "type": "string",
                        "default": env["name"],
                        "description": "Nombre del servidor local"
                    }
                ]
            },
            {
                "network": [
                    {
                        "type": "string",
                        "default": env["network"],
                        "description": "Nombre de la red local"
                    }
                ]
            }
        ]
    }

    with open(os.path.join(env_dir, "network.tf.json"), "w") as fp:
        json.dump(config, fp, sort_keys=True, indent=4)
    
    # Genera main.tf.json que use variables
    config = {
        "resource": [
            {
                "null_resource": [
                    {
                        env["name"]: [
                            {
                                "triggers": {
                                    "name":    "${var.name}",
                                    "network": "${var.network}"
                                },
                                "provisioner": [
                                    {
                                        "local-exec": {
                                            "command": (
                                                "echo 'Arrancando servidor ${var.name} en red ${var.network}'"
                                            )
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }

    with open(os.path.join(env_dir, "main.tf.json"), "w") as fp:
        json.dump(config, fp, sort_keys=True, indent=4)


if __name__ == "__main__":
    # # Limpia entornos viejos NO SE DEBE ELIMINAR
    # if os.path.isdir(OUT_DIR):
    #     import shutil
    #     shutil.rmtree(OUT_DIR)
    #     print("Entorno viejo eliminado")

    for env in ENVS:
        render_and_write(env)
    print(f"Generados {len(ENVS)} entornos en '{OUT_DIR}/'")
