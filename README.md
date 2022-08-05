# datasync


```spark-submit driver.py --resource device_7d.yaml --loaddate '2018-01-08';```  

### To build on local and run  
``` python setup.py bdist_egg```  
```spark-submit --py-files file:///Users/rohitkumar/desktop/test-spark-egg/datasync-1.0.0-py3.7.egg driver.py --resource device_7d.yaml  --loaddate 2018-01-08```  

### To run on aws   
```spark-submit --deploy-mode client  --driver-memory 12g --num-executors 80 --executor-cores 4 --executor-memory 12g --conf spark.driver.memoryOverhead=8g --conf spark.executor.memoryOverhead=3g --conf spark.driver.maxResultSize=4g --conf spark.yarn.maxAppAttempts=1 --conf spark.network.timeout=600s --conf spark.rpc.askTimeout=600s --conf spark.executor.heartbeatInterval=240s --conf spark.hadoop.fs.hdfs.impl.disable.cache=true --conf spark.speculation=true --conf spark.speculation.multiplier=1.5  --py-files s3://hulu-proton-airflow-deployment-nonprod/rohit/datasync/config/datasync-1.0.0-py3.7.egg s3://hulu-proton-airflow-deployment-nonprod/rohit/datasync/config/driver.py  --resource device_7d.yaml --loaddate '2022-01-08';```
