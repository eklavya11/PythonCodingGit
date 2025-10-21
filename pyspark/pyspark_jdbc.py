# Read from Delta
delta_df = spark.table("sales.customers_delta")

# Optional: apply transformations
transformed_df = delta_df.select("customer_id", "name", "country")

# Define Oracle connection
oracle_url = "jdbc:oracle:thin:@//oracleserver:1521/orclpdb1"
oracle_properties = {
    "user": dbutils.secrets.get("oracle_scope", "user"),
    "password": dbutils.secrets.get("oracle_scope", "password"),
    "driver": "oracle.jdbc.driver.OracleDriver"
}

# Write to Oracle
transformed_df.repartition(4).write \
    .mode("append") \
    .jdbc(oracle_url, "HR.CUSTOMER_DIM", oracle_properties)
