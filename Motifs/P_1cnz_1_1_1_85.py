'''
FUNC:P_1cnz_1_1_1_85
PDB:1cnz
EC:1.1.1.85
RESI:lys,asp,tyr
LOCI:a-195,227;b-145;
'''
import motifFunctions as cmd
LYS_ASP = { 
	'distances':
		[[9.74, 9.05, 9.87, 7.85], [9.08, 8.3, 9.02, 7.16], [7.62, 6.79, 7.52, 5.65], [7.47, 6.49, 6.96, 5.56], [6.7, 5.46, 5.69, 4.67]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'ASP', 9.74), ('CB', 'LYS', 'CG', 'ASP', 9.05), ('CB', 'LYS', 'OD1', 'ASP', 9.87), ('CB', 'LYS', 'OD2', 'ASP', 7.85)], [('CG', 'LYS', 'CB', 'ASP', 9.08), ('CG', 'LYS', 'CG', 'ASP', 8.3), ('CG', 'LYS', 'OD1', 'ASP', 9.02), ('CG', 'LYS', 'OD2', 'ASP', 7.16)], [('CD', 'LYS', 'CB', 'ASP', 7.62), ('CD', 'LYS', 'CG', 'ASP', 6.79), ('CD', 'LYS', 'OD1', 'ASP', 7.52), ('CD', 'LYS', 'OD2', 'ASP', 5.65)], [('CE', 'LYS', 'CB', 'ASP', 7.47), ('CE', 'LYS', 'CG', 'ASP', 6.49), ('CE', 'LYS', 'OD1', 'ASP', 6.96), ('CE', 'LYS', 'OD2', 'ASP', 5.56)], [('NZ', 'LYS', 'CB', 'ASP', 6.7), ('NZ', 'LYS', 'CG', 'ASP', 5.46), ('NZ', 'LYS', 'OD1', 'ASP', 5.69), ('NZ', 'LYS', 'OD2', 'ASP', 4.67)]]}
LYS_TYR = { 
	'distances':
		[[10.16, 9.07, 9.5, 7.86, 8.87, 7.03, 7.63, 7.34], [9.09, 7.93, 8.21, 6.86, 7.55, 5.99, 6.42, 6.19], [9.82, 8.53, 8.48, 7.63, 7.57, 6.56, 6.53, 5.91], [9.21, 7.93, 7.67, 7.33, 6.77, 6.36, 6.03, 5.54], [10.4, 9.14, 8.69, 8.69, 7.73, 7.74, 7.19, 6.55]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'TYR', 10.16), ('CB', 'LYS', 'CG', 'TYR', 9.07), ('CB', 'LYS', 'CD1', 'TYR', 9.5), ('CB', 'LYS', 'CD2', 'TYR', 7.86), ('CB', 'LYS', 'CE1', 'TYR', 8.87), ('CB', 'LYS', 'CE2', 'TYR', 7.03), ('CB', 'LYS', 'CZ', 'TYR', 7.63), ('CB', 'LYS', 'OH', 'TYR', 7.34)], [('CG', 'LYS', 'CB', 'TYR', 9.09), ('CG', 'LYS', 'CG', 'TYR', 7.93), ('CG', 'LYS', 'CD1', 'TYR', 8.21), ('CG', 'LYS', 'CD2', 'TYR', 6.86), ('CG', 'LYS', 'CE1', 'TYR', 7.55), ('CG', 'LYS', 'CE2', 'TYR', 5.99), ('CG', 'LYS', 'CZ', 'TYR', 6.42), ('CG', 'LYS', 'OH', 'TYR', 6.19)], [('CD', 'LYS', 'CB', 'TYR', 9.82), ('CD', 'LYS', 'CG', 'TYR', 8.53), ('CD', 'LYS', 'CD1', 'TYR', 8.48), ('CD', 'LYS', 'CD2', 'TYR', 7.63), ('CD', 'LYS', 'CE1', 'TYR', 7.57), ('CD', 'LYS', 'CE2', 'TYR', 6.56), ('CD', 'LYS', 'CZ', 'TYR', 6.53), ('CD', 'LYS', 'OH', 'TYR', 5.91)], [('CE', 'LYS', 'CB', 'TYR', 9.21), ('CE', 'LYS', 'CG', 'TYR', 7.93), ('CE', 'LYS', 'CD1', 'TYR', 7.67), ('CE', 'LYS', 'CD2', 'TYR', 7.33), ('CE', 'LYS', 'CE1', 'TYR', 6.77), ('CE', 'LYS', 'CE2', 'TYR', 6.36), ('CE', 'LYS', 'CZ', 'TYR', 6.03), ('CE', 'LYS', 'OH', 'TYR', 5.54)], [('NZ', 'LYS', 'CB', 'TYR', 10.4), ('NZ', 'LYS', 'CG', 'TYR', 9.14), ('NZ', 'LYS', 'CD1', 'TYR', 8.69), ('NZ', 'LYS', 'CD2', 'TYR', 8.69), ('NZ', 'LYS', 'CE1', 'TYR', 7.73), ('NZ', 'LYS', 'CE2', 'TYR', 7.74), ('NZ', 'LYS', 'CZ', 'TYR', 7.19), ('NZ', 'LYS', 'OH', 'TYR', 6.55)]]}
ASP_TYR = { 
	'distances':
		[[13.5, 12.03, 11.24, 11.58, 9.9, 10.29, 9.36, 8.08], [13.01, 11.6, 10.87, 11.15, 9.61, 9.94, 9.08, 7.93], [13.4, 12.04, 11.24, 11.73, 10.04, 10.6, 9.69, 8.65], [12.41, 11.0, 10.43, 10.43, 9.21, 9.21, 8.52, 7.41]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'TYR', 13.5), ('CB', 'ASP', 'CG', 'TYR', 12.03), ('CB', 'ASP', 'CD1', 'TYR', 11.24), ('CB', 'ASP', 'CD2', 'TYR', 11.58), ('CB', 'ASP', 'CE1', 'TYR', 9.9), ('CB', 'ASP', 'CE2', 'TYR', 10.29), ('CB', 'ASP', 'CZ', 'TYR', 9.36), ('CB', 'ASP', 'OH', 'TYR', 8.08)], [('CG', 'ASP', 'CB', 'TYR', 13.01), ('CG', 'ASP', 'CG', 'TYR', 11.6), ('CG', 'ASP', 'CD1', 'TYR', 10.87), ('CG', 'ASP', 'CD2', 'TYR', 11.15), ('CG', 'ASP', 'CE1', 'TYR', 9.61), ('CG', 'ASP', 'CE2', 'TYR', 9.94), ('CG', 'ASP', 'CZ', 'TYR', 9.08), ('CG', 'ASP', 'OH', 'TYR', 7.93)], [('OD1', 'ASP', 'CB', 'TYR', 13.4), ('OD1', 'ASP', 'CG', 'TYR', 12.04), ('OD1', 'ASP', 'CD1', 'TYR', 11.24), ('OD1', 'ASP', 'CD2', 'TYR', 11.73), ('OD1', 'ASP', 'CE1', 'TYR', 10.04), ('OD1', 'ASP', 'CE2', 'TYR', 10.6), ('OD1', 'ASP', 'CZ', 'TYR', 9.69), ('OD1', 'ASP', 'OH', 'TYR', 8.65)], [('OD2', 'ASP', 'CB', 'TYR', 12.41), ('OD2', 'ASP', 'CG', 'TYR', 11.0), ('OD2', 'ASP', 'CD1', 'TYR', 10.43), ('OD2', 'ASP', 'CD2', 'TYR', 10.43), ('OD2', 'ASP', 'CE1', 'TYR', 9.21), ('OD2', 'ASP', 'CE2', 'TYR', 9.21), ('OD2', 'ASP', 'CZ', 'TYR', 8.52), ('OD2', 'ASP', 'OH', 'TYR', 7.41)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LYS_ASP, d, 'P_1cnz_1_1_1_85')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(LYS_TYR, d, 'P_1cnz_1_1_1_85')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_TYR, d, 'P_1cnz_1_1_1_85')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'LYS_ASP' :  match1,
		'LYS_TYR' :  match2,
		'ASP_TYR' :  match3}