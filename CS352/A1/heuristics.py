# =============================
# Student Names: Logan Fleck, Batuhan Aktan, Rahul Seebaransingh
# Group ID: 64
# Date: 2023-02-08
# =============================
# CISC 352 - W23
# heuristics.py
# desc:
#


#Look for #IMPLEMENT tags in this file. These tags indicate what has
#to be implemented to complete problem solution.

'''This file will contain different constraint propagators to be used within
   the propagators

var_ordering == a function with the following template
    var_ordering(csp)
        ==> returns Variable

    csp is a CSP object---the heuristic can use this to get access to the
    variables and constraints of the problem. The assigned variables can be
    accessed via methods, the values assigned can also be accessed.

    var_ordering returns the next Variable to be assigned, as per the definition
    of the heuristic it implements.
   '''

def ord_dh(csp):
    ''' return variables according to the Degree Heuristic '''
    unvar = csp.get_all_unasgn_vars()

    max = 0
    #iterates through unbound variables
    for i in unvar:
        if max == 0:
            max = i
        else:
            #checks what var has more contraints affecting it
            if len(csp.get_cons_with_var(i)) > len(csp.get_cons_with_var(max)):
                max = i
    return max

def ord_mrv(csp):
    ''' return variable according to the Minimum Remaining Values heuristic '''
    unvar = csp.get_all_unasgn_vars()
    min = 0

 #iterates through variables
    for i in range(0,len(unvar),1):
        if min == 0:
            #records domain size for variable
            min = unvar[i].cur_domain_size()
            minval = unvar[i]
        else:
            #compares domain size and updates min variable
            temp = unvar[i].cur_domain_size()
            if temp < min:
                min = temp
                minval = unvar[i]
    return minval
