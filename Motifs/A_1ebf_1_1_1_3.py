'''
FUNC:A_1ebf_1_1_1_3
PDB:1ebf
EC:1.1.1.3
RESI:asp,lys
LOCI:a-219,223;
'''
import motifFunctions as cmd
LYS_ASP = { 
	'distances':
		[[8.79, 8.17, 8.51, 7.68, 5.84, 6.89, 8.2, 9.26], [7.89, 7.04, 7.39, 6.41, 5.33, 6.4, 7.48, 8.73], [7.63, 6.58, 6.58, 6.18, 5.82, 6.6, 7.61, 8.93], [7.38, 6.06, 6.0, 5.49, 6.3, 6.97, 7.62, 9.05], [7.75, 6.32, 5.83, 6.05, 7.37, 7.8, 8.33, 9.74], [11.72, 11.25, 11.7, 10.68, 8.48, 9.55, 10.86, 11.69], [10.64, 10.28, 10.78, 9.77, 7.36, 8.39, 9.73, 10.5], [9.42, 8.97, 9.52, 8.35, 6.18, 7.32, 8.56, 9.47], [8.61, 8.39, 9.14, 7.79, 5.28, 6.4, 7.54, 8.32]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'ASP', 8.79), ('CB', 'LYS', 'CG', 'ASP', 8.17), ('CB', 'LYS', 'OD1', 'ASP', 8.51), ('CB', 'LYS', 'OD2', 'ASP', 7.68), ('CB', 'LYS', 'O', 'ASP', 5.84), ('CB', 'LYS', 'C', 'ASP', 6.89), ('CB', 'LYS', 'CA', 'ASP', 8.2), ('CB', 'LYS', 'N', 'ASP', 9.26)], [('CG', 'LYS', 'CB', 'ASP', 7.89), ('CG', 'LYS', 'CG', 'ASP', 7.04), ('CG', 'LYS', 'OD1', 'ASP', 7.39), ('CG', 'LYS', 'OD2', 'ASP', 6.41), ('CG', 'LYS', 'O', 'ASP', 5.33), ('CG', 'LYS', 'C', 'ASP', 6.4), ('CG', 'LYS', 'CA', 'ASP', 7.48), ('CG', 'LYS', 'N', 'ASP', 8.73)], [('CD', 'LYS', 'CB', 'ASP', 7.63), ('CD', 'LYS', 'CG', 'ASP', 6.58), ('CD', 'LYS', 'OD1', 'ASP', 6.58), ('CD', 'LYS', 'OD2', 'ASP', 6.18), ('CD', 'LYS', 'O', 'ASP', 5.82), ('CD', 'LYS', 'C', 'ASP', 6.6), ('CD', 'LYS', 'CA', 'ASP', 7.61), ('CD', 'LYS', 'N', 'ASP', 8.93)], [('CE', 'LYS', 'CB', 'ASP', 7.38), ('CE', 'LYS', 'CG', 'ASP', 6.06), ('CE', 'LYS', 'OD1', 'ASP', 6.0), ('CE', 'LYS', 'OD2', 'ASP', 5.49), ('CE', 'LYS', 'O', 'ASP', 6.3), ('CE', 'LYS', 'C', 'ASP', 6.97), ('CE', 'LYS', 'CA', 'ASP', 7.62), ('CE', 'LYS', 'N', 'ASP', 9.05)], [('NZ', 'LYS', 'CB', 'ASP', 7.75), ('NZ', 'LYS', 'CG', 'ASP', 6.32), ('NZ', 'LYS', 'OD1', 'ASP', 5.83), ('NZ', 'LYS', 'OD2', 'ASP', 6.05), ('NZ', 'LYS', 'O', 'ASP', 7.37), ('NZ', 'LYS', 'C', 'ASP', 7.8), ('NZ', 'LYS', 'CA', 'ASP', 8.33), ('NZ', 'LYS', 'N', 'ASP', 9.74)], [('O', 'LYS', 'CB', 'ASP', 11.72), ('O', 'LYS', 'CG', 'ASP', 11.25), ('O', 'LYS', 'OD1', 'ASP', 11.7), ('O', 'LYS', 'OD2', 'ASP', 10.68), ('O', 'LYS', 'O', 'ASP', 8.48), ('O', 'LYS', 'C', 'ASP', 9.55), ('O', 'LYS', 'CA', 'ASP', 10.86), ('O', 'LYS', 'N', 'ASP', 11.69)], [('C', 'LYS', 'CB', 'ASP', 10.64), ('C', 'LYS', 'CG', 'ASP', 10.28), ('C', 'LYS', 'OD1', 'ASP', 10.78), ('C', 'LYS', 'OD2', 'ASP', 9.77), ('C', 'LYS', 'O', 'ASP', 7.36), ('C', 'LYS', 'C', 'ASP', 8.39), ('C', 'LYS', 'CA', 'ASP', 9.73), ('C', 'LYS', 'N', 'ASP', 10.5)], [('CA', 'LYS', 'CB', 'ASP', 9.42), ('CA', 'LYS', 'CG', 'ASP', 8.97), ('CA', 'LYS', 'OD1', 'ASP', 9.52), ('CA', 'LYS', 'OD2', 'ASP', 8.35), ('CA', 'LYS', 'O', 'ASP', 6.18), ('CA', 'LYS', 'C', 'ASP', 7.32), ('CA', 'LYS', 'CA', 'ASP', 8.56), ('CA', 'LYS', 'N', 'ASP', 9.47)], [('N', 'LYS', 'CB', 'ASP', 8.61), ('N', 'LYS', 'CG', 'ASP', 8.39), ('N', 'LYS', 'OD1', 'ASP', 9.14), ('N', 'LYS', 'OD2', 'ASP', 7.79), ('N', 'LYS', 'O', 'ASP', 5.28), ('N', 'LYS', 'C', 'ASP', 6.4), ('N', 'LYS', 'CA', 'ASP', 7.54), ('N', 'LYS', 'N', 'ASP', 8.32)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LYS_ASP, d, 'A_1ebf_1_1_1_3')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'LYS_ASP' :  match1}