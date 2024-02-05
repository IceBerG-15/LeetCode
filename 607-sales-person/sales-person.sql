/* Write your PL/SQL query statement below */
select name from salesperson 
where sales_id not in 
(select s.sales_id from salesperson s join orders o
on s.sales_id = o.sales_id join company c
on c.com_id = o.com_id
where c.name='RED');

