# Confluent Kafka

## Linkedin
<a href="https://www.linkedin.com/in/sami-alashabi/" target="_blank"><img src="https://raw.githubusercontent.com/nakulbhati/nakulbhati/master/contain/in.png" alt="LinkedIn" width="30"></a>


## Introduction

Create Confluent Kafka Producer & Consumer with Python.

For more info:
* https://www.confluent.io/
* https://confluent.cloud/

Link to Dataset: https://datasets.imdbws.com/

## Producers
cd /home/github/confluent_kafka/
/root/.local/share/virtualenvs/confluent_kafka-uEDxVY-e/bin/python producer_python.py -f "data/json/title_akas_tsv_gz.json"
/root/.local/share/virtualenvs/confluent_kafka-uEDxVY-e/bin/python producer_python.py -f "data/json/title_basics_tsv_gz.json"
/root/.local/share/virtualenvs/confluent_kafka-uEDxVY-e/bin/python producer_python.py -f "data/json/title_crew_tsv_gz.json"
/root/.local/share/virtualenvs/confluent_kafka-uEDxVY-e/bin/python producer_python.py -f "data/json/title_episode_tsv_gz.json"
/root/.local/share/virtualenvs/confluent_kafka-uEDxVY-e/bin/python producer_python.py -f "data/json/title_principals_tsv_gz.json"
/root/.local/share/virtualenvs/confluent_kafka-uEDxVY-e/bin/python producer_python.py -f "data/json/title_ratings_tsv_gz.json"
/root/.local/share/virtualenvs/confluent_kafka-uEDxVY-e/bin/python producer_python.py -f "data/json/name_basics_tsv_gz.json"

## Consumers
cd /home/github/confluent_kafka/
/root/.local/share/virtualenvs/confluent_kafka-uEDxVY-e/bin/python consumer.py -f python.config -t title_akas_tsv_gz
/root/.local/share/virtualenvs/confluent_kafka-uEDxVY-e/bin/python consumer.py -f python.config -t title_basics_tsv_gz
/root/.local/share/virtualenvs/confluent_kafka-uEDxVY-e/bin/python consumer.py -f python.config -t title_crew_tsv_gz
/root/.local/share/virtualenvs/confluent_kafka-uEDxVY-e/bin/python consumer.py -f python.config -t title_ratings_tsv_gz


## Dataset Information

IMDb Dataset Details

Each dataset is contained in a gzipped, tab-separated-values (TSV) formatted file in the UTF-8 character set. The first line in each file contains headers that describe what is in each column. A ???\N??? is used to denote that a particular field is missing or null for that title/name. The available datasets are as follows:

title.akas.tsv.gz - Contains the following information for titles:
titleId (string) - a tconst, an alphanumeric unique identifier of the title
ordering (integer) ??? a number to uniquely identify rows for a given titleId
title (string) ??? the localized title
region (string) - the region for this version of the title
language (string) - the language of the title
types (array) - Enumerated set of attributes for this alternative title. One or more of the following: "alternative", "dvd", "festival", "tv", "video", "working", "original", "imdbDisplay". New values may be added in the future without warning
attributes (array) - Additional terms to describe this alternative title, not enumerated
isOriginalTitle (boolean) ??? 0: not original title; 1: original title

title.basics.tsv.gz - Contains the following information for titles:
tconst (string) - alphanumeric unique identifier of the title
titleType (string) ??? the type/format of the title (e.g. movie, short, tvseries, tvepisode, video, etc)
primaryTitle (string) ??? the more popular title / the title used by the filmmakers on promotional materials at the point of release
originalTitle (string) - original title, in the original language
isAdult (boolean) - 0: non-adult title; 1: adult title
startYear (YYYY) ??? represents the release year of a title. In the case of TV Series, it is the series start year
endYear (YYYY) ??? TV Series end year. ???\N??? for all other title types
runtimeMinutes ??? primary runtime of the title, in minutes
genres (string array) ??? includes up to three genres associated with the title

title.crew.tsv.gz ??? Contains the director and writer information for all the titles in IMDb. Fields include:
tconst (string) - alphanumeric unique identifier of the title
directors (array of nconsts) - director(s) of the given title
writers (array of nconsts) ??? writer(s) of the given title

title.episode.tsv.gz ??? Contains the tv episode information. Fields include:
tconst (string) - alphanumeric identifier of episode
parentTconst (string) - alphanumeric identifier of the parent TV Series
seasonNumber (integer) ??? season number the episode belongs to
episodeNumber (integer) ??? episode number of the tconst in the TV series

title.principals.tsv.gz ??? Contains the principal cast/crew for titles:
tconst (string) - alphanumeric unique identifier of the title
ordering (integer) ??? a number to uniquely identify rows for a given titleId
nconst (string) - alphanumeric unique identifier of the name/person
category (string) - the category of job that person was in
job (string) - the specific job title if applicable, else '\N'
characters (string) - the name of the character played if applicable, else '\N'

title.ratings.tsv.gz ??? Contains the IMDb rating and votes information for titles:
tconst (string) - alphanumeric unique identifier of the title
averageRating ??? weighted average of all the individual user ratings
numVotes - number of votes the title has received

name.basics.tsv.gz ??? Contains the following information for names:
nconst (string) - alphanumeric unique identifier of the name/person
primaryName (string)??? name by which the person is most often credited
birthYear ??? in YYYY format
deathYear ??? in YYYY format if applicable, else '\N'
primaryProfession (array of strings)??? the top-3 professions of the person
knownForTitles (array of tconsts) ??? titles the person is known for
