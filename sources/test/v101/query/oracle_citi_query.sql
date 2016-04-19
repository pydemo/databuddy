select *  from csmartotd.otd_vol_fx PARTITION(P20141014) 
 where cob_dt='14-OCT-14' 
   and src_file_cd='FXMLVGB1' 
   and TRD_VOL_FX_MM_SID in (731,7311,7310);


