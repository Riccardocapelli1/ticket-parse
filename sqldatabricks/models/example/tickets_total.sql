
{{ config(materialized='table') }}

with source_data as (

    select * from hive_metastore.default.lidl_text_info

)

select 
 transaction_date
,total_amount_due
,file_key
from source_data
