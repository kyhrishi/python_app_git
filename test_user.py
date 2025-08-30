import pytest
from pydantic import ValidationError
from user import User

def test_user_creation():
    user = User(name="Alice", email="alice@example.com", userid=1)
    assert user.name == "Alice"
    assert user.email == "alice@example.com"
    assert user.userid == 1
    user_dict = user.model()
    assert user_dict == {
        "name": "Alice",
        "email": "alice@example.com",
        "userid": 1
    }

def test_user_invalid_email_raises_error():
    with pytest.raises(ValidationError):
        User(name="Bob", email="not-an-email", userid=2)
