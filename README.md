
Основы веб-разработки на Django. "Сервис рассылок"

Данный проект представляет из себя сервис управления рассылками сообщений клиентам пользователей и сбора статистики.
Главная страница выглядит следующим образом:
![image](https://github.com/user-attachments/assets/f5d4247b-7375-4b8d-8ba4-ac120bda5049)

На главной странице отображается следующая информация:
1. количество рассылок всего
2. количество активных рассылок
3. количество уникальных клиентов для рассылок
4. три случайные статьи из блога

Для того, чтобы начать работу, пользователю необходимо зарегистрироваться. Для этого необходимо перейти на форму регистрации, нажав соответствующую кнопку вверху экрана.
![image](https://github.com/user-attachments/assets/46e4b1c1-e935-4fae-b3c8-a49ed10ad86d)
После ввода своих данных на почту придет письмо для подтверджения регистрации. Необходимо перейти по ссылке, указанной в письме.
![image](https://github.com/user-attachments/assets/20579a1e-3e5d-4fe6-bc7b-67665a80fc38)
В случае, если пользователь уже зарегистрирован, ему необходиом авторизоваться, нажав соответствующую кнопку - Войти.
После авторизации отобразится интерфейс, который зависит от того, кем является авторизованный пользователь. 

Ниже пердставлены варианты интерфеса:
1. Для обычного пользователя сервиса, который создает сообщения, клиентов и формирует рассылки
![image](https://github.com/user-attachments/assets/a2299c16-9347-4c3b-8069-36dd38f9ccdd)
2. Для менеджера, который управляет поьзователями и их рассылками
![image](https://github.com/user-attachments/assets/e3f965e3-4c9d-4971-af60-3b3b58cb5a29)
3. Для контент менеджера, который выполняет наполнение контентом главной страницы сайта
![image](https://github.com/user-attachments/assets/173a24d2-a715-4051-8d6e-76812ac681fb)

Как видно, главная страница сайта отличается только набором кнопок вверху экрана.

Для того, чтобы начать работу, пользователю необходимо создать клиентов, создать сообщения, и после этого создать рассылки для клиентов. В параметрах создаваемой рассылки пользователь уазывает необходимые параметры и нажимает кнопку сохранить. Так же, если пользователь хочет временно отключить рассылку, то он может ее деактивировать путем нажатия кнопки "Редактировать" и снять галочку в чекбоксе "Актуальность рассылки" и сохранить, либо выбрать статус рассылки "Завершена". Кроме этого при нажатии на кнопку "Лог" можно отследить статус попыток отправки своих рассылок.

Если пользователь входит в группу Менеджеров, то его функционал следующий:
1. Может просматривать любые рассылки.
2. Может просматривать список пользователей сервиса.
3. Может блокировать пользователей сервиса.
4. Может отключать рассылки.
5. Не может редактировать рассылки.
6. Не может управлять списком рассылок.
7. Не может изменять рассылки и сообщения.

Если пользователь входит в группу Контент-менеджера, то ему доступно лишь наполнение контентом главвной страницы сайта.

Так же каждому пользователю доступно редактирование своего профиля, нажав соответствующуу кнопку вверху экрана.


Запуск проекта.

1. Переименуйте файл .env.sample в .env и заполните необходимые данные
2. Создать виртуальное окружение.
3. Установить все зависимости виртуального окружения.
4. Создать базу данных CW6_django в PostgreSQL
5. Выполнить команду python3 manage.py migrate(для Ubuntu)
6. Создать суперпользователя выполнив команду python3 manage.py csuser (admin@sky.pro, 1238)
7. Запустите Redis: sudo service redis-server start
8. Запустите проект python3 manage.py runserver
9. Добавить задачу из CRONJOBS в crontab командой python3 manage.py crontab add
10. Перейти по адресу в веб-браузер http://127.0.0.1:8000
11. Начать работу


