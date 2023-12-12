from fastapi.testclient import TestClient
from main import app

class TranslationRequest(BaseModel):
    text: str

client = TestClient(app)


def test_hello():
    translation_request = TranslationRequest(text='Привет')
    response = client.post("/translate", translation_request.dict())
    assert response.status_code == 200
    assert response.json()["translation"] == "Hello"


def test_cat():
    translation_request = TranslationRequest(text='Кот')
    response = client.post("/translate", translation_request.dict())
    assert response.status_code == 200
    assert response.json()["translation"] == "Cat"


def test_dog():
    translation_request = TranslationRequest(text='Собака')
    response = client.post("/translate", translation_request.dict())
    assert response.status_code == 200
    assert response.json()["translation"] == "Dog"
