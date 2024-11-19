# Обрезка ссылок с помощью VK
Скрипт сокращает любую ссылку через api-VK.
Если передать в него уже сокращенную ссылку формата vk.cc, то отобразится количество просмотров.

## Настройка окружения

### Зависимости

1. Должен быть установлен `python 3.8` и выше
1. Создайте виртуальное окружение, например [virtuatenv/venv](https://docs.python.org/3/library/venv.html)
1. Установите зависимости `pip install —r requirements.txt`

### Переменные окружения

1. Скопируйте файл `.env.example` с новым названием `.env`
1. Заполните VK_SERVICE_TOKEN вашим значением

#### Как получить VK_SERVICE_TOKEN
1. [Создать приложение](https://id.vk.com/about/business/go/docs/ru/vkid/latest/vk-id/connection/create-application)
1. Скопировать ваш сервисный токен приложения vk [Сервисный токен приложения](https://id.vk.com/about/business/go/docs/ru/vkid/latest/vk-id/connection/tokens/service-token)



## Запуск

Запустите скрипт с обязательным аргументом - вашей обычной или сокращенной ссылкой `python3 main.py **ссылка**`

