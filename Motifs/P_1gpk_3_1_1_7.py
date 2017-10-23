'''
FUNC:P_1gpk_3_1_1_7
PDB:1gpk
EC:3.1.1.7
RESI:ser,glu,his
LOCI:a-200,327,440;
'''
import motifFunctions as cmd
GLU_HIS = { 
	'distances':
		[[6.98, 7.15, 6.5, 8.26, 7.37, 8.35], [7.55, 7.6, 6.72, 8.76, 7.55, 8.7], [6.86, 6.73, 5.73, 7.87, 6.54, 7.75], [5.65, 5.49, 4.56, 6.66, 5.55, 6.67], [7.76, 7.52, 6.42, 8.59, 7.06, 8.33]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'HIS', 6.98), ('CB', 'GLU', 'CG', 'HIS', 7.15), ('CB', 'GLU', 'ND1', 'HIS', 6.5), ('CB', 'GLU', 'CD2', 'HIS', 8.26), ('CB', 'GLU', 'CE1', 'HIS', 7.37), ('CB', 'GLU', 'NE2', 'HIS', 8.35)], [('CG', 'GLU', 'CB', 'HIS', 7.55), ('CG', 'GLU', 'CG', 'HIS', 7.6), ('CG', 'GLU', 'ND1', 'HIS', 6.72), ('CG', 'GLU', 'CD2', 'HIS', 8.76), ('CG', 'GLU', 'CE1', 'HIS', 7.55), ('CG', 'GLU', 'NE2', 'HIS', 8.7)], [('CD', 'GLU', 'CB', 'HIS', 6.86), ('CD', 'GLU', 'CG', 'HIS', 6.73), ('CD', 'GLU', 'ND1', 'HIS', 5.73), ('CD', 'GLU', 'CD2', 'HIS', 7.87), ('CD', 'GLU', 'CE1', 'HIS', 6.54), ('CD', 'GLU', 'NE2', 'HIS', 7.75)], [('OE1', 'GLU', 'CB', 'HIS', 5.65), ('OE1', 'GLU', 'CG', 'HIS', 5.49), ('OE1', 'GLU', 'ND1', 'HIS', 4.56), ('OE1', 'GLU', 'CD2', 'HIS', 6.66), ('OE1', 'GLU', 'CE1', 'HIS', 5.55), ('OE1', 'GLU', 'NE2', 'HIS', 6.67)], [('OE2', 'GLU', 'CB', 'HIS', 7.76), ('OE2', 'GLU', 'CG', 'HIS', 7.52), ('OE2', 'GLU', 'ND1', 'HIS', 6.42), ('OE2', 'GLU', 'CD2', 'HIS', 8.59), ('OE2', 'GLU', 'CE1', 'HIS', 7.06), ('OE2', 'GLU', 'NE2', 'HIS', 8.33)]]}
SER_GLU = { 
	'distances':
		[[11.16, 11.13, 9.96, 9.11, 10.07], [10.68, 10.87, 9.86, 8.96, 10.17]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'GLU', 11.16), ('CB', 'SER', 'CG', 'GLU', 11.13), ('CB', 'SER', 'CD', 'GLU', 9.96), ('CB', 'SER', 'OE1', 'GLU', 9.11), ('CB', 'SER', 'OE2', 'GLU', 10.07)], [('OG', 'SER', 'CB', 'GLU', 10.68), ('OG', 'SER', 'CG', 'GLU', 10.87), ('OG', 'SER', 'CD', 'GLU', 9.86), ('OG', 'SER', 'OE1', 'GLU', 8.96), ('OG', 'SER', 'OE2', 'GLU', 10.17)]]}
SER_HIS = { 
	'distances':
		[[8.76, 7.33, 7.0, 6.44, 5.85, 5.38], [8.37, 6.91, 6.67, 5.87, 5.45, 4.74]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'HIS', 8.76), ('CB', 'SER', 'CG', 'HIS', 7.33), ('CB', 'SER', 'ND1', 'HIS', 7.0), ('CB', 'SER', 'CD2', 'HIS', 6.44), ('CB', 'SER', 'CE1', 'HIS', 5.85), ('CB', 'SER', 'NE2', 'HIS', 5.38)], [('OG', 'SER', 'CB', 'HIS', 8.37), ('OG', 'SER', 'CG', 'HIS', 6.91), ('OG', 'SER', 'ND1', 'HIS', 6.67), ('OG', 'SER', 'CD2', 'HIS', 5.87), ('OG', 'SER', 'CE1', 'HIS', 5.45), ('OG', 'SER', 'NE2', 'HIS', 4.74)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_HIS, d, 'P_1gpk_3_1_1_7')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(SER_GLU, d, 'P_1gpk_3_1_1_7')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(SER_HIS, d, 'P_1gpk_3_1_1_7')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_HIS' :  match1,
		'SER_GLU' :  match2,
		'SER_HIS' :  match3}