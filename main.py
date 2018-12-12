import time


def sequential_search(tab, valeur, tab_length):
    i = 0
    while tab[i] !=  valeur and i < tab_length:
        i +=1
    if tab[i] == valeur:
        print('Valeur: ', valeur,' trouvée après ', i+1, ' comparaisons')
    else:
        print('Valeur non présente')


def print_tab(tab, tab_length):
    for i in range (0, tab_length):
        print(tab[i], end='')
        if i < tab_length - 1:
            print(',', end='')
    print()


def select_sort_tab(tab, tab_length, verbose):
    start_time = time.time()
    print('--début du tri sélection--')
    for j in range(0, tab_length):
        min = tab[j]
        index_min = j
        for i in range(j+1, tab_length):
            if tab[i] < min:
                min = tab[i]
                index_min = i
        tmp = tab[j]
        tab[j] = tab[index_min]
        tab[index_min] = tmp
        if verbose == 1:
            print_tab(tab, tab_length)
    print('--fin du tri sélection--')
    print("Execution time : %s seconds" % (time.time() - start_time))


def dichotomy(tab, min, max, valeur, verbose, cpt):
    length = max - min
    cpt += 1
    if verbose == 1:
        print('Longueur :', int(length))
        print('min: ', min, 'max: ', max, 'valeur: ', valeur, 'pivot: ', int(min+length/2))

    if tab[int(min+length/2)] == valeur:
        print('Valeur:', valeur, 'présente à l\'indice: ', int(min+length/2), 'trouvée après', cpt, ' comparaisons')
        return int(min+length/2)
    elif tab[min] == valeur:
        print('Valeur:', valeur, 'présente à l\'indice: ', min, 'trouvée après', cpt, ' comparaisons')
        return min
    elif tab[max] == valeur:
        print('Valeur:', valeur, 'présente à l\'indice: ', max, 'trouvée après', cpt, 'comparaisons')
        return max
    elif tab[int(min+length/2)] < valeur and length > 1:
        new_min = int(min+length/2)
        dichotomy(tab, new_min, max, valeur, verbose, cpt)
    elif tab[int(min+length/2)] > valeur and length > 1:
        new_max = int(min+length/2)
        dichotomy(tab, min, new_max, valeur, verbose, cpt)
    else:
        print('Valeur non présente dans le tableau')
        return -1


#for i in range(0, 10):
#     saisie = int(input('Saisir un entier'))
#     tab.append(saisie)

tab = [37, 10, 8, 29, 97, 4, 11, 76, 55, 34]
select_tab = list(tab)
print('Affichage du tableau avant tri: ', end='')
print_tab(select_tab, len(select_tab))
select_sort_tab(select_tab, len(select_tab), 0)
print('Affichage du tableau après tri: ', end='')
print_tab(select_tab, len(select_tab))
sequential_search(select_tab, 55, len(select_tab))
dichotomy(select_tab, 0, len(select_tab)-1, 55, 0, 0)