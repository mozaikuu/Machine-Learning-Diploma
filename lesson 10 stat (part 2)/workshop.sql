DECLARE @Periodic_TypeId INT = 1604,
        @Periodic_FirstDate DATETIME = '2023-01-01',
        @Periodic_Value FLOAT = 400;

CREATE TABLE #TempPeriodicItems (
    p_period VARCHAR(20),
    p_dt DATETIME,
    p_value FLOAT
);

DECLARE @year_ VARCHAR(10);
SET @year_ = YEAR(@Periodic_FirstDate);

DECLARE @QNo INT = 1;
DECLARE @Month INT = 1;
WHILE (@QNo <= 4)
BEGIN
    DECLARE @payDate DATETIME;
    -- why use if else?
    -- IF (@QNo = 1) 
    --     SET @payDate = DATEFROMPARTS(@year_, 1, 1);
    -- ELSE IF (@QNo = 2) 
    --     SET @payDate = DATEFROMPARTS(@year_, 4, 1);
    -- ELSE IF (@QNo = 3) 
    --     SET @payDate = DATEFROMPARTS(@year_, 7, 1);
    -- ELSE 
    --     SET @payDate = DATEFROMPARTS(@year_, 10, 1);

    SET @payDate = DATEFROMPARTS(@year_, @Month, 1);

    -- Insert data into the temporary table
    INSERT INTO #TempPeriodicItems (p_period, p_dt, p_value)
    VALUES (@year_ + '-Q' + CAST(@QNo AS VARCHAR(10)), @payDate, @Periodic_Value);

    SET @QNo = @QNo + 1;
    SET @Month = @Month + 3;
END

SELECT * FROM #TempPeriodicItems;

DROP TABLE #TempPeriodicItems;