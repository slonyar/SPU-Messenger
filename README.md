# SPU Messenger

## ENG

### About The Project


Messenger project in *Python 3.10* using the *Qt* framework.

### Description Of Capabilities
<li>In the start window you can register a new account or connect to the server with existing login and password</li>
<li>After successful authorization, the main window will open. It displays the username, field to enter your message and chat window with other messenger users</li>
<li>You can exit the application window using the "Exit" button. You can also exit using the hotkey combination "Ctrl+Shift+Q"</li>
<li>You are able to delete an account you are logged into using the "Delete account" button</li>
<li>You can write messages and send them with the "Send message" button (sending with the "Return" key also works). After that they will appear in the chat window</li>

### Preparing To Launch The Application
<li>Download the repo to your device</li>
<li>If you don't have the "Ubuntu" font installed, you can do it using the archive font/Ubuntu.zip</li>
<li>Before running any file, make sure that all the necessary modules from the requirements.txt file are installed</li>
<li>So that you can connect to the server, you need to run the run_server.py file on your device. The server will be available at http://127.0.0.1:5000</li>
<li>Now you can run the main.py file and use the application's features</li>

### The Role Of The Server In The Operation Of The Application

<li>The application interacts with the server using the script handler/data_handler.py</li>
<li>The server stores in SQL tables information about user accounts (passwords are hashed) and the history of user messages during a given server session</li>
<li>The client on the local device sends requests to the server after each user action. The list of messages in the chat window is updated every 200 ms. The update frequency can be configured in the src/messenger_class.py file</li>

### Editing

To edit server settings, just open the `server/server.py` file.
Databases responsible for storing accounts (`users`) and messages for a given server session (`messages`) are also stored in the `server` directory.
To adjust the operation of the request handler (for example, change the address of the server to which requests will be sent), you need to correct the `handler/data_handler.py` file.
You can change the window design using *Qt Designer*. For this purpose there are files `src/authorization_window.ui`, `src/messenger_window.ui`. The icons used are in the `icons` directory.
The `src/authorization_class.py` and `src/messenger_class.py` files are responsible for the functionality of the windows.

### Contact

Telegram: [@malinovyvlad](https://t.me/malinovyvlad)

<hr>

## RUS

### О Проекте

Проект мессенджера на *Python 3.10* с использованием фреймворка *Qt*.

### Описание Возможностей
<li>В стартовом окне Вы можете зарегистрировать новый аккаунт или подключиться к серверу с существующими логином и паролем</li>
<li>После успешной авторизации открывается главное окно. В нём отображаются имя пользователя, поле для ввода Вашего сообщения и окно чата с другими пользователями мессенджера</li>
<li>Вы можете выйти из приложения, используя кнопку "Exit". Также доступен выход с помощью комбинации горячих клавиш "Ctrl+Shift+Q"</li>
<li>Вы можете удалить аккаунт, в который выполнен вход с помощью кнопки "Delete account"</li>
<li>Вы сожете писать сообщения и отправлять их кнопкой "Send message" (отправка клавишей "Ввод" также работает. После этого они появятся в окне чата</li>

### Подготовка К Запуску Приложения
<li>Загрузите репозиторий на своё устройство</li>
<li>Если у Вас не установлен шрифт "Ubuntu", то Вы можете это сделать, воспользовавшись архивом font/Ubuntu.zip</li>
<li>Перед запуском каких-либо файлов убедитесь, что все необходимые модули из файла requirements.txt установлены</li>
<li>Для того чтобы Вы могли подключиться к серверу, на Вашем устройстве должен быть запущен файл run_server.py. Сервер будет доступен по адресу http://127.0.0.1:5000</li>
<li>Теперь Вы можете запустить файл main.py и пользоваться возможностями приложения</li>

### Роль Сервера В Работе Приложения
<li>Приложение взаимодействует с сервером с помощью скрипта handler/data_handler.py</li>
<li>Сервер хранит в SQL таблицах информацию об учётных записях пользователей (пароли захешированы) и историю сообщений пользователей в данную сессию работы сервера</li>
<li>Клиент на локальном устройстве после каждого действия пользователя отправляет запросы на сервер. Каждые 200 мс происходит обновление списка сообщений в окне чата. Частоту обновлений можно настраивать в файле src/messenger_class.py</li>

### Редактирование

Для редактирования настроек сервера достаточно открыть файл `server/server.py`.
Базы данных, отвечающие за хранение учётных записей (`users`) и сообщений за данную сессию работы сервера (`messages`), тоже хранятся в директории `server`.
Чтобы скорректировать работу обработчика запросов (например, изменить адрес сервера, к которому будут идти запросы), нужно исправить файл `handler/data_handler.py`.
Изменить дизайн окон можно с помощью *Qt Designer*. Для этого есть файлы `src/authorization_window.ui`, `src/messenger_window.ui`. Используемые иконки лежат в директории `icons`.
За функционал окон отвечают файлы `src/authorization_class.py` и `src/messenger_class.py`.

### Контакт

Telegram: [@malinovyvlad](https://t.me/malinovyvlad)