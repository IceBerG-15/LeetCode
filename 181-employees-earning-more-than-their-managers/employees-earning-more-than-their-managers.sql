/* Write your PL/SQL query statement below */
select emp.name as Employee from employee emp join employee mgr on emp.managerId=mgr.id
where emp.salary>mgr.salary;