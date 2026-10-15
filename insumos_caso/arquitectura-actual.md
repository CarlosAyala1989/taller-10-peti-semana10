<div align="center">
  <strong>EPS AGUAS DEL SUR S.A.</strong><br>
  <em>Documento del caso</em>
</div>

---

# Inventario de la arquitectura actual

| | |
|---|---|
| **Organización** | EPS AGUAS DEL SUR S.A. |
| **Documento** | Inventario de la arquitectura actual |
| **Entregado por** | Tecnologías de la Información, a pedido del equipo |
| **Fecha de entrega** | 15 de junio de 2026 |
| **Clasificación** | Restringido |

> Documento de una organización ficticia, elaborado para el curso. Cualquier parecido con una empresa real es coincidencia.

---

## 1. Qué es este documento

Es lo que el área de tecnologías de la información entrega cuando se le pide **cómo están armados sus sistemas**. No existía. Se armó a pedido del equipo con lo que el área sabe, y el propio jefe advierte que «faltan cosas que solo están en la cabeza de alguien».

## 2. Aplicaciones que operan

Los sistemas de la ficha, más **las hojas de cálculo que operan como sistema**. El área reconoce que sin ellas la organización no funciona.

| Aplicación | Qué es | Dónde corre | ¿Tiene soporte vigente? |
|---|---|---|---|
| **Sistema comercial** | Producto del sector saneamiento: catastro, facturación y cobranza | Servidor propio | Sí |
| **SCADA de plantas y reservorios** | Sistema del proveedor de automatización | Red industrial separada | Sí |
| **Micromedición y lectura** | Terminales portátiles del proveedor | Mixto | Sí |
| **SIAF y patrimonio** | Sistemas del MEF | Cliente local | MEF |
| **Atención de reclamos** | Formulario web y hoja de cálculo | Hosting propio | No |
| **Hoja de cálculo · Conciliación catastro–facturación, mensual** | Libro de cálculo que un área mantiene por su cuenta | PC del área o carpeta compartida | No |
| **Hoja de cálculo · Reclamos, alimentado por el formulario web** | Libro de cálculo que un área mantiene por su cuenta | PC del área o carpeta compartida | No |
| **Hoja de cálculo · Indicadores para SUNASS** | Libro de cálculo que un área mantiene por su cuenta | PC del área o carpeta compartida | No |

## 3. Qué sistema soporta cada proceso

| Proceso de negocio | Sistema que lo soporta |
|---|---|
| Catastro comercial de usuarios | Sistema comercial |
| Lectura de medidores y facturación | Micromedición y lectura |
| Cobranza y corte/reconexión | Sistema comercial |
| Atención de reclamos comerciales | Atención de reclamos |
| Operación de plantas y redes | SCADA de plantas y reservorios |
| Contrataciones y presupuesto público | SIAF y patrimonio |

## 4. Integraciones entre sistemas

| De | A | Cómo se integra hoy |
|---|---|---|
| Micromedición y lectura | Sistema comercial | Archivo de lecturas cargado por lote. El archivo no se conserva |
| Sistema comercial | SIAF | Manual. La recaudación se digita |
| Atención de reclamos | Sistema comercial | El formulario carga al libro de cálculo; de ahí al comercial, a mano |
| SCADA | Nadie | Ninguna. La red industrial se unió a la administrativa en 2023 |

## 5. Entidades de datos y dónde viven

Lo que el área pudo reconstruir. Los conteos son los que cada sistema devuelve hoy; cuando no coinciden, el área no sabe cuál es el bueno.

| Entidad | Sistemas donde reside | Registros por sistema | ¿Fuente autoritativa declarada? | Dueño del dato, por cargo | Discrepancia que el área conoce | Clasificación | ¿Datos personales? |
|---|---|---|---|---|---|---|---|
| Conexión y usuario | Catastro del comercial · Facturación del comercial · Lecturas · Reclamos | 86 000 · 86 000 · 84 100 · 4 800 | Catastro, declarada | Gerencia comercial | 3 100 conexiones con categoría tarifaria distinta entre catastro y facturación | Confidencial | Sí |
| Lectura | Terminales portátiles · Archivo de carga · Facturación | 1 030 000 al año | Ninguna. El archivo de carga se borra | Jefe de micromedición | 11 200 conexiones facturadas por estimación en tres ciclos | Interna | No |
| Reclamo | Formulario web · Libro de reclamos · Sistema comercial · Reporte a SUNASS | 4 800 al año | El libro de cálculo | Atención al usuario | Plazos distintos en el libro y en el reporte | Confidencial | Sí |
| Trabajador | AIRHSP del MEF · Planilla · Biométrico | 312 · 312 · 370 | AIRHSP | Recursos Humanos | 58 por servicios no figuran en el AIRHSP | Restringida | Sí |

## 6. Nodos, dispositivos y redes

**Nodos.** Servidor propio del sistema comercial · la red industrial del SCADA, con switches compartidos con la administrativa desde 2023 · terminales portátiles de lectura · cliente del SIAF · hosting propio del formulario de reclamos · 140 estaciones.

**Redes.** Red administrativa y red industrial unidas desde la ampliación de 2023. Plantas y reservorios por radioenlace.

## 7. Lo que la organización responde

| Pregunta del equipo | Respuesta |
|---|---|
| ¿Existe un diagrama de arquitectura? | «Hay uno de red en una pizarra. Nunca se dibujaron los sistemas» |
| ¿Quién aprueba que un área cree una hoja de cálculo para operar? | «Nadie. Aparecen y después hay que alimentarlas» |
| ¿Quién es el dueño de cada dato? | «El sistema que lo tiene. Si está en dos, los dos» |
| ¿Qué pasa cuando dos sistemas dicen cifras distintas? | «Se pregunta al que lo lleva y se usa esa» |
| ¿Hay principios de arquitectura escritos? | «No» |

## 8. Marco de referencia

| Marco | Qué aporta |
|---|---|
| **TOGAF, 10.ª edición · ADM** | Fases B, C y D para la arquitectura de negocio, de sistemas de información y de tecnología, y el análisis de brechas |
| **ArchiMate 3.2** | El lenguaje con el que se modelan las capas y sus relaciones |
| **COBIT 2019 · APO03** | Gestión de la arquitectura empresarial |

