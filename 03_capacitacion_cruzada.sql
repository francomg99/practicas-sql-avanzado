--=====================================================================
-- Objetivo: Identificar pares de habilidades que los empleados dominan
--           en conjunto para diseñar planes de capacitación cruzada.
-- Herramientas utilizadas: SELF JOIN y optimización de cruces lógicos.
--=====================================================================

SELECT
  h1.id_empleado,
  h1.herramienta AS herramienta_a
  h2.herramienta AS herramienta_b
FROM habilidades_empleado AS h1
INNER JOIN habilidades_empleado AS h2
  ON h1.id_empleado = h2.id_empleado
WHERE h1.herramienta < h2.herramienta;
