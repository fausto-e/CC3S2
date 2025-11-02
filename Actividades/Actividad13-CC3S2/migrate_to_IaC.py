#!/usr/bin/env python3
import os
import json
import re

def parse_config(config_path):
    config = {}
    with open(config_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                if '=' in line:
                    key, value = line.split('=', 1)
                    config[key] = value
    return config

def generate_terraform(config, output_dir):
    variables = {
        "variable": []
    }
    
    for key, value in config.items():
        variables["variable"].append({
            key.lower(): [{
                "type": "string",
                "default": value,
                "description": f"Migrado desde config.cfg: {key}"
            }]
        })

    main_config = {
        "resource": [{
            "null_resource": [{
                "legacy_migration": [{
                    "triggers": {
                        key.lower(): f"${{var.{key.lower()}}}" 
                        for key in config.keys()
                    },
                    "provisioner": [{
                        "local-exec": {
                            "command": (
                                f"echo 'Arrancando ${{var.app_name}}' && "
                                f"echo 'Puerto: ${{var.port}}' && "
                                f"echo 'Entorno: ${{var.environment}}'"
                            )
                        }
                    }]
                }]
            }]
        }]
    }

    os.makedirs(output_dir, exist_ok=True)
    
    with open(os.path.join(output_dir, "network.tf.json"), 'w') as f:
        json.dump(variables, f, indent=4)
    
    with open(os.path.join(output_dir, "main.tf.json"), 'w') as f:
        json.dump(main_config, f, indent=4)
    
    print(f"[OK] Archivos Terraform generados en '{output_dir}/'")

def main():
    # Rutas
    config_path = "legacy/config.cfg"
    script_path = "legacy/run.sh"
    output_dir = "terraform_migrated"

    print(" Leyendo configuración legacy...")
    config = parse_config(config_path)
    print(f"   Encontradas {len(config)} variables: {list(config.keys())}")

    print(" Generando archivos Terraform...")
    generate_terraform(config, output_dir)
    
    print("[OK] MIGRACIÓN COMPLETADA")

if __name__ == "__main__":
    main()