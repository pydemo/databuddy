echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\qc32\qc32.exe ^
-w "csv2ora11g" ^
-t "|" ^
-r 1 ^
-o 1 ^
-i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
-y 1000 ^
-e "YYYY-MM-DD HH24.MI.SS" ^
-m "YYYY-MM-DD HH24.MI.SS.FF2" ^
-O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
-Z C:\app\alex_buz\product\11.2.0\dbhome_2\BIN ^
-d orcl ^
-p tiger2 ^
-a SCOTT.Timestamp_test_to ^
-u SCOTT ^
-X 1

