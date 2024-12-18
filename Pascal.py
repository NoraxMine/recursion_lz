inp = int(input("Введите значение, до которого должен быть построен треугольник Паскаля "))

def pascal(k, tr=None):
    if tr is None:
        tr = [[1]]
    if k == 1:
        return tr
    else:
        prev_tr = tr[-1]
        new_tr = [1] + [sum(i) for i in zip(prev_tr, prev_tr[1:])] + [1]
        return pascal(k - 1, tr + [new_tr])
    
print("Вот итог: ")    
print(pascal(inp))