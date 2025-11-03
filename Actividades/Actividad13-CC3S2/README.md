### Respuestas fase 1
Pregunta 1: ¿Cómo interpreta Terraform el cambio de variable?

Detecta un cambio en el estado deseado comparándolo contra terraform.tfstate, identifica que el valor del trigger cambió de "local-network" a "lab-net" y marca el recurso para recreación (destroy + create) porque los triggers son inmutables.


Pregunta 2: ¿Qué diferencia hay entre modificar el JSON vs. parchear directamente el recurso?

Modificar network.tf.json permite regenerar automáticamente los 10 entornos con un solo comando y editar directamente main.tf.json requiere cambios manuales en cada entorno (10 archivos).


Pregunta 3: ¿Por qué Terraform no recrea todo el recurso, sino que aplica el cambio "in-place"?

Terraform sí recrea el recurso completo (-/+ replace), NO hace cambio in-place. Los triggers de null_resource son inmutables, cualquier cambio fuerza destrucción + creación.

Pregunta 4: ¿Qué pasa si editas directamente main.tf.json en lugar de la plantilla de variables?

Terraform detectará el cambio y recreará el recurso (-/+) correctamente para ese entorno. Sin embargo, los otros entornos no se verán afectados y mantendrán la configuración anterior, lo que puede llevar a inconsistencias si se espera que todos los entornos tengan la misma configuración.
