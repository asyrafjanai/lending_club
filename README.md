## Introduction

This repositories contains machine learning model training process and deployment in flask framework.

1. Model training and data visualization can be found in *data_analysis.ipynb* notebook.
2. Flask deployment can be found in *flask_app* folder.
3. *test_script.py* is the script used to send request to flask server.
4. Package requirements for both flask_app and test_script is located at *flask_app/requirements.txt*


## Getting started

1. Download the dataset from kaggle and extract the files.

1. Open jupyter notebook and run all cells. This will save the model for the flask app later.

2. Create docker image from dockerfile.

    `docker build -t flask_app .`
    
2. Run *flask_app* image in a container.

    `docker run -p 5000:5000 flask_app`

3. In a new terminal, run test script to send file to api. This will use preprocessed 2018 to be uploaded to the flask API. 
    Make sure to install the requirements in requirements.txt first.

    `python test_script.py`

4. The script will upload the whole csv file containing 2018 data to flask API for batch prediction. For this purpose, this is better than sending eachline as separate API call.

5. The test script will then save the prediction result in a new csv file named result_{date}.csv.The last column is the predicted result. We can use this to compare with loan status column in the original data, ml_2018.csv.
