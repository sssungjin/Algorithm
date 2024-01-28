-- 코드를 입력하세요
SELECT fh.FLAVOR
from FIRST_HALF as fh
join icecream_info as ii
on ii.flavor = fh.flavor
where fh.TOTAL_ORDER > 3000 and ii.ingredient_type = 'fruit_based'
order by total_order desc;