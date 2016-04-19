BULK INSERT dbo.Persons_pipe2
FROM 'C:\Python27\ora_data_pipe\logs\20140902_154523\shard_0.data'
WITH
  (	
    DATAFILETYPE = 'char',
    FIELDTERMINATOR = '|',
    ROWTERMINATOR = '\n'
  );
 