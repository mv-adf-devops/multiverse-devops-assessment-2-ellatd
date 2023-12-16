
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
                                
    return capitalised_user_names