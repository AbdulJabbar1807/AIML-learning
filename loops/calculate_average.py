def main():
    print(calculate_average())

def calculate_average():
    n = int(input("enter the 'n': "))
    item_list = list()
    
    for i in range(n):
        num = int(input("enter the number: "))
        item_list.append(num)

    total_sum = 0
    for j in item_list:
        total_sum += j
    average = total_sum/n
    return average
        
main()
    