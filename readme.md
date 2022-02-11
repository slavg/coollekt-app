# Coollekt

Coollekt is the platform to create and share personal collections, being music, comics, movies, or any other collectibles.
Coollektors can build, share or sell their collections as well as follow, like or comment on other coollektors and purchase their items.
Collections can be private, open only for registered users, and the public that is open for both registered and non-registered users.
In order to be able to follow collections or coolektors, like, comment, or purchase their items, you must be registered user.


## Run it with docker-compose


```
git clone
cd coollekt-project
docker-compose build 
docker-compose up -d 
```

<br/>

Check that is running in local:
```
http://127.0.0.1:8000/
```

<br/>

Check API Schema at:
```
http://127.0.0.1:8000/api/schema/redoc/
http://127.0.0.1:8000/api/schema/swagger-ui/
```

<br/>

Linter/Formatter
```
black coollekt
flake8 coollekt
```

<br/>

Run Tests and Coverage
```
pytest
```

<br/><br/>
Any comment or question: slavko@glisic.com
