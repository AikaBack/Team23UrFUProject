from fastapi.testclient import TestClient
from main import app
from pydantic import BaseModel

class TranslationRequest(BaseModel):
    text: str

client = TestClient(app)


def test_hello():
    translation_request = TranslationRequest(text='Один')
    response = client.post("/translate", json=translation_request.dict())
    assert response.status_code == 200
    assert response.json()["translation"].replace(".", "") == "One"

def test_cat():
    translation_request = TranslationRequest(text='Десять')
    response = client.post("/translate", json=translation_request.dict())
    assert response.status_code == 200
    assert response.json()["translation"].replace(".", "") == "Ten"

def test_dog():
    translation_request = TranslationRequest(text='Собака')
    response = client.post("/translate", json=translation_request.dict())
    assert response.status_code == 200
    assert response.json()["translation"].replace(".", "") == "Dog"
