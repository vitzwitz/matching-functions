'''
FUNC:M_1w0h_3_1_-_-
PDB:1w0h
EC:3.1.-.-
RESI:glu,his,mg
LOCI:a-136,293,1001;
'''
import motifFunctions as cmd
HIS_MG = { 
	'distances':
		[[7.13], [7.46], [6.87], [8.64], [7.84], [8.82]],
	'comparisons':
		[[('CB', 'HIS', 'MG', 'MG', 7.13)], [('CG', 'HIS', 'MG', 'MG', 7.46)], [('ND1', 'HIS', 'MG', 'MG', 6.87)], [('CD2', 'HIS', 'MG', 'MG', 8.64)], [('CE1', 'HIS', 'MG', 'MG', 7.84)], [('NE2', 'HIS', 'MG', 'MG', 8.82)]]}
GLU_MG = { 
	'distances':
		[[7.51], [6.49], [5.2], [5.58], [4.15]],
	'comparisons':
		[[('CB', 'GLU', 'MG', 'MG', 7.51)], [('CG', 'GLU', 'MG', 'MG', 6.49)], [('CD', 'GLU', 'MG', 'MG', 5.2)], [('OE1', 'GLU', 'MG', 'MG', 5.58)], [('OE2', 'GLU', 'MG', 'MG', 4.15)]]}
GLU_HIS = { 
	'distances':
		[[8.45, 9.56, 9.57, 10.87, 10.85, 11.57], [7.48, 8.66, 8.76, 9.98, 10.07, 10.73], [6.5, 7.49, 7.41, 8.84, 8.7, 9.46], [6.11, 6.93, 6.75, 8.27, 8.0, 8.81], [6.59, 7.45, 7.29, 8.77, 8.52, 9.31]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'HIS', 8.45), ('CB', 'GLU', 'CG', 'HIS', 9.56), ('CB', 'GLU', 'ND1', 'HIS', 9.57), ('CB', 'GLU', 'CD2', 'HIS', 10.87), ('CB', 'GLU', 'CE1', 'HIS', 10.85), ('CB', 'GLU', 'NE2', 'HIS', 11.57)], [('CG', 'GLU', 'CB', 'HIS', 7.48), ('CG', 'GLU', 'CG', 'HIS', 8.66), ('CG', 'GLU', 'ND1', 'HIS', 8.76), ('CG', 'GLU', 'CD2', 'HIS', 9.98), ('CG', 'GLU', 'CE1', 'HIS', 10.07), ('CG', 'GLU', 'NE2', 'HIS', 10.73)], [('CD', 'GLU', 'CB', 'HIS', 6.5), ('CD', 'GLU', 'CG', 'HIS', 7.49), ('CD', 'GLU', 'ND1', 'HIS', 7.41), ('CD', 'GLU', 'CD2', 'HIS', 8.84), ('CD', 'GLU', 'CE1', 'HIS', 8.7), ('CD', 'GLU', 'NE2', 'HIS', 9.46)], [('OE1', 'GLU', 'CB', 'HIS', 6.11), ('OE1', 'GLU', 'CG', 'HIS', 6.93), ('OE1', 'GLU', 'ND1', 'HIS', 6.75), ('OE1', 'GLU', 'CD2', 'HIS', 8.27), ('OE1', 'GLU', 'CE1', 'HIS', 8.0), ('OE1', 'GLU', 'NE2', 'HIS', 8.81)], [('OE2', 'GLU', 'CB', 'HIS', 6.59), ('OE2', 'GLU', 'CG', 'HIS', 7.45), ('OE2', 'GLU', 'ND1', 'HIS', 7.29), ('OE2', 'GLU', 'CD2', 'HIS', 8.77), ('OE2', 'GLU', 'CE1', 'HIS', 8.52), ('OE2', 'GLU', 'NE2', 'HIS', 9.31)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_MG, d, 'M_1w0h_3_1_-_-')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_MG, d, 'M_1w0h_3_1_-_-')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_HIS, d, 'M_1w0h_3_1_-_-')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_MG' :  match1,
		'GLU_MG' :  match2,
		'GLU_HIS' :  match3}