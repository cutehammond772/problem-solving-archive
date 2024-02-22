WITH 
    SKILLS AS (
        SELECT a.ID, b.NAME, b.CATEGORY
        FROM 
            DEVELOPERS a INNER JOIN SKILLCODES b
            ON (a.SKILL_CODE & b.CODE) > 0
    ),
    FRONTEND_DEV AS (
        SELECT DISTINCT ID
        FROM SKILLS
        WHERE CATEGORY = "Front End"
    ),
    PYTHON_DEV AS (
        SELECT DISTINCT ID
        FROM SKILLS
        WHERE NAME = "Python"
    ),
    GRADE_A AS (
        SELECT DISTINCT a.ID
        FROM FRONTEND_DEV a, PYTHON_DEV b
        WHERE a.ID = b.ID
    ),
    GRADE_B AS (
        SELECT DISTINCT ID
        FROM SKILLS
        WHERE 
            NAME = "C#" 
            AND ID NOT IN (SELECT * FROM GRADE_A)
    ),
    GRADE_C AS (
        SELECT ID
        FROM FRONTEND_DEV
        WHERE ID NOT IN (
            SELECT ID FROM GRADE_A 
            UNION
            SELECT ID FROM GRADE_B
        )
    ),
    ABC_DEVELOPERS AS (
        SELECT "A" AS GRADE, a.ID
        FROM GRADE_A a
        UNION ALL
        SELECT "B" AS GRADE, b.ID
        FROM GRADE_B b
        UNION ALL
        SELECT "C" AS GRADE, c.ID
        FROM GRADE_C c
    )
SELECT a.GRADE, a.ID, b.EMAIL
FROM ABC_DEVELOPERS a, DEVELOPERS b
WHERE a.ID = b.ID
ORDER BY a.GRADE, a.ID;