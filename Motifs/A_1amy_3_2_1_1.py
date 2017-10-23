'''
FUNC:A_1amy_3_2_1_1
PDB:1amy
EC:3.2.1.1
RESI:asp,glu
LOCI:a-179,204;
'''
import motifFunctions as cmd
ASP_GLU = { 
	'distances':
		[[7.78, 8.43, 7.8, 6.86, 8.57, 8.73, 9.38, 8.87, 8.71], [8.11, 8.44, 7.49, 6.48, 8.06, 8.86, 9.64, 9.33, 9.43], [7.71, 7.79, 6.72, 5.85, 7.12, 8.7, 9.41, 9.06, 9.37], [9.05, 9.35, 8.31, 7.21, 8.85, 9.42, 10.33, 10.19, 10.28], [7.9, 8.76, 8.32, 7.19, 9.33, 7.52, 8.43, 8.44, 8.09], [6.87, 7.65, 7.16, 6.05, 8.17, 6.84, 7.71, 7.6, 7.42], [6.62, 7.48, 7.09, 6.15, 8.06, 7.42, 8.04, 7.55, 7.3], [7.09, 8.22, 8.12, 7.3, 9.17, 7.94, 8.41, 7.76, 7.15]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLU', 7.78), ('CB', 'ASP', 'CG', 'GLU', 8.43), ('CB', 'ASP', 'CD', 'GLU', 7.8), ('CB', 'ASP', 'OE1', 'GLU', 6.86), ('CB', 'ASP', 'OE2', 'GLU', 8.57), ('CB', 'ASP', 'O', 'GLU', 8.73), ('CB', 'ASP', 'C', 'GLU', 9.38), ('CB', 'ASP', 'CA', 'GLU', 8.87), ('CB', 'ASP', 'N', 'GLU', 8.71)], [('CG', 'ASP', 'CB', 'GLU', 8.11), ('CG', 'ASP', 'CG', 'GLU', 8.44), ('CG', 'ASP', 'CD', 'GLU', 7.49), ('CG', 'ASP', 'OE1', 'GLU', 6.48), ('CG', 'ASP', 'OE2', 'GLU', 8.06), ('CG', 'ASP', 'O', 'GLU', 8.86), ('CG', 'ASP', 'C', 'GLU', 9.64), ('CG', 'ASP', 'CA', 'GLU', 9.33), ('CG', 'ASP', 'N', 'GLU', 9.43)], [('OD1', 'ASP', 'CB', 'GLU', 7.71), ('OD1', 'ASP', 'CG', 'GLU', 7.79), ('OD1', 'ASP', 'CD', 'GLU', 6.72), ('OD1', 'ASP', 'OE1', 'GLU', 5.85), ('OD1', 'ASP', 'OE2', 'GLU', 7.12), ('OD1', 'ASP', 'O', 'GLU', 8.7), ('OD1', 'ASP', 'C', 'GLU', 9.41), ('OD1', 'ASP', 'CA', 'GLU', 9.06), ('OD1', 'ASP', 'N', 'GLU', 9.37)], [('OD2', 'ASP', 'CB', 'GLU', 9.05), ('OD2', 'ASP', 'CG', 'GLU', 9.35), ('OD2', 'ASP', 'CD', 'GLU', 8.31), ('OD2', 'ASP', 'OE1', 'GLU', 7.21), ('OD2', 'ASP', 'OE2', 'GLU', 8.85), ('OD2', 'ASP', 'O', 'GLU', 9.42), ('OD2', 'ASP', 'C', 'GLU', 10.33), ('OD2', 'ASP', 'CA', 'GLU', 10.19), ('OD2', 'ASP', 'N', 'GLU', 10.28)], [('O', 'ASP', 'CB', 'GLU', 7.9), ('O', 'ASP', 'CG', 'GLU', 8.76), ('O', 'ASP', 'CD', 'GLU', 8.32), ('O', 'ASP', 'OE1', 'GLU', 7.19), ('O', 'ASP', 'OE2', 'GLU', 9.33), ('O', 'ASP', 'O', 'GLU', 7.52), ('O', 'ASP', 'C', 'GLU', 8.43), ('O', 'ASP', 'CA', 'GLU', 8.44), ('O', 'ASP', 'N', 'GLU', 8.09)], [('C', 'ASP', 'CB', 'GLU', 6.87), ('C', 'ASP', 'CG', 'GLU', 7.65), ('C', 'ASP', 'CD', 'GLU', 7.16), ('C', 'ASP', 'OE1', 'GLU', 6.05), ('C', 'ASP', 'OE2', 'GLU', 8.17), ('C', 'ASP', 'O', 'GLU', 6.84), ('C', 'ASP', 'C', 'GLU', 7.71), ('C', 'ASP', 'CA', 'GLU', 7.6), ('C', 'ASP', 'N', 'GLU', 7.42)], [('CA', 'ASP', 'CB', 'GLU', 6.62), ('CA', 'ASP', 'CG', 'GLU', 7.48), ('CA', 'ASP', 'CD', 'GLU', 7.09), ('CA', 'ASP', 'OE1', 'GLU', 6.15), ('CA', 'ASP', 'OE2', 'GLU', 8.06), ('CA', 'ASP', 'O', 'GLU', 7.42), ('CA', 'ASP', 'C', 'GLU', 8.04), ('CA', 'ASP', 'CA', 'GLU', 7.55), ('CA', 'ASP', 'N', 'GLU', 7.3)], [('N', 'ASP', 'CB', 'GLU', 7.09), ('N', 'ASP', 'CG', 'GLU', 8.22), ('N', 'ASP', 'CD', 'GLU', 8.12), ('N', 'ASP', 'OE1', 'GLU', 7.3), ('N', 'ASP', 'OE2', 'GLU', 9.17), ('N', 'ASP', 'O', 'GLU', 7.94), ('N', 'ASP', 'C', 'GLU', 8.41), ('N', 'ASP', 'CA', 'GLU', 7.76), ('N', 'ASP', 'N', 'GLU', 7.15)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_GLU, d, 'A_1amy_3_2_1_1')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_GLU' :  match1}