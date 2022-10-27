# Проект Yamdb
## Ссылки
`http://178.154.225.187/redoc/` - redoc

`http://178.154.225.187/api/v1/` - api

`http://178.154.225.187/admin/login/?next=/admin/` - admin
## Описание 
Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории: «Книги», «Фильмы», «Музыка». 

Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

Произведению может быть присвоен жанр. Новые жанры может создавать только администратор. Читатели оставляют к произведениям текстовые отзывы и выставляют произведению рейтинг (оценку в диапазоне от одного до десяти). Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы (Review) и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.

## Установка
Клонируем репозиторий на локальную машину:

`git clone git@github.com:oladushkin/yamdb_final.git`

Создаем виртуальное окружение:

`python -m venv venv`

Устанавливаем зависимости:

`pip install -r requirements.txt`

Применяем миграции:

`python manage.py migrate`

Запуск:

`python manage.py runserver`

### Статус работы:

![example workflow](https://github.com/oladushkin/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

### Над проектом работали:

- Шелепин Дмитрий | [Github](https://github.com/oladushkin)
