import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home route"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to Todo API!' in response.data

def test_health(client):
    """Test the health check route"""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'healthy'

def test_get_todos(client):
    """Test getting all todos"""
    response = client.get('/todos')
    assert response.status_code == 200
    assert 'todos' in response.json

def test_add_todo(client):
    """Test adding a new todo"""
    new_todo = {'task': 'Test task'}
    response = client.post('/todos', json=new_todo)
    assert response.status_code == 201
    assert response.json['task'] == 'Test task'
    assert response.json['completed'] == False

def test_update_todo(client):
    """Test updating a todo"""
    update_data = {'completed': True}
    response = client.put('/todos/1', json=update_data)
    assert response.status_code == 200
    assert response.json['completed'] == True

def test_delete_todo(client):
    """Test deleting a todo"""
    response = client.delete('/todos/1')
    assert response.status_code == 200