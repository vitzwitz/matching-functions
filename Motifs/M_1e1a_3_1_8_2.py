'''
FUNC:M_1e1a_3_1_8_2
PDB:1e1a
EC:3.1.8.2
RESI:glu,his,ca
LOCI:a-37,287,401;
'''
import motifFunctions as cmd
HIS_CA = { 
	'distances':
		[[12.07], [10.73], [9.66], [10.46], [8.64], [9.17]],
	'comparisons':
		[[('CB', 'HIS', 'CA', 'CA', 12.07)], [('CG', 'HIS', 'CA', 'CA', 10.73)], [('ND1', 'HIS', 'CA', 'CA', 9.66)], [('CD2', 'HIS', 'CA', 'CA', 10.46)], [('CE1', 'HIS', 'CA', 'CA', 8.64)], [('NE2', 'HIS', 'CA', 'CA', 9.17)]]}
GLU_CA = { 
	'distances':
		[[13.5], [12.25], [11.87], [12.78], [10.78]],
	'comparisons':
		[[('CB', 'GLU', 'CA', 'CA', 13.5)], [('CG', 'GLU', 'CA', 'CA', 12.25)], [('CD', 'GLU', 'CA', 'CA', 11.87)], [('OE1', 'GLU', 'CA', 'CA', 12.78)], [('OE2', 'GLU', 'CA', 'CA', 10.78)]]}
HIS_GLU = { 
	'distances':
		[[10.27, 9.92, 8.74, 8.88, 7.9], [9.7, 9.23, 8.15, 8.54, 7.15], [9.54, 8.81, 7.67, 8.11, 6.54], [9.62, 9.24, 8.39, 8.99, 7.37], [9.37, 8.57, 7.64, 8.33, 6.43], [9.41, 8.83, 8.08, 8.85, 6.95]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLU', 10.27), ('CB', 'HIS', 'CG', 'GLU', 9.92), ('CB', 'HIS', 'CD', 'GLU', 8.74), ('CB', 'HIS', 'OE1', 'GLU', 8.88), ('CB', 'HIS', 'OE2', 'GLU', 7.9)], [('CG', 'HIS', 'CB', 'GLU', 9.7), ('CG', 'HIS', 'CG', 'GLU', 9.23), ('CG', 'HIS', 'CD', 'GLU', 8.15), ('CG', 'HIS', 'OE1', 'GLU', 8.54), ('CG', 'HIS', 'OE2', 'GLU', 7.15)], [('ND1', 'HIS', 'CB', 'GLU', 9.54), ('ND1', 'HIS', 'CG', 'GLU', 8.81), ('ND1', 'HIS', 'CD', 'GLU', 7.67), ('ND1', 'HIS', 'OE1', 'GLU', 8.11), ('ND1', 'HIS', 'OE2', 'GLU', 6.54)], [('CD2', 'HIS', 'CB', 'GLU', 9.62), ('CD2', 'HIS', 'CG', 'GLU', 9.24), ('CD2', 'HIS', 'CD', 'GLU', 8.39), ('CD2', 'HIS', 'OE1', 'GLU', 8.99), ('CD2', 'HIS', 'OE2', 'GLU', 7.37)], [('CE1', 'HIS', 'CB', 'GLU', 9.37), ('CE1', 'HIS', 'CG', 'GLU', 8.57), ('CE1', 'HIS', 'CD', 'GLU', 7.64), ('CE1', 'HIS', 'OE1', 'GLU', 8.33), ('CE1', 'HIS', 'OE2', 'GLU', 6.43)], [('NE2', 'HIS', 'CB', 'GLU', 9.41), ('NE2', 'HIS', 'CG', 'GLU', 8.83), ('NE2', 'HIS', 'CD', 'GLU', 8.08), ('NE2', 'HIS', 'OE1', 'GLU', 8.85), ('NE2', 'HIS', 'OE2', 'GLU', 6.95)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_CA, d, 'M_1e1a_3_1_8_2')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_CA, d, 'M_1e1a_3_1_8_2')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_GLU, d, 'M_1e1a_3_1_8_2')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_CA' :  match1,
		'GLU_CA' :  match2,
		'HIS_GLU' :  match3}