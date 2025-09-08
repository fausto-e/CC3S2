### FF vs rebase vs cherry-pick
En este proyecto se muestran diferentes estrategias de integración en Git.
El merge fast-forward avanza la rama principal sin crear commits extras, manteniendo un historial simple. e uso la rama `feature/msg` como ejemplo.
El rebase reubica los commits de una rama sobre otra, generando un historial lineal y más limpio. Se uso la rama `feature/rebase` como ejemplo.
El cherry-pick permite aplicar un commit específico de otra rama sin fusionar todo su historial. e uso la rama `hotfix` como ejemplo.

### 3.2 API + jq
Se recibió un header con el tipo de contenido: `content-type: application/json; charset=utf-8`