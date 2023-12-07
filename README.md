Описание
=
Данный проект скачивает фото с сайтов NASA, Space-X.

Установка
=

```
pip install -r requirements.txt
```

Переменные окружения
=
Для настройки переменных окружения нужно создать файл .env указать там переменную окружения с токеном ```NASA_TOKEN=токен```
```TG_TOKEN=токен``` и ```CHAT_ID=cgat_id```.

Ключ API.  Ключ API NASA можно получить в кабинете  [Сайт NASA](https://api.nasa.gov/).

Зарегистрировать бота и получить токен  [Как регистрировать бота](bit.ly/47ELQuZ).


Инструкция
=

```
python3 fetch_spacex_images.py
``` 
Ссылка - скачивает фотографии запусков SpaceX.

```
python3 apod.py ссылка
```
Скачивает фотографии с сайта NASA.

```
python3 nasa_earth.py
``` 
Ссылка - скачивает фотографии Земли.

```
download_picture.py
``` 
Функция для скачивание фотографий в директории.

```
get_extention.py
``` 
Забирает расширение файла.

```
python3 telegram_bot.py
``` 
количество секунд - устанавливает необходимое количество секунд отправки файла в ТГ бота, если пусто, то задержка 4 часа. Если фотографии в директории заканчиваются, то меняется их порядок и отправляются заново.

Примеры запуска скриптов
=

```
$ python3 telegram_bot.py 50
```
Pадержка между публикациями 50 секунд.

```
$ python3 apod.py https://api.nasa.gov/planetary/
``` 
API_token - скачивание фото дня с сайта [NASA[(https://api.nasa.gov/).

```
$ python3 fetch_spacex_images.py https://api.spacexdata.com/v5/launches/
``` 
id запуска скачивает фото с запуска по Id.

```
$ python3 nasa_earth.py  https://api.nasa.gov/EPIC/archive/natural/2019/05/30/png/epic_1b_20190530011359.png?api
``` 
API_Key скачивает фото Земли с сайта [NASA](https://api.nasa.gov/).

