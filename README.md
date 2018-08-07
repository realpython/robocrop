# RoboCrop

## Local Testing

```
pip install -r requirements.txt
heroku local
open http://localhost:5000/?url=...&w=100
```

## Deployment

```
heroku config:set DEBUG=no
git push heroku master
```
