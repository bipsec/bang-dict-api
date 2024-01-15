## Table of Contents
Here in this repo, a digitization of the Bengali Dictionary [Riddhi] is presented.

### Project Structure

```sh
bang-dict-api/
├── app/
│   ├── api/
│   │  ├──__init__.py
│   │  ├──dictionary.py
│   │  ├──ipa.py
│   │  ├──load_data.py
│   │  ├──load_audio.py
│   ├── events/
│   │   ├── __init__.py
│   │   └── startup_shutdown.py
│   ├── model/
│   │   ├── ipa_model.pth
│   ├── db/
│   │   ├── __init__.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── schemas.py
│   ├── data/
│   │   ├── __init__.py
│   │   ├── bangla_dictionary.csv
│   │   ├── bangla_dictionary_updated.csv
│   │   ├── sushmitIPAData.csv
│   │   ├── word_ipa.csv
│   ├── scripts/
│   │   ├── audio.py
│   │   ├── avro_testing.py
│   │   ├── ipa_converter.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── ...
│   ├── main.py
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── README.md
├── LICENSE
├── run.sh
└── requirements.txt
```


### Up and Run

```sh
git clone https://github.com/bipsec/bang-dict-api.git
cd bang-dict-api
docker-compose up --build
```

### API Checking

```sh
# for single word
http://0.0.0.0:8001/dictionary/words?word=<word>

# for all word in the dictionary
http://0.0.0.0:8001/dictionary/all_words
```
