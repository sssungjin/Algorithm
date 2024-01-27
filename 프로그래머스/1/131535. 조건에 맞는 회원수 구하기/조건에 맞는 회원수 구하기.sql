-- 코드를 입력하세요
SELECT count(USER_ID) as USERS
from user_info
where YEAR(joined) = 2021
and age between 20 and 29;