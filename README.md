## Table of Contents


### Project Structure

```sh
bang-dict-api/
├── app/
│   ├── celery/
│   │  ├──__init__.py
│   │  ├──app.py
│   │  ├──worker.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
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