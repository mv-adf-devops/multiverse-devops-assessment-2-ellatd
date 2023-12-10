def read_csv(filename):
    rows = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            rows.append(line.strip().split(','))
        
    #TICKET 3: Ignore any empty lists
    removed_empty_lists = [line for line in rows if line != ['', '', '', '', '', '']]

    return rows