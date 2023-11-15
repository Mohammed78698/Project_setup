from lib.check_codeword import check_codeword

def test_with_correct_codeword():
    result = check_codeword("horse")
    assert result == "Correct! Come in."
    result = check_codeword("hare")
    assert result == "Close, but nope."
    result = check_codeword('Apple')
    assert result == "WRONG!"
    result = check_codeword("mouse")
    assert result == "WRONG!"