'''
FUNC:A_135l_3_2_1_17
PDB:135l
EC:3.2.1.17
RESI:glu,asp
LOCI:a-35,52;
'''
import motifFunctions as cmd
GLU_ASP = { 
	'distances':
		[[9.97, 10.27, 11.21, 9.71], [10.18, 10.23, 11.04, 9.6], [9.41, 9.24, 10.04, 8.48], [8.42, 8.3, 9.19, 7.49], [10.04, 9.66, 10.32, 8.85]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ASP', 9.97), ('CB', 'GLU', 'CG', 'ASP', 10.27), ('CB', 'GLU', 'OD1', 'ASP', 11.21), ('CB', 'GLU', 'OD2', 'ASP', 9.71)], [('CG', 'GLU', 'CB', 'ASP', 10.18), ('CG', 'GLU', 'CG', 'ASP', 10.23), ('CG', 'GLU', 'OD1', 'ASP', 11.04), ('CG', 'GLU', 'OD2', 'ASP', 9.6)], [('CD', 'GLU', 'CB', 'ASP', 9.41), ('CD', 'GLU', 'CG', 'ASP', 9.24), ('CD', 'GLU', 'OD1', 'ASP', 10.04), ('CD', 'GLU', 'OD2', 'ASP', 8.48)], [('OE1', 'GLU', 'CB', 'ASP', 8.42), ('OE1', 'GLU', 'CG', 'ASP', 8.3), ('OE1', 'GLU', 'OD1', 'ASP', 9.19), ('OE1', 'GLU', 'OD2', 'ASP', 7.49)], [('OE2', 'GLU', 'CB', 'ASP', 10.04), ('OE2', 'GLU', 'CG', 'ASP', 9.66), ('OE2', 'GLU', 'OD1', 'ASP', 10.32), ('OE2', 'GLU', 'OD2', 'ASP', 8.85)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_ASP, d, 'A_135l_3_2_1_17')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_ASP' :  match1}