import os
import json
from shutil import copyfile


ENVS = [
    {"name": f"app{i}", "network": f"net{i}", "port": 8790+i} 
    for i in range(1, 3)
] + [
    {"name": "app3", "network": "net2-peered", "port": 8793, "depends_on": "app2"}
] + [
    {"name": f"app{i}", "network": f"net{i}", "port": 8790+i} 
    for i in range(4, 11)
]

MODULE_DIR = "modules/simulated_app"
OUT_DIR = "environments"

# Mapa para lookup de dependencias
ENVS_MAP = {env["name"]: env for env in ENVS}

def get_network_value(env):
    if "depends_on" in env:
        parent_env = ENVS_MAP.get(env["depends_on"])
        if parent_env:
            return f"{parent_env['network']}-peered"
    return env["network"]

def render_and_write(env):
    env_dir = os.path.join(OUT_DIR, env["name"])
    os.makedirs(env_dir, exist_ok=True)

    # Calcular network con dependencias
    network_value = get_network_value(env)
    
    # Verificar que API_KEY existe en el entorno
    api_key = os.environ.get("TF_VAR_api_key")
    if not api_key:
        print(f"WARNING: TF_VAR_api_key no definida. Usa: export API_KEY='clave-secreta'")

    # Genera network.tf.json
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
                        "default": network_value,
                        "description": "Nombre de la red local"
                    }
                ]
            },
            {
                "port": [
                    {
                        "type": "number",
                        "default": env["port"],
                        "description": "Puerto de la app" 
                    }
                ]
            },
            {
                "api_key": [
                    {
                        "type": "string",
                        "sensitive": True,
                        "description": "API Key secreta (pasar via TF_VAR_api_key)"
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
                        "local_server-" + env["name"]: [
                            {
                                "triggers": {
                                    "name": "${var.name}",
                                    "network": "${var.network}",
                                    "port": "${var.port}",
                                    "api_key_hash": "${md5(var.api_key)}"
                                },
                                "provisioner": [
                                    {
                                        "local-exec": {
                                            "command": (
                                                "echo 'Arrancando servidor ${var.name} "
                                                "en red ${var.network}:${var.port} "
                                                "(autenticado)'"
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
    
    # Información sobre dependencias
    if "depends_on" in env:
        print(f"  {env['name']}: network={network_value} (depende de {env['depends_on']})")
    else:
        print(f"  {env['name']}: network={network_value}")


if __name__ == "__main__":
    print("Generando entornos con dependencias y secretos...")
    
    for env in ENVS:
        render_and_write(env)
    
    print(f"\nGenerados {len(ENVS)} entornos en '{OUT_DIR}/'")
    print("\nProximos pasos:")
    print("1. export TF_VAR_api_key='tu-clave-secreta'")
    print("2. cd environments/app3")
    print("3. terraform init")
    print("4. terraform plan")
    print("5. terraform apply")