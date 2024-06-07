# Local test
```
export FLASK_APP=main.py
flask run --reload --debugger
```


# Deploy
- Authenticate to Google using the SDK CLI
```
gcloud auth login
```

- Set the project
```
gcloud config set project my-web-page-290122
```

- Deploy the app 
```
gcloud app deploy
```