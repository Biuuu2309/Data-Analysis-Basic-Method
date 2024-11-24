-----------------------------------------------------------------------Cleaning Data-------------------------------------------------------------------------------------

--------------------------------------------Kiem tra du lieu 

SELECT * FROM Youtube_Table
ORDER BY Youtube_Table.[index] ASC
--------------------------------------------Kiem tra cac du lieu bi thieu

SELECT * FROM Youtube_Table
WHERE video_id IS NULL OR trending_date IS NULL OR title IS NULL OR channel_title IS NULL 
OR category_id IS NULL OR publish_date IS NULL OR time_frame IS NULL OR published_day_of_week IS NULL
OR publish_country IS NULL OR tags IS NULL OR views IS NULL OR likes IS NULL OR dislikes IS NULL 
OR comment_count IS NULL OR comments_disabled IS NULL OR ratings_disabled IS NULL OR video_error_or_removed IS NULL

--------------------------------------------Chu dong xoa tat ca cac fields 5 gia tri ngoai tru cac fields ID

--Trending date

UPDATE Youtube_Table
	SET trending_date = NULL
	WHERE Youtube_Table.[index] BETWEEN 0 AND 4

--Publish date

UPDATE Youtube_Table
	SET publish_date = NULL
	WHERE Youtube_Table.[index] BETWEEN 5 AND 9

--Time frame

UPDATE Youtube_Table
	SET time_frame = NULL
	WHERE Youtube_Table.[index] BETWEEN 10 AND 14

--Publish day of week

UPDATE Youtube_Table
	SET published_day_of_week = NULL
	WHERE Youtube_Table.[index] BETWEEN 15 AND 19

--Publish country

UPDATE Youtube_Table
	SET publish_country = NULL
	WHERE Youtube_Table.[index] BETWEEN 20 AND 24

--Views

UPDATE Youtube_Table
	SET views = NULL
	WHERE Youtube_Table.[index] BETWEEN 25 AND 29

--Likes

UPDATE Youtube_Table
	SET likes = NULL
	WHERE Youtube_Table.[index] BETWEEN 30 AND 34

--Dislikes

UPDATE Youtube_Table
	SET dislikes = NULL
	WHERE Youtube_Table.[index] BETWEEN 35 AND 39

--Comment count

UPDATE Youtube_Table
	SET comment_count = NULL
	WHERE Youtube_Table.[index] BETWEEN 40 AND 44

--Comments disable

UPDATE Youtube_Table
	SET comments_disabled = NULL
	WHERE Youtube_Table.[index] BETWEEN 45 AND 49

--Ratings disable

UPDATE Youtube_Table
	SET ratings_disabled = NULL
	WHERE Youtube_Table.[index] BETWEEN 50 AND 54

--Video error or removed

UPDATE Youtube_Table
	SET video_error_or_removed = NULL
	WHERE Youtube_Table.[index] BETWEEN 55 AND 59

--Category id

UPDATE Youtube_Table
	SET category_id = NULL
	WHERE Youtube_Table.[index] BETWEEN 60 AND 64

--Tags

UPDATE Youtube_Table
	SET tags = NULL
	WHERE Youtube_Table.[index] BETWEEN 65 AND 69


-------------------------------------------------Dien cac gia tri vao cac fields NULL

--Trending date
SELECT Youtube_Table.[index], 
FROM Youtube_Table








-----------------------------------------------------------------------Cleaning Data-------------------------------------------------------------------------------------