CREATE PROCEDURE TestProcedure
AS
BEGIN
    -- Qəsdən eyni cədvəli CTE içində təkrar istifadə edirik ki, CodeRabbit bunu tutsun
    WITH CTE1 AS (
        SELECT * FROM Employees WHERE DepartmentId = 1
    ),
    CTE2 AS (
        SELECT * FROM Employees WHERE DepartmentId = 1 -- Təkrarsorğu
    )
    SELECT * FROM CTE1 UNION ALL SELECT * FROM CTE2;
END;
