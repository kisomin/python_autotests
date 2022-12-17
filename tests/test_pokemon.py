import requests
import pytest

def test_status_code():
    status = requests.get('https://pokemonbattle.me:5000/trainers')
    assert status.status_code == 200

def test_name():
    name = requests.get('https://pokemonbattle.me:5000/trainers', params={'trainer_id':'1524'})
    assert name.json()['trainer_name'] == 'Мин'