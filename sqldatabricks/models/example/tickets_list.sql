
{{ config(materialized='table') }}

with source_data as (

    select * from hive_metastore.default.lidl_text_products

)

select 
 product_name
,price
,file_key
from source_data
