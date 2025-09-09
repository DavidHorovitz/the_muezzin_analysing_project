Hostile Podcast Analysis

First we go through all the file paths 
and then we pass it through Kafka

Step Two
We receive the files from Kafka

Now we have several classics that each do one thing.

We have a class that converts audio files to text.

We have another class that loads the content into Mongo.

And we have another class that loads the content into Elastic.


And we have another class that first creates an id for each file based on its name and size
And currently also acts as a manager that does the rest
1 Runs the consumer
2 Converts the audio
(I preferred to put this here immediately in the input so as not to have to update later and then have to change the mapping)
3 Loads to Elastic
4 Loads to Mongo