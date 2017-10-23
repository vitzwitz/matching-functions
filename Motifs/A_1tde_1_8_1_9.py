'''
FUNC:A_1tde_1_8_1_9
PDB:1tde
EC:1.8.1.9
RESI:cys,cys,asp
LOCI:a-135,138,139;
'''
import motifFunctions as cmd
CYS_ASP = { 
	'distances':
		[[6.58, 6.07, 5.92, 6.36], [8.21, 7.62, 7.53, 7.64], [8.08, 7.67, 8.18, 7.2], [8.57, 8.27, 8.56, 8.13]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'ASP', 6.58), ('CB', 'CYS', 'CG', 'ASP', 6.07), ('CB', 'CYS', 'OD1', 'ASP', 5.92), ('CB', 'CYS', 'OD2', 'ASP', 6.36)], [('SG', 'CYS', 'CB', 'ASP', 8.21), ('SG', 'CYS', 'CG', 'ASP', 7.62), ('SG', 'CYS', 'OD1', 'ASP', 7.53), ('SG', 'CYS', 'OD2', 'ASP', 7.64)], [('CB', 'CYS', 'CB', 'ASP', 8.08), ('CB', 'CYS', 'CG', 'ASP', 7.67), ('CB', 'CYS', 'OD1', 'ASP', 8.18), ('CB', 'CYS', 'OD2', 'ASP', 7.2)], [('SG', 'CYS', 'CB', 'ASP', 8.57), ('SG', 'CYS', 'CG', 'ASP', 8.27), ('SG', 'CYS', 'OD1', 'ASP', 8.56), ('SG', 'CYS', 'OD2', 'ASP', 8.13)]]}
CYS_CYS = { 
	'distances':
		[[5.61, 5.06], [4.99, 4.01], [5.61, 4.99], [5.06, 4.01]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'CYS', 5.61), ('CB', 'CYS', 'SG', 'CYS', 5.06)], [('SG', 'CYS', 'CB', 'CYS', 4.99), ('SG', 'CYS', 'SG', 'CYS', 4.01)], [('CB', 'CYS', 'CB', 'CYS', 5.61), ('CB', 'CYS', 'SG', 'CYS', 4.99)], [('SG', 'CYS', 'CB', 'CYS', 5.06), ('SG', 'CYS', 'SG', 'CYS', 4.01)]]}
ASP_CYSI = { 
	'distances':
		[[8.08, 8.57], [7.67, 8.27], [8.18, 8.56], [7.2, 8.13]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'CYSI', 8.08), ('CB', 'ASP', 'SG', 'CYSI', 8.57)], [('CG', 'ASP', 'CB', 'CYSI', 7.67), ('CG', 'ASP', 'SG', 'CYSI', 8.27)], [('OD1', 'ASP', 'CB', 'CYSI', 8.18), ('OD1', 'ASP', 'SG', 'CYSI', 8.56)], [('OD2', 'ASP', 'CB', 'CYSI', 7.2), ('OD2', 'ASP', 'SG', 'CYSI', 8.13)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(CYS_ASP, d, 'A_1tde_1_8_1_9')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(CYS_CYS, d, 'A_1tde_1_8_1_9')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_CYSI, d, 'A_1tde_1_8_1_9')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'CYS_ASP' :  match1,
		'CYS_CYS' :  match2,
		'ASP_CYSI' :  match3}