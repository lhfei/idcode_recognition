### Prepared


```shell
sudo yum install python3-devel mysql-devel
```



#### Create DB

```SQL
CREATE DATABASE idcode_recognition
  DEFAULT CHARACTER SET utf8
  DEFAULT COLLATE utf8_general_ci;

CREATE USER 'ocr_user'@'localhost' IDENTIFIED BY 'Ocruser_1473';
CREATE USER 'ocr_user'@'%' IDENTIFIED BY 'Ocruser_1473';

# for MySQL 8 before
GRANT ALL ON idcode_recognition.* TO 'ocr_user'@'%' IDENTIFIED BY 'Ocruser_1473';

# for MySQL 8 and later
GRANT ALL ON idcode_recognition.* TO "ocr_user"@"localhost" WITH GRANT OPTION;
GRANT ALL ON idcode_recognition.* TO "ocr_user"@"%"  WITH GRANT OPTION;

FLUSH PRIVILEGES;
```





### Create Super user

```shell
python manage.py createsuperuser
Username (leave blank to use 'lhfei'):admin
Email address: *******
Password:[Lhfeilaile01]
Password (again):[Lhfeilaile01]
Superuser created successfully.
```

### Create tables

```shell
python manage.py makemigrations js_app

python manage.py migrate
```



### Create Sessions

```shell
python manage.py migrate sessions
```



### Start

```python
python manage.py runserver
```

