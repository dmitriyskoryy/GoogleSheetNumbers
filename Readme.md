## Название проекта: testnumbersss


### Запуск приложения (для ОС Windows)
### Google Sheets документ: https://docs.google.com/spreadsheets/d/1AEVkEYg_3Q2Z-qk2QvHAx2qIqEbLwfqhXAvGtohdnUA/edit?usp=sharing
Проект выполнен на Python/Django. Чтобы проверить его работу, 
необходимо:
 - скачать и установить PostgreSQL 
(создать БД с именем "postgres", пользователь "postgres", пароль "1")
 - скачать проект с Github на ПК
 - перейти в директорию ..\testnumbersss\project\googlesheet
 - открыть файл config.py
 - Ввести TOKEN и ID_CHAT вашего телеграм-бота (необходимо для отправки сообщения в телеграм. 
Чтобы узнать ID_CHAT бота, необходимо в поисковике телеграма набрать @getmyid_bot,
и запустить его, бот выдаст 9 значный ID_CHAT)
 - Далее необходимо запустить командную сроку в Windows (cmd)
и перейти в папку (..\testnumbersss\venv\Scripts)
 - набрать команду: activate.bat (при этот активируется виртуальное окружение)
 - перейти папку (..\testnumbersss\project)
 - набрать команду: python manage.py runserver (при этом запустится сервер Django)
 - Далее открыть браузер (Chrome, Yandex и пр)
 - Перейти на адрес: http://127.0.0.1:8000/googlesheet/
