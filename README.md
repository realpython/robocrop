# RoboCrop

* https://github.com/agschwender/pilbox

## Local Testing

Create local `.env`:

```
DEBUG=yes
CLIENT_KEY=testkey
WEB_CONCURRENCY=2
```

```
pip install -r requirements.txt
heroku local
open http://localhost:5000/?url=...&w=100
```

## Deployment

```
heroku config:set DEBUG=no CLIENT_KEY=...
git push heroku master
```
