from lib.report_length import report_length
def test_report_length():
    assert report_length("Hello, world!") == "This string was 13 characters long."
    assert report_length("1") == "This string was 1 characters long."
    assert report_length("Forex") == "This string was 5 characters long."
