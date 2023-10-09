# Blog Posts Project
### An app that can create blogs. The main purpose to create this app to practice flask skills and make the source code available online for other developers to start this repo for their own custom need

<!-- ![Alt home page](md_images/01.png "Home Page")
![Alt reg page](md_images/02.png "Registeration Page")
![Alt login page](md_images/03.png "Login Page | in chinese")
![Alt create a post](md_images/04.png "Create a Post")
![Alt list page](md_images/05.png "List the Post") -->

## Setup (Recommended)
1. install anaconda
2. create an environment using
``` conda create -n "flask-blog-posts" python=3.10```
3. run ```conda activate flask-blog-posts```
4. run ```pip install -r requirements.txt```
5. flask run


## Deployment
1. Please refer to [https://flask.lyskills.com](https://flask.lyskills.com) for website reference
2. Do not work to create .env and instance/db.sqlite3 file and change permission
```
chown root .env
chown root instance/db.sqlite3
```
2. All deployment is made using ```gunicorn & nginx```. You may refer to [this](https://github.com/NoumanAhmad448/django-blog-posts/blob/master/deployment.md)

## Commands
### Langauges
```
pybabel extract -F flask-babel.cfg -o messages.pot .
pybabel init -i messages.pot -d translations -l zh
pybabel compile -d translations
```
```
pybabel update -i messages.pot -d translations
```

### migrations
```
flask db migrate -m "Initial migration."
```
```
flask db upgrade
```

```
flask db revision --rev-id 215a43277d61
```

## minify css and js
```
css-html-js-minify.py static/
```