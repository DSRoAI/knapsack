import os
import csv

def read_testcase(filepath): 
    '''
    Output:
    number_of_items: int
    capacity: int
    values: list
    weights: list
    '''
    with open(filepath, 'r') as f:
        raw_data = []
        for line in f:
            if line !='\n':
                raw_data.append(line.strip())
                
        number_of_items = int(raw_data[0])
        capacity = int(raw_data[1])
        values = []
        weights = []
        for index_item in range(2, len(raw_data)):
            value, weight = [int(num) for num in raw_data[index_item].split()]
            values.append(value)
            weights.append(weight)
    return number_of_items, capacity, values, weights

def write_testcase_csv(filepath, computed_value, total_weight, is_optimal, id = 0):
    csv_path = os.path.join(os.getcwd(), 'snapsack/knapsack_result.csv')
    with open(csv_path, 'a', newline = '') as csvfile:
        fieldnames = ['Filepath', 'Total Value', 'Total Weight', 'Is Optimal']
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if id == 0:
            csvwriter.writeheader()
        csvwriter.writerow({
            'Filepath': filepath,
            'Computed Value': computed_value,
            'Total Weight': total_weight,
            'Is Optimal': is_optimal
        })

def write_testcase_txt(filepath, computed_value, total_weight, packed_items, packed_weights, id = 0):
    txt_path = os.path.join(os.getcwd(), 'snapsack/knapsack_result.txt')
    with open(txt_path, 'a') as txtfile:
        txtfile.write(f'------------------{id}------------------\n')
        txtfile.write(f'Filepath: {filepath}\n')
        txtfile.write(f'Computed Value: {computed_value}\n')
        txtfile.write(f'Total Weight: {total_weight}\n')
        txtfile.write(f'Packed Items: {packed_items}\n')
        txtfile.write(f'Packed Weights: {packed_weights}\n')
        txtfile.write('--------------------------------------\n')

def get_filepath():
    testcase_dir = os.path.join(os.getcwd(), 'snapsack/kplib')
    parent_dir_lst = [os.path.join(testcase_dir, dir) for dir in os.listdir(testcase_dir) if os.path.isdir(os.path.join(testcase_dir, dir))]

    n_dir_lst = []
    for parent_dir in parent_dir_lst:
        if parent_dir != os.path.join(testcase_dir, '.git'):
            n_dir_lst.append([os.path.join(parent_dir, n_dir) for n_dir in os.listdir(parent_dir)])

    r_dir_lst = []
    for lst_of_n_dir in n_dir_lst:
        lst = []
        lst += [os.path.join(n_dir, 'R01000') for n_dir in lst_of_n_dir]
        lst += [os.path.join(n_dir, 'R10000') for n_dir in lst_of_n_dir]
        r_dir_lst.append(lst)
        
    testcase_path_lst = []
    for lst_of_r_dir in r_dir_lst:
        lst = []
        for r_dir in lst_of_r_dir:
            lst += [os.path.join(r_dir, filename) for filename in os.listdir(r_dir)]
        testcase_path_lst.append(lst)
    return testcase_path_lst