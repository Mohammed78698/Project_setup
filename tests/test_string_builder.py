from lib.string_builder import StringBuilder

def test_initial_output_is_a_string():
    string_builder = StringBuilder()
    assert string_builder.output() == ""

def test_adding_string_outputs_that_a_string():
    string_builder = StringBuilder()
    string_builder.add("hello")
    assert string_builder.output() == "hello"

def test_adding_a_string_sets_size_to_that_strings_size():
    string_builder = StringBuilder()
    string_builder.add("hello")
    assert string_builder.size() == 5

def test_adding_multiple_strings_outputs_concatenated_strings():
    string_builder = StringBuilder()
    string_builder.add("hello")
    string_builder.add(" ")
    string_builder.add("world")
    assert string_builder.output() == "hello world"

def test_adding_multiple_strings_has_total_size():
    string_builder = StringBuilder()
    string_builder.add("hello")
    string_builder.add(" ")
    string_builder.add("world")
    assert string_builder.size() == 11
