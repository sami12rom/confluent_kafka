-- Create a new Stream from a newly created kafka topic

DEFINE topic_name = 'akas';
CREATE STREAM ${topic_name} (id INTEGER KEY, titleId STRING, ordering STRING, title STRING, region STRING, language STRING, types STRING, attributes STRING, isOriginalTitle STRING) 
WITH (kafka_topic='${topic_name}', value_format='JSON');

DEFINE topic_name = 'title_basics';
CREATE STREAM ${topic_name}  (id INTEGER KEY, tconst STRING, titleType STRING, primaryTitle STRING, originalTitle STRING, isAdult STRING, startYear STRING, endYear STRING, runtimeMinutes STRING, genres STRING) 
WITH (kafka_topic='${topic_name}', value_format='JSON');

DEFINE topic_name = 'crew';
CREATE STREAM ${topic_name}  (id INTEGER KEY, tconst STRING, directors STRING, writers STRING) 
WITH (kafka_topic='${topic_name}', value_format='JSON');

DEFINE topic_name = 'ratings';
CREATE STREAM ${topic_name}  (id INTEGER KEY, tconst STRING, averageRating STRING, numVotes STRING) 
WITH (kafka_topic='${topic_name}', value_format='JSON');

DEFINE topic_name = 'episode';
CREATE STREAM ${topic_name}  (id INTEGER KEY, tconst STRING, parentTconst STRING, seasonNumber STRING, episodeNumber STRING) 
WITH (kafka_topic='${topic_name}', value_format='JSON');

DEFINE topic_name = 'principals';
CREATE STREAM ${topic_name}  (id INTEGER KEY, tconst STRING, ordering STRING, nconst STRING, category STRING, job STRING, characters STRING) 
WITH (kafka_topic='${topic_name}', value_format='JSON');


-- Join two streams together
CREATE STREAM COMBINED AS
  SELECT akas.titleId,akas.ordering,akas.title,akas.region,akas.language,akas.types,akas.attributes,akas.isOriginalTitle,EPISODE.episodeNumber, EPISODE.seasonNumber
  FROM akas
  JOIN EPISODE WITHIN 1 MINUTES
  ON akas.titleId = EPISODE.tconst EMIT CHANGES;



-- Join two streams together
CREATE STREAM s3 AS
  SELECT akas.titleId,akas.ordering,akas.titleId,akas.title,akas.region,akas.language,akas.types,akas.attributes,akas.isOriginalTitle,title_basics.originalTitle, title_basics.isAdult,title_basics.startYear, title_basics.endYear
  FROM akas
  JOIN title_basics WITHIN 5 MINUTES
  ON akas.titleId = title_basics.tconst EMIT CHANGES;



--SELECT statement to get all users from the users Stream that are under 65. This will print the results of the query in the message viewer below.
SELECT id, gender, name, age FROM users WHERE age<65 EMIT CHANGES;

--insert data into your newly created users topic.
INSERT INTO users (id, gender, name, age) VALUES (0, 'female', 'sarah', 42);
INSERT INTO users (id, gender, name, age) VALUES (1, 'male', 'john', 28);
INSERT INTO users (id, gender, name, age) VALUES (42, 'female', 'jessica', 70);

--SELECT statement to get all users from the users Stream that are under 65. This will print the results of the query in the message viewer below.
SELECT id, gender, name, age FROM users WHERE age<65 EMIT CHANGES;

--make the previous query a Persistent Query so that it continuously writes the results to a new topic.
CREATE STREAM users_filtered AS SELECT id, gender, name, age FROM users WHERE age<65;



CREATE TABLE t1 (c1 VARCHAR PRIMARY KEY, c2 INTEGER)
WITH (kafka_topic='t1', value_format='json');


-- Join two streams together
CREATE STREAM s3 AS
  SELECT s1.c1, s2.c2
  FROM s1
  JOIN s2 WITHIN 5 MINUTES
  ON s1.c1 = s2.c1 EMIT CHANGES;

-- Join a stream and a table together
CREATE STREAM s3 AS
  SELECT my_stream.c1, my_table.c2
  FROM my_stream
  JOIN my_table
  ON s1.c1 = s2.c1 EMIT CHANGES;


