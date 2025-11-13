import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Api")))

from app import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_buscar_operadora():
    response = client.get("/buscar", params={"nome": "amil"})
    assert response.status_code == 200
    print(response.json())

if __name__ == "__main__":
    test_buscar_operadora()

from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_buscar_operadora():
    response = client.get("/buscar", params={"nome": "unimed"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)
