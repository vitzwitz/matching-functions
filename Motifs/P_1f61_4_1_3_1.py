'''
FUNC:P_1f61_4_1_3_1
PDB:1f61
EC:4.1.3.1
RESI:his,cys,arg
LOCI:a-180,191,228;
'''
import motifFunctions as cmd
HIS_CYS = { 
	'distances':
		[[26.99, 26.02], [26.05, 25.04], [24.7, 23.68], [26.28, 25.26], [24.12, 23.08], [25.09, 24.05]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'CYS', 26.99), ('CB', 'HIS', 'SG', 'CYS', 26.02)], [('CG', 'HIS', 'CB', 'CYS', 26.05), ('CG', 'HIS', 'SG', 'CYS', 25.04)], [('ND1', 'HIS', 'CB', 'CYS', 24.7), ('ND1', 'HIS', 'SG', 'CYS', 23.68)], [('CD2', 'HIS', 'CB', 'CYS', 26.28), ('CD2', 'HIS', 'SG', 'CYS', 25.26)], [('CE1', 'HIS', 'CB', 'CYS', 24.12), ('CE1', 'HIS', 'SG', 'CYS', 23.08)], [('NE2', 'HIS', 'CB', 'CYS', 25.09), ('NE2', 'HIS', 'SG', 'CYS', 24.05)]]}
HIS_ARG = { 
	'distances':
		[[7.24, 8.41, 8.23, 9.5, 10.03, 9.5, 11.3], [7.52, 8.39, 7.85, 8.98, 9.28, 8.57, 10.51], [7.07, 7.7, 6.98, 7.95, 8.17, 7.51, 9.34], [8.45, 9.18, 8.44, 9.51, 9.62, 8.7, 10.83], [7.78, 8.13, 7.12, 7.9, 7.83, 6.95, 8.94], [8.57, 9.01, 8.02, 8.88, 8.77, 7.75, 9.9]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ARG', 7.24), ('CB', 'HIS', 'CG', 'ARG', 8.41), ('CB', 'HIS', 'CD', 'ARG', 8.23), ('CB', 'HIS', 'NE', 'ARG', 9.5), ('CB', 'HIS', 'CZ', 'ARG', 10.03), ('CB', 'HIS', 'NH1', 'ARG', 9.5), ('CB', 'HIS', 'NH2', 'ARG', 11.3)], [('CG', 'HIS', 'CB', 'ARG', 7.52), ('CG', 'HIS', 'CG', 'ARG', 8.39), ('CG', 'HIS', 'CD', 'ARG', 7.85), ('CG', 'HIS', 'NE', 'ARG', 8.98), ('CG', 'HIS', 'CZ', 'ARG', 9.28), ('CG', 'HIS', 'NH1', 'ARG', 8.57), ('CG', 'HIS', 'NH2', 'ARG', 10.51)], [('ND1', 'HIS', 'CB', 'ARG', 7.07), ('ND1', 'HIS', 'CG', 'ARG', 7.7), ('ND1', 'HIS', 'CD', 'ARG', 6.98), ('ND1', 'HIS', 'NE', 'ARG', 7.95), ('ND1', 'HIS', 'CZ', 'ARG', 8.17), ('ND1', 'HIS', 'NH1', 'ARG', 7.51), ('ND1', 'HIS', 'NH2', 'ARG', 9.34)], [('CD2', 'HIS', 'CB', 'ARG', 8.45), ('CD2', 'HIS', 'CG', 'ARG', 9.18), ('CD2', 'HIS', 'CD', 'ARG', 8.44), ('CD2', 'HIS', 'NE', 'ARG', 9.51), ('CD2', 'HIS', 'CZ', 'ARG', 9.62), ('CD2', 'HIS', 'NH1', 'ARG', 8.7), ('CD2', 'HIS', 'NH2', 'ARG', 10.83)], [('CE1', 'HIS', 'CB', 'ARG', 7.78), ('CE1', 'HIS', 'CG', 'ARG', 8.13), ('CE1', 'HIS', 'CD', 'ARG', 7.12), ('CE1', 'HIS', 'NE', 'ARG', 7.9), ('CE1', 'HIS', 'CZ', 'ARG', 7.83), ('CE1', 'HIS', 'NH1', 'ARG', 6.95), ('CE1', 'HIS', 'NH2', 'ARG', 8.94)], [('NE2', 'HIS', 'CB', 'ARG', 8.57), ('NE2', 'HIS', 'CG', 'ARG', 9.01), ('NE2', 'HIS', 'CD', 'ARG', 8.02), ('NE2', 'HIS', 'NE', 'ARG', 8.88), ('NE2', 'HIS', 'CZ', 'ARG', 8.77), ('NE2', 'HIS', 'NH1', 'ARG', 7.75), ('NE2', 'HIS', 'NH2', 'ARG', 9.9)]]}
CYS_ARG = { 
	'distances':
		[[23.96, 22.58, 21.87, 20.41, 19.65, 20.29, 18.32], [23.27, 21.94, 21.16, 19.72, 18.92, 19.51, 17.63]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'ARG', 23.96), ('CB', 'CYS', 'CG', 'ARG', 22.58), ('CB', 'CYS', 'CD', 'ARG', 21.87), ('CB', 'CYS', 'NE', 'ARG', 20.41), ('CB', 'CYS', 'CZ', 'ARG', 19.65), ('CB', 'CYS', 'NH1', 'ARG', 20.29), ('CB', 'CYS', 'NH2', 'ARG', 18.32)], [('SG', 'CYS', 'CB', 'ARG', 23.27), ('SG', 'CYS', 'CG', 'ARG', 21.94), ('SG', 'CYS', 'CD', 'ARG', 21.16), ('SG', 'CYS', 'NE', 'ARG', 19.72), ('SG', 'CYS', 'CZ', 'ARG', 18.92), ('SG', 'CYS', 'NH1', 'ARG', 19.51), ('SG', 'CYS', 'NH2', 'ARG', 17.63)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_CYS, d, 'P_1f61_4_1_3_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_ARG, d, 'P_1f61_4_1_3_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(CYS_ARG, d, 'P_1f61_4_1_3_1')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_CYS' :  match1,
		'HIS_ARG' :  match2,
		'CYS_ARG' :  match3}