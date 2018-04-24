select ID,
TITLE,
ISIN,
COUNTRY,
DESCRIPTION,
SECURITYTYPE,
TO_CHAR(CREATED,'YYYY-MM-DD HH24.MI.SS.FF2') created, to_char(created, 'TZH:TZM') timezone from Timezone_test_from t;


