
# coding: utf-8

# In[ ]:

# example of spark stream
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext, StreamingListener

# initialize spark config
conf = SparkConf().setMaster('local[*]').setAppName('TweetCount')
# initialize spark context
sc = SparkContext(conf = conf)
# initialize sparkcontext object with batchDuration 60 seconds
ssc = StreamingContext(sparkContext = sc, batchDuration = 10)
# initialize DStream(textFileStream) for streaming
lines = ssc.socketTextStream('localhost',6666)

# Some work with DStream
# Split each line into words
# words = lines.flatMap(lambda line: line.split(" "))
# Count each word in each batch
# pairs = words.map(lambda word: (word, 1))
pairs = lines.map(lambda line: (line, 1))
wordCounts = pairs.reduceByKey(lambda x, y: x + y)
# Print the first ten elements of each RDD generated in this DStream to the console
wordCounts.pprint()

ssc.start()             # Start the computation
ssc.awaitTermination()  # Wait for the computation to terminate


# In[ ]:

from pymongo import MongoClient

client = MongoClient('localhost', 32801)
db = client['twitter']
collection = db['country']
country_count = {
                    'country': country_name,
                    'count': number
}
collection.insert_one(country_count).inserted_id

