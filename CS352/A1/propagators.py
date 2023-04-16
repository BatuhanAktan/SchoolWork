# =============================
# Student Names: Logan Fleck, Batuhan Aktan, Rahul Seebaransingh
# Group ID: 64
# Date: 2023-02-05
# =============================
# CISC 352 - W23
# propagators.py
# desc:
#

#Look for #IMPLEMENT tags in this file. These tags indicate what has
#to be implemented to complete problem solution.

'''This file will contain different constraint propagators to be used within
   bt_search.

   propagator == a function with the following template
      propagator(csp, newly_instantiated_variable=None)
           ==> returns (True/False, [(Variable, Value), (Variable, Value) ...]

      csp is a CSP object---the propagator can use this to get access
      to the variables and constraints of the problem. The assigned variables
      can be accessed via methods, the values assigned can also be accessed.

      newly_instaniated_variable is an optional argument.
      if newly_instantiated_variable is not None:
          then newly_instantiated_variable is the most
           recently assigned variable of the search.
      else:
          progator is called before any assignments are made
          in which case it must decide what processing to do
           prior to any variables being assigned. SEE BELOW

       The propagator returns True/False and a list of (Variable, Value) pairs.
       Return is False if a deadend has been detected by the propagator.
       in this case bt_search will backtrack
       return is true if we can continue.

      The list of variable values pairs are all of the values
      the propagator pruned (using the variable's prune_value method).
      bt_search NEEDS to know this in order to correctly restore these
      values when it undoes a variable assignment.

      NOTE propagator SHOULD NOT prune a value that has already been
      pruned! Nor should it prune a value twice

      PROPAGATOR called with newly_instantiated_variable = None
      PROCESSING REQUIRED:
        for plain backtracking (where we only check fully instantiated
        constraints)
        we do nothing...return true, []

        for forward checking (where we only check constraints with one
        remaining variable)
        we look for unary constraints of the csp (constraints whose scope
        contains only one variable) and we forward_check these constraints.

        for gac we establish initial GAC by initializing the GAC queue
        with all constaints of the csp


      PROPAGATOR called with newly_instantiated_variable = a variable V
      PROCESSING REQUIRED:
         for plain backtracking we check all constraints with V (see csp method
         get_cons_with_var) that are fully assigned.

         for forward checking we forward check all constraints with V
         that have one unassigned variable left

         for gac we initialize the GAC queue with all constraints containing V.
   '''

def prop_BT(csp, newVar=None):
    '''Do plain backtracking propagation. That is, do no
    propagation at all. Just check fully instantiated constraints'''

    if not newVar:
        return True, []
    for c in csp.get_cons_with_var(newVar):
        if c.get_n_unasgn() == 0:
            vals = []
            vars = c.get_scope()
            for var in vars:
                vals.append(var.get_assigned_value())
            if not c.check_tuple(vals):
                return False, []
    return True, []

def prop_FC(csp, newVar=None):
    '''Do forward checking. That is check constraints with
       only one uninstantiated variable. Remember to keep
       track of all pruned variable,value pairs and return '''

    pruned_vars = [] #storage for pruned vars

    constraints = csp.get_all_cons() #getting all the contstraints

    if newVar is None: #in the case that no new var is given.

        for c in constraints: #iterating through the constraints

            scope = c.get_scope() #getting the scope of the constraint.

            if len(scope) == 1: #if there is scope.

                new_pruned = [] #new list to store in current domain

                domain = variable.cur_domain() #get current domain

                for element in domain:

                    if not c.has_support(variable,element): 

                        new_pruned += [(variable, element)] #adding if the constraint has support for element and variable.
                        variable.prune_value(element)

                pruned_vars += new_pruned

                if variable.cur_domain_size() == 0:
                    return False, pruned_vars

    else:
        for c in constraints:
            if (newVar in c.get_scope()) and (c.get_n_unasgn() == 1): #checking newvar conditions.

                variable = c.get_unasgn_vars()[0] #getting unassigned vars.

                new_pruned = [] #new list for current domain.

                domain = variable.cur_domain()

                for element in domain:
                    if not c.has_support(variable,element):
                        new_pruned += [(variable, element)]
                        variable.prune_value(element)

                pruned_vars += new_pruned

                if variable.cur_domain_size() == 0:
                    return False, pruned_vars

    return True, pruned_vars #if falses fail returning true with all the pruned vars.


def prop_GAC(csp, newVar=None):
    '''Do GAC propagation. If newVar is None we do initial GAC enforce
       processing all constraints. Otherwise we do GAC enforce with
       constraints containing newVar on GAC Queue'''
    global queue
    pruned = []
    queue = []
    if newVar is None:
        constraints = csp.get_all_cons()
    else:
        constraints = csp.get_cons_with_var(newVar)

    for c in constraints:
        queue.append(c)

    status, newPruned = GAC_Enforce(csp)
    pruned += newPruned
    if status == 1:
        return False, pruned
    return True, pruned


def GAC_Enforce(csp):
    """
     GAC_Queue contains all contraints one of whose variables has had its domain reduced.
     At the root of the search tree first we fun GAC_Enfore with all constraints on GAC_Queue.
    """

    global queue
    pruned = []

    while queue: #queue

        constraint = queue[0]

        queue = queue[1:] #popping first element.

        scope = constraint.get_scope()

        for variable in scope:

            domain = variable.cur_domain() #current domain

            for value in domain: #iterating through the domain.

                if not constraint.has_support(variable, value):

                    pruned.append((variable, value)) #adding to the pruned list.
                    variable.prune_value(value)

                    if variable.cur_domain_size() == 0: #if domain is empty

                        queue = [] #clear queue
                        return 1, pruned

                    else:

                        cons = csp.get_cons_with_var(variable)
                        cons.remove(constraint)

                        for c in cons:
                            queue.append(c)
    return 0, pruned
