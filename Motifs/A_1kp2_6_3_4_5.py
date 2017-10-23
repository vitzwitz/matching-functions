'''
FUNC:A_1kp2_6_3_4_5
PDB:1kp2
EC:6.3.4.5
RESI:arg,asp
LOCI:a-106,135;
'''
import motifFunctions as cmd
ASP_ARG = { 
	'distances':
		[[7.32, 6.18, 6.0, 5.24, 5.86, 7.01, 5.69, 9.88, 9.64, 8.55, 9.17], [6.8, 5.44, 5.27, 4.25, 4.82, 6.1, 4.54, 9.63, 9.21, 7.96, 8.34], [7.59, 6.13, 5.7, 4.4, 4.51, 5.78, 3.82, 10.39, 9.93, 8.58, 8.8], [5.88, 4.53, 4.73, 3.93, 4.83, 6.1, 4.83, 8.88, 8.34, 7.12, 7.43], [7.01, 6.62, 6.81, 6.89, 7.87, 8.73, 8.24, 8.76, 8.86, 8.3, 9.38], [7.63, 6.98, 7.12, 6.91, 7.79, 8.79, 7.93, 9.71, 9.68, 8.97, 9.91], [7.15, 6.25, 6.47, 6.03, 6.92, 8.06, 6.93, 9.67, 9.45, 8.54, 9.28], [8.13, 7.19, 7.57, 7.0, 7.84, 9.07, 7.65, 10.82, 10.49, 9.58, 10.19]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ARG', 7.32), ('CB', 'ASP', 'CG', 'ARG', 6.18), ('CB', 'ASP', 'CD', 'ARG', 6.0), ('CB', 'ASP', 'NE', 'ARG', 5.24), ('CB', 'ASP', 'CZ', 'ARG', 5.86), ('CB', 'ASP', 'NH1', 'ARG', 7.01), ('CB', 'ASP', 'NH2', 'ARG', 5.69), ('CB', 'ASP', 'O', 'ARG', 9.88), ('CB', 'ASP', 'C', 'ARG', 9.64), ('CB', 'ASP', 'CA', 'ARG', 8.55), ('CB', 'ASP', 'N', 'ARG', 9.17)], [('CG', 'ASP', 'CB', 'ARG', 6.8), ('CG', 'ASP', 'CG', 'ARG', 5.44), ('CG', 'ASP', 'CD', 'ARG', 5.27), ('CG', 'ASP', 'NE', 'ARG', 4.25), ('CG', 'ASP', 'CZ', 'ARG', 4.82), ('CG', 'ASP', 'NH1', 'ARG', 6.1), ('CG', 'ASP', 'NH2', 'ARG', 4.54), ('CG', 'ASP', 'O', 'ARG', 9.63), ('CG', 'ASP', 'C', 'ARG', 9.21), ('CG', 'ASP', 'CA', 'ARG', 7.96), ('CG', 'ASP', 'N', 'ARG', 8.34)], [('OD1', 'ASP', 'CB', 'ARG', 7.59), ('OD1', 'ASP', 'CG', 'ARG', 6.13), ('OD1', 'ASP', 'CD', 'ARG', 5.7), ('OD1', 'ASP', 'NE', 'ARG', 4.4), ('OD1', 'ASP', 'CZ', 'ARG', 4.51), ('OD1', 'ASP', 'NH1', 'ARG', 5.78), ('OD1', 'ASP', 'NH2', 'ARG', 3.82), ('OD1', 'ASP', 'O', 'ARG', 10.39), ('OD1', 'ASP', 'C', 'ARG', 9.93), ('OD1', 'ASP', 'CA', 'ARG', 8.58), ('OD1', 'ASP', 'N', 'ARG', 8.8)], [('OD2', 'ASP', 'CB', 'ARG', 5.88), ('OD2', 'ASP', 'CG', 'ARG', 4.53), ('OD2', 'ASP', 'CD', 'ARG', 4.73), ('OD2', 'ASP', 'NE', 'ARG', 3.93), ('OD2', 'ASP', 'CZ', 'ARG', 4.83), ('OD2', 'ASP', 'NH1', 'ARG', 6.1), ('OD2', 'ASP', 'NH2', 'ARG', 4.83), ('OD2', 'ASP', 'O', 'ARG', 8.88), ('OD2', 'ASP', 'C', 'ARG', 8.34), ('OD2', 'ASP', 'CA', 'ARG', 7.12), ('OD2', 'ASP', 'N', 'ARG', 7.43)], [('O', 'ASP', 'CB', 'ARG', 7.01), ('O', 'ASP', 'CG', 'ARG', 6.62), ('O', 'ASP', 'CD', 'ARG', 6.81), ('O', 'ASP', 'NE', 'ARG', 6.89), ('O', 'ASP', 'CZ', 'ARG', 7.87), ('O', 'ASP', 'NH1', 'ARG', 8.73), ('O', 'ASP', 'NH2', 'ARG', 8.24), ('O', 'ASP', 'O', 'ARG', 8.76), ('O', 'ASP', 'C', 'ARG', 8.86), ('O', 'ASP', 'CA', 'ARG', 8.3), ('O', 'ASP', 'N', 'ARG', 9.38)], [('C', 'ASP', 'CB', 'ARG', 7.63), ('C', 'ASP', 'CG', 'ARG', 6.98), ('C', 'ASP', 'CD', 'ARG', 7.12), ('C', 'ASP', 'NE', 'ARG', 6.91), ('C', 'ASP', 'CZ', 'ARG', 7.79), ('C', 'ASP', 'NH1', 'ARG', 8.79), ('C', 'ASP', 'NH2', 'ARG', 7.93), ('C', 'ASP', 'O', 'ARG', 9.71), ('C', 'ASP', 'C', 'ARG', 9.68), ('C', 'ASP', 'CA', 'ARG', 8.97), ('C', 'ASP', 'N', 'ARG', 9.91)], [('CA', 'ASP', 'CB', 'ARG', 7.15), ('CA', 'ASP', 'CG', 'ARG', 6.25), ('CA', 'ASP', 'CD', 'ARG', 6.47), ('CA', 'ASP', 'NE', 'ARG', 6.03), ('CA', 'ASP', 'CZ', 'ARG', 6.92), ('CA', 'ASP', 'NH1', 'ARG', 8.06), ('CA', 'ASP', 'NH2', 'ARG', 6.93), ('CA', 'ASP', 'O', 'ARG', 9.67), ('CA', 'ASP', 'C', 'ARG', 9.45), ('CA', 'ASP', 'CA', 'ARG', 8.54), ('CA', 'ASP', 'N', 'ARG', 9.28)], [('N', 'ASP', 'CB', 'ARG', 8.13), ('N', 'ASP', 'CG', 'ARG', 7.19), ('N', 'ASP', 'CD', 'ARG', 7.57), ('N', 'ASP', 'NE', 'ARG', 7.0), ('N', 'ASP', 'CZ', 'ARG', 7.84), ('N', 'ASP', 'NH1', 'ARG', 9.07), ('N', 'ASP', 'NH2', 'ARG', 7.65), ('N', 'ASP', 'O', 'ARG', 10.82), ('N', 'ASP', 'C', 'ARG', 10.49), ('N', 'ASP', 'CA', 'ARG', 9.58), ('N', 'ASP', 'N', 'ARG', 10.19)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_ARG, d, 'A_1kp2_6_3_4_5')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_ARG' :  match1}