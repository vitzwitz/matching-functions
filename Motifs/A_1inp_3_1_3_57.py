'''
FUNC:A_1inp_3_1_3_57
PDB:1inp
EC:3.1.3.57
RESI:lys,thr
LOCI:a-37,158;
'''
import motifFunctions as cmd
LYS_THR = { 
	'distances':
		[[9.31, 8.65, 9.72, 11.0, 10.76, 10.67, 11.29], [8.3, 7.45, 8.73, 10.3, 9.88, 9.66, 10.09], [7.4, 6.42, 8.12, 9.17, 8.67, 8.6, 9.0], [6.36, 5.67, 7.21, 7.83, 7.49, 7.55, 8.2], [5.83, 5.05, 7.02, 6.87, 6.42, 6.7, 7.29], [12.48, 11.67, 12.87, 14.15, 13.87, 13.82, 14.3], [11.48, 10.61, 11.97, 13.12, 12.79, 12.78, 13.23], [10.5, 9.76, 11.07, 11.89, 11.68, 11.77, 12.37], [10.11, 9.38, 10.91, 11.12, 10.95, 11.24, 11.87]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'THR', 9.31), ('CB', 'LYS', 'OG1', 'THR', 8.65), ('CB', 'LYS', 'CG2', 'THR', 9.72), ('CB', 'LYS', 'O', 'THR', 11.0), ('CB', 'LYS', 'C', 'THR', 10.76), ('CB', 'LYS', 'CA', 'THR', 10.67), ('CB', 'LYS', 'N', 'THR', 11.29)], [('CG', 'LYS', 'CB', 'THR', 8.3), ('CG', 'LYS', 'OG1', 'THR', 7.45), ('CG', 'LYS', 'CG2', 'THR', 8.73), ('CG', 'LYS', 'O', 'THR', 10.3), ('CG', 'LYS', 'C', 'THR', 9.88), ('CG', 'LYS', 'CA', 'THR', 9.66), ('CG', 'LYS', 'N', 'THR', 10.09)], [('CD', 'LYS', 'CB', 'THR', 7.4), ('CD', 'LYS', 'OG1', 'THR', 6.42), ('CD', 'LYS', 'CG2', 'THR', 8.12), ('CD', 'LYS', 'O', 'THR', 9.17), ('CD', 'LYS', 'C', 'THR', 8.67), ('CD', 'LYS', 'CA', 'THR', 8.6), ('CD', 'LYS', 'N', 'THR', 9.0)], [('CE', 'LYS', 'CB', 'THR', 6.36), ('CE', 'LYS', 'OG1', 'THR', 5.67), ('CE', 'LYS', 'CG2', 'THR', 7.21), ('CE', 'LYS', 'O', 'THR', 7.83), ('CE', 'LYS', 'C', 'THR', 7.49), ('CE', 'LYS', 'CA', 'THR', 7.55), ('CE', 'LYS', 'N', 'THR', 8.2)], [('NZ', 'LYS', 'CB', 'THR', 5.83), ('NZ', 'LYS', 'OG1', 'THR', 5.05), ('NZ', 'LYS', 'CG2', 'THR', 7.02), ('NZ', 'LYS', 'O', 'THR', 6.87), ('NZ', 'LYS', 'C', 'THR', 6.42), ('NZ', 'LYS', 'CA', 'THR', 6.7), ('NZ', 'LYS', 'N', 'THR', 7.29)], [('O', 'LYS', 'CB', 'THR', 12.48), ('O', 'LYS', 'OG1', 'THR', 11.67), ('O', 'LYS', 'CG2', 'THR', 12.87), ('O', 'LYS', 'O', 'THR', 14.15), ('O', 'LYS', 'C', 'THR', 13.87), ('O', 'LYS', 'CA', 'THR', 13.82), ('O', 'LYS', 'N', 'THR', 14.3)], [('C', 'LYS', 'CB', 'THR', 11.48), ('C', 'LYS', 'OG1', 'THR', 10.61), ('C', 'LYS', 'CG2', 'THR', 11.97), ('C', 'LYS', 'O', 'THR', 13.12), ('C', 'LYS', 'C', 'THR', 12.79), ('C', 'LYS', 'CA', 'THR', 12.78), ('C', 'LYS', 'N', 'THR', 13.23)], [('CA', 'LYS', 'CB', 'THR', 10.5), ('CA', 'LYS', 'OG1', 'THR', 9.76), ('CA', 'LYS', 'CG2', 'THR', 11.07), ('CA', 'LYS', 'O', 'THR', 11.89), ('CA', 'LYS', 'C', 'THR', 11.68), ('CA', 'LYS', 'CA', 'THR', 11.77), ('CA', 'LYS', 'N', 'THR', 12.37)], [('N', 'LYS', 'CB', 'THR', 10.11), ('N', 'LYS', 'OG1', 'THR', 9.38), ('N', 'LYS', 'CG2', 'THR', 10.91), ('N', 'LYS', 'O', 'THR', 11.12), ('N', 'LYS', 'C', 'THR', 10.95), ('N', 'LYS', 'CA', 'THR', 11.24), ('N', 'LYS', 'N', 'THR', 11.87)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LYS_THR, d, 'A_1inp_3_1_3_57')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'LYS_THR' :  match1}