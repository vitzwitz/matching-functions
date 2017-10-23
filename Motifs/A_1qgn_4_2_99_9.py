'''
FUNC:A_1qgn_4_2_99_9
PDB:1qgn
EC:4.2.99.9
RESI:tyr,asp,lys
LOCI:a-163,236,261;
'''
import motifFunctions as cmd
TYR_ASP = { 
	'distances':
		[[9.52, 8.95, 9.87, 7.76], [10.17, 9.35, 10.09, 8.11], [10.5, 9.57, 10.19, 8.4], [10.74, 9.84, 10.52, 8.59], [11.33, 10.25, 10.7, 9.11], [11.56, 10.5, 11.02, 9.28], [11.83, 10.69, 11.1, 9.51], [12.8, 11.55, 11.82, 10.44]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'ASP', 9.52), ('CB', 'TYR', 'CG', 'ASP', 8.95), ('CB', 'TYR', 'OD1', 'ASP', 9.87), ('CB', 'TYR', 'OD2', 'ASP', 7.76)], [('CG', 'TYR', 'CB', 'ASP', 10.17), ('CG', 'TYR', 'CG', 'ASP', 9.35), ('CG', 'TYR', 'OD1', 'ASP', 10.09), ('CG', 'TYR', 'OD2', 'ASP', 8.11)], [('CD1', 'TYR', 'CB', 'ASP', 10.5), ('CD1', 'TYR', 'CG', 'ASP', 9.57), ('CD1', 'TYR', 'OD1', 'ASP', 10.19), ('CD1', 'TYR', 'OD2', 'ASP', 8.4)], [('CD2', 'TYR', 'CB', 'ASP', 10.74), ('CD2', 'TYR', 'CG', 'ASP', 9.84), ('CD2', 'TYR', 'OD1', 'ASP', 10.52), ('CD2', 'TYR', 'OD2', 'ASP', 8.59)], [('CE1', 'TYR', 'CB', 'ASP', 11.33), ('CE1', 'TYR', 'CG', 'ASP', 10.25), ('CE1', 'TYR', 'OD1', 'ASP', 10.7), ('CE1', 'TYR', 'OD2', 'ASP', 9.11)], [('CE2', 'TYR', 'CB', 'ASP', 11.56), ('CE2', 'TYR', 'CG', 'ASP', 10.5), ('CE2', 'TYR', 'OD1', 'ASP', 11.02), ('CE2', 'TYR', 'OD2', 'ASP', 9.28)], [('CZ', 'TYR', 'CB', 'ASP', 11.83), ('CZ', 'TYR', 'CG', 'ASP', 10.69), ('CZ', 'TYR', 'OD1', 'ASP', 11.1), ('CZ', 'TYR', 'OD2', 'ASP', 9.51)], [('OH', 'TYR', 'CB', 'ASP', 12.8), ('OH', 'TYR', 'CG', 'ASP', 11.55), ('OH', 'TYR', 'OD1', 'ASP', 11.82), ('OH', 'TYR', 'OD2', 'ASP', 10.44)]]}
ASP_LYS = { 
	'distances':
		[[13.0, 12.24, 13.15, 12.9, 11.51], [11.59, 10.78, 11.67, 11.4, 10.02], [10.73, 10.04, 11.07, 10.95, 9.66], [11.49, 10.51, 11.24, 10.8, 9.37]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'LYS', 13.0), ('CB', 'ASP', 'CG', 'LYS', 12.24), ('CB', 'ASP', 'CD', 'LYS', 13.15), ('CB', 'ASP', 'CE', 'LYS', 12.9), ('CB', 'ASP', 'NZ', 'LYS', 11.51)], [('CG', 'ASP', 'CB', 'LYS', 11.59), ('CG', 'ASP', 'CG', 'LYS', 10.78), ('CG', 'ASP', 'CD', 'LYS', 11.67), ('CG', 'ASP', 'CE', 'LYS', 11.4), ('CG', 'ASP', 'NZ', 'LYS', 10.02)], [('OD1', 'ASP', 'CB', 'LYS', 10.73), ('OD1', 'ASP', 'CG', 'LYS', 10.04), ('OD1', 'ASP', 'CD', 'LYS', 11.07), ('OD1', 'ASP', 'CE', 'LYS', 10.95), ('OD1', 'ASP', 'NZ', 'LYS', 9.66)], [('OD2', 'ASP', 'CB', 'LYS', 11.49), ('OD2', 'ASP', 'CG', 'LYS', 10.51), ('OD2', 'ASP', 'CD', 'LYS', 11.24), ('OD2', 'ASP', 'CE', 'LYS', 10.8), ('OD2', 'ASP', 'NZ', 'LYS', 9.37)]]}
TYR_LYS = { 
	'distances':
		[[13.97, 12.61, 12.49, 11.48, 10.13], [13.02, 11.61, 11.35, 10.24, 8.98], [12.25, 10.89, 10.51, 9.49, 8.27], [13.07, 11.6, 11.3, 10.05, 8.88], [11.5, 10.11, 9.55, 8.44, 7.37], [12.39, 10.89, 10.44, 9.1, 8.08], [11.59, 10.12, 9.52, 8.22, 7.26], [11.09, 9.62, 8.84, 7.46, 6.78]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'LYS', 13.97), ('CB', 'TYR', 'CG', 'LYS', 12.61), ('CB', 'TYR', 'CD', 'LYS', 12.49), ('CB', 'TYR', 'CE', 'LYS', 11.48), ('CB', 'TYR', 'NZ', 'LYS', 10.13)], [('CG', 'TYR', 'CB', 'LYS', 13.02), ('CG', 'TYR', 'CG', 'LYS', 11.61), ('CG', 'TYR', 'CD', 'LYS', 11.35), ('CG', 'TYR', 'CE', 'LYS', 10.24), ('CG', 'TYR', 'NZ', 'LYS', 8.98)], [('CD1', 'TYR', 'CB', 'LYS', 12.25), ('CD1', 'TYR', 'CG', 'LYS', 10.89), ('CD1', 'TYR', 'CD', 'LYS', 10.51), ('CD1', 'TYR', 'CE', 'LYS', 9.49), ('CD1', 'TYR', 'NZ', 'LYS', 8.27)], [('CD2', 'TYR', 'CB', 'LYS', 13.07), ('CD2', 'TYR', 'CG', 'LYS', 11.6), ('CD2', 'TYR', 'CD', 'LYS', 11.3), ('CD2', 'TYR', 'CE', 'LYS', 10.05), ('CD2', 'TYR', 'NZ', 'LYS', 8.88)], [('CE1', 'TYR', 'CB', 'LYS', 11.5), ('CE1', 'TYR', 'CG', 'LYS', 10.11), ('CE1', 'TYR', 'CD', 'LYS', 9.55), ('CE1', 'TYR', 'CE', 'LYS', 8.44), ('CE1', 'TYR', 'NZ', 'LYS', 7.37)], [('CE2', 'TYR', 'CB', 'LYS', 12.39), ('CE2', 'TYR', 'CG', 'LYS', 10.89), ('CE2', 'TYR', 'CD', 'LYS', 10.44), ('CE2', 'TYR', 'CE', 'LYS', 9.1), ('CE2', 'TYR', 'NZ', 'LYS', 8.08)], [('CZ', 'TYR', 'CB', 'LYS', 11.59), ('CZ', 'TYR', 'CG', 'LYS', 10.12), ('CZ', 'TYR', 'CD', 'LYS', 9.52), ('CZ', 'TYR', 'CE', 'LYS', 8.22), ('CZ', 'TYR', 'NZ', 'LYS', 7.26)], [('OH', 'TYR', 'CB', 'LYS', 11.09), ('OH', 'TYR', 'CG', 'LYS', 9.62), ('OH', 'TYR', 'CD', 'LYS', 8.84), ('OH', 'TYR', 'CE', 'LYS', 7.46), ('OH', 'TYR', 'NZ', 'LYS', 6.78)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(TYR_ASP, d, 'A_1qgn_4_2_99_9')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_LYS, d, 'A_1qgn_4_2_99_9')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(TYR_LYS, d, 'A_1qgn_4_2_99_9')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'TYR_ASP' :  match1,
		'ASP_LYS' :  match2,
		'TYR_LYS' :  match3}