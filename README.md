# RoboCrop

* https://github.com/agschwender/pilbox

## Local Testing

Create local `.env`:

```
DEBUG=yes
CLIENT_NAME=test
CLIENT_KEY=testkey
```

```
pip install -r requirements.txt
heroku local
open http://localhost:5000/?url=...&w=100
```

## Deployment

```
heroku config:set DEBUG=no CLIENT_NAME=... CLIENT_KEY=...
git push heroku master
```
