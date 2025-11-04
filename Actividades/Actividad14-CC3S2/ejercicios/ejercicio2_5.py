from iac_patterns.builder import InfrastructureBuilder
import os

def main() -> None:
    builder = InfrastructureBuilder(env_name="Ejercicio2_5")

    builder.build_group("ej25",10)

    path = os.path.join("output", "ejercicio2_5")
    path = os.path.join(path, "main.tf.json")
    
    builder.export(path=str(path))
    
if __name__ == "__main__":
    main()