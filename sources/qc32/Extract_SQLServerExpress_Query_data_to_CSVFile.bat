::Extract SQLServerExpress_Query data to CSVFile
echo y|csvextractor32.exe ^
-w ssexp2csv ^
-o 1 ^
-r 1 ^
-t "|" ^
-q C:\Python27\csvextractor_1235\test\v101\query\ss_query.sql ^
-j sa ^
-x test_pwd ^
-b master ^
-n ALEX_BUZ-PC\SQLEXPRESS ^
-z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
-g C:\Python27\csvextractor_1235\CSV_OUT\testSSEXP_Query.data