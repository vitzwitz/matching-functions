'''
FUNC:A_2ebn_3_2_1_96
PDB:2ebn
EC:3.2.1.96
RESI:asp,glu
LOCI:a-130,132;
'''
import motifFunctions as cmd
ASP_GLU = { 
	'distances':
		[[7.61, 7.31, 7.46, 8.64, 6.58, 8.43, 8.78, 8.06, 7.21], [6.66, 6.17, 6.06, 7.21, 5.1, 8.14, 8.27, 7.44, 6.88], [5.78, 5.09, 5.21, 6.42, 4.48, 7.65, 7.57, 6.53, 6.02], [7.19, 6.72, 6.22, 7.2, 5.07, 8.77, 8.9, 8.19, 7.85], [6.63, 6.91, 7.77, 8.94, 7.46, 6.31, 6.82, 6.34, 5.16], [6.93, 6.83, 7.66, 8.88, 7.28, 7.23, 7.53, 6.73, 5.48], [7.83, 7.47, 7.96, 9.19, 7.29, 8.49, 8.79, 7.95, 6.83], [9.12, 8.89, 9.41, 10.64, 8.7, 9.3, 9.78, 9.09, 7.87]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLU', 7.61), ('CB', 'ASP', 'CG', 'GLU', 7.31), ('CB', 'ASP', 'CD', 'GLU', 7.46), ('CB', 'ASP', 'OE1', 'GLU', 8.64), ('CB', 'ASP', 'OE2', 'GLU', 6.58), ('CB', 'ASP', 'O', 'GLU', 8.43), ('CB', 'ASP', 'C', 'GLU', 8.78), ('CB', 'ASP', 'CA', 'GLU', 8.06), ('CB', 'ASP', 'N', 'GLU', 7.21)], [('CG', 'ASP', 'CB', 'GLU', 6.66), ('CG', 'ASP', 'CG', 'GLU', 6.17), ('CG', 'ASP', 'CD', 'GLU', 6.06), ('CG', 'ASP', 'OE1', 'GLU', 7.21), ('CG', 'ASP', 'OE2', 'GLU', 5.1), ('CG', 'ASP', 'O', 'GLU', 8.14), ('CG', 'ASP', 'C', 'GLU', 8.27), ('CG', 'ASP', 'CA', 'GLU', 7.44), ('CG', 'ASP', 'N', 'GLU', 6.88)], [('OD1', 'ASP', 'CB', 'GLU', 5.78), ('OD1', 'ASP', 'CG', 'GLU', 5.09), ('OD1', 'ASP', 'CD', 'GLU', 5.21), ('OD1', 'ASP', 'OE1', 'GLU', 6.42), ('OD1', 'ASP', 'OE2', 'GLU', 4.48), ('OD1', 'ASP', 'O', 'GLU', 7.65), ('OD1', 'ASP', 'C', 'GLU', 7.57), ('OD1', 'ASP', 'CA', 'GLU', 6.53), ('OD1', 'ASP', 'N', 'GLU', 6.02)], [('OD2', 'ASP', 'CB', 'GLU', 7.19), ('OD2', 'ASP', 'CG', 'GLU', 6.72), ('OD2', 'ASP', 'CD', 'GLU', 6.22), ('OD2', 'ASP', 'OE1', 'GLU', 7.2), ('OD2', 'ASP', 'OE2', 'GLU', 5.07), ('OD2', 'ASP', 'O', 'GLU', 8.77), ('OD2', 'ASP', 'C', 'GLU', 8.9), ('OD2', 'ASP', 'CA', 'GLU', 8.19), ('OD2', 'ASP', 'N', 'GLU', 7.85)], [('O', 'ASP', 'CB', 'GLU', 6.63), ('O', 'ASP', 'CG', 'GLU', 6.91), ('O', 'ASP', 'CD', 'GLU', 7.77), ('O', 'ASP', 'OE1', 'GLU', 8.94), ('O', 'ASP', 'OE2', 'GLU', 7.46), ('O', 'ASP', 'O', 'GLU', 6.31), ('O', 'ASP', 'C', 'GLU', 6.82), ('O', 'ASP', 'CA', 'GLU', 6.34), ('O', 'ASP', 'N', 'GLU', 5.16)], [('C', 'ASP', 'CB', 'GLU', 6.93), ('C', 'ASP', 'CG', 'GLU', 6.83), ('C', 'ASP', 'CD', 'GLU', 7.66), ('C', 'ASP', 'OE1', 'GLU', 8.88), ('C', 'ASP', 'OE2', 'GLU', 7.28), ('C', 'ASP', 'O', 'GLU', 7.23), ('C', 'ASP', 'C', 'GLU', 7.53), ('C', 'ASP', 'CA', 'GLU', 6.73), ('C', 'ASP', 'N', 'GLU', 5.48)], [('CA', 'ASP', 'CB', 'GLU', 7.83), ('CA', 'ASP', 'CG', 'GLU', 7.47), ('CA', 'ASP', 'CD', 'GLU', 7.96), ('CA', 'ASP', 'OE1', 'GLU', 9.19), ('CA', 'ASP', 'OE2', 'GLU', 7.29), ('CA', 'ASP', 'O', 'GLU', 8.49), ('CA', 'ASP', 'C', 'GLU', 8.79), ('CA', 'ASP', 'CA', 'GLU', 7.95), ('CA', 'ASP', 'N', 'GLU', 6.83)], [('N', 'ASP', 'CB', 'GLU', 9.12), ('N', 'ASP', 'CG', 'GLU', 8.89), ('N', 'ASP', 'CD', 'GLU', 9.41), ('N', 'ASP', 'OE1', 'GLU', 10.64), ('N', 'ASP', 'OE2', 'GLU', 8.7), ('N', 'ASP', 'O', 'GLU', 9.3), ('N', 'ASP', 'C', 'GLU', 9.78), ('N', 'ASP', 'CA', 'GLU', 9.09), ('N', 'ASP', 'N', 'GLU', 7.87)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_GLU, d, 'A_2ebn_3_2_1_96')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_GLU' :  match1}