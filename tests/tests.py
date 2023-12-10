from extract import read_csv

"""
The results.csv data file can be successfully processed into an array.
● Each line of the file is read into a new array item.
● The file read method must be in a sub-module.
"""

def test_file_read_into_list():
    #Arrange - defining out filenames, variables, functions etc.
    filename = "results.csv"
    expected_output = list

    #Act - calling a e.g. function
    output = type(read_csv(filename))

    #Assert
    assert output == expected_output

def test_list_not_empty():
    #Arrange - defining out filenames, variables, functions etc.
    filename = "results.csv"
    
    #Act - calling a e.g. function
    output = read_csv(filename)

    #Assert
    assert len(output) > 0

def test_first_row_is_correct():
     #Arrange - defining out filenames, variables, functions etc.
    filename = "results.csv"
    expected_output = ["user_id", "first_name", "last_name", "answer_1", "answer_2", "answer_3"]

     #Act - calling a e.g. function
    output = read_csv(filename)
              
    #Assert
    assert output[0] == expected_output
