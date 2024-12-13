# Используем базовый образ Python с нужной версией
FROM python:3.9

# Устанавливаем необходимые пакеты, включая git
RUN apt-get update && apt-get install -y git

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл с зависимостями в контейнер
COPY ./requirements.txt /app/

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Копируем остальные файлы проекта в контейнер
COPY ./formula_project/ /app/formula_project/
COPY ./formula_project/Mainapp/ /app/Mainapp/
COPY ./formula_project/template/ /app/template/
COPY ./formula_project/db.sqlite3 /app/db.sqlite3
COPY ./formula_project/manage.py /app/manage.py

# Открываем порт 8000
EXPOSE 8000

# Команда для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]