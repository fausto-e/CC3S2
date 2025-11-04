#!/usr/bin/env python3
from iac_patterns.composite import CompositeModule
from iac_patterns.factory import NullResourceFactory
import json
import os

def crear_modulo_network() -> dict:
    return {
        "module": {
            "network": {
                "source": "./modules/network",
                "vpc_cidr": "10.0.0.0/16",
                "environment": "dev"
            }
        }
    }

def crear_modulo_app() -> dict:
    return {
        "module": {
            "app": {
                "source": "./modules/app",
                "instance_count": 2,
                "app_name": "mi-aplicacion",
                "depends_on": ["module.network"]
            }
        }
    }

def crear_recurso_local_file(nombre: str, contenido: str) -> dict:
    return {
        "resource": [{
            "local_file": [{
                nombre: [{
                    "content": contenido,
                    "filename": f"${{path.module}}/{nombre}.txt"
                }]
            }]
        }]
    }

def main():
    # Crear el módulo compuesto
    composite = CompositeModule()
    
    # 1. Agregar submódulo de red
    composite.add(crear_modulo_network())
    
    # 2. Agregar submódulo de aplicación
    composite.add(crear_modulo_app())
    
    # 3. Agregar algunos recursos null
    composite.add(NullResourceFactory.create("network_init", {
        "description": "Inicialización de red"
    }))
    composite.add(NullResourceFactory.create("app_init", {
        "description": "Inicialización de aplicación"
    }))
    
    # 4. Agregar archivos de documentación
    composite.add(crear_recurso_local_file(
        "network_readme",
        "Documentación del módulo de red\n\nVPC CIDR: 10.0.0.0/16"
    ))
    
    # 5. Exportar la configuración completa
    output_dir = os.path.join("output", "ejercicio2_4")
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = os.path.join(output_dir, "main.tf.json")
    
    with open(output_path, "w") as f:
        json.dump(composite.export(), f, indent=4)

if __name__ == "__main__":
    main()