'''
FUNC:A_1ofg_1_1_99_28
PDB:1ofg
EC:1.1.99.28
RESI:lys,tyr
LOCI:a-129,217;
'''
import motifFunctions as cmd
LYS_TYR = { 
	'distances':
		[[10.76, 9.79, 9.45, 9.48, 8.78, 8.82, 8.45, 8.16], [10.07, 8.93, 8.52, 8.53, 7.67, 7.68, 7.2, 6.73], [8.85, 7.71, 7.52, 7.14, 6.77, 6.33, 6.11, 5.85], [9.44, 8.33, 8.41, 7.47, 7.7, 6.61, 6.75, 6.4], [9.56, 8.34, 8.46, 7.29, 7.62, 6.22, 6.43, 5.86]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'TYR', 10.76), ('CB', 'LYS', 'CG', 'TYR', 9.79), ('CB', 'LYS', 'CD1', 'TYR', 9.45), ('CB', 'LYS', 'CD2', 'TYR', 9.48), ('CB', 'LYS', 'CE1', 'TYR', 8.78), ('CB', 'LYS', 'CE2', 'TYR', 8.82), ('CB', 'LYS', 'CZ', 'TYR', 8.45), ('CB', 'LYS', 'OH', 'TYR', 8.16)], [('CG', 'LYS', 'CB', 'TYR', 10.07), ('CG', 'LYS', 'CG', 'TYR', 8.93), ('CG', 'LYS', 'CD1', 'TYR', 8.52), ('CG', 'LYS', 'CD2', 'TYR', 8.53), ('CG', 'LYS', 'CE1', 'TYR', 7.67), ('CG', 'LYS', 'CE2', 'TYR', 7.68), ('CG', 'LYS', 'CZ', 'TYR', 7.2), ('CG', 'LYS', 'OH', 'TYR', 6.73)], [('CD', 'LYS', 'CB', 'TYR', 8.85), ('CD', 'LYS', 'CG', 'TYR', 7.71), ('CD', 'LYS', 'CD1', 'TYR', 7.52), ('CD', 'LYS', 'CD2', 'TYR', 7.14), ('CD', 'LYS', 'CE1', 'TYR', 6.77), ('CD', 'LYS', 'CE2', 'TYR', 6.33), ('CD', 'LYS', 'CZ', 'TYR', 6.11), ('CD', 'LYS', 'OH', 'TYR', 5.85)], [('CE', 'LYS', 'CB', 'TYR', 9.44), ('CE', 'LYS', 'CG', 'TYR', 8.33), ('CE', 'LYS', 'CD1', 'TYR', 8.41), ('CE', 'LYS', 'CD2', 'TYR', 7.47), ('CE', 'LYS', 'CE1', 'TYR', 7.7), ('CE', 'LYS', 'CE2', 'TYR', 6.61), ('CE', 'LYS', 'CZ', 'TYR', 6.75), ('CE', 'LYS', 'OH', 'TYR', 6.4)], [('NZ', 'LYS', 'CB', 'TYR', 9.56), ('NZ', 'LYS', 'CG', 'TYR', 8.34), ('NZ', 'LYS', 'CD1', 'TYR', 8.46), ('NZ', 'LYS', 'CD2', 'TYR', 7.29), ('NZ', 'LYS', 'CE1', 'TYR', 7.62), ('NZ', 'LYS', 'CE2', 'TYR', 6.22), ('NZ', 'LYS', 'CZ', 'TYR', 6.43), ('NZ', 'LYS', 'OH', 'TYR', 5.86)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LYS_TYR, d, 'A_1ofg_1_1_99_28')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'LYS_TYR' :  match1}