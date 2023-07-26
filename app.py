import os
import csv
import pandas as pd
from flask import Flask, jsonify, request

app = Flask(__name__)

data_file_path = os.path.join("data", "demo_data.csv")
df = pd.read_csv(data_file_path)


# print(df)


if __name__ == '__main__':
    app.run(debug=True)
