#Configuration
Basic configuration required for Databuddy 0.3.3 to run properly.
- modify default host_map.py: ![host_map.py](https://raw.githubusercontent.com/data-buddy/DataBuddy/master/screenshots/edit_hostmap.png "Edit host_map.py")

> You can click pop-up menu item or open `..\qc32\config\host_map2.py ` (relative to Databuddy 0.3.3 home)

- set your 'source' and 'target' dirs for local clients for each database.

##Configuration for Oracle
```
 'host_list': {0: {'db_env': {'ORA11G': {'source': 'C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN',
                                         'target': 'C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN'},
```
Set your __'source'__ and __'target'__ to actual locations of `sqlplus.exe` and `sqlldr.exe` in your system.
'source' is source Oracle client home
'target' is target Oracle client Home
Most often they will point to the same location, but, it you use Oracle versions with incompatible clients or 2 clients with different tnsnames.ora file you can set it here.

##Configuration for MongDB
```python
 'host_list': {0: {'db_env': {'MONGO': {'source': r'C:\Program Files\MongoDB\Server\3.0\bin',
                                         'target': r'C:\Program Files\MongoDB\Server\3.0\bin'},
```
Set your __'source'__ and __'target'__ to actual locations of `mongo.exe`, `mongoexport.exe`, and `mongoimport.exe` in your system.
Most probable they will point to the same location. Just giving an option here in case you want to draw the line between 2 local installs of MongoDB client.



