## Table of Contents

## Clone Project

```sh
git clone https://github.com/bipsec/bang-dict-api.git
```

## Virtual Env Setup
```python
# Create a virtual env
python3.10 -m venv venv

# activate the venv
source venv/bin/activate
```
```python
pip install -r requirements.txt
```


## Run

```sh
python app.py
```

# API Checking

```sh
# for single word
http://localhost:5000/dictionary/word/?word=<word>

# for the entire dictioanry
http://localhost:5000/dictionary/all_words
```