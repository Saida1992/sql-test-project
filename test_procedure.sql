CREATE PROCEDURE GetEmployeeDetails 
    @EmployeeId INT
AS
BEGIN
    -- Sadə SQL sorğusu test üçün for coderabbit
    SELECT * FROM Employees WHERE Id = @EmployeeId;
END
    --for test
    ;
