'''
FUNC:A_2thi_2_5_1_2
PDB:2thi
EC:2.5.1.2
RESI:cys,glu
LOCI:a-113,241;
'''
import motifFunctions as cmd
CYS_GLU = { 
	'distances':
		[[9.51, 8.79, 7.27, 6.82, 6.79], [8.87, 7.89, 6.43, 6.18, 5.88]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'GLU', 9.51), ('CB', 'CYS', 'CG', 'GLU', 8.79), ('CB', 'CYS', 'CD', 'GLU', 7.27), ('CB', 'CYS', 'OE1', 'GLU', 6.82), ('CB', 'CYS', 'OE2', 'GLU', 6.79)], [('SG', 'CYS', 'CB', 'GLU', 8.87), ('SG', 'CYS', 'CG', 'GLU', 7.89), ('SG', 'CYS', 'CD', 'GLU', 6.43), ('SG', 'CYS', 'OE1', 'GLU', 6.18), ('SG', 'CYS', 'OE2', 'GLU', 5.88)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(CYS_GLU, d, 'A_2thi_2_5_1_2')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'CYS_GLU' :  match1}