'''
FUNC:A_132l_3_2_1_17
PDB:132l
EC:3.2.1.17
RESI:glu,asp
LOCI:a-35,52;
'''
import motifFunctions as cmd
GLU_ASP = { 
	'distances':
		[[9.74, 10.17, 10.93, 9.8], [9.96, 10.12, 10.75, 9.7], [9.13, 9.09, 9.72, 8.52], [8.17, 8.19, 8.95, 7.56], [9.78, 9.5, 10.01, 8.88]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ASP', 9.74), ('CB', 'GLU', 'CG', 'ASP', 10.17), ('CB', 'GLU', 'OD1', 'ASP', 10.93), ('CB', 'GLU', 'OD2', 'ASP', 9.8)], [('CG', 'GLU', 'CB', 'ASP', 9.96), ('CG', 'GLU', 'CG', 'ASP', 10.12), ('CG', 'GLU', 'OD1', 'ASP', 10.75), ('CG', 'GLU', 'OD2', 'ASP', 9.7)], [('CD', 'GLU', 'CB', 'ASP', 9.13), ('CD', 'GLU', 'CG', 'ASP', 9.09), ('CD', 'GLU', 'OD1', 'ASP', 9.72), ('CD', 'GLU', 'OD2', 'ASP', 8.52)], [('OE1', 'GLU', 'CB', 'ASP', 8.17), ('OE1', 'GLU', 'CG', 'ASP', 8.19), ('OE1', 'GLU', 'OD1', 'ASP', 8.95), ('OE1', 'GLU', 'OD2', 'ASP', 7.56)], [('OE2', 'GLU', 'CB', 'ASP', 9.78), ('OE2', 'GLU', 'CG', 'ASP', 9.5), ('OE2', 'GLU', 'OD1', 'ASP', 10.01), ('OE2', 'GLU', 'OD2', 'ASP', 8.88)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_ASP, d, 'A_132l_3_2_1_17')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_ASP' :  match1}