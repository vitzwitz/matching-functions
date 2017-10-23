'''
FUNC:P_1qj5_2_6_1_62
PDB:1qj5
EC:2.6.1.62
RESI:tyr,asp,lys
LOCI:a-144,245,274;
'''
import motifFunctions as cmd
TYR_ASP = { 
	'distances':
		[[10.32, 9.62, 10.15, 8.72], [10.76, 9.84, 10.28, 8.84], [11.77, 10.86, 11.36, 9.77], [10.41, 9.32, 9.58, 8.38], [12.35, 11.31, 11.72, 10.19], [11.11, 9.88, 10.04, 8.91], [12.05, 10.86, 11.12, 9.8], [12.9, 11.63, 11.8, 10.57]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'ASP', 10.32), ('CB', 'TYR', 'CG', 'ASP', 9.62), ('CB', 'TYR', 'OD1', 'ASP', 10.15), ('CB', 'TYR', 'OD2', 'ASP', 8.72)], [('CG', 'TYR', 'CB', 'ASP', 10.76), ('CG', 'TYR', 'CG', 'ASP', 9.84), ('CG', 'TYR', 'OD1', 'ASP', 10.28), ('CG', 'TYR', 'OD2', 'ASP', 8.84)], [('CD1', 'TYR', 'CB', 'ASP', 11.77), ('CD1', 'TYR', 'CG', 'ASP', 10.86), ('CD1', 'TYR', 'OD1', 'ASP', 11.36), ('CD1', 'TYR', 'OD2', 'ASP', 9.77)], [('CD2', 'TYR', 'CB', 'ASP', 10.41), ('CD2', 'TYR', 'CG', 'ASP', 9.32), ('CD2', 'TYR', 'OD1', 'ASP', 9.58), ('CD2', 'TYR', 'OD2', 'ASP', 8.38)], [('CE1', 'TYR', 'CB', 'ASP', 12.35), ('CE1', 'TYR', 'CG', 'ASP', 11.31), ('CE1', 'TYR', 'OD1', 'ASP', 11.72), ('CE1', 'TYR', 'OD2', 'ASP', 10.19)], [('CE2', 'TYR', 'CB', 'ASP', 11.11), ('CE2', 'TYR', 'CG', 'ASP', 9.88), ('CE2', 'TYR', 'OD1', 'ASP', 10.04), ('CE2', 'TYR', 'OD2', 'ASP', 8.91)], [('CZ', 'TYR', 'CB', 'ASP', 12.05), ('CZ', 'TYR', 'CG', 'ASP', 10.86), ('CZ', 'TYR', 'OD1', 'ASP', 11.12), ('CZ', 'TYR', 'OD2', 'ASP', 9.8)], [('OH', 'TYR', 'CB', 'ASP', 12.9), ('OH', 'TYR', 'CG', 'ASP', 11.63), ('OH', 'TYR', 'OD1', 'ASP', 11.8), ('OH', 'TYR', 'OD2', 'ASP', 10.57)]]}
ASP_LYS = { 
	'distances':
		[[13.38, 12.31, 12.78, 12.23, 11.06], [12.11, 10.97, 11.45, 10.88, 9.67], [11.04, 9.98, 10.56, 10.14, 9.03], [12.32, 11.06, 11.45, 10.74, 9.42]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'LYS', 13.38), ('CB', 'ASP', 'CG', 'LYS', 12.31), ('CB', 'ASP', 'CD', 'LYS', 12.78), ('CB', 'ASP', 'CE', 'LYS', 12.23), ('CB', 'ASP', 'NZ', 'LYS', 11.06)], [('CG', 'ASP', 'CB', 'LYS', 12.11), ('CG', 'ASP', 'CG', 'LYS', 10.97), ('CG', 'ASP', 'CD', 'LYS', 11.45), ('CG', 'ASP', 'CE', 'LYS', 10.88), ('CG', 'ASP', 'NZ', 'LYS', 9.67)], [('OD1', 'ASP', 'CB', 'LYS', 11.04), ('OD1', 'ASP', 'CG', 'LYS', 9.98), ('OD1', 'ASP', 'CD', 'LYS', 10.56), ('OD1', 'ASP', 'CE', 'LYS', 10.14), ('OD1', 'ASP', 'NZ', 'LYS', 9.03)], [('OD2', 'ASP', 'CB', 'LYS', 12.32), ('OD2', 'ASP', 'CG', 'LYS', 11.06), ('OD2', 'ASP', 'CD', 'LYS', 11.45), ('OD2', 'ASP', 'CE', 'LYS', 10.74), ('OD2', 'ASP', 'NZ', 'LYS', 9.42)]]}
TYR_LYS = { 
	'distances':
		[[14.12, 12.62, 12.03, 10.62, 9.49], [13.53, 12.0, 11.43, 10.0, 8.84], [14.47, 12.95, 12.37, 10.95, 9.8], [12.16, 10.64, 10.08, 8.67, 7.48], [14.14, 12.64, 12.1, 10.71, 9.59], [11.78, 10.26, 9.75, 8.38, 7.19], [12.86, 11.37, 10.87, 9.52, 8.39], [12.78, 11.34, 10.9, 9.64, 8.6]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'LYS', 14.12), ('CB', 'TYR', 'CG', 'LYS', 12.62), ('CB', 'TYR', 'CD', 'LYS', 12.03), ('CB', 'TYR', 'CE', 'LYS', 10.62), ('CB', 'TYR', 'NZ', 'LYS', 9.49)], [('CG', 'TYR', 'CB', 'LYS', 13.53), ('CG', 'TYR', 'CG', 'LYS', 12.0), ('CG', 'TYR', 'CD', 'LYS', 11.43), ('CG', 'TYR', 'CE', 'LYS', 10.0), ('CG', 'TYR', 'NZ', 'LYS', 8.84)], [('CD1', 'TYR', 'CB', 'LYS', 14.47), ('CD1', 'TYR', 'CG', 'LYS', 12.95), ('CD1', 'TYR', 'CD', 'LYS', 12.37), ('CD1', 'TYR', 'CE', 'LYS', 10.95), ('CD1', 'TYR', 'NZ', 'LYS', 9.8)], [('CD2', 'TYR', 'CB', 'LYS', 12.16), ('CD2', 'TYR', 'CG', 'LYS', 10.64), ('CD2', 'TYR', 'CD', 'LYS', 10.08), ('CD2', 'TYR', 'CE', 'LYS', 8.67), ('CD2', 'TYR', 'NZ', 'LYS', 7.48)], [('CE1', 'TYR', 'CB', 'LYS', 14.14), ('CE1', 'TYR', 'CG', 'LYS', 12.64), ('CE1', 'TYR', 'CD', 'LYS', 12.1), ('CE1', 'TYR', 'CE', 'LYS', 10.71), ('CE1', 'TYR', 'NZ', 'LYS', 9.59)], [('CE2', 'TYR', 'CB', 'LYS', 11.78), ('CE2', 'TYR', 'CG', 'LYS', 10.26), ('CE2', 'TYR', 'CD', 'LYS', 9.75), ('CE2', 'TYR', 'CE', 'LYS', 8.38), ('CE2', 'TYR', 'NZ', 'LYS', 7.19)], [('CZ', 'TYR', 'CB', 'LYS', 12.86), ('CZ', 'TYR', 'CG', 'LYS', 11.37), ('CZ', 'TYR', 'CD', 'LYS', 10.87), ('CZ', 'TYR', 'CE', 'LYS', 9.52), ('CZ', 'TYR', 'NZ', 'LYS', 8.39)], [('OH', 'TYR', 'CB', 'LYS', 12.78), ('OH', 'TYR', 'CG', 'LYS', 11.34), ('OH', 'TYR', 'CD', 'LYS', 10.9), ('OH', 'TYR', 'CE', 'LYS', 9.64), ('OH', 'TYR', 'NZ', 'LYS', 8.6)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(TYR_ASP, d, 'P_1qj5_2_6_1_62')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_LYS, d, 'P_1qj5_2_6_1_62')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(TYR_LYS, d, 'P_1qj5_2_6_1_62')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'TYR_ASP' :  match1,
		'ASP_LYS' :  match2,
		'TYR_LYS' :  match3}