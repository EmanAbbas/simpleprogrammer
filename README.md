# Simple Programmer

The website is be based on the basic features of https://simpleprogrammer.com/.
it has the following top level menu items:
- Articles
- Videos
- Resources
- About


## Requirements
1. Download Git bash
https://git-scm.com/downloads

2. Get Python3
https://www.python.org/downloads/
- Add python to PATH  (windows)
- get Pip
- download this file and run it using python
https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py
python get-pip.py


## Installation
1. ```git clone https://github.com/ndebuhr/opencamd-dev.git```
2. ```cd .. ```
### Linux ,Mac:
- ```virtualenv -p python3 env```
- ```source env/bin/activate```
### Windows:
```virtualenv -p python3.exe env```
```source env/Scripts/activate```

3. ```cd simpleprogrammer```

4. ```sudo pip install -r requirements.txt```
5. ```python manage.py migrate```
6. ```python manage.py runserver --settings simpleprogrammer.local_settings ```

Ctrl+C to exit environment

### To Run this project on Heroku you should set these environment variables
- **SECRET_KEY:**  Django Hash key
- **WEB_URL:** Website publish url
- **DATABASE_URL:** database connection string(automatically set on heroku)

**- if using S3 bucket for media storage**
- AWS_STORAGE_BUCKET_NAME:
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY


## To view admin site 

```python manage.py createsuperuser```