'''
FUNC:A_1vzz_5_3_3_1
PDB:1vzz
EC:5.3.3.1
RESI:tyr,asp,leu
LOCI:a-16,40,103;
'''
import motifFunctions as cmd
TYR_ASP = { 
	'distances':
		[[14.54, 14.14, 15.1, 12.96], [13.09, 12.68, 13.65, 11.49], [12.44, 11.88, 12.76, 10.66], [12.52, 12.25, 13.3, 11.11], [11.15, 10.55, 11.43, 9.33], [11.24, 10.98, 12.03, 9.85], [10.48, 10.05, 11.03, 8.86], [9.26, 8.8, 9.77, 7.61]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'ASP', 14.54), ('CB', 'TYR', 'CG', 'ASP', 14.14), ('CB', 'TYR', 'OD1', 'ASP', 15.1), ('CB', 'TYR', 'OD2', 'ASP', 12.96)], [('CG', 'TYR', 'CB', 'ASP', 13.09), ('CG', 'TYR', 'CG', 'ASP', 12.68), ('CG', 'TYR', 'OD1', 'ASP', 13.65), ('CG', 'TYR', 'OD2', 'ASP', 11.49)], [('CD1', 'TYR', 'CB', 'ASP', 12.44), ('CD1', 'TYR', 'CG', 'ASP', 11.88), ('CD1', 'TYR', 'OD1', 'ASP', 12.76), ('CD1', 'TYR', 'OD2', 'ASP', 10.66)], [('CD2', 'TYR', 'CB', 'ASP', 12.52), ('CD2', 'TYR', 'CG', 'ASP', 12.25), ('CD2', 'TYR', 'OD1', 'ASP', 13.3), ('CD2', 'TYR', 'OD2', 'ASP', 11.11)], [('CE1', 'TYR', 'CB', 'ASP', 11.15), ('CE1', 'TYR', 'CG', 'ASP', 10.55), ('CE1', 'TYR', 'OD1', 'ASP', 11.43), ('CE1', 'TYR', 'OD2', 'ASP', 9.33)], [('CE2', 'TYR', 'CB', 'ASP', 11.24), ('CE2', 'TYR', 'CG', 'ASP', 10.98), ('CE2', 'TYR', 'OD1', 'ASP', 12.03), ('CE2', 'TYR', 'OD2', 'ASP', 9.85)], [('CZ', 'TYR', 'CB', 'ASP', 10.48), ('CZ', 'TYR', 'CG', 'ASP', 10.05), ('CZ', 'TYR', 'OD1', 'ASP', 11.03), ('CZ', 'TYR', 'OD2', 'ASP', 8.86)], [('OH', 'TYR', 'CB', 'ASP', 9.26), ('OH', 'TYR', 'CG', 'ASP', 8.8), ('OH', 'TYR', 'OD1', 'ASP', 9.77), ('OH', 'TYR', 'OD2', 'ASP', 7.61)]]}
TYR_LEU = { 
	'distances':
		[[9.71, 9.56, 8.22, 10.11], [8.93, 8.53, 7.12, 9.0], [8.06, 7.58, 6.11, 8.26], [9.41, 8.82, 7.47, 9.01], [7.7, 6.9, 5.4, 7.49], [9.12, 8.28, 6.97, 8.32], [8.28, 7.31, 5.93, 7.52], [8.4, 7.17, 5.98, 7.2]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'LEU', 9.71), ('CB', 'TYR', 'CG', 'LEU', 9.56), ('CB', 'TYR', 'CD1', 'LEU', 8.22), ('CB', 'TYR', 'CD2', 'LEU', 10.11)], [('CG', 'TYR', 'CB', 'LEU', 8.93), ('CG', 'TYR', 'CG', 'LEU', 8.53), ('CG', 'TYR', 'CD1', 'LEU', 7.12), ('CG', 'TYR', 'CD2', 'LEU', 9.0)], [('CD1', 'TYR', 'CB', 'LEU', 8.06), ('CD1', 'TYR', 'CG', 'LEU', 7.58), ('CD1', 'TYR', 'CD1', 'LEU', 6.11), ('CD1', 'TYR', 'CD2', 'LEU', 8.26)], [('CD2', 'TYR', 'CB', 'LEU', 9.41), ('CD2', 'TYR', 'CG', 'LEU', 8.82), ('CD2', 'TYR', 'CD1', 'LEU', 7.47), ('CD2', 'TYR', 'CD2', 'LEU', 9.01)], [('CE1', 'TYR', 'CB', 'LEU', 7.7), ('CE1', 'TYR', 'CG', 'LEU', 6.9), ('CE1', 'TYR', 'CD1', 'LEU', 5.4), ('CE1', 'TYR', 'CD2', 'LEU', 7.49)], [('CE2', 'TYR', 'CB', 'LEU', 9.12), ('CE2', 'TYR', 'CG', 'LEU', 8.28), ('CE2', 'TYR', 'CD1', 'LEU', 6.97), ('CE2', 'TYR', 'CD2', 'LEU', 8.32)], [('CZ', 'TYR', 'CB', 'LEU', 8.28), ('CZ', 'TYR', 'CG', 'LEU', 7.31), ('CZ', 'TYR', 'CD1', 'LEU', 5.93), ('CZ', 'TYR', 'CD2', 'LEU', 7.52)], [('OH', 'TYR', 'CB', 'LEU', 8.4), ('OH', 'TYR', 'CG', 'LEU', 7.17), ('OH', 'TYR', 'CD1', 'LEU', 5.98), ('OH', 'TYR', 'CD2', 'LEU', 7.2)]]}
LEU_ASP = { 
	'distances':
		[[10.45, 9.96, 10.62, 9.14], [9.14, 8.58, 9.3, 7.69], [9.59, 8.98, 9.77, 7.91], [8.17, 7.9, 8.75, 7.13]],
	'comparisons':
		[[('CB', 'LEU', 'CB', 'ASP', 10.45), ('CB', 'LEU', 'CG', 'ASP', 9.96), ('CB', 'LEU', 'OD1', 'ASP', 10.62), ('CB', 'LEU', 'OD2', 'ASP', 9.14)], [('CG', 'LEU', 'CB', 'ASP', 9.14), ('CG', 'LEU', 'CG', 'ASP', 8.58), ('CG', 'LEU', 'OD1', 'ASP', 9.3), ('CG', 'LEU', 'OD2', 'ASP', 7.69)], [('CD1', 'LEU', 'CB', 'ASP', 9.59), ('CD1', 'LEU', 'CG', 'ASP', 8.98), ('CD1', 'LEU', 'OD1', 'ASP', 9.77), ('CD1', 'LEU', 'OD2', 'ASP', 7.91)], [('CD2', 'LEU', 'CB', 'ASP', 8.17), ('CD2', 'LEU', 'CG', 'ASP', 7.9), ('CD2', 'LEU', 'OD1', 'ASP', 8.75), ('CD2', 'LEU', 'OD2', 'ASP', 7.13)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(TYR_ASP, d, 'A_1vzz_5_3_3_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(TYR_LEU, d, 'A_1vzz_5_3_3_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(LEU_ASP, d, 'A_1vzz_5_3_3_1')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'TYR_ASP' :  match1,
		'TYR_LEU' :  match2,
		'LEU_ASP' :  match3}