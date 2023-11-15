from lib.greet import greet
def test_greets_person_of_given_name():
    result = greet("Mohammed")
    assert result == "Hello, Mohammed!"