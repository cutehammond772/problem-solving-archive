SELECT COUNT(*) AS FISH_COUNT
FROM FISH_INFO fi
INNER JOIN FISH_NAME_INFO fni ON fi.FISH_TYPE = fni.FISH_TYPE
WHERE fni.FISH_NAME IN ("BASS", "SNAPPER")