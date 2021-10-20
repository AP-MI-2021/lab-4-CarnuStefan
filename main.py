def read_lst():
    '''
    Citire lista de stringuri si transformare in lista de floaturi
    '''
    lst=[]
    lst_str=input('Introduceti numere separate prin spatiu: ')
    lst_str_split=lst_str.split(' ')
    for num_str in lst_str_split:
        lst.append(float(num_str))
    return lst

def parte_intreaga(lst:list):
    '''
    Ia numerele dintro lista si returneza partea lor intreaga
    :param lst: lista de floaturi
    :return: lista cu partea intreaga

    '''
    result=[]
    lst_str=[]
    for num in lst:
        num_str=(str(num))
        lst_str=num_str.split('.')
        result.append(int(lst_str[0]))
    return result

def test_parte_intreaga():
    assert parte_intreaga([1.5, -3.3, 8, 9.8, 3.2]) == [1, -3, 8, 9, 3]

def in_interval(lst:list,inter:tuple):
    '''
    Gaseste numerele din lista lst care se afla in intervalul inter
    :param lst: lista cu numere
    :param inter: intervalul
    :return: lista cu numere din interval
    '''
    result=[]
    for num in lst:
        if (num>inter[0]) & (num<inter[1]):
            result.append(num)
    return result

def test_in_interval():
    assert in_interval([1.5, -3.3, 8, 9.8, 3.2],(-4,5)) ==[1.5, -3.3, 3.2]

def frac_div_int(lst):
    '''
    Gaseste numerele a caror parte fractionare se divide cu partea lor intreaga
    :param lst: lista cu numere
    :return: lista cu numere a caror parte fractionare se divide cu partea lor intreaga
    '''
    result=[]
    for num in lst:
        num_str=(str(num))
        lst_str=num_str.split('.')
        if int(num)!=num:
            if (int(lst_str[1])%int(lst_str[0]))==0:
                result.append(num)
    return result

def test_frac_div_int():
    assert frac_div_int([1.5, -3.3, 8, 9.8, 3.2])==[1.5, -3.3]

def read_interval():
    while True:
        low=float(input('Introduceti capatul inferior al intervalului: '))
        upp=float(input('Introduceti capatul superior al intervalului: '))
        if low<upp:
            return (low,upp)
        else: print('Interval invalid')

def showmenu():
    print("1. Citire lista")
    print("2. Afisarea partilor intregi lae numerelor din lista")
    print("3. Afiseaza toate numerele aflate intr-un interval dat")
    print("4. Afiseaza toate numerele a caror parte fractionare se divide cu partea lor intreaga")
    print("x. Exit")

def main():
    while True:
        showmenu()
        opt=input('Alegeti optiunea: ')
        if opt=='1':
            lst=read_lst()
        elif opt=='2':
            print (parte_intreaga(lst))
        elif opt=='3':
            interval=read_interval()
            print( in_interval(lst,interval))
        elif opt=='4':
            print(frac_div_int(lst))
        elif opt=='x':
            break

if __name__=='__main__':
    test_parte_intreaga()
    test_in_interval()
    test_frac_div_int()
    main()