# NEEDED = [
#     ('ASP', 'GLU', 0),     ('ASP', 'GLU'),
#     ('ASP', 'ASP', 0),     ('ASP', 'ASP'),
#     ('GLU', 'ASP', 0),     ('GLU', 'ASP'),
#     ('GLU', 'ASP', 0),
#     ('ASP', 'ASP', 0),     ('ASPI', 'ASP'),
#     ('ASP', 'GLU', 0),     ('ASPI', 'GLU')]
#
# HAVE = [
#     ('ASP', 'GLU'),
#     ('ASP', 'ASP'),
#     ('GLU', 'ASP'),
#     ('ASPI', 'ASP'),
#     ('ASPI', 'GLU')]
#
# i = 0
# CURR_ELE = {}
# CURR_COLLECTED = {}
# NEEDS = {}
# HAS = {}
# NEEDS[i] = {'ASP': ['ASP', 'ASPi'], 'GLU': ['GLU']}
#
#
# CURR_ELE[i] = ('ASP', 'GLU')
# CURR_COLLECTED[i] = ['ASP']
# HAS[i] = []
#
# i+=1
# '======================================='
#
# CURR_ELE[i] = ('ASP', 'ASP')
# CURR_COLLECTED[i] = ['ASP']
# HAS[i] = [('ASP', 'GLU')]
#
# i+=1
# '======================================='
#
# CURR_ELE[i] = ('GLU', 'ASP')
# CURR_COLLECTED[i] = ['ASP', 'GLU']
# HAS[i] = [('ASP', 'GLU'), ('ASP', 'ASP')]
#
# i+=1
# '======================================='
#
# CURR_ELE[i] = ('ASPI', 'ASP')
# CURR_COLLECTED[i] = ['ASP', 'GLU', 'ASPI']
# HAS[i] = [('ASP', 'GLU'), ('ASP', 'ASP'), ('GLU', 'ASP')]
#
# i+=1
# '======================================='
#
# CURR_ELE[i] = ('ASPI', 'GLU')
# CURR_COLLECTED[i] = ['ASP', 'GLU', 'ASPI']
# HAS[i] = [('ASP', 'GLU'), ('ASP', 'ASP'), ('GLU', 'ASP'), ('ASPI', 'ASP')]
#
# '======================================='
#
#
# print "RESULTS of ", "1a0j"
# print



def main():

    # line = "		[[('CB', 'ASP', 'CB', 'ASP', 11.59), ('CB', 'ASP', 'CG', 'ASP', 10.18), ('CB', 'ASP', 'OD1', 'ASP', 10.03), ('CB', 'ASP', 'OD2', 'ASP', 9.38), ('CB', 'ASP', 'O', 'ASP', 14.2), ('CB', 'ASP', 'C', 'ASP', 13.1), ('CB', 'ASP', 'CA', 'ASP', 12.34), ('CB', 'ASP', 'N', 'ASP', 13.41)], [('CG', 'ASP', 'CB', 'ASP', 10.47), ('CG', 'ASP', 'CG', 'ASP', 9.07), ('CG', 'ASP', 'OD1', 'ASP', 8.84), ('CG', 'ASP', 'OD2', 'ASP', 8.4), ('CG', 'ASP', 'O', 'ASP', 13.18), ('CG', 'ASP', 'C', 'ASP', 12.14), ('CG', 'ASP', 'CA', 'ASP', 11.37), ('CG', 'ASP', 'N', 'ASP', 12.44)], [('OD1', 'ASP', 'CB', 'ASP', 10.87), ('OD1', 'ASP', 'CG', 'ASP', 9.53), ('OD1', 'ASP', 'OD1', 'ASP', 9.23), ('OD1', 'ASP', 'OD2', 'ASP', 8.97), ('OD1', 'ASP', 'O', 'ASP', 13.69), ('OD1', 'ASP', 'C', 'ASP', 12.71), ('OD1', 'ASP', 'CA', 'ASP', 11.91), ('OD1', 'ASP', 'N', 'ASP', 12.92)], [('OD2', 'ASP', 'CB', 'ASP', 9.33), ('OD2', 'ASP', 'CG', 'ASP', 7.9), ('OD2', 'ASP', 'OD1', 'ASP', 7.68), ('OD2', 'ASP', 'OD2', 'ASP', 7.23), ('OD2', 'ASP', 'O', 'ASP', 11.97), ('OD2', 'ASP', 'C', 'ASP', 10.92), ('OD2', 'ASP', 'CA', 'ASP', 10.19), ('OD2', 'ASP', 'N', 'ASP', 11.3)], [('O', 'ASP', 'CB', 'ASP', 14.55), ('O', 'ASP', 'CG', 'ASP', 13.12), ('O', 'ASP', 'OD1', 'ASP', 12.9), ('O', 'ASP', 'OD2', 'ASP', 12.34), ('O', 'ASP', 'O', 'ASP', 17.1), ('O', 'ASP', 'C', 'ASP', 15.99), ('O', 'ASP', 'CA', 'ASP', 15.29), ('O', 'ASP', 'N', 'ASP', 16.38)], [('C', 'ASP', 'CB', 'ASP', 13.97), ('C', 'ASP', 'CG', 'ASP', 12.6), ('C', 'ASP', 'OD1', 'ASP', 12.5), ('C', 'ASP', 'OD2', 'ASP', 11.73), ('C', 'ASP', 'O', 'ASP', 16.61), ('C', 'ASP', 'C', 'ASP', 15.49), ('C', 'ASP', 'CA', 'ASP', 14.69), ('C', 'ASP', 'N', 'ASP', 15.7)], [('CA', 'ASP', 'CB', 'ASP', 12.67), ('CA', 'ASP', 'CG', 'ASP', 11.33), ('CA', 'ASP', 'OD1', 'ASP', 11.25), ('CA', 'ASP', 'OD2', 'ASP', 10.49), ('CA', 'ASP', 'O', 'ASP', 15.42), ('CA', 'ASP', 'C', 'ASP', 14.33), ('CA', 'ASP', 'CA', 'ASP', 13.46), ('CA', 'ASP', 'N', 'ASP', 14.44)], [('N', 'ASP', 'CB', 'ASP', 12.41), ('N', 'ASP', 'CG', 'ASP', 11.17), ('N', 'ASP', 'OD1', 'ASP', 11.27), ('N', 'ASP', 'OD2', 'ASP', 10.25), ('N', 'ASP', 'O', 'ASP', 15.26), ('N', 'ASP', 'C', 'ASP', 14.15), ('N', 'ASP', 'CA', 'ASP', 13.15), ('N', 'ASP', 'N', 'ASP', 14.0)]]}\n"
    # line = "		[[7.57, 6.21, 5.68, 6.05], [7.69, 6.23, 5.97, 5.69], [6.91, 5.47, 5.51, 4.68], [8.98, 7.52, 7.29, 6.84], [7.87, 6.5, 6.66, 5.54], [9.01, 7.59, 7.57, 6.71]],\n"

    line = "		[[('CB', 'ASP', 'CB', 'ASP', 11.59), ('CB', 'ASP', 'CG', 'ASP', 10.18), ('CB', 'ASP', 'OD1', 'ASP', 10.03), ('CB', 'ASP', 'OD2', 'ASP', 9.38), ('CB', 'ASP', 'O', 'ASP', 14.2), ('CB', 'ASP', 'C', 'ASP', 13.1), ('CB', 'ASP', 'CA', 'ASP', 12.34), ('CB', 'ASP', 'N', 'ASP', 13.41)], [('CG', 'ASP', 'CB', 'ASP', 10.47), ('CG', 'ASP', 'CG', 'ASP', 9.07), ('CG', 'ASP', 'OD1', 'ASP', 8.84), ('CG', 'ASP', 'OD2', 'ASP', 8.4), ('CG', 'ASP', 'O', 'ASP', 13.18), ('CG', 'ASP', 'C', 'ASP', 12.14), ('CG', 'ASP', 'CA', 'ASP', 11.37), ('CG', 'ASP', 'N', 'ASP', 12.44)], [('OD1', 'ASP', 'CB', 'ASP', 10.87), ('OD1', 'ASP', 'CG', 'ASP', 9.53), ('OD1', 'ASP', 'OD1', 'ASP', 9.23), ('OD1', 'ASP', 'OD2', 'ASP', 8.97), ('OD1', 'ASP', 'O', 'ASP', 13.69), ('OD1', 'ASP', 'C', 'ASP', 12.71), ('OD1', 'ASP', 'CA', 'ASP', 11.91), ('OD1', 'ASP', 'N', 'ASP', 12.92)], [('OD2', 'ASP', 'CB', 'ASP', 9.33), ('OD2', 'ASP', 'CG', 'ASP', 7.9), ('OD2', 'ASP', 'OD1', 'ASP', 7.68), ('OD2', 'ASP', 'OD2', 'ASP', 7.23), ('OD2', 'ASP', 'O', 'ASP', 11.97), ('OD2', 'ASP', 'C', 'ASP', 10.92), ('OD2', 'ASP', 'CA', 'ASP', 10.19), ('OD2', 'ASP', 'N', 'ASP', 11.3)], [('O', 'ASP', 'CB', 'ASP', 14.55), ('O', 'ASP', 'CG', 'ASP', 13.12), ('O', 'ASP', 'OD1', 'ASP', 12.9), ('O', 'ASP', 'OD2', 'ASP', 12.34), ('O', 'ASP', 'O', 'ASP', 17.1), ('O', 'ASP', 'C', 'ASP', 15.99), ('O', 'ASP', 'CA', 'ASP', 15.29), ('O', 'ASP', 'N', 'ASP', 16.38)], [('C', 'ASP', 'CB', 'ASP', 13.97), ('C', 'ASP', 'CG', 'ASP', 12.6), ('C', 'ASP', 'OD1', 'ASP', 12.5), ('C', 'ASP', 'OD2', 'ASP', 11.73), ('C', 'ASP', 'O', 'ASP', 16.61), ('C', 'ASP', 'C', 'ASP', 15.49), ('C', 'ASP', 'CA', 'ASP', 14.69), ('C', 'ASP', 'N', 'ASP', 15.7)], [('CA', 'ASP', 'CB', 'ASP', 12.67), ('CA', 'ASP', 'CG', 'ASP', 11.33), ('CA', 'ASP', 'OD1', 'ASP', 11.25), ('CA', 'ASP', 'OD2', 'ASP', 10.49), ('CA', 'ASP', 'O', 'ASP', 15.42), ('CA', 'ASP', 'C', 'ASP', 14.33), ('CA', 'ASP', 'CA', 'ASP', 13.46), ('CA', 'ASP', 'N', 'ASP', 14.44)], [('N', 'ASP', 'CB', 'ASP', 12.41), ('N', 'ASP', 'CG', 'ASP', 11.17), ('N', 'ASP', 'OD1', 'ASP', 11.27), ('N', 'ASP', 'OD2', 'ASP', 10.25), ('N', 'ASP', 'O', 'ASP', 15.26), ('N', 'ASP', 'C', 'ASP', 14.15), ('N', 'ASP', 'CA', 'ASP', 13.15), ('N', 'ASP', 'N', 'ASP', 14.0)]]}\n"

    line = line[5:-5].split(")], [(")
    # for i in range(len(line)):
    #     if i == 0:
    #         line[i] += "]"
    #     elif i == len(line) - 1:
    #         line[i] = "[" + line[i]
    #     else:
    #         line[i] = "[" + line[i] + "]"

    i = 0
    for row in line:
        line[i] = row.split("), (")
        for e in range(len(line[i])):
            line[i][e] = "(" + line[i][e] + ")"
        i += 1




    for row in line:
        for ele in row:
            print ele
        print "\n"

if __name__ == '__main__':
    main()








