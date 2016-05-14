
# coding: utf-8

# In[ ]:

# example of spark stream
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext, StreamingListener

# initialize spark config
conf = SparkConf().setMaster('local[*]').setAppName('TweetCount')
# initialize spark context
sc = SparkContext(conf = conf)
# initialize sparkcontext object with batchDuration 10 seconds
ssc = StreamingContext(sparkContext = sc, batchDuration = 10)
# initialize DStream(textFileStream) for streaming
lines = ssc.textFileStream('HDFS/')

# Some work with DStream
# Split each line into words
words = lines.flatMap(lambda line: line.split(" "))
# Count each word in each batch
pairs = words.map(lambda word: (word, 1))
wordCounts = pairs.reduceByKey(lambda x, y: x + y)
# Print the first ten elements of each RDD generated in this DStream to the console
wordCounts.pprint()

ssc.start()             # Start the computation
ssc.awaitTermination()  # Wait for the computation to terminate

