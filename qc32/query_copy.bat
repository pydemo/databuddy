REM From ORA_Query to ORA
echo y|query_copy.exe ^
-w ora2ora ^
-o 1 ^
-r 1 ^
-t "|" ^
-q C:\Python27.2.5\data_mule_ora_full_rel_citi\oracle_citi_query.sql ^
-f AD45676/Sep2014@SMARTC1B ^
-e "YYYY-MM-DD HH24.MI.SS" ^
-m "YYYY-MM-DD HH24.MI.SS.FF" ^
-z "C:\ORACLE\product\11.1.0\client_1\BIN" ^
-g CSMARTOTD/sl14Hm@SMARTD1 ^
-a CSMARTOTD.OTD_VOL_FX ^
-e "YYYY-MM-DD HH24.MI.SS" ^
-m "YYYY-MM-DD HH24.MI.SS.FF" ^
-Z "C:\ORACLE\product\11.1.0\client_1\BIN"