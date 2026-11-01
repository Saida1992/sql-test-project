CREATE PROCEDURE GetEmployeeDetails 
    @EmployeeId INT
AS
BEGIN
    -- Sadə SQL sorğusu test üçün
    SELECT * FROM Employees WHERE Id = @EmployeeId;
END;
