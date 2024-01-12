## Table of Contents
Here in this repo, a digitization of the Bengali Dictionary [Riddhi] is presented.

### Project Structure

```sh
bang-dict-api/
├── app/
│   ├── api/
│   │  ├──__init__.py
│   │  ├──dictionary.py
│   ├── events/
│   │   ├── __init__.py
│   │   └── startup_shutdown.py
│   ├── db/
│   │   ├── __init__.py
│   │   ├── database.py
│   ├── data/
│   │   ├── __init__.py
│   │   ├── demo_data.csv
│   ├── services/
│   │   ├── __init__.py
│   │   └── ...
│   ├── main.py
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── README.md
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
http://0.0.0.0:8002/dictionary/words?word=<word>

# for all word in the dictionary
http://0.0.0.0:8002/dictionary/all_words
```
