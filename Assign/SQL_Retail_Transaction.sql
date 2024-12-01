SELECT * FROM Retail_Transactions
--Tạo 1 cột mới khi tách []
ALTER TABLE Retail_Transactions
	ADD Product2 NVARCHAR(MAX)

--Tạo bảng Test

SELECT * INTO Retail_Transactions_Test
FROM Retail_Transactions

--Cập nhật lại cột Product2
UPDATE RTT
	SET RTT.Product2 = (	SELECT SUBSTRING(Product, 2, LEN(Product)-2) 
							FROM Retail_Transactions_Test
							WHERE RTT.Transaction_ID = Retail_Transactions_Test.Transaction_ID)
FROM Retail_Transactions_Test RTT

--Add column
DECLARE @Product NVARCHAR(MAX);
DECLARE @query NVARCHAR(MAX);

DECLARE Add_Column CURSOR FOR
SELECT DISTINCT SUBSTRING(TRIM(s.value), 2, LEN(TRIM(s.value)) - 2) AS Product
FROM Retail_Transactions_Test t
CROSS APPLY STRING_SPLIT(t.Product2, ',') s;

OPEN Add_Column;

FETCH NEXT FROM Add_Column INTO @Product;

WHILE @@FETCH_STATUS = 0
BEGIN
    SET @query = 'ALTER TABLE Retail_Transactions_Test ADD [' + @Product + '] BIT;';
    EXEC sp_executesql @query;

    FETCH NEXT FROM Add_Column INTO @Product;
END;

CLOSE Add_Column;
DEALLOCATE Add_Column;

SELECT * FROM Retail_Transactions_Test ORDER BY Transaction_ID ASC

--SELECT ID và Product sau tách
SELECT Transaction_ID, SUBSTRING(TRIM(s.value), 2, LEN(TRIM(s.value)) - 2) AS Product
FROM Retail_Transactions_Test t
CROSS APPLY STRING_SPLIT(t.Product2, ',') s
ORDER BY Transaction_ID ASC


--Add data

DECLARE @SQL NVARCHAR(MAX);
DECLARE @query NVARCHAR(MAX);
DECLARE @column_name NVARCHAR(MAX);

DECLARE Add_Data CURSOR FOR
SELECT COLUMN_NAME
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'Retail_Transactions_Test'
AND ORDINAL_POSITION BETWEEN 15 AND 95;

OPEN Add_Data;

FETCH NEXT FROM Add_Data INTO @column_name;

WHILE @@FETCH_STATUS = 0
BEGIN
    SET @query = '
        UPDATE RTT
        SET RTT.[' + @column_name + '] = 
            CASE 
                WHEN EXISTS (
                    SELECT 1 
                    FROM (
                        SELECT Transaction_ID, SUBSTRING(TRIM(s.value), 2, LEN(TRIM(s.value)) - 2) AS Product
                        FROM Retail_Transactions_Test t
                        CROSS APPLY STRING_SPLIT(t.Product2, '','')
                    ) AS SplitData
                    WHERE SplitData.Product = ''' + @column_name + ''' 
                          AND SplitData.Transaction_ID = RTT.Transaction_ID
                ) THEN 1
                ELSE 0
            END
        FROM Retail_Transactions_Test RTT;';

    EXEC sp_executesql @query;

    FETCH NEXT FROM Add_Data INTO @column_name;
END;

CLOSE Add_Data;
DEALLOCATE Add_Data;



SELECT * FROM Retail_Transactions_Test ORDER BY Transaction_ID ASC

--Cau2
ALTER TABLE Retail_Transactions_Test 
ADD Details NVARCHAR(MAX);

DECLARE @SQL NVARCHAR(MAX) = '';

-- Lấy danh sách các cột từ vị trí 5 đến 11
SELECT @SQL = @SQL + '[' + COLUMN_NAME + '], '
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'Retail_Transactions_Test'
AND ORDINAL_POSITION BETWEEN 5 AND 11;

-- Loại bỏ dấu phẩy cuối cùng
SET @SQL = 'SELECT ' + LEFT(@SQL, LEN(@SQL) - 1) + ' FROM Retail_Transactions_Test;';

-- Thực thi câu lệnh SELECT động
EXEC sp_executesql @SQL;



