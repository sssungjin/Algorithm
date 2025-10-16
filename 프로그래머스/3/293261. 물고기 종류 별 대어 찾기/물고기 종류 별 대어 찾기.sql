# -- WITH 절을 사용해 순위를 매긴 가상 테이블을 먼저 만듭니다.
# WITH FISH_RANK AS (
#     SELECT
#         FI.ID,
#         FN.FISH_NAME,
#         FI.LENGTH,
#         -- FISH_TYPE 별로 그룹을 나누고, 그 안에서 LENGTH가 긴 순서로 순위를 매깁니다.
#         RANK() OVER (PARTITION BY FI.FISH_TYPE ORDER BY FI.LENGTH DESC) as rnk
#     FROM
#         FISH_INFO FI
#     JOIN
#         FISH_NAME_INFO FN ON FI.FISH_TYPE = FN.FISH_TYPE
# )
# -- 위에서 만든 가상 테이블에서 순위가 1등인 물고기만 조회합니다.
# SELECT
#     ID,
#     FISH_NAME,
#     LENGTH
# FROM
#     FISH_RANK
# WHERE
#     rnk = 1
# ORDER BY
#     ID;


SELECT 
    fi.ID,
    fni.FISH_NAME, 
    fi.LENGTH 
FROM FISH_INFO fi
INNER JOIN FISH_NAME_INFO fni
ON fi.FISH_TYPE = fni.FISH_TYPE
WHERE (fi.FISH_TYPE, fi.LENGTH) IN (SELECT FISH_TYPE, MAX(LENGTH)
                                    FROM FISH_INFO
                                    GROUP BY FISH_TYPE)
ORDER BY 1;