def permutation(p): 
    if len(p) == 1:
        return [p]

    free_list = [] 
    for t in p:
        elements = [m for m in p if m != t]
        z = permutation(elements) 

        for t in z:
            free_list.append([t] + t)

    return free_list


def main():
    n = int(input('Введите желаемый размер списка:'))
    array = [i+1 for i in range(n)]
    print('Возможные перестановки элементов списка: ')
    for line in permutation(array):
        print(line)

main() 