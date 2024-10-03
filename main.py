import csv
from datetime import datetime


def load_data(file_path):
    data = []
    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        for row in csv_reader:
            date_str = row[0]
            profit_loss = float(row[1])
            date = datetime.strptime(date_str,'%m-%d') 
            data.append((date, profit_loss))
    return data

def selection_sort(data):
    n = len(data)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if data[j][0] < data[min_index][0]: 
                min_index = j
        
        data[i], data[min_index] = data[min_index], data[i]

def insertion_sort(data):
    n = len(data)
    for i in range(1, n):
        key = data[i]
        j = i - 1
        while j >= 0 and key[0] < data[j][0]:  
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key


def main():
    file_path = 'budget_data.csv'
    data = load_data(file_path)

   
    print("Original Dataset (First 5 records):")
    for record in data[:5]:
        print(record)

   
    selection_sorted_data = data.copy()
    selection_sort(selection_sorted_data)
    print("\nSelection Sorted Dataset (First 5 records):")
    for record in selection_sorted_data[:5]:
        print(record)

   
    insertion_sorted_data = data.copy()
    insertion_sort(insertion_sorted_data)
    print("\nInsertion Sorted Dataset (First 5 records):")
    for record in insertion_sorted_data[:5]:
        print(record)