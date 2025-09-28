# Parte teórica
**¿Qué es y qué no es? Explica DevOps desde el código hasta la producción, diferenciándolo de waterfall. Discute "you build it, you run it" en el laboratorio, y separa mitos (ej. solo herramientas) vs realidades (CALMS, feedback, métricas, gates).**

**Qué es:**
- Un conjunto de prácticas y una cultura que busca integrar los equipos de desarrollo, operaciones y QA para entregar software más rápido, más seguro y más confiable.
- Se centra en la automatización, la colaboración entre equipos, la observabilidad y la entrega continua.
- Va desde el código hasta la producción, incluyendo: control de versiones, pruebas automatizadas, CI/CD, monitoreo y retroalimentación.

**Qué no es:**
- No es un rol único.
- No es simplemente usar herramientas como instalar Jenkins, Docker o Kubernetes.
- No es un modelo rígido como waterfall; DevOps es iterativo y adaptativo.
- No significa eliminar la necesidad de operaciones, sino integrarlas.

**Del código a la producción**
1. Planificación: backlog en Jira/GitHub Issues → historias pequeñas e iterativas.
2. Código: los devs trabajan en ramas de Git → buenas prácticas, code review.
3. Integración continua (CI): cada commit dispara pruebas automáticas (unitarias, estáticas, seguridad).
4. Entrega continua (CD): builds automatizados → generación de artefactos listos para producción (ej: contenedores).
5. Despliegue: pipelines que llevan el artefacto a staging/producción → con blue/green o canary release.
6. Operación: monitoreo (logs, métricas, trazas), alertas, observabilidad.
7. Feedback: métricas de uso, fallos, tiempos de respuesta → vuelven al backlog para mejorar.
s
**Devops del código a producción:**
Tip: Piensa en ejemplos concretos: ¿cómo se vería un gate de calidad en tu Makefile?
Marco CALMS en acción: Describe cada pilar y su integración en el laboratorio (ej. Automation con Makefile, Measurement con endpoints de salud). Propón extender Sharing con runbooks/postmortems en equipo.

Tip: Relaciona cada letra de CALMS con un archivo del laboratorio.
Visión cultural de DevOps y paso a DevSecOps: Analiza colaboración para evitar silos, y evolución a DevSecOps (integrar seguridad como cabeceras TLS, escaneo dependencias en CI/CD). Propón escenario retador: fallo certificado y mitigación cultural. Señala 3 controles de seguridad sin contenedores y su lugar en CI/CD.

Tip: Usa el archivo de Nginx y systemd para justificar tus controles.
Metodología 12-Factor App: Elige 4 factores (incluye config por entorno, port binding, logs como flujos) y explica implementación en laboratorio. Reto: manejar la ausencia de estado (statelessness) con servicios de apoyo (backing services).

Tip: No solo describas: muestra dónde el laboratorio falla o podría mejorar.

TODO pdf de máximo 4 paginas de resumen  con informe resumido, cuadro de evidencias y checklist de trazabilidad.