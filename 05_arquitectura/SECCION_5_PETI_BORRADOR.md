# 5. Arquitectura empresarial — EPS Aguas del Sur S.A.

**Carácter:** propuesta académica derivada de ficha e inventario del caso ficticio. **No certifica una implantación.**

## 5.1 Principios de arquitectura

Se establecen seis principios que deberán aprobarse formalmente antes de orientar inversiones.

## P01. Segregación de redes IT/OT

- **Declaración:** Los sistemas industriales y administrativos deben mantener dominios de seguridad separados y accesos controlados.
- **Razón:** Los switches son compartidos entre SCADA y red administrativa desde 2023.
- **Implicancias:** Toda conectividad IT/OT será evaluada y autorizada; la arquitectura objetivo contempla segmentación, filtrado y supervisión.
- **Trazabilidad:** Ficha C/H; inventario 6; COBIT APO03

## P02. Trazabilidad y conservación de lecturas

- **Declaración:** Cada carga comercial debe poder reconstruirse mediante archivo original, identificador, validación y registro de procesamiento.
- **Razón:** Se eliminaron archivos de carga y hubo facturación estimada para 11 200 conexiones.
- **Implicancias:** No aceptar cargas sin conservación, comprobación de integridad, control de errores y capacidad de auditoría.
- **Trazabilidad:** Ficha G; inventario 4–5

## P03. Fuente autoritativa y responsabilidad del dato

- **Declaración:** Cada entidad crítica tendrá una fuente oficial y un responsable por cargo, con reglas de calidad y conciliación.
- **Razón:** Hay 3 100 discrepancias tarifarias; la lectura carece de fuente autoritativa.
- **Implicancias:** Definir propietarios antes de implementar indicadores y sincronizaciones; las discrepancias requieren conciliación.
- **Trazabilidad:** Inventario 5 y 7

## P04. Integraciones controladas y auditables

- **Declaración:** El intercambio entre sistemas debe tener autorización, validaciones y registros verificables.
- **Razón:** La recaudación se digita manualmente en SIAF y el reclamo se transfiere desde Excel.
- **Implicancias:** Definir contratos de interfaz, conciliación, acuses y controles según las interfaces permitidas.
- **Trazabilidad:** Inventario 4; ficha C/D

## P05. Continuidad verificable

- **Declaración:** Los servicios críticos deben contar con respaldo protegido y restauración probada.
- **Razón:** Los respaldos son locales y nunca se probó una restauración completa.
- **Implicancias:** Aprobar RTO/RPO y plan de pruebas; mantener evidencias de restauración.
- **Trazabilidad:** Ficha E/F

## P06. Gobierno digital y seguridad por diseño

- **Declaración:** Las decisiones de TI deben tener responsables, política, actas y trazabilidad de cumplimiento.
- **Razón:** No existe política de seguridad, comité formalizado ni Plan de Gobierno Digital.
- **Implicancias:** Documentar responsabilidades, revisar obligaciones, gestionar accesos y priorizar cumplimiento de forma verificable.
- **Trazabilidad:** Ficha B/E/F/H

## 5.2 Arquitectura actual (AS-IS)

### 5.2.1 Capa de negocio

La empresa opera los seis procesos comerciales, operativos y públicos definidos en la ficha D. Sus actores y responsabilidades se incluyen en el modelo.

### 5.2.2 Capa de datos

| entidad | registros_por_sistema | fuente_autoritativa | dueno_dato_cargo | clasificacion |
| --- | --- | --- | --- | --- |
| Conexión y usuario | 86000; 86000; 84100; 4800 | Catastro comercial | Gerencia Comercial | Confidencial |
| Lectura | 1030000/año total; desglose por sistema no informado | Ninguna; archivo de carga borrado | Jefe de Micromedición | Interna |
| Reclamo | 4800/año total; desglose por sistema no informado | Libro de cálculo | Atención al Usuario | Confidencial |
| Trabajador | 312; 312; 370 | AIRHSP | Recursos Humanos | Restringida |
| Proveedor | 156 en archivo entregado; conteo por sistema PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE |
| Pago a proveedor | 19281 pagos en archivo 2025; conteo por sistema PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE |
| Cuenta de usuario ERP | 192 cuentas en archivo entregado; conteo por sistema PENDIENTE | PENDIENTE | PENDIENTE | Restringida (propuesta) |

**Fuentes autoritativas ausentes confirmadas:** 1 de 7 entidades documentadas. **Pendientes de verificar:** 3 entidades. El primer conteo NO debe confundirse con la cantidad de fuentes no verificadas.

### 5.2.3 Capa de aplicación

Se identifican cinco sistemas funcionales y tres hojas de cálculo críticas que operan como aplicaciones: conciliación catastro-facturación, reclamos e indicadores SUNASS. La integración entre lecturas y comercial elimina los originales; el vínculo comercial-SIAF implica digitación; los reclamos pasan por hojas de cálculo.

### 5.2.4 Capa de tecnología

El sistema comercial funciona en servidor propio, SCADA en infraestructura industrial con radioenlaces y switches compartidos con la red administrativa desde 2023; existen terminales portátiles, cliente SIAF, hosting de reclamos y 140 estaciones. Los respaldos son locales y no tienen evidencia de restauración completa.

### 5.2.5 Cooperación proceso-aplicación

| Proceso | Sistemas que lo soportan | Valoración propuesta | Evidencia |
| --- | --- | --- | --- |
| Catastro comercial de usuarios | Sistema comercial; Excel conciliación | Parcial: 3100 discrepancias tarifarias | Inventario 2,3,5 |
| Lectura de medidores y facturación | Micromedición; sistema comercial | Deficiente: archivo eliminado, 11200 conexiones estimadas | Inventario 4,5; Ficha G |
| Cobranza y corte/reconexión | Sistema comercial; traspaso manual SIAF | Parcial: transcripción manual | Inventario 3,4 |
| Atención de reclamos comerciales | Formulario web; Excel reclamos; comercial | Deficiente: múltiples estados/plazos | Inventario 2,4,5 |
| Operación de plantas y redes | SCADA | Riesgo alto: switches compartidos IT/OT | Ficha C/H; inventario 6 |
| Contrataciones y presupuesto público | SIAF y patrimonio; Excel indicadores SUNASS | Parcial: revisar integraciones y reportería | Ficha D; inventario 2,4 |

**Procesos evaluados con soporte deficiente:** 2 de 6 (lectura/facturación y reclamos), según valoración académica preliminar. Un tercer proceso presenta riesgo tecnológico alto (operación industrial); esta categoría no significa ausencia de soporte funcional.

## 5.3 Arquitectura objetivo (TO-BE)

### 5.3.1 Derivación

El diseño se deriva de los hechos de ficha e inventario, los seis principios propuestos y del objetivo declarado de TI (segmentación de la red industrial y trazabilidad del ciclo comercial). **Debe contrastarse además con las secciones 2.2, 3.1.5, 3.5, 4.1.5 y 4.2 del PETI del equipo; no fueron aportadas al notebook.**

### 5.3.2 Cambios por capa

Negocio: registro trazable de reclamos, lecturas auditables y gobierno digital. Datos: conciliación tarifaria, responsables y fuente oficial de lecturas. Aplicaciones: conservación y validación de lotes, integración controlada, reclamos centralizados y reportería verificada. Tecnología: segmentación de redes, supervisión industrial sin exposición innecesaria y copias restaurables.

### 5.3.3 Vistas objetivo

Consultar `EPS08_arquitectura_intercambio.xml` (vistas 01 a 05) y `graficos/03_TOBE_PREVISUALIZACION.png`. Debe comprobarse su importación en Archi y exportarse la vista definitiva desde la herramienta.

## 5.4 Análisis de brechas

### 5.4.1 Brechas por capa y tipo

| codigo | capa | actual | objetivo | tipo_brecha | esfuerzo | origen |
| --- | --- | --- | --- | --- | --- | --- |
| BR-01 | Tecnología | Switches compartidos IT/OT | Segmentación IT/OT y control fronterizo | Modificar | Alto | Ficha C/H; inventario 6; P01 |
| BR-02 | Aplicación | Micromedición y lectura | Repositorio de lotes y bitácora | Nuevo | Medio | Ficha G; inventario 4; P02 |
| BR-03 | Datos | Conexión y usuario | Conexión maestra conciliada | Modificar | Medio | Inventario 5; P03 |
| BR-04 | Aplicación | Excel de reclamos | Gestor centralizado de reclamos | Reemplazar | Alto | Inventario 2 y 4; P04 |
| BR-05 | Aplicación | SIAF y patrimonio | Capa de integración y conciliación | Modificar | Alto | Inventario 4; P04 |
| BR-06 | Aplicación | Excel indicadores SUNASS | Indicadores reguladores validados | Reemplazar | Medio | Inventario 2; P03 |
| BR-07 | Tecnología | Servidor propio del comercial | Respaldo protegido y restauración probada | Modificar | Medio | Ficha F; P05 |
| BR-08 | Aplicación | Sistema comercial | Gestión de identidades y MFA | Modificar | Medio | Ficha F; P06 |
| BR-09 | Negocio | Política de seguridad ausente | Política de seguridad aprobada | Nuevo | Medio | Ficha B/E; P06 |
| BR-10 | Negocio | Plan de continuidad ausente | Plan continuidad y pruebas | Nuevo | Alto | Ficha E; P05 |
| BR-11 | Negocio | Formalización gobierno digital ausente | Gobierno digital formalizado | Modificar | Medio | Ficha B/E; P06 |
| BR-12 | Aplicación | Excel conciliación catastro-facturación | Gobierno de calidad de datos | Reemplazar | Alto | Inventario 2 y 5; P03 |
| BR-13 | Datos | Lectura | Lectura original + auditoría | Modificar | Medio | Inventario 5; P02 |
| BR-14 | Tecnología | Infraestructura industrial SCADA | Servicio de registros y monitoreo | Nuevo | Medio | Ficha H; inventario 6; P01 |

### 5.4.2 Paquetes de trabajo

| paquete | nombre | brechas | dependencias | fase_topologica |
| --- | --- | --- | --- | --- |
| PT-01 | Gobierno y calidad del dato | BR-03; BR-12 | Ninguna | 1 |
| PT-02 | Protección de la red industrial | BR-01; BR-14 | Ninguna | 1 |
| PT-07 | Continuidad y recuperación | BR-07; BR-10 | Ninguna | 1 |
| PT-08 | Seguridad y gobierno digital | BR-08; BR-09; BR-11 | Ninguna | 1 |
| PT-03 | Trazabilidad de lecturas | BR-02; BR-13 | PT-01 | 2 |
| PT-04 | Gestión de reclamos | BR-04 | PT-01 | 2 |
| PT-05 | Integraciones autorizadas | BR-05 | PT-01; PT-02 | 2 |
| PT-06 | Indicadores regulatorios | BR-06 | PT-01; PT-03; PT-05 | 3 |

### 5.4.3 Dependencias y secuencia

Fase 1: PT-01, PT-02, PT-07, PT-08

Fase 2: PT-03, PT-04, PT-05

Fase 3: PT-06

Esta es una ordenación topológica posible; otros paquetes de la misma fase pueden realizarse en paralelo. El orden técnico y los esfuerzos requieren contrastación presupuestal y operativa.

### Limitaciones y validaciones pendientes

No se afirma que se hayan ejecutado proyectos objetivo, ni que se haya probado una restauración o una segmentación. Faltan datos operativos sobre tres entidades de apoyo; deben completarse en entrevista simulada. Se necesita abrir el modelo en Archi, comprobar cada vista y exportar PNG definitivas. Además debe cotejarse la sección 5 con el PETI previo del equipo.
