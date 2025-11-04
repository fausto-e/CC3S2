## 1. Singleton - Garantía de instancia única

El patrón Singleton utiliza una metaclase (`SingletonMeta`) que intercepta la creación de objetos y mantiene un diccionario global de instancias. Cuando se intenta crear un nuevo objeto, primero verifica si ya existe una instancia en el diccionario; si existe, devuelve esa misma instancia, y si no, crea una nueva y la almacena. El `threading.Lock` es esencial para garantizar que en ambientes multi-hilo solo un hilo pueda ejecutar la verificación y creación de instancia a la vez, evitando que múltiples hilos creen instancias simultáneamente y rompan el patrón singleton.

## 2. Factory - Encapsulación estandarizada

La Factory encapsula toda la lógica de creación de recursos `null_resource` en un único método estático, eliminando la necesidad de escribir manualmente la estructura JSON completa cada vez que se necesita un recurso. Los `triggers` son parámetros que Terraform utiliza para determinar cuándo recrear un recurso; la Factory incluye automáticamente un `factory_uuid` (para garantizar unicidad) y un `timestamp` (para auditoría), aunque permite sobrescribirlos con triggers personalizados según las necesidades específicas de cada recurso.

## 3. Prototype - Clonación eficiente con personalización

El patrón Prototype utiliza `copy.deepcopy()` para crear copias profundas de un objeto plantilla, asegurando que las modificaciones al clon no afecten al original (a diferencia de la copia superficial que solo copia referencias). El `mutator` es una función callback que recibe el clon recién creado y lo modifica in-place antes de devolverlo, permitiendo personalizar cada instancia clonada de manera flexible sin necesidad de crear subclases o modificar la plantilla original, ideal para generar múltiples recursos similares con pequeñas variaciones.

## 4. Composite - Unificación de recursos heterogéneos

El patrón Composite permite tratar recursos individuales y grupos de recursos de manera uniforme mediante una estructura de árbol donde todos los elementos comparten la misma interfaz. El método `export()` itera sobre todos los hijos agregados al composite, extrayendo sus bloques de recursos y fusionándolos progresivamente en un único diccionario usando `setdefault()` para crear nuevos tipos de recursos y `update()` para agregar recursos al mismo tipo, resultando en un JSON válido de Terraform que puede contener múltiples tipos de recursos (null_resource, local_file, etc.) organizados jerárquicamente.

## 5. Builder - Orquestación fluida de patrones

El Builder actúa como director de orquesta coordinando Factory (para crear plantillas base), Prototype (para clonar y personalizar), y Composite (para agregar y unificar), todo a través de una API fluida con métodos encadenables. El método `build_null_fleet()` ejemplifica esta orquestación: usa Factory para crear una plantilla, la envuelve en un Prototype, ejecuta un loop donde clona y personaliza cada recurso mediante un mutator que renombra dinámicamente el recurso, y finalmente agrega cada clon al Composite; al llamar `export()`, el Builder delega al Composite la fusión de todos los recursos y escribe el resultado en un archivo JSON, abstrayendo toda la complejidad en una interfaz simple y expresiva.