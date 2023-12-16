import csv

#TICKET 1: 
def read_csv(filename):
    rows = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            rows.append(line.strip().split(','))

    #TICKET 2: remove duplicates
    non_duplicates_list = []
    for line in rows:
        if line[0] not in [i[0] for i in non_duplicates_list]:
            non_duplicates_list.append(line)
   
    #TICKET 3: ignore any empty lists
    removed_empty_lists = [line for line in non_duplicates_list if line != ['', '', '', '', '', '']]
    
    #TICKET 4: capitalise user name fields
    capitalised_user_names = []
    for line in removed_empty_lists:
        line[1] = line[1].capitalize()
        line[2] = line[2].capitalize()
        capitalised_user_names.append(line)

    #TICKET 5: Validate answer 3s are correct
    answer_3s_validated = []
    for i in capitalised_user_names[1:]:
        if i[5] != '' and (int(i[5]) >=1 and int(i[5]) <= 10):
            answer_3s_validated.append(i)

    #TICKET 6: read results into new csv file
    output_filename = "clean_results.csv"
    with open(output_filename, 'w') as output_filename:
        for line in answer_3s_validated:
            output_filename.write(','.join(line) + '\n')
    
    return answer_3s_validated