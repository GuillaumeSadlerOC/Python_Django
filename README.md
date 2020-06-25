<p align="center">
    <img width=100% src="https://github.com/GuillaumeSadlerOC/Python_Django/blob/master/static/github/project-name.png">
</p>

![Python](https://img.shields.io/badge/Python-3.6-blue.svg)
![Django](https://img.shields.io/badge/Django-2.2.5-blue.svg)
![Licence](https://img.shields.io/badge/Licence-GPLv3-blue.svg)
![Status](https://img.shields.io/badge/Status-RefactoringInProgress-orange.svg)
![Version](https://img.shields.io/badge/Version-1-blue.svg)

> Substitute products program with Django and Python.

### DEVICES
![Extrasmall](https://img.shields.io/badge/Extrasmall-<576px-red.svg)
![Small](https://img.shields.io/badge/Small->576px-red.svg)
![Medium](https://img.shields.io/badge/Medium->768px-red.svg)
![Large](https://img.shields.io/badge/Large->992px-red.svg)
![ExtraLarge](https://img.shields.io/badge/ExtraLarge->1200px-green.svg)

### FEATURES
- Coming soon

## REQUIREMENTS
- Python 3.6+
- Django 2.2.5
- more informations to <a href="https://github.com/GRELDAS/Django-substitute-products/blob/master/requirements.txt">requirements.txt</a>

## GETTING STARTED (PRODUCTION)
> Coming soon

## GETTING STARTED (LOCAL)

### **Step 1 - Clone this repository**
- HTTP > Clone this repo to your local machine using `https://github.com/GRELDAS/Django-substitute-products.git`
- SSH  > Clone this repo to your local machine using `git@github.com:GRELDAS/Django-substitute-products.git`

### **Step 2 - Install requirements**
```shell
$ pip install -r requirements.txt
```

### **Step 3 - Database settings**

This application use PostgreSQL but you can use another database, just change settings.

_For postgresql command line : Go to https://gist.github.com/Kartones/dd3ff5ec5ea238d4c546_

- **Admin database connection**
```shell
$ sudo -u postgres psql
```

- **Create app database**
```shell
postgres=# CREATE DATABASE dbname;
```

- **Create an database user**
```shell
postgres=# CREATE USER username WITH PASSWORD 'userpassword';
```

- **Change configurations like Django recommendations
https://docs.djangoproject.com/en/1.11/ref/databases/**

```shell
postgres=# ALTER ROLE username SET client_encoding TO 'utf8';
```
```shell
postgres=# ALTER ROLE username SET default_transaction_isolation TO 'read committed';
```
```shell
postgres=# ALTER ROLE username SET timezone TO 'UTC';
```

- **Grant all privileges to your new user on your database**
```shell
postgres=# GRANT ALL PRIVILEGES ON DATABASE dbname TO username;
```

### **Step 4 - Make Django migrations**

```shell
$ python manage.py migrate
```

### **Step 5 - Run local server**
```shell
$ python manage.py runserver
```

## TESTS
- **For run tests** :
```shell
$ pip python manage.py test
```

## CONFIGURATIONS

### **Internationalization**

Edit <a href="https://github.com/GRELDAS/Django-substitute-products/blob/master/purbeurreV2/settings/common.py">common settings file</a>

- In 'Internationalization' change settings
- For more informations : https://docs.djangoproject.com/en/2.2/topics/i18n/timezones/#timezone
```shell
LANGUAGE_CODE 'en-us' # Change to your settings
TIME_ZONE = 'Europe/Paris' # Change to your settings
```

### Social auth

- Google Authentication
Go to : https://console.developers.google.com/projectselector2/apis/library?supportedpurview=project
and select your project.

## Managments commands

- Import products to database
```shell
$ python manage.py products_import
```

## Product

- <b>name</b> (Char)

Example : Saucisson sec
- <b>image</b> (Url)

Example : https://static.openfoodfacts.org/images/products/68740269/front_fr.5.400.jpg

- <b>url</b> (Char)

Example : https://fr.openfoodfacts.org/produit/68740269/saucisson-sec-louis-auvergne

- <b>creator</b> (Char)

Example: openfoodfacts-contributors

- <b>brands</b> (Char)

Example : louis auvergne

- <b>stores</b> (Text)

Example : inter marché

- <b>nutriscore</b> (Int)

Example : 5

- <b>categories</b> (Text)

Example : meats,prepared-meats,saucissons,saucissons-secs
- <b>ingredient</b> (Text)

Example : [{"text": "maigre et gras de porc", "rank": 1, "id": "fr:maigre-et-gras-de-porc"}, {"rank": 2, "id": "fr:jambon-de-porc", "percent": "25", "text": "jambon de porc"}, {"id": "en:salt", "rank": 3, "text": "sel"}, {"rank": 4, "id": "en:lactose", "text": "lactose"}, {"id": "fr:dextrose  saccharose  \u00e9pices alcool ferments lactique conservateur", "rank": 5, "text": "dextrose  saccharose  \u00e9pices alcool ferments lactique conservateur"}, {"id": "fr:e252", "text": "E252"}, {"id": "fr:boyau-naturel-de-porc", "text": "boyau naturel de porc"}]

- <b>nutriments</b> (Text)

Example : {"carbohydrates": 1.4, "carbohydrates_100g": 1.4, "energy_kcal": 382.0, "energy_kcal_100g": 0.0, "energy_kj": 1599.36, "energy_kj_100g": 0.0, "fat": 28.7, "fat_100g": 28.7, "fiber": 0.0, "fiber_100g": 0.0, "proteins": 29.6, "proteins_100g": 29.6, "salt": 5.42, "salt_100g": 5.42, "saturated-fat": 12.2, "saturated-fat_100g": 12.2, "sodium": 2.13, "sodium_100g": 2.13, "sugars": 1.37, "sugars_100g": 1.37, "sugars_block": 0}
