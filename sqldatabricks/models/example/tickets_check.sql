
-- Use the `ref` function to select from other models
with tickets_list as (
select *, dense_rank() over (order by file_key) as row_id
from {{ ref('tickets_list') }}
),

tickets_total as (
select *, dense_rank() over (order by file_key) as row_id
from {{ ref('tickets_total') }}
)



select 
 tot.transaction_date
,lis.product_name
,lis.price
,SUM(lis.price) OVER (PARTITION BY lis.row_id ORDER BY lis.row_id) as total_amount_due_by_price
,tot.total_amount_due AS total_amount_due_by_ticket

from tickets_list AS lis
left join tickets_total AS tot ON 
lis.row_id = tot.row_id
GROUP BY
 tot.transaction_date
,lis.product_name
,lis.price
,lis.row_id
,tot.total_amount_due

