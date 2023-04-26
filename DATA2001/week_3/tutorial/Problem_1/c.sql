-- Name the five oldest Australian fuel companies listed.
SET search_path TO NSWFuel;

-- 전세계에서 5번째로 오래된 회사들 (공동 순위 포함)
SELECT * FROM Companies
WHERE founded <= (SELECT MAX(founded) FROM
	(SELECT founded FROM Companies
	ORDER BY founded LIMIT 5) T5);

-- 호주에서 5번째로 오래된 회사들 (top n-query, 공동 무시)
SELECT * FROM Companies
	WHERE hqcountry = 'Australia'
	ORDER BY founded LIMIT 5;