CONNECT to 'test@ol_s_101014_181102' user  informix USING infor_pwd;
UNLOAD TO "C:\\Python27\\data_mule_informix\\logs\\20141011_215455\\shard_0.data" DELIMITER '|' SELECT * FROM PERSONS_PIPE_DATETIME_1;
