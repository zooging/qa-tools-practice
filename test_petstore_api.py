import requests
import pytest

BASE_URL = "https://petstore.swagger.io/v2"

# Словарь для сохранения состояния (ID питомца) между тестами
pet_data = {"id": None}

def test_create_pet():
    payload = {
        "id": 999888777666,
        "category": {"id": 1, "name": "Dogs"},
        "name": "Balu",
        "photoUrls": ["https://example.com/dog.jpg"],
        "tags": [{"id": 1, "name": "goodboy"}],
        "status": "available"
    }
    response = requests.post(f"{BASE_URL}/pet", json=payload)
    
    # Проверки статус-кода и тела ответа
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    data = response.json()
    assert data["name"] == "Balu"
    
    # Сохраняем сгенерированный ID для следующих тестов
    pet_data["id"] = data["id"]
    
    # Проверка времени ответа (менее 800 мс)
    assert response.elapsed.total_seconds() < 0.8

def test_get_pet_by_id():
    pet_id = pet_data["id"]
    response = requests.get(f"{BASE_URL}/pet/{pet_id}")
    
    assert response.status_code == 200
    assert response.headers.get("Content-Type") == "application/json"
    assert response.json()["id"] == pet_id

def test_update_pet():
    payload = {
        "id": pet_data["id"],
        "category": {"id": 1, "name": "Dogs"},
        "name": "Balu",
        "photoUrls": ["https://example.com/dog.jpg"],
        "tags": [{"id": 1, "name": "goodboy"}],
        "status": "sold"  # Изменяем статус на sold
    }
    response = requests.put(f"{BASE_URL}/pet", json=payload)
    
    assert response.status_code == 200
    assert response.json()["status"] == "sold"

def test_find_pet_by_status():
    # Передаем параметры запроса через аргумент params
    response = requests.get(f"{BASE_URL}/pet/findByStatus", params={"status": "sold"})
    
    assert response.status_code == 200
    # Проверяем, что ответ является списком (массивом JSON)
    assert isinstance(response.json(), list)

def test_delete_pet():
    pet_id = pet_data["id"]
    response = requests.delete(f"{BASE_URL}/pet/{pet_id}")
    
    assert response.status_code == 200
    # API возвращает ID удаленного объекта в виде строки в поле message
    assert response.json()["message"] == str(pet_id)

def test_verify_deletion():
    pet_id = pet_data["id"]
    response = requests.get(f"{BASE_URL}/pet/{pet_id}")
    
    assert response.status_code == 404
    assert response.json()["message"] == "Pet not found"