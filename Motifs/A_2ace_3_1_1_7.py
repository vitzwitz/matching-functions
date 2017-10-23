'''
FUNC:A_2ace_3_1_1_7
PDB:2ace
EC:3.1.1.7
RESI:ser,glu,his
LOCI:a-200,327,440;
'''
import motifFunctions as cmd
HIS_SER = { 
	'distances':
		[[8.72, 8.33], [7.27, 6.86], [6.87, 6.44], [6.44, 5.95], [5.73, 5.17], [5.35, 4.7]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'SER', 8.72), ('CB', 'HIS', 'OG', 'SER', 8.33)], [('CG', 'HIS', 'CB', 'SER', 7.27), ('CG', 'HIS', 'OG', 'SER', 6.86)], [('ND1', 'HIS', 'CB', 'SER', 6.87), ('ND1', 'HIS', 'OG', 'SER', 6.44)], [('CD2', 'HIS', 'CB', 'SER', 6.44), ('CD2', 'HIS', 'OG', 'SER', 5.95)], [('CE1', 'HIS', 'CB', 'SER', 5.73), ('CE1', 'HIS', 'OG', 'SER', 5.17)], [('NE2', 'HIS', 'CB', 'SER', 5.35), ('NE2', 'HIS', 'OG', 'SER', 4.7)]]}
GLU_SER = { 
	'distances':
		[[10.95, 10.25], [10.91, 10.41], [9.76, 9.43], [8.84, 8.47], [9.94, 9.81]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'SER', 10.95), ('CB', 'GLU', 'OG', 'SER', 10.25)], [('CG', 'GLU', 'CB', 'SER', 10.91), ('CG', 'GLU', 'OG', 'SER', 10.41)], [('CD', 'GLU', 'CB', 'SER', 9.76), ('CD', 'GLU', 'OG', 'SER', 9.43)], [('OE1', 'GLU', 'CB', 'SER', 8.84), ('OE1', 'GLU', 'OG', 'SER', 8.47)], [('OE2', 'GLU', 'CB', 'SER', 9.94), ('OE2', 'GLU', 'OG', 'SER', 9.81)]]}
GLU_HIS = { 
	'distances':
		[[7.12, 7.28, 6.59, 8.34, 7.36, 8.36], [7.62, 7.67, 6.77, 8.8, 7.54, 8.7], [6.85, 6.74, 5.73, 7.87, 6.53, 7.74], [5.73, 5.5, 4.52, 6.63, 5.43, 6.57], [7.63, 7.45, 6.4, 8.55, 7.1, 8.35]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'HIS', 7.12), ('CB', 'GLU', 'CG', 'HIS', 7.28), ('CB', 'GLU', 'ND1', 'HIS', 6.59), ('CB', 'GLU', 'CD2', 'HIS', 8.34), ('CB', 'GLU', 'CE1', 'HIS', 7.36), ('CB', 'GLU', 'NE2', 'HIS', 8.36)], [('CG', 'GLU', 'CB', 'HIS', 7.62), ('CG', 'GLU', 'CG', 'HIS', 7.67), ('CG', 'GLU', 'ND1', 'HIS', 6.77), ('CG', 'GLU', 'CD2', 'HIS', 8.8), ('CG', 'GLU', 'CE1', 'HIS', 7.54), ('CG', 'GLU', 'NE2', 'HIS', 8.7)], [('CD', 'GLU', 'CB', 'HIS', 6.85), ('CD', 'GLU', 'CG', 'HIS', 6.74), ('CD', 'GLU', 'ND1', 'HIS', 5.73), ('CD', 'GLU', 'CD2', 'HIS', 7.87), ('CD', 'GLU', 'CE1', 'HIS', 6.53), ('CD', 'GLU', 'NE2', 'HIS', 7.74)], [('OE1', 'GLU', 'CB', 'HIS', 5.73), ('OE1', 'GLU', 'CG', 'HIS', 5.5), ('OE1', 'GLU', 'ND1', 'HIS', 4.52), ('OE1', 'GLU', 'CD2', 'HIS', 6.63), ('OE1', 'GLU', 'CE1', 'HIS', 5.43), ('OE1', 'GLU', 'NE2', 'HIS', 6.57)], [('OE2', 'GLU', 'CB', 'HIS', 7.63), ('OE2', 'GLU', 'CG', 'HIS', 7.45), ('OE2', 'GLU', 'ND1', 'HIS', 6.4), ('OE2', 'GLU', 'CD2', 'HIS', 8.55), ('OE2', 'GLU', 'CE1', 'HIS', 7.1), ('OE2', 'GLU', 'NE2', 'HIS', 8.35)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_SER, d, 'A_2ace_3_1_1_7')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_SER, d, 'A_2ace_3_1_1_7')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_HIS, d, 'A_2ace_3_1_1_7')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_SER' :  match1,
		'GLU_SER' :  match2,
		'GLU_HIS' :  match3}