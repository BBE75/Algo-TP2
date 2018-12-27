import time
from random import randint


def q_sort(tab, min, max, cpt):
    if min < max:
        cpt += 1

        j = min
        for i in range(min, max + 1):
            if tab[i] < tab[max]:
                if i != j:
                    tmp = tab[i]
                    tab[i] = tab[j]
                    tab[j] = tmp
                j += 1
        tmp = tab[j]
        tab[j] = tab[max]
        tab[max] = tmp
    if min < max:
        q_sort(tab, min, j - 1, cpt)
        q_sort(tab, j + 1, max, cpt)


def quick_sort(tab, min, max, cpt, verbose):

    start_time = time.time()
    print('--début du tri sélection--')
    if verbose == 1:
        print_tab(tab, max)

    q_sort(tab, min, max, cpt)

    print('--fin du tri rapide--')
    if verbose == 1:
        print_tab(tab, max)
    print("Execution time : %s seconds" % (time.time() - start_time))


def sequential_search(tab, valeur, tab_length):

    print('--Recherche sequentiel--')
    i = 0

    while tab[i] != valeur and i < tab_length:
        i += 1
    if tab[i] == valeur:
        print('Valeur: ', valeur, ' trouvée après ', i+1, ' comparaisons à l\'indice ', i)
    else:
        print('Valeur ', valeur, 'non présente dans le tableau')


def print_tab(tab, tab_length):
    for i in range (0, tab_length):
        print(tab[i], end='')
        if i < tab_length - 1:
            print(',', end='')
    print()


def select_sort_tab(tab, tab_length, verbose):
    start_time = time.time()
    print('--début du tri sélection--')
    if verbose == 1:
        print_tab(tab, tab_length)
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

    print('--fin du tri sélection--')
    if verbose == 1:
        print_tab(tab, tab_length)
    print("Execution time : %s seconds" % (time.time() - start_time))


def insert_sort(tab, tab_length, verbose):
    start_time = time.time()
    print('--début du tri par insertion--')
    if verbose == 1:
        print_tab(tab, tab_length)

    for i in range(1, tab_length-1):
        if tab[i] > tab[i+1]:
            for j in range(0, i+1):
                if tab[j] > tab[i+1]:
                    tmp = tab[j]
                    tab[j] = tab[i+1]
                    tab[i+1]= tmp
    print('--fin du tri par insertion--')
    if verbose == 1:
        print_tab(tab, tab_length)
    print("Execution time : %s seconds" % (time.time() - start_time))


def dichotomy_search(tab, min, max, valeur, cpt):
    if cpt == 0:
        print('--Recherche dychotomique--')
    length = max - min
    cpt += 1

    if tab[int(min+length/2)] == valeur:
        print('Valeur:', valeur, 'présente à l\'indice: ', int(min+length/2), 'trouvée après', cpt, ' divisions')
        return int(min+length/2)
    elif tab[min] == valeur:
        print('Valeur:', valeur, 'présente à l\'indice: ', min, 'trouvée après', cpt, ' divisions')
        return min
    elif tab[max] == valeur:
        print('Valeur:', valeur, 'présente à l\'indice: ', max, 'trouvée après', cpt, ' divisions')
        return max
    elif tab[int(min+length/2)] < valeur and length > 1:
        new_min = int(min+length/2)
        dichotomy_search(tab, new_min, max, valeur, cpt)
    elif tab[int(min+length/2)] > valeur and length > 1:
        new_max = int(min+length/2)
        dichotomy_search(tab, min, new_max, valeur, cpt)
    else:
        print('Valeur ', valeur, 'non présente dans le tableau')
        return -1


# Génération d'un tableau de 10000 éléments avec valeurs comprisent entre 0 et 100
tab = []
for i in range(0, 10000):
    tab.append(randint(0, 101))

# 1 pour afficher les tableaux non triés puis triés
verbose = 0
select_tab = list(tab)
insert_tab = list(tab)
quick_tab = list(tab)

select_sort_tab(select_tab, len(select_tab), verbose)
insert_sort(insert_tab, len(insert_tab), verbose)
quick_sort(quick_tab, 0, len(quick_tab)-1, 0, verbose)
sequential_search(select_tab, 55, len(select_tab)-1)
dichotomy_search(select_tab, 0, len(select_tab)-1, 55, 0)

