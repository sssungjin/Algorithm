-- 코드를 입력하세요
SELECT b.TITLE, b.BOARD_ID, r.REPLY_ID, r.WRITER_ID, r.CONTENTS, DATE_FORMAT(r.CREATED_DATE, '%Y-%m-%d') AS CREATED_DATE
from used_goods_board as b
join used_goods_reply as r
on r.board_id = b.board_id
where YEAR(b.CREATED_DATE) = 2022 and MONTH(b.CREATED_DATE) = 10
order by r.created_date, b.title;