# Python Practice

Early Python and Django exercises from my studies.

| Folder | What it shows |
|---|---|
| [`coffee-machine`](coffee-machine) | A command-line coffee machine simulator: a menu stored in dictionaries, a resource check before each drink, coin input and change calculation, and a `report` command showing remaining stock. A classic beginner project. |
| [`django-contacts`](django-contacts) | My first Django project: a `Person` model, a view that lists contacts from the database, URL routing with `include()` and named URLs, and the Django admin. |

For a fuller Django project, see my **Django Coffee Shop** repository.

## Running

```bash
# Coffee machine
python coffee-machine/coffee_machine.py
# type espresso, latte, cappuccino, report, or off

# Django contacts
pip install "Django>=5.1,<6"
cd django-contacts
python manage.py migrate
python manage.py createsuperuser   # then add people at /admin/
python manage.py runserver
```
