select ID,
TITLE,
ISIN,
COUNTRY,
DESCRIPTION,
SECURITYTYPE,
TO_CHAR(CREATED,'YYYY-MM-DD-HH24.MI.SS.FF') created, to_number(to_char(created, 'TZHTZM'))*100.00 timezone from Timezone_test_from t;


