# Докер сборка для чистого приложения на python

для запуска контейнера

```bash
docker-compose up -d --build
```

для перехода внутрь контейнера
```bash
docker exec -it some-app bash
```

для запуска скрипта внутри контейнера
```bash
python main.py
```

## Зависимости

можно докинуть в файл ./app/requirements.txt

пример:
```txt
flask
flask-cors
requests
gunicorn
fast-bitrix24
python-dotenv
google-api-python-client
oauth2client
gspread
schedule
```

и после этого пересобрать контейнер 

либо внутри контейнера поставить зависимость
чрез пакетный менеджер pip(но лучше так не делать)