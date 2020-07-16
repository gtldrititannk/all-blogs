# All-Blogs

  It is the Micro Blog Web Application implemented in Django Framework.


## All-Blogs Installation steps

1:- Repository Clone

```
git clone https://github.com/gtldrititannk/all-blogs.git
```

2:- Creating Virtual Environment
 
 > Note:- Virtual Environment is  never committed in Version Control.

```
virtualenv -p python3.6 venv_all_blogs
```

- Activate The Virtual Environment

```
source venv_ride_sharing/bin/activate 
```

3:-  Install dependencies from requirements.txt File.

```
pip install -r requirements.txt
```

4:- Create local.py file 

```
cp all_blogs/all_blogs/settings/example-production.py all_blogs/all_blogs//settings/local.py
```

5:- Run migrations

> Note:- manage.py file is located in project root folder

```
python manage.py makemigrations
python manage.py migrate
```

6:- Run the project
```
python manage.py runserver
```


