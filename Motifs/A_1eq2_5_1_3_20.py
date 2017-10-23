'''
FUNC:A_1eq2_5_1_3_20
PDB:1eq2
EC:5.1.3.20
RESI:ser,tyr,lys
LOCI:a-116,140,144;
'''
import motifFunctions as cmd
SER_TYR = { 
	'distances':
		[[9.62, 8.32, 8.26, 7.4, 7.27, 6.21, 6.13, 5.43], [9.33, 8.04, 8.18, 6.92, 7.28, 5.7, 5.95, 5.31]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'TYR', 9.62), ('CB', 'SER', 'CG', 'TYR', 8.32), ('CB', 'SER', 'CD1', 'TYR', 8.26), ('CB', 'SER', 'CD2', 'TYR', 7.4), ('CB', 'SER', 'CE1', 'TYR', 7.27), ('CB', 'SER', 'CE2', 'TYR', 6.21), ('CB', 'SER', 'CZ', 'TYR', 6.13), ('CB', 'SER', 'OH', 'TYR', 5.43)], [('OG', 'SER', 'CB', 'TYR', 9.33), ('OG', 'SER', 'CG', 'TYR', 8.04), ('OG', 'SER', 'CD1', 'TYR', 8.18), ('OG', 'SER', 'CD2', 'TYR', 6.92), ('OG', 'SER', 'CE1', 'TYR', 7.28), ('OG', 'SER', 'CE2', 'TYR', 5.7), ('OG', 'SER', 'CZ', 'TYR', 5.95), ('OG', 'SER', 'OH', 'TYR', 5.31)]]}
LYS_TYR = { 
	'distances':
		[[8.75, 7.97, 7.72, 7.85, 7.32, 7.46, 7.19, 7.39], [7.98, 7.0, 6.5, 6.98, 5.94, 6.47, 5.93, 6.13], [9.1, 8.03, 7.25, 8.09, 6.44, 7.41, 6.55, 6.41], [8.93, 7.73, 6.71, 7.88, 5.68, 7.11, 5.95, 5.67], [10.3, 9.11, 7.98, 9.29, 6.91, 8.45, 7.22, 6.71]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'TYR', 8.75), ('CB', 'LYS', 'CG', 'TYR', 7.97), ('CB', 'LYS', 'CD1', 'TYR', 7.72), ('CB', 'LYS', 'CD2', 'TYR', 7.85), ('CB', 'LYS', 'CE1', 'TYR', 7.32), ('CB', 'LYS', 'CE2', 'TYR', 7.46), ('CB', 'LYS', 'CZ', 'TYR', 7.19), ('CB', 'LYS', 'OH', 'TYR', 7.39)], [('CG', 'LYS', 'CB', 'TYR', 7.98), ('CG', 'LYS', 'CG', 'TYR', 7.0), ('CG', 'LYS', 'CD1', 'TYR', 6.5), ('CG', 'LYS', 'CD2', 'TYR', 6.98), ('CG', 'LYS', 'CE1', 'TYR', 5.94), ('CG', 'LYS', 'CE2', 'TYR', 6.47), ('CG', 'LYS', 'CZ', 'TYR', 5.93), ('CG', 'LYS', 'OH', 'TYR', 6.13)], [('CD', 'LYS', 'CB', 'TYR', 9.1), ('CD', 'LYS', 'CG', 'TYR', 8.03), ('CD', 'LYS', 'CD1', 'TYR', 7.25), ('CD', 'LYS', 'CD2', 'TYR', 8.09), ('CD', 'LYS', 'CE1', 'TYR', 6.44), ('CD', 'LYS', 'CE2', 'TYR', 7.41), ('CD', 'LYS', 'CZ', 'TYR', 6.55), ('CD', 'LYS', 'OH', 'TYR', 6.41)], [('CE', 'LYS', 'CB', 'TYR', 8.93), ('CE', 'LYS', 'CG', 'TYR', 7.73), ('CE', 'LYS', 'CD1', 'TYR', 6.71), ('CE', 'LYS', 'CD2', 'TYR', 7.88), ('CE', 'LYS', 'CE1', 'TYR', 5.68), ('CE', 'LYS', 'CE2', 'TYR', 7.11), ('CE', 'LYS', 'CZ', 'TYR', 5.95), ('CE', 'LYS', 'OH', 'TYR', 5.67)], [('NZ', 'LYS', 'CB', 'TYR', 10.3), ('NZ', 'LYS', 'CG', 'TYR', 9.11), ('NZ', 'LYS', 'CD1', 'TYR', 7.98), ('NZ', 'LYS', 'CD2', 'TYR', 9.29), ('NZ', 'LYS', 'CE1', 'TYR', 6.91), ('NZ', 'LYS', 'CE2', 'TYR', 8.45), ('NZ', 'LYS', 'CZ', 'TYR', 7.22), ('NZ', 'LYS', 'OH', 'TYR', 6.71)]]}
LYS_SER = { 
	'distances':
		[[6.47, 7.52], [6.1, 7.04], [6.51, 7.62], [6.77, 7.67], [7.69, 8.67]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'SER', 6.47), ('CB', 'LYS', 'OG', 'SER', 7.52)], [('CG', 'LYS', 'CB', 'SER', 6.1), ('CG', 'LYS', 'OG', 'SER', 7.04)], [('CD', 'LYS', 'CB', 'SER', 6.51), ('CD', 'LYS', 'OG', 'SER', 7.62)], [('CE', 'LYS', 'CB', 'SER', 6.77), ('CE', 'LYS', 'OG', 'SER', 7.67)], [('NZ', 'LYS', 'CB', 'SER', 7.69), ('NZ', 'LYS', 'OG', 'SER', 8.67)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(SER_TYR, d, 'A_1eq2_5_1_3_20')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(LYS_TYR, d, 'A_1eq2_5_1_3_20')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(LYS_SER, d, 'A_1eq2_5_1_3_20')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'SER_TYR' :  match1,
		'LYS_TYR' :  match2,
		'LYS_SER' :  match3}