/* Write your PL/SQL query statement below */
select d.name as Department,e.name as Employee,e.salary as Salary
from Department d join employee e on d.id=e.departmentid
where (e.departmentid,e.salary) in (select departmentid,max(salary) from employee group by departmentid);