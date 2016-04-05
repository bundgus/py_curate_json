CREATE EXTERNAL TABLE mlb_udf_parq_test
LIKE PARQUET '/user/sg217516/ecommerce_checkin/transformed_json_logs/businessRecord.parq/part-m-00000.parquet'
  STORED AS PARQUET
  LOCATION '/user/sg217516/ecommerce_checkin/transformed_json_logs/businessRecord.parq';
