from pyspark.sql import SparkSession
from pyspark.sql.functions import when


def create_spark_session():
    return (
        SparkSession.builder
        .appName("CustomerSalesETL")
        .master("local[*]")
        .getOrCreate()
    )


def transform_customers(df):
    return df.withColumn(
        "customer_segment",
        when(df.total_spend >= 5000, "HIGH_VALUE")
        .otherwise("STANDARD")
    )


def main():
    spark = create_spark_session()

    df = spark.read.csv(
        "data/customers.csv",
        header=True,
        inferSchema=True
    )

    transformed_df = transform_customers(df)

    transformed_df.show()

    spark.stop()


if __name__ == "__main__":
    main()