import pytest
from pyspark.sql import SparkSession


@pytest.fixture
def spark():
    spark = (
        SparkSession.builder
        .appName("CustomerETLTests")
        .master("local[2]")
        .getOrCreate()
    )

    yield spark

    spark.stop()