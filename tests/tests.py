from extract import read_csv

#TICKET 1:
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
    expected_output = ["user_id", "First_name", "Last_name", "answer_1", "answer_2", "answer_3"]

     #Act - calling a e.g. function
    output = read_csv(filename)
              
    #Assert
    assert output[0] == expected_output

<<<<<<< HEAD
#TICKET 3: ignore empty lists
=======
#TICKET 3 TEST
>>>>>>> origin
def test_empty_lists_ignored():
    #Arrange - defining out filenames, variables, functions etc.
    filename = "results.csv"

    #Act - calling a e.g. function
    output = read_csv(filename)
              
    #Assert
    assert output not in ['', '', '', '', '', '']

<<<<<<< HEAD
#TICKET 2: Remove duplicate lists
def test_duplicate_lists_removed():
    #Arrange - defining out filenames, variables, functions etc.
    filename = "results.csv"

    #Act - calling a e.g. function
    output = read_csv(filename)
    duplicates = any(output.count(row) > 1 for row in output)

    #Assert
    assert not duplicates

#TICKET #4: Capitalise user name fields
def test_capitalised_names():
    #Arrange - defining out filenames, variables, functions etc.
    filename = "results.csv"

    #Act - calling a e.g. function
    output = read_csv(filename)
    failures = 0
    for line in output:
        if line[1] != line[1].capitalize():
            failures = failures + 1
        if line[2] != line[2].capitalize():
            failures = failures + 1

    # Assert
    assert failures == 0
=======
#TICKET 2 TEST
def test_duplicates_removed():
	#Arrange - defining out filenames, variables, functions etc.
    filename = "results.csv"
	
    #Act - calling an e.g. function
    output = read_csv(filename)
    duplicates = any(output.count(row) > 1 for row in output)
	
    assert not duplicates
>>>>>>> origin
