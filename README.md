Hostile Podcast Analysis

First we go through all the file paths 
and then we pass it through Kafka

Step Two
We receive the files from Kafka

Now we have several classics that each do one thing.

We have a class that converts audio files to text.

We have another class that loads the content into Mongo.

And we have another class that loads the content into Elastic.


And we have another class that creates an id for each file based on its name and size
and converts the content from audio to text and inserts the text into the dictionary


Now we have a class and inside it there are 2 functions.
One that converts the dangerous words that are encoded in base64 to text,
and the second that gives each word a value.
The more dangerous words have a value of 2
and the less dangerous have a value of 1

Now we have a class that analyzes the text data and checks the value of each text in relation to bds.

There are 2 functions there.

In the first function I give a value to each text 
and calculate the percentages in relation to all the words in the text

And in the second function I divide them all into three parts
1 Low (up to 15)
2 Medium (between 16 and 25)
3 High (above 25)
I calculated it this way because I saw that this is the range of risk levels

And the text is penalized at 25 percent because it is already close to the top third.

And of course we have the manager that runs the second service (from the part we get from Kafka).
