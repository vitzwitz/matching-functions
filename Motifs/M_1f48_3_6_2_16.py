'''
FUNC:M_1f48_3_6_2_16
PDB:1f48
EC:3.6.2.16
RESI:gly,lys,mg
LOCI:a-18,21;a-592;
'''
import motifFunctions as cmd
GLY_MG = { 
	'distances':
		[[9.84], [9.25], [8.71], [8.11]],
	'comparisons':
		[[('O', 'GLY', 'MG', 'MG', 9.84)], [('C', 'GLY', 'MG', 'MG', 9.25)], [('CA', 'GLY', 'MG', 'MG', 8.71)], [('N', 'GLY', 'MG', 'MG', 8.11)]]}
LYS_MG = { 
	'distances':
		[[6.81], [7.8], [7.91], [6.84], [6.68]],
	'comparisons':
		[[('CB', 'LYS', 'MG', 'MG', 6.81)], [('CG', 'LYS', 'MG', 'MG', 7.8)], [('CD', 'LYS', 'MG', 'MG', 7.91)], [('CE', 'LYS', 'MG', 'MG', 6.84)], [('NZ', 'LYS', 'MG', 'MG', 6.68)]]}
LYS_GLY = { 
	'distances':
		[[9.52, 8.94, 9.33, 8.88], [9.39, 8.68, 9.17, 8.62], [10.28, 9.4, 9.66, 8.85], [9.99, 9.02, 8.99, 8.01], [8.61, 7.6, 7.53, 6.56]],
	'comparisons':
		[[('CB', 'LYS', 'O', 'GLY', 9.52), ('CB', 'LYS', 'C', 'GLY', 8.94), ('CB', 'LYS', 'CA', 'GLY', 9.33), ('CB', 'LYS', 'N', 'GLY', 8.88)], [('CG', 'LYS', 'O', 'GLY', 9.39), ('CG', 'LYS', 'C', 'GLY', 8.68), ('CG', 'LYS', 'CA', 'GLY', 9.17), ('CG', 'LYS', 'N', 'GLY', 8.62)], [('CD', 'LYS', 'O', 'GLY', 10.28), ('CD', 'LYS', 'C', 'GLY', 9.4), ('CD', 'LYS', 'CA', 'GLY', 9.66), ('CD', 'LYS', 'N', 'GLY', 8.85)], [('CE', 'LYS', 'O', 'GLY', 9.99), ('CE', 'LYS', 'C', 'GLY', 9.02), ('CE', 'LYS', 'CA', 'GLY', 8.99), ('CE', 'LYS', 'N', 'GLY', 8.01)], [('NZ', 'LYS', 'O', 'GLY', 8.61), ('NZ', 'LYS', 'C', 'GLY', 7.6), ('NZ', 'LYS', 'CA', 'GLY', 7.53), ('NZ', 'LYS', 'N', 'GLY', 6.56)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLY_MG, d, 'M_1f48_3_6_2_16')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(LYS_MG, d, 'M_1f48_3_6_2_16')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(LYS_GLY, d, 'M_1f48_3_6_2_16')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLY_MG' :  match1,
		'LYS_MG' :  match2,
		'LYS_GLY' :  match3}