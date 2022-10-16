# Price prediction of a house
This is a project which helps in predicting the house price on the basis of parameters given. The project basically consists of a model which is been trained on a dataset of housing prediction to predict the price. This also contains logs , pretained models, artifacts directories and config file to maintain the scalability. The user is only supposed to give few details in a form such as Total Bedrooms, Total rooms, Households etc to predict the overall price. 

## Software and account requirements:

1. [Github Account] (https://github.com/)
2. [Heroku Account] (https://id.heroku.com/login)
3. [Git cli] (https://git-scm.com/download/win)
4. [VS Code IDE] (https://code.visualstudio.com/download)

## Steps to be followed: 

Creating conda environment
```
conda create -p venv python==3.7 -y
```
```
conda acitvate venv/
```
OR
```
conda activate venv
```
```
Install Flask
pip install -r requirements.txt
```

To add files in git
```
git add .
```
To add file in git
```
git add <filename>
```

Note :- To ignore file or folder from git we can write file/folder name in .gitignore file.

To check status of git
```
git status
```

To check the logs of git
```
git log
```
To commit/version the file in git
```
git commit -m "<message>"
```
To send version/changes to github
```
git push origin main
```
To setup CI/CD pipeline in heroku we need 3 information

HEROKU_EMAIL = "Herokuemailid"
HEROKU_API_KEY = "Herokuapikey"
HEROKU_APP_NAME = "Herokuappname"

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```

Note: Image name for docker must be lowercase

To list docker image
```
docker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 f8c749e73678
```

To check running container in docker
```
docker ps
```

To stop docker conatiner
```
docker stop <container_id>
```

Install kernel for VS Code
```
pip install ipykernel
```

## Project in Brief:

This Project is divided into 6 parts or categories. 
1. Data Ingestion - Collecting the data from a url , extracting and creating separate train and test data.

2. Data Validation - Validating the data such as file exists or not , checking column values , checking data drift , creating a report and saving report.

3. Data Transformation - Transforming the data with correct shape and size for a model.

4. Model Trainer - Training of model on the above data with creating a class of model factory which includes GridSearchCV , Regression as algorithms and picking out any one of them as a best model.

5. Model Evaluator - Evaluating the trained model with Metrics and accuracy score such RMSE, MSE on the basis of best model obtained from model trainer and comparing it with the old trained model for better observation if its present. 

6. Model Pusher - Exporting the model and Pushing the new trained model with better accuracy to the deployment via flask app.

![img](https://raw.githubusercontent.com/rajashekarnagalikar/machine_learning_project/main/Study/project.png)

Deployed Platform:-
![url](https://ml-regression-project.herokuapp.com/predict)

## Key Points :

Data Drift:
When your dataset stats gets change we call it as data drift.Basically while comparing two datasets if the dataset stats differs or change then it is refered.
