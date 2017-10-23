'''
FUNC:A_2phk_2_7_1_38
PDB:2phk
EC:2.7.1.38
RESI:asp,lys
LOCI:a-149,151;
'''
import motifFunctions as cmd
LYS_ASP = { 
	'distances':
		[[8.2, 7.62, 6.88, 8.18, 5.94, 6.53, 7.66, 8.86], [7.49, 6.72, 6.15, 7.05, 5.41, 6.28, 7.3, 8.63], [7.72, 6.63, 5.89, 6.81, 6.26, 7.05, 7.74, 9.16], [7.58, 6.32, 5.87, 6.13, 6.53, 7.45, 7.97, 9.42], [7.75, 6.31, 5.79, 5.98, 7.36, 8.12, 8.31, 9.76], [9.45, 9.19, 8.95, 9.5, 6.73, 7.61, 9.06, 10.02], [9.64, 9.29, 8.86, 9.72, 6.95, 7.7, 9.12, 10.13], [8.73, 8.43, 7.86, 9.05, 6.12, 6.66, 8.02, 9.02], [7.84, 7.83, 7.43, 8.55, 5.14, 5.56, 7.03, 7.87]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'ASP', 8.2), ('CB', 'LYS', 'CG', 'ASP', 7.62), ('CB', 'LYS', 'OD1', 'ASP', 6.88), ('CB', 'LYS', 'OD2', 'ASP', 8.18), ('CB', 'LYS', 'O', 'ASP', 5.94), ('CB', 'LYS', 'C', 'ASP', 6.53), ('CB', 'LYS', 'CA', 'ASP', 7.66), ('CB', 'LYS', 'N', 'ASP', 8.86)], [('CG', 'LYS', 'CB', 'ASP', 7.49), ('CG', 'LYS', 'CG', 'ASP', 6.72), ('CG', 'LYS', 'OD1', 'ASP', 6.15), ('CG', 'LYS', 'OD2', 'ASP', 7.05), ('CG', 'LYS', 'O', 'ASP', 5.41), ('CG', 'LYS', 'C', 'ASP', 6.28), ('CG', 'LYS', 'CA', 'ASP', 7.3), ('CG', 'LYS', 'N', 'ASP', 8.63)], [('CD', 'LYS', 'CB', 'ASP', 7.72), ('CD', 'LYS', 'CG', 'ASP', 6.63), ('CD', 'LYS', 'OD1', 'ASP', 5.89), ('CD', 'LYS', 'OD2', 'ASP', 6.81), ('CD', 'LYS', 'O', 'ASP', 6.26), ('CD', 'LYS', 'C', 'ASP', 7.05), ('CD', 'LYS', 'CA', 'ASP', 7.74), ('CD', 'LYS', 'N', 'ASP', 9.16)], [('CE', 'LYS', 'CB', 'ASP', 7.58), ('CE', 'LYS', 'CG', 'ASP', 6.32), ('CE', 'LYS', 'OD1', 'ASP', 5.87), ('CE', 'LYS', 'OD2', 'ASP', 6.13), ('CE', 'LYS', 'O', 'ASP', 6.53), ('CE', 'LYS', 'C', 'ASP', 7.45), ('CE', 'LYS', 'CA', 'ASP', 7.97), ('CE', 'LYS', 'N', 'ASP', 9.42)], [('NZ', 'LYS', 'CB', 'ASP', 7.75), ('NZ', 'LYS', 'CG', 'ASP', 6.31), ('NZ', 'LYS', 'OD1', 'ASP', 5.79), ('NZ', 'LYS', 'OD2', 'ASP', 5.98), ('NZ', 'LYS', 'O', 'ASP', 7.36), ('NZ', 'LYS', 'C', 'ASP', 8.12), ('NZ', 'LYS', 'CA', 'ASP', 8.31), ('NZ', 'LYS', 'N', 'ASP', 9.76)], [('O', 'LYS', 'CB', 'ASP', 9.45), ('O', 'LYS', 'CG', 'ASP', 9.19), ('O', 'LYS', 'OD1', 'ASP', 8.95), ('O', 'LYS', 'OD2', 'ASP', 9.5), ('O', 'LYS', 'O', 'ASP', 6.73), ('O', 'LYS', 'C', 'ASP', 7.61), ('O', 'LYS', 'CA', 'ASP', 9.06), ('O', 'LYS', 'N', 'ASP', 10.02)], [('C', 'LYS', 'CB', 'ASP', 9.64), ('C', 'LYS', 'CG', 'ASP', 9.29), ('C', 'LYS', 'OD1', 'ASP', 8.86), ('C', 'LYS', 'OD2', 'ASP', 9.72), ('C', 'LYS', 'O', 'ASP', 6.95), ('C', 'LYS', 'C', 'ASP', 7.7), ('C', 'LYS', 'CA', 'ASP', 9.12), ('C', 'LYS', 'N', 'ASP', 10.13)], [('CA', 'LYS', 'CB', 'ASP', 8.73), ('CA', 'LYS', 'CG', 'ASP', 8.43), ('CA', 'LYS', 'OD1', 'ASP', 7.86), ('CA', 'LYS', 'OD2', 'ASP', 9.05), ('CA', 'LYS', 'O', 'ASP', 6.12), ('CA', 'LYS', 'C', 'ASP', 6.66), ('CA', 'LYS', 'CA', 'ASP', 8.02), ('CA', 'LYS', 'N', 'ASP', 9.02)], [('N', 'LYS', 'CB', 'ASP', 7.84), ('N', 'LYS', 'CG', 'ASP', 7.83), ('N', 'LYS', 'OD1', 'ASP', 7.43), ('N', 'LYS', 'OD2', 'ASP', 8.55), ('N', 'LYS', 'O', 'ASP', 5.14), ('N', 'LYS', 'C', 'ASP', 5.56), ('N', 'LYS', 'CA', 'ASP', 7.03), ('N', 'LYS', 'N', 'ASP', 7.87)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LYS_ASP, d, 'A_2phk_2_7_1_38')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'LYS_ASP' :  match1}