SELECT PersonID, LastName, FirstName, Address, City, PersonID2, LastName2, FirstName2, Address2, City2
FROM Persons_pipe_datetime
INTO OUTFILE 'C:\\Python27\\data_mule_mysql\\out_datetime4.csv'
FIELDS ENCLOSED BY '' TERMINATED BY '|' ESCAPED BY ''
LINES TERMINATED BY '\r\n';