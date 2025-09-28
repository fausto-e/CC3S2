# Resolución de la actividad 6

Repositorio de pruebas utilizado: [git-demo](https://github.com/fausto-e/git-demo)

### ejemplo de merge y branches
```bash
~/Documents/UNI/Desarrollo_software/kapumota-repo
↳ fernando@Nitro-5$ git lago
* 8cb5fa5 (HEAD -> develop, master) Agrega main.py
* 8152947 Configura la documentación del repositorio
* 3cf3e97 Commit inicial con README.md
~/Documents/UNI/Desarrollo_software/kapumota-repo
↳ fernando@Nitro-5$ echo "Cambio desde develop" >> README.md 
~/Documents/UNI/Desarrollo_software/kapumota-repo
↳ fernando@Nitro-5$ git add .
~/Documents/UNI/Desarrollo_software/kapumota-repo
↳ fernando@Nitro-5$ git cm "Agregar cambio a README.md  desde devolop"
[develop b1b9133] Agregar cambio a README.md  desde devolop
 1 file changed, 1 insertion(+)
 ~/Documents/UNI/Desarrollo_software/kapumota-repo
↳ fernando@Nitro-5$ git checkout master
Switched to branch 'master'
~/Documents/UNI/Desarrollo_software/kapumota-repo
↳ fernando@Nitro-5$ git merge --no-ff develop
Merge made by the 'ort' strategy.
 README.md | 1 +
 1 file changed, 1 insertion(+)
~/Documents/UNI/Desarrollo_software/kapumota-repo
↳ fernando@Nitro-5$ git lago
*   1dc01b4 (HEAD -> master) Fusion de la rama develop.
|\  
| * b1b9133 (develop) Agregar cambio a README.md  desde devolop
|/  
* 8cb5fa5 Agrega main.py
* 8152947 Configura la documentación del repositorio
* 3cf3e97 Commit inicial con README.md
~/Documents/UNI/Desarrollo_software/kapumota-repo
↳ fernando@Nitro-5$ git branch -d develop
Deleted branch develop (was b1b9133).
~/Documents/UNI/Desarrollo_software/kapumota-repo
↳ fernando@Nitro-5$ git lago
*   1dc01b4 (HEAD -> master) Fusion de la rama develop.
|\  
| * b1b9133 Agregar cambio a README.md  desde devolop
|/  
* 8cb5fa5 Agrega main.py
* 8152947 Configura la documentación del repositorio
* 3cf3e97 Commit inicial con README.md
 ```

- ¿Cómo te ha ayudado Git a mantener un historial claro y organizado de tus cambios?
Historial claro y trazable:

El comando git log --graph (o mi alias lago) muestra de forma visual cómo se creó un commit en la rama develop y luego se integró a master.

Queda registrado no solo el contenido de los cambios, sino también cuándo y desde qué rama se hizo la modificación, lo que da contexto al equipo.

- ¿Qué beneficios ves en el uso de ramas para desarrollar nuevas características o corregir errores?

Aislamiento de cambios: en este caso, el cambio al README.md se hizo en develop, sin afectar inmediatamente a master. Esto permite trabajar en paralelo sin romper la rama principal.

Control de integración: el merge --no-ff generó un commit de fusión que deja explícito en la historia que hubo una integración de ramas. Así se conserva la trazabilidad de que hubo un flujo de desarrollo independiente.

Facilidad de limpieza: se eliminó develop porque su trabajo ya fue integrado. Esto mantiene el repositorio ordenado sin perder el historial.

### Ejercicio 1



### Ejercicio 2

Realize un `git revert` para deshacer el commit que agrega una `dummy`.

Tambien cree una rama `feature/rebase` en el commit del merge anterior y realize 3 commits de prueba. Luego, realize un rebase interactivo para combinar los 3 commits en uno solo con un mensaje descriptivo.

Visualizamos con `git log --graph --oneline --all` después del rebase interactivo. Podemos observar que los tres commits se han combinado en uno solo, manteniendo un historial más limpio y organizado.

### Ejercicio 3

Desde el commit `dummy change` cree una rama `bugfix/rollback-feature`, realize un commit y realize un merge desde `master`. Finalmente, eliminé la rama `bugfix/rollback-feature`.

### Ejercicio 4

Se editó el archivo main.py para introducir un cambio temporal con el mensaje "Introduce un cambio para restablecer".
Luego, se confirmó con git add y git commit.

Posteriormente, se utilizó git reset --hard HEAD~1 para deshacer el commit y volver al estado anterior, verificando que el commit fue eliminado del historial y que el archivo recuperó su contenido original.

Después, se realizaron cambios no confirmados en README.md. Con git status se verificó la modificación pendiente y, finalmente, se utilizó git restore README.md para descartar dichos cambios. Se comprobó que el archivo volvió a su estado previo, mostrando cómo git restore permite revertir ediciones sin necesidad de un commit.

### Ejercicio 5

Se creó un nuevo repositorio remoto con los avances que se realizaron hasta ahora.
A continuación, se generó una rama de desarrollo llamada feature/team-feature para trabajar en una nueva característica.

En esta rama, se añadió el archivo colaboracion.py con un mensaje en consola y se confirmó el cambio con el commit "Agrega script de colaboración".
Posteriormente, la rama fue enviada al repositorio remoto con git push origin feature/team-feature.

En Github se abrió un Pull Request (PR) dirigido a la rama main, incluyendo una descripción detallada del propósito de los cambios.
Se simuló una revisión de código con comentarios y, tras realizar los ajustes necesarios, el PR fue aprobado y fusionado en main.

Finalmente, la rama feature/team-feature se eliminó tanto local como remotamente, manteniendo el historial ordenado y evitando ramas obsoletas.

Repositorio remoto de prueba utilizado: [git-demo](https://github.com/fausto-e/git-demo)

### Ejercicio 6

Se realizaron y confirmaron cambios en main.py dentro de la rama master con el commit "Agrega ejemplo de cherry-pick".

Posteriormente, se creó una nueva rama feature/cherry-pick, en la cual se añadió un commit adicional con nuevos cambios.
Desde la rama master, se utilizó git cherry-pick para aplicar dicho commit específico, integrando así las modificaciones de feature/cherry-pick sin necesidad de fusionar toda la rama.

Luego, se trabajó con git stash: se hicieron cambios temporales en main.py, se confirmaron algunos commits intermedios, y se guardaron modificaciones en el stash.
Tras realizar otros cambios y confirmarlos, se aplicaron los cambios guardados con git stash pop, y posteriormente se confirmó el commit que incorporó esas modificaciones recuperadas.