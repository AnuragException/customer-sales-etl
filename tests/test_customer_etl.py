from src.customer_etl import transform_customers


def test_customer_segmentation(spark):
    data = [
        (1, "John", "India", 5000),
        (2, "Bob", "India", 3000),
    ]

    columns = ["customer_id", "name", "country", "total_spend"]

    df = spark.createDataFrame(data, columns)

    result = transform_customers(df)

    rows = result.collect()

    assert rows[0]["customer_segment"] == "HIGH_VALUE"
    assert rows[1]["customer_segment"] == "STANDARD"