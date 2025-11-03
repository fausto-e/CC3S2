# generate_envs.py refactorizado con click
import os
import json
import click
from shutil import copyfile

MODULE_DIR = "modules/simulated_app"
OUT_DIR = "environments"

@click.command()
@click.option('--count', default=10, help='Numero de entornos a generar')
@click.option('--prefix', default='app', help='Prefijo para nombres de entornos')
@click.option('--port', default=8790, help='Puerto base (se incrementa por entorno)')
@click.option('--network-prefix', default='net', help='Prefijo para nombres de redes')
@click.option('--output-dir', default='environments', help='Directorio de salida')
def generate_envs(count, prefix, port, network_prefix, output_dir):
    envs = [
        {
            "name": f"{prefix}{i}",
            "network": f"{network_prefix}{i}",
            "port": port + i - 1
        }
        for i in range(1, count + 1)
    ]
    
    os.makedirs(output_dir, exist_ok=True)
    
    for env in envs:
        render_and_write(env, output_dir)
    
    click.secho(f"\n\tGenerados {len(envs)} entornos en '{output_dir}/'", fg='green', bold=True)

def render_and_write(env, output_dir):
    env_dir = os.path.join(output_dir, env["name"])
    os.makedirs(env_dir, exist_ok=True)
    
    # Generar network.tf.json
    network_config = {
        "variable": [
            {
                "name": [{
                    "type": "string",
                    "default": env["name"],
                    "description": "Nombre del servidor local"
                }]
            },
            {
                "network": [{
                    "type": "string",
                    "default": env["network"],
                    "description": "Nombre de la red local"
                }]
            },
            {
                "port": [{
                    "type": "number",
                    "default": env["port"],
                    "description": "Puerto de la app"
                }]
            }
        ]
    }
    
    with open(os.path.join(env_dir, "network.tf.json"), "w") as fp:
        json.dump(network_config, fp, sort_keys=True, indent=4)

    main_config = {
        "resource": [{
            "null_resource": [{
                f"local_server-{env['name']}": [{
                    "triggers": {
                        "name": "${var.name}",
                        "network": "${var.network}",
                        "port": "${var.port}"
                    },
                    "provisioner": [{
                        "local-exec": {
                            "command": (
                                "echo 'Arrancando servidor ${var.name} "
                                "en red ${var.network}:${var.port}'"
                            )
                        }
                    }]
                }]
            }]
        }]
    }
    
    with open(os.path.join(env_dir, "main.tf.json"), "w") as fp:
        json.dump(main_config, fp, sort_keys=True, indent=4)
    
    click.echo(f"{env['name']}: network={env['network']}, port={env['port']}")

if __name__ == "__main__":
    generate_envs()