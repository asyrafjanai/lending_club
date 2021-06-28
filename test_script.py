import json

import numpy as np
import pandas as pd
import pendulum
import requests


def send_request(file_path):
    # url = 'http://127.0.0.1:5000/predict/'
    url = 'http://localhost:5000/predict'
    files = {'file': open(file_path, 'rb')}

    r = requests.post(url, files=files)
    result = json.loads(r.json()['result'])

    return result

if __name__ == '__main__':
    start = pendulum.now()
    file_to_send = 'ml_2018.csv'
    result = send_request(file_to_send)
    df = pd.read_csv(file_to_send)
    df['loan_prediction'] = result

    # print(df)

    save_path = f'result_{pendulum.now().to_date_string()}.csv'

    df.to_csv(save_path, index=False)
    print(f'[INFO] File saved at {save_path}')

    period = pendulum.now() - start

    print(f'[INFO] Time take: {period.in_words()}')

