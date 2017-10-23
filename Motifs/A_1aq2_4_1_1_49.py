'''
FUNC:A_1aq2_4_1_1_49
PDB:1aq2
EC:4.1.1.49
RESI:his,lys,arg
LOCI:a-232,254,333;
'''
import motifFunctions as cmd
HIS_LYS = { 
	'distances':
		[[10.01, 9.13, 7.62, 7.36, 7.97], [9.3, 8.47, 6.99, 6.39, 6.81], [9.24, 8.25, 6.91, 6.25, 6.25], [8.96, 8.38, 6.93, 6.02, 6.52], [8.87, 8.04, 6.81, 5.8, 5.54], [8.69, 8.11, 6.81, 5.63, 5.71]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'LYS', 10.01), ('CB', 'HIS', 'CG', 'LYS', 9.13), ('CB', 'HIS', 'CD', 'LYS', 7.62), ('CB', 'HIS', 'CE', 'LYS', 7.36), ('CB', 'HIS', 'NZ', 'LYS', 7.97)], [('CG', 'HIS', 'CB', 'LYS', 9.3), ('CG', 'HIS', 'CG', 'LYS', 8.47), ('CG', 'HIS', 'CD', 'LYS', 6.99), ('CG', 'HIS', 'CE', 'LYS', 6.39), ('CG', 'HIS', 'NZ', 'LYS', 6.81)], [('ND1', 'HIS', 'CB', 'LYS', 9.24), ('ND1', 'HIS', 'CG', 'LYS', 8.25), ('ND1', 'HIS', 'CD', 'LYS', 6.91), ('ND1', 'HIS', 'CE', 'LYS', 6.25), ('ND1', 'HIS', 'NZ', 'LYS', 6.25)], [('CD2', 'HIS', 'CB', 'LYS', 8.96), ('CD2', 'HIS', 'CG', 'LYS', 8.38), ('CD2', 'HIS', 'CD', 'LYS', 6.93), ('CD2', 'HIS', 'CE', 'LYS', 6.02), ('CD2', 'HIS', 'NZ', 'LYS', 6.52)], [('CE1', 'HIS', 'CB', 'LYS', 8.87), ('CE1', 'HIS', 'CG', 'LYS', 8.04), ('CE1', 'HIS', 'CD', 'LYS', 6.81), ('CE1', 'HIS', 'CE', 'LYS', 5.8), ('CE1', 'HIS', 'NZ', 'LYS', 5.54)], [('NE2', 'HIS', 'CB', 'LYS', 8.69), ('NE2', 'HIS', 'CG', 'LYS', 8.11), ('NE2', 'HIS', 'CD', 'LYS', 6.81), ('NE2', 'HIS', 'CE', 'LYS', 5.63), ('NE2', 'HIS', 'NZ', 'LYS', 5.71)]]}
LYS_ARG = { 
	'distances':
		[[15.72, 15.02, 13.55, 12.97, 11.78, 10.97, 11.55], [16.52, 15.7, 14.24, 13.51, 12.28, 11.6, 11.86], [16.52, 15.67, 14.27, 13.49, 12.2, 11.51, 11.73], [15.22, 14.32, 12.97, 12.15, 10.84, 10.18, 10.34], [14.82, 13.8, 12.45, 11.49, 10.2, 9.74, 9.54]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'ARG', 15.72), ('CB', 'LYS', 'CG', 'ARG', 15.02), ('CB', 'LYS', 'CD', 'ARG', 13.55), ('CB', 'LYS', 'NE', 'ARG', 12.97), ('CB', 'LYS', 'CZ', 'ARG', 11.78), ('CB', 'LYS', 'NH1', 'ARG', 10.97), ('CB', 'LYS', 'NH2', 'ARG', 11.55)], [('CG', 'LYS', 'CB', 'ARG', 16.52), ('CG', 'LYS', 'CG', 'ARG', 15.7), ('CG', 'LYS', 'CD', 'ARG', 14.24), ('CG', 'LYS', 'NE', 'ARG', 13.51), ('CG', 'LYS', 'CZ', 'ARG', 12.28), ('CG', 'LYS', 'NH1', 'ARG', 11.6), ('CG', 'LYS', 'NH2', 'ARG', 11.86)], [('CD', 'LYS', 'CB', 'ARG', 16.52), ('CD', 'LYS', 'CG', 'ARG', 15.67), ('CD', 'LYS', 'CD', 'ARG', 14.27), ('CD', 'LYS', 'NE', 'ARG', 13.49), ('CD', 'LYS', 'CZ', 'ARG', 12.2), ('CD', 'LYS', 'NH1', 'ARG', 11.51), ('CD', 'LYS', 'NH2', 'ARG', 11.73)], [('CE', 'LYS', 'CB', 'ARG', 15.22), ('CE', 'LYS', 'CG', 'ARG', 14.32), ('CE', 'LYS', 'CD', 'ARG', 12.97), ('CE', 'LYS', 'NE', 'ARG', 12.15), ('CE', 'LYS', 'CZ', 'ARG', 10.84), ('CE', 'LYS', 'NH1', 'ARG', 10.18), ('CE', 'LYS', 'NH2', 'ARG', 10.34)], [('NZ', 'LYS', 'CB', 'ARG', 14.82), ('NZ', 'LYS', 'CG', 'ARG', 13.8), ('NZ', 'LYS', 'CD', 'ARG', 12.45), ('NZ', 'LYS', 'NE', 'ARG', 11.49), ('NZ', 'LYS', 'CZ', 'ARG', 10.2), ('NZ', 'LYS', 'NH1', 'ARG', 9.74), ('NZ', 'LYS', 'NH2', 'ARG', 9.54)]]}
HIS_ARG = { 
	'distances':
		[[18.54, 17.56, 16.49, 15.56, 14.26, 13.74, 13.59], [17.16, 16.15, 15.07, 14.1, 12.8, 12.34, 12.11], [17.01, 15.9, 14.81, 13.74, 12.45, 12.12, 11.63], [15.94, 14.98, 13.92, 13.01, 11.72, 11.19, 11.12], [15.74, 14.61, 13.52, 12.43, 11.15, 10.85, 10.31], [15.02, 13.97, 12.9, 11.91, 10.62, 10.19, 9.92]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ARG', 18.54), ('CB', 'HIS', 'CG', 'ARG', 17.56), ('CB', 'HIS', 'CD', 'ARG', 16.49), ('CB', 'HIS', 'NE', 'ARG', 15.56), ('CB', 'HIS', 'CZ', 'ARG', 14.26), ('CB', 'HIS', 'NH1', 'ARG', 13.74), ('CB', 'HIS', 'NH2', 'ARG', 13.59)], [('CG', 'HIS', 'CB', 'ARG', 17.16), ('CG', 'HIS', 'CG', 'ARG', 16.15), ('CG', 'HIS', 'CD', 'ARG', 15.07), ('CG', 'HIS', 'NE', 'ARG', 14.1), ('CG', 'HIS', 'CZ', 'ARG', 12.8), ('CG', 'HIS', 'NH1', 'ARG', 12.34), ('CG', 'HIS', 'NH2', 'ARG', 12.11)], [('ND1', 'HIS', 'CB', 'ARG', 17.01), ('ND1', 'HIS', 'CG', 'ARG', 15.9), ('ND1', 'HIS', 'CD', 'ARG', 14.81), ('ND1', 'HIS', 'NE', 'ARG', 13.74), ('ND1', 'HIS', 'CZ', 'ARG', 12.45), ('ND1', 'HIS', 'NH1', 'ARG', 12.12), ('ND1', 'HIS', 'NH2', 'ARG', 11.63)], [('CD2', 'HIS', 'CB', 'ARG', 15.94), ('CD2', 'HIS', 'CG', 'ARG', 14.98), ('CD2', 'HIS', 'CD', 'ARG', 13.92), ('CD2', 'HIS', 'NE', 'ARG', 13.01), ('CD2', 'HIS', 'CZ', 'ARG', 11.72), ('CD2', 'HIS', 'NH1', 'ARG', 11.19), ('CD2', 'HIS', 'NH2', 'ARG', 11.12)], [('CE1', 'HIS', 'CB', 'ARG', 15.74), ('CE1', 'HIS', 'CG', 'ARG', 14.61), ('CE1', 'HIS', 'CD', 'ARG', 13.52), ('CE1', 'HIS', 'NE', 'ARG', 12.43), ('CE1', 'HIS', 'CZ', 'ARG', 11.15), ('CE1', 'HIS', 'NH1', 'ARG', 10.85), ('CE1', 'HIS', 'NH2', 'ARG', 10.31)], [('NE2', 'HIS', 'CB', 'ARG', 15.02), ('NE2', 'HIS', 'CG', 'ARG', 13.97), ('NE2', 'HIS', 'CD', 'ARG', 12.9), ('NE2', 'HIS', 'NE', 'ARG', 11.91), ('NE2', 'HIS', 'CZ', 'ARG', 10.62), ('NE2', 'HIS', 'NH1', 'ARG', 10.19), ('NE2', 'HIS', 'NH2', 'ARG', 9.92)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_LYS, d, 'A_1aq2_4_1_1_49')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(LYS_ARG, d, 'A_1aq2_4_1_1_49')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_ARG, d, 'A_1aq2_4_1_1_49')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_LYS' :  match1,
		'LYS_ARG' :  match2,
		'HIS_ARG' :  match3}