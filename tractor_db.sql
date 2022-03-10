use tractor;

select sum(quantity)
from hist_data;

select sales_team.emp_id, sum(quantity) AS team_quantity_total
from sales_team
join hist_data
	ON sales_team.emp_id = hist_data.emp_id
		group by emp_id;


SELECT hist_data.emp_id, sale_week_date,quantity,
	CASE
    WHEN hist_data.sale_year = 2019 THEN price_19Q1*quantity
    WHEN hist_data.sale_year = 2020 THEN price_20Q1*quantity
END AS total_sales
FROM hist_data
JOIN date_dim
	ON hist_data.sale_week = date_dim.sale_week
JOIN product;
select* from hist_data;

select hist_data.emp_id,quantity,hist_data.sale_week,sale_year
from hist_data;