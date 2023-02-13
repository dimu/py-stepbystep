import pyspark.pandas
from pyspark import SparkConf,SparkContext
from pyspark.streaming import StreamingContext

if __name__ == '__main__':
    SparkContext()
    textfile = pyspark.pandas.read_json("person.json")
    print(textfile.count)