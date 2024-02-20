SELECT
    left(PRODUCT_CODE, 2) as PRODUCT_ID
    , count (PRODUCT_CODE) as PRODUCTS

from PRODUCT 
group by (left(PRODUCT_CODE, 2))
order by PRODUCT_CODE