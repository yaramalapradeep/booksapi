import json
import requests
BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'EmployeeListCBV2/'


def create_resource():
    new_emp = {
        'eno': 600,
        'ename':'pradeep',
        'esal': 6000,
        'eaddr':'chennai',

    }

    r = requests.post(BASE_URL+ENDPOINT, data=json.dumps(new_emp))
    print(r.status_code)
    print(r.text)
    print(r.json())

create_resource()