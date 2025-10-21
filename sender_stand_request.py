import requests
import data
import configuration

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH)

def get_kit_table():
    return requests.get(configuration.URL_SERVICE + configuration.KITS_TABLE_PATH)

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

def post_new_client_kit(kit_body):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=data.headers)

response = post_new_user(data.user_body)
print(response.json())