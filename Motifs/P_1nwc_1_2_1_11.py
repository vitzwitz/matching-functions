'''
FUNC:P_1nwc_1_2_1_11
PDB:1nwc
EC:1.2.1.11
RESI:cys,gln,his
LOCI:a-136,163,277;
'''
import motifFunctions as cmd
GLN_HIS = { 
	'distances':
		[[6.9, 6.15, 5.45, 6.53, 5.48, 6.14], [6.41, 5.83, 5.66, 6.05, 5.81, 6.03], [7.35, 6.57, 6.55, 6.34, 6.32, 6.17], [7.55, 6.51, 6.44, 5.96, 5.87, 5.53], [8.27, 7.69, 7.78, 7.45, 7.63, 7.42]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'HIS', 6.9), ('CB', 'GLN', 'CG', 'HIS', 6.15), ('CB', 'GLN', 'ND1', 'HIS', 5.45), ('CB', 'GLN', 'CD2', 'HIS', 6.53), ('CB', 'GLN', 'CE1', 'HIS', 5.48), ('CB', 'GLN', 'NE2', 'HIS', 6.14)], [('CG', 'GLN', 'CB', 'HIS', 6.41), ('CG', 'GLN', 'CG', 'HIS', 5.83), ('CG', 'GLN', 'ND1', 'HIS', 5.66), ('CG', 'GLN', 'CD2', 'HIS', 6.05), ('CG', 'GLN', 'CE1', 'HIS', 5.81), ('CG', 'GLN', 'NE2', 'HIS', 6.03)], [('CD', 'GLN', 'CB', 'HIS', 7.35), ('CD', 'GLN', 'CG', 'HIS', 6.57), ('CD', 'GLN', 'ND1', 'HIS', 6.55), ('CD', 'GLN', 'CD2', 'HIS', 6.34), ('CD', 'GLN', 'CE1', 'HIS', 6.32), ('CD', 'GLN', 'NE2', 'HIS', 6.17)], [('OE1', 'GLN', 'CB', 'HIS', 7.55), ('OE1', 'GLN', 'CG', 'HIS', 6.51), ('OE1', 'GLN', 'ND1', 'HIS', 6.44), ('OE1', 'GLN', 'CD2', 'HIS', 5.96), ('OE1', 'GLN', 'CE1', 'HIS', 5.87), ('OE1', 'GLN', 'NE2', 'HIS', 5.53)], [('NE2', 'GLN', 'CB', 'HIS', 8.27), ('NE2', 'GLN', 'CG', 'HIS', 7.69), ('NE2', 'GLN', 'ND1', 'HIS', 7.78), ('NE2', 'GLN', 'CD2', 'HIS', 7.45), ('NE2', 'GLN', 'CE1', 'HIS', 7.63), ('NE2', 'GLN', 'NE2', 'HIS', 7.42)]]}
CYS_GLN = { 
	'distances':
		[[10.02, 9.44, 9.06, 8.23, 9.92], [8.84, 8.35, 7.77, 6.78, 8.66]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'GLN', 10.02), ('CB', 'CYS', 'CG', 'GLN', 9.44), ('CB', 'CYS', 'CD', 'GLN', 9.06), ('CB', 'CYS', 'OE1', 'GLN', 8.23), ('CB', 'CYS', 'NE2', 'GLN', 9.92)], [('SG', 'CYS', 'CB', 'GLN', 8.84), ('SG', 'CYS', 'CG', 'GLN', 8.35), ('SG', 'CYS', 'CD', 'GLN', 7.77), ('SG', 'CYS', 'OE1', 'GLN', 6.78), ('SG', 'CYS', 'NE2', 'GLN', 8.66)]]}
CYS_HIS = { 
	'distances':
		[[8.0, 7.14, 7.88, 5.92, 7.36, 6.12], [8.0, 6.85, 7.3, 5.51, 6.49, 5.23]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'HIS', 8.0), ('CB', 'CYS', 'CG', 'HIS', 7.14), ('CB', 'CYS', 'ND1', 'HIS', 7.88), ('CB', 'CYS', 'CD2', 'HIS', 5.92), ('CB', 'CYS', 'CE1', 'HIS', 7.36), ('CB', 'CYS', 'NE2', 'HIS', 6.12)], [('SG', 'CYS', 'CB', 'HIS', 8.0), ('SG', 'CYS', 'CG', 'HIS', 6.85), ('SG', 'CYS', 'ND1', 'HIS', 7.3), ('SG', 'CYS', 'CD2', 'HIS', 5.51), ('SG', 'CYS', 'CE1', 'HIS', 6.49), ('SG', 'CYS', 'NE2', 'HIS', 5.23)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLN_HIS, d, 'P_1nwc_1_2_1_11')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(CYS_GLN, d, 'P_1nwc_1_2_1_11')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(CYS_HIS, d, 'P_1nwc_1_2_1_11')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLN_HIS' :  match1,
		'CYS_GLN' :  match2,
		'CYS_HIS' :  match3}