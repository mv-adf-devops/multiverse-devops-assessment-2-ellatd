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
    
    return removed_empty_lists