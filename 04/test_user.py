import pytest
from user import validate_user


@pytest.fixture
def valid_user_data():
    return {
        "name": "Test",
        "email": "test@testcase.com",
        "age": 20,
    }


def test_validate_user_with_valid_data(valid_user_data):
    result = validate_user(valid_user_data)
    assert result == True
    

def test_validate_suer_with_invalid_email(valid_user_data):
    valid_user_data['email'] = 'testcase.com'
    result = validate_user(valid_user_data)
    assert result == False
    
    
def test_validate_suer_with_invalid_name(valid_user_data):
    valid_user_data['name'] = 'Test10?!'
    result = validate_user(valid_user_data)
    assert result == False

def test_validate_suer_with_invalid_age(valid_user_data):
    valid_user_data['age'] = 16
    result = validate_user(valid_user_data)
    assert result == False