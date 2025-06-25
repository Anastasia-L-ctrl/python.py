import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '822e8149e9407def35ad6f621b2da961'
HEADER = {"Content-Type":"application/json", "trainer_token":TOKEN} 
PAGE = '1'


def test_status_code():
    response=requests.get(url=f'{URL}/trainers', params={'1':PAGE})
    assert response.status_code==200

TRAINER_ID = '36058'
TRAINER_NAME = "котик Гатти"

def test_trainer_name():
        response_get = requests.get(url=f'{URL}/trainers',params={'trainer_id' : TRAINER_ID}) 
        print  (response_get.json()) 
        data = response_get.json()['data'] 
        assert data[0]['trainer_name'] == 'котик Гатти'
