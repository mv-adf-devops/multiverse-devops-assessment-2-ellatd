
#TICKET 1: 
def read_csv(filename):
    rows = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            rows.append(line.strip().split(','))
   
    #TICKET 3: ignore any empty lists
    removed_empty_lists = [line for line in non_duplicates_list if line != ['', '', '', '', '', '']]
    
    return removed_empty_lists