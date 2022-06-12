# machine_learning_project
This is the first machine learning project

## Software and account requirements:

1. [Github Account] (https://github.com/)
2. [Heroku Account] (https://id.heroku.com/login)
3. [Git cli] (https://git-scm.com/download/win)
4. [VS Code IDE] (https://code.visualstudio.com/download)

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




