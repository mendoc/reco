def nb_els_prec(nbu, n):
    if n < 1 or nbu < 1:
        return 0
    elif nbu == 1 :
        return n
    else:
        res = 1
        for i in range(nbu):
            res *= (n + i)/(i + 1)
        return int(res)
