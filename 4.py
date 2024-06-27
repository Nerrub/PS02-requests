# Используйте API, который позволяет фильтрацию данных через
# URL-параметры (например, https://jsonplaceholder.typicode.com/posts).
#
# Отправьте GET-запрос с параметром userId, равным 1.
#
# Распечатайте полученные записи.

import requests
import pprint

params = {
    'userid' : 1
}
response = requests.get('https://jsonplaceholder.typicode.com/posts', params=params)

response_json = response.json()
pprint.pprint(response_json)

