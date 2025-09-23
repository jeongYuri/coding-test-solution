CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      select DISTINCT salary
      from(select salary, DENSE_RANK() OVER(order by salary desc)as rnk
      from Employee
      ) as t
      where rnk = N

  );
END
