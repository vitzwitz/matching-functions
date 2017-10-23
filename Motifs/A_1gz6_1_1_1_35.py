'''
FUNC:A_1gz6_1_1_1_35
PDB:1gz6
EC:1.1.1.35
RESI:tyr,lys
LOCI:a-164,168;
'''
import motifFunctions as cmd
TYR_LYS = { 
	'distances':
		[[8.21, 7.36, 8.36, 8.38, 9.74, 11.26, 10.19, 8.9, 8.17], [7.56, 6.47, 7.36, 7.16, 8.53, 10.77, 9.82, 8.44, 7.98], [8.0, 6.67, 7.18, 6.65, 7.83, 11.09, 10.26, 8.78, 8.36], [7.04, 6.05, 7.13, 7.0, 8.45, 10.37, 9.45, 8.18, 7.99], [8.0, 6.53, 6.79, 5.91, 6.98, 11.06, 10.36, 8.89, 8.74], [7.03, 5.87, 6.73, 6.32, 7.69, 10.33, 9.56, 8.3, 8.39], [7.53, 6.13, 6.55, 5.72, 6.9, 10.69, 10.03, 8.66, 8.76], [8.08, 6.69, 6.81, 5.72, 6.61, 11.04, 10.55, 9.25, 9.56], [5.43, 5.2, 6.35, 7.16, 8.51, 8.06, 6.94, 5.75, 4.88], [6.52, 6.22, 7.43, 8.05, 9.45, 9.22, 8.06, 6.95, 6.06], [7.72, 7.09, 8.07, 8.39, 9.71, 10.46, 9.35, 8.11, 7.14], [8.91, 8.44, 9.44, 9.8, 11.09, 11.44, 10.29, 9.17, 8.05]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'LYS', 8.21), ('CB', 'TYR', 'CG', 'LYS', 7.36), ('CB', 'TYR', 'CD', 'LYS', 8.36), ('CB', 'TYR', 'CE', 'LYS', 8.38), ('CB', 'TYR', 'NZ', 'LYS', 9.74), ('CB', 'TYR', 'O', 'LYS', 11.26), ('CB', 'TYR', 'C', 'LYS', 10.19), ('CB', 'TYR', 'CA', 'LYS', 8.9), ('CB', 'TYR', 'N', 'LYS', 8.17)], [('CG', 'TYR', 'CB', 'LYS', 7.56), ('CG', 'TYR', 'CG', 'LYS', 6.47), ('CG', 'TYR', 'CD', 'LYS', 7.36), ('CG', 'TYR', 'CE', 'LYS', 7.16), ('CG', 'TYR', 'NZ', 'LYS', 8.53), ('CG', 'TYR', 'O', 'LYS', 10.77), ('CG', 'TYR', 'C', 'LYS', 9.82), ('CG', 'TYR', 'CA', 'LYS', 8.44), ('CG', 'TYR', 'N', 'LYS', 7.98)], [('CD1', 'TYR', 'CB', 'LYS', 8.0), ('CD1', 'TYR', 'CG', 'LYS', 6.67), ('CD1', 'TYR', 'CD', 'LYS', 7.18), ('CD1', 'TYR', 'CE', 'LYS', 6.65), ('CD1', 'TYR', 'NZ', 'LYS', 7.83), ('CD1', 'TYR', 'O', 'LYS', 11.09), ('CD1', 'TYR', 'C', 'LYS', 10.26), ('CD1', 'TYR', 'CA', 'LYS', 8.78), ('CD1', 'TYR', 'N', 'LYS', 8.36)], [('CD2', 'TYR', 'CB', 'LYS', 7.04), ('CD2', 'TYR', 'CG', 'LYS', 6.05), ('CD2', 'TYR', 'CD', 'LYS', 7.13), ('CD2', 'TYR', 'CE', 'LYS', 7.0), ('CD2', 'TYR', 'NZ', 'LYS', 8.45), ('CD2', 'TYR', 'O', 'LYS', 10.37), ('CD2', 'TYR', 'C', 'LYS', 9.45), ('CD2', 'TYR', 'CA', 'LYS', 8.18), ('CD2', 'TYR', 'N', 'LYS', 7.99)], [('CE1', 'TYR', 'CB', 'LYS', 8.0), ('CE1', 'TYR', 'CG', 'LYS', 6.53), ('CE1', 'TYR', 'CD', 'LYS', 6.79), ('CE1', 'TYR', 'CE', 'LYS', 5.91), ('CE1', 'TYR', 'NZ', 'LYS', 6.98), ('CE1', 'TYR', 'O', 'LYS', 11.06), ('CE1', 'TYR', 'C', 'LYS', 10.36), ('CE1', 'TYR', 'CA', 'LYS', 8.89), ('CE1', 'TYR', 'N', 'LYS', 8.74)], [('CE2', 'TYR', 'CB', 'LYS', 7.03), ('CE2', 'TYR', 'CG', 'LYS', 5.87), ('CE2', 'TYR', 'CD', 'LYS', 6.73), ('CE2', 'TYR', 'CE', 'LYS', 6.32), ('CE2', 'TYR', 'NZ', 'LYS', 7.69), ('CE2', 'TYR', 'O', 'LYS', 10.33), ('CE2', 'TYR', 'C', 'LYS', 9.56), ('CE2', 'TYR', 'CA', 'LYS', 8.3), ('CE2', 'TYR', 'N', 'LYS', 8.39)], [('CZ', 'TYR', 'CB', 'LYS', 7.53), ('CZ', 'TYR', 'CG', 'LYS', 6.13), ('CZ', 'TYR', 'CD', 'LYS', 6.55), ('CZ', 'TYR', 'CE', 'LYS', 5.72), ('CZ', 'TYR', 'NZ', 'LYS', 6.9), ('CZ', 'TYR', 'O', 'LYS', 10.69), ('CZ', 'TYR', 'C', 'LYS', 10.03), ('CZ', 'TYR', 'CA', 'LYS', 8.66), ('CZ', 'TYR', 'N', 'LYS', 8.76)], [('OH', 'TYR', 'CB', 'LYS', 8.08), ('OH', 'TYR', 'CG', 'LYS', 6.69), ('OH', 'TYR', 'CD', 'LYS', 6.81), ('OH', 'TYR', 'CE', 'LYS', 5.72), ('OH', 'TYR', 'NZ', 'LYS', 6.61), ('OH', 'TYR', 'O', 'LYS', 11.04), ('OH', 'TYR', 'C', 'LYS', 10.55), ('OH', 'TYR', 'CA', 'LYS', 9.25), ('OH', 'TYR', 'N', 'LYS', 9.56)], [('O', 'TYR', 'CB', 'LYS', 5.43), ('O', 'TYR', 'CG', 'LYS', 5.2), ('O', 'TYR', 'CD', 'LYS', 6.35), ('O', 'TYR', 'CE', 'LYS', 7.16), ('O', 'TYR', 'NZ', 'LYS', 8.51), ('O', 'TYR', 'O', 'LYS', 8.06), ('O', 'TYR', 'C', 'LYS', 6.94), ('O', 'TYR', 'CA', 'LYS', 5.75), ('O', 'TYR', 'N', 'LYS', 4.88)], [('C', 'TYR', 'CB', 'LYS', 6.52), ('C', 'TYR', 'CG', 'LYS', 6.22), ('C', 'TYR', 'CD', 'LYS', 7.43), ('C', 'TYR', 'CE', 'LYS', 8.05), ('C', 'TYR', 'NZ', 'LYS', 9.45), ('C', 'TYR', 'O', 'LYS', 9.22), ('C', 'TYR', 'C', 'LYS', 8.06), ('C', 'TYR', 'CA', 'LYS', 6.95), ('C', 'TYR', 'N', 'LYS', 6.06)], [('CA', 'TYR', 'CB', 'LYS', 7.72), ('CA', 'TYR', 'CG', 'LYS', 7.09), ('CA', 'TYR', 'CD', 'LYS', 8.07), ('CA', 'TYR', 'CE', 'LYS', 8.39), ('CA', 'TYR', 'NZ', 'LYS', 9.71), ('CA', 'TYR', 'O', 'LYS', 10.46), ('CA', 'TYR', 'C', 'LYS', 9.35), ('CA', 'TYR', 'CA', 'LYS', 8.11), ('CA', 'TYR', 'N', 'LYS', 7.14)], [('N', 'TYR', 'CB', 'LYS', 8.91), ('N', 'TYR', 'CG', 'LYS', 8.44), ('N', 'TYR', 'CD', 'LYS', 9.44), ('N', 'TYR', 'CE', 'LYS', 9.8), ('N', 'TYR', 'NZ', 'LYS', 11.09), ('N', 'TYR', 'O', 'LYS', 11.44), ('N', 'TYR', 'C', 'LYS', 10.29), ('N', 'TYR', 'CA', 'LYS', 9.17), ('N', 'TYR', 'N', 'LYS', 8.05)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(TYR_LYS, d, 'A_1gz6_1_1_1_35')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'TYR_LYS' :  match1}