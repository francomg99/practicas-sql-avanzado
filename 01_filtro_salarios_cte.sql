-- =======================================================================
-- Objetivo: Obtener los empleados que ganan más que el promedio 
--           de su propio departamento.
-- Herramientas utilizadas: CTEs y Window Functions (OVER / PARTITION BY)
-- =======================================================================

-- 1. Creamos una tabla virtual (CTE) para aislar el cálculo del promedio departamental
WITH EmpleadosConPromedios AS(
  SELECT 
      nombre_empleado, 
      salario,
      AVG(salario) OVER (PARTITION BY departamento) AS promedio_depto
  FROM empleados
)

-- 2. Consultamos la CTE y aplicamos el filtro matemático
SELECT
    nombre_empleado,
    salario
FROM EmpleadosConPromedios
WHERE salario > promedio_depto;
