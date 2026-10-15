# AR01 — Principios de arquitectura empresarial

EPS Aguas del Sur S.A. | Propuesta académica | Semana 10

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

