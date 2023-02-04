# Write your MySQL query statement below
select stock_name, sum(price) as capital_gain_loss
from
(
    select stock_name, operation_day, IF(operation = 'Buy', -price, price) as price
    from `Stocks`
    order by stock_name, operation_day
) master
group by master.stock_name