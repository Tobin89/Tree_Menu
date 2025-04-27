# Tree_Menu
### Запуск проекта

```shell
git clone git@github.com:Tobin89/Tree_Menu.git
cd tree_menu
python -m venv venv
venv/Scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
```
Для корректной работы приложения необходимо:
 * создать суперпользователя
```shell
python manage.py createsuperuser
```
 * создать меню и его элементы через административную панель.

Запустить сервер разработки
```shell
python manage.py runserver
```
