# Plan de Descontaminación PPDA

## 1. ¿Qué es el PPDA?
El PPDA es un plan de descontaminación implementado en las comunas de Concón, Quintero y Puchuncaví (Región de Valparaíso, Chile) con el objetivo de reducir la contaminación del aire. Se enfoca en la reducción de los niveles de material particulado (MP10 y MP2.5) y otros contaminantes como dióxido de azufre (SO2) y óxidos de nitrógeno (NOx).

El plan establece medidas específicas a implementar por diversos organismos públicos (como la Superintendencia del Medio Ambiente, Municipalidades, Seremi de Salud, etc.) para reducir las emisiones y mejorar la calidad del aire.

## 2. ¿Qué es el Estado de Avance del PPDA?
El **estado de avance** se refiere al progreso de las medidas del PPDA. Cada organismo público debe reportar:

- Actividades realizadas (por ejemplo, fiscalizaciones, implementación de sistemas de control de emisiones, etc.).
- Porcentaje de cumplimiento de las medidas asignadas.
- Reducción de emisiones lograda.

Estos datos se consolidan en un informe anual que permite evaluar si el plan está cumpliendo sus objetivos.

## 3. ¿Qué debe hacer el Sistema en FastAPI?
El sistema que se desarrollará en **FastAPI** debe permitir las siguientes funcionalidades:

- **Registrar actividades**: Los organismos públicos podrán registrar las actividades realizadas para cumplir con las medidas del PPDA.
- **Calcular el avance**: El sistema debe calcular el porcentaje de cumplimiento de cada medida utilizando fórmulas establecidas.
- **Generar reportes**: El sistema debe generar informes anuales que muestren el estado de avance del PPDA.
- **Visualizar datos**: Los usuarios podrán ver el estado de avance de las medidas en una interfaz amigable, con gráficos, tablas, etc.

## 4. Estructura del Sistema en FastAPI
...

### a) Modelos de Datos (Base de Datos)

- **Medidas**: Cada medida del PPDA (por ejemplo, "Control de emisiones de MP en fuentes areales").
- **Actividades**: Las actividades realizadas por los organismos para cumplir las medidas.
- **Organismos**: Los organismos públicos responsables (por ejemplo, Seremi de Salud, CONAF, etc.).
- **Reportes**: Los informes anuales de avance.


