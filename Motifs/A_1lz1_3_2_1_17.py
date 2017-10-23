'''
FUNC:A_1lz1_3_2_1_17
PDB:1lz1
EC:3.2.1.17
RESI:glu,asp
LOCI:a-35,53;
'''
import motifFunctions as cmd
GLU_ASP = { 
	'distances':
		[[9.72, 10.32, 10.87, 10.37], [9.8, 10.18, 10.56, 10.27], [9.09, 9.21, 9.57, 9.18], [8.2, 8.35, 8.86, 8.21], [9.7, 9.61, 9.84, 9.56]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ASP', 9.72), ('CB', 'GLU', 'CG', 'ASP', 10.32), ('CB', 'GLU', 'OD1', 'ASP', 10.87), ('CB', 'GLU', 'OD2', 'ASP', 10.37)], [('CG', 'GLU', 'CB', 'ASP', 9.8), ('CG', 'GLU', 'CG', 'ASP', 10.18), ('CG', 'GLU', 'OD1', 'ASP', 10.56), ('CG', 'GLU', 'OD2', 'ASP', 10.27)], [('CD', 'GLU', 'CB', 'ASP', 9.09), ('CD', 'GLU', 'CG', 'ASP', 9.21), ('CD', 'GLU', 'OD1', 'ASP', 9.57), ('CD', 'GLU', 'OD2', 'ASP', 9.18)], [('OE1', 'GLU', 'CB', 'ASP', 8.2), ('OE1', 'GLU', 'CG', 'ASP', 8.35), ('OE1', 'GLU', 'OD1', 'ASP', 8.86), ('OE1', 'GLU', 'OD2', 'ASP', 8.21)], [('OE2', 'GLU', 'CB', 'ASP', 9.7), ('OE2', 'GLU', 'CG', 'ASP', 9.61), ('OE2', 'GLU', 'OD1', 'ASP', 9.84), ('OE2', 'GLU', 'OD2', 'ASP', 9.56)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_ASP, d, 'A_1lz1_3_2_1_17')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_ASP' :  match1}