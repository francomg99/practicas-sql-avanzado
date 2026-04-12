--===============================================================
-- Objetivo: Reporte de anomalías salariales. Encontrar empleados
--           que ganen un salario mayor al de su jefe directo.
-- Herramientas utilizadas: SELF JOIN y comparación Inter-Filas-
--===============================================================

SELECT
  e1.nombre AS nombre_empleado
  e1.salario AS salario_empleado
  e2.nombre AS nombre_jefe
  e2.salario AS salario_jefe
FROM empleados AS e1
INNER JOIN empleados AS e2
  ON (e1.id_jefe = e2.id_empleado)
WHERE e1.salario > e2.salario;
