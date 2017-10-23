'''
FUNC:A_1hy3_2_8_2_4
PDB:1hy3
EC:2.8.2.4
RESI:lys,his,ser
LOCI:a-47,107,137;
'''
import motifFunctions as cmd
LYS_HIS = { 
	'distances':
		[[11.42, 10.47, 9.82, 10.28, 9.22, 9.5], [11.31, 10.32, 9.88, 9.92, 9.19, 9.2], [11.36, 10.2, 9.74, 9.61, 8.84, 8.73], [12.7, 11.48, 10.91, 10.87, 9.92, 9.87], [13.89, 12.72, 12.24, 12.07, 11.29, 11.15]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'HIS', 11.42), ('CB', 'LYS', 'CG', 'HIS', 10.47), ('CB', 'LYS', 'ND1', 'HIS', 9.82), ('CB', 'LYS', 'CD2', 'HIS', 10.28), ('CB', 'LYS', 'CE1', 'HIS', 9.22), ('CB', 'LYS', 'NE2', 'HIS', 9.5)], [('CG', 'LYS', 'CB', 'HIS', 11.31), ('CG', 'LYS', 'CG', 'HIS', 10.32), ('CG', 'LYS', 'ND1', 'HIS', 9.88), ('CG', 'LYS', 'CD2', 'HIS', 9.92), ('CG', 'LYS', 'CE1', 'HIS', 9.19), ('CG', 'LYS', 'NE2', 'HIS', 9.2)], [('CD', 'LYS', 'CB', 'HIS', 11.36), ('CD', 'LYS', 'CG', 'HIS', 10.2), ('CD', 'LYS', 'ND1', 'HIS', 9.74), ('CD', 'LYS', 'CD2', 'HIS', 9.61), ('CD', 'LYS', 'CE1', 'HIS', 8.84), ('CD', 'LYS', 'NE2', 'HIS', 8.73)], [('CE', 'LYS', 'CB', 'HIS', 12.7), ('CE', 'LYS', 'CG', 'HIS', 11.48), ('CE', 'LYS', 'ND1', 'HIS', 10.91), ('CE', 'LYS', 'CD2', 'HIS', 10.87), ('CE', 'LYS', 'CE1', 'HIS', 9.92), ('CE', 'LYS', 'NE2', 'HIS', 9.87)], [('NZ', 'LYS', 'CB', 'HIS', 13.89), ('NZ', 'LYS', 'CG', 'HIS', 12.72), ('NZ', 'LYS', 'ND1', 'HIS', 12.24), ('NZ', 'LYS', 'CD2', 'HIS', 12.07), ('NZ', 'LYS', 'CE1', 'HIS', 11.29), ('NZ', 'LYS', 'NE2', 'HIS', 11.15)]]}
SER_LYS = { 
	'distances':
		[[5.57, 6.04, 6.83, 6.34, 5.9], [5.39, 5.7, 6.04, 5.21, 4.82]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'LYS', 5.57), ('CB', 'SER', 'CG', 'LYS', 6.04), ('CB', 'SER', 'CD', 'LYS', 6.83), ('CB', 'SER', 'CE', 'LYS', 6.34), ('CB', 'SER', 'NZ', 'LYS', 5.9)], [('OG', 'SER', 'CB', 'LYS', 5.39), ('OG', 'SER', 'CG', 'LYS', 5.7), ('OG', 'SER', 'CD', 'LYS', 6.04), ('OG', 'SER', 'CE', 'LYS', 5.21), ('OG', 'SER', 'NZ', 'LYS', 4.82)]]}
SER_HIS = { 
	'distances':
		[[14.96, 14.03, 13.39, 13.79, 12.75, 12.98], [14.71, 13.65, 12.98, 13.31, 12.2, 12.39]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'HIS', 14.96), ('CB', 'SER', 'CG', 'HIS', 14.03), ('CB', 'SER', 'ND1', 'HIS', 13.39), ('CB', 'SER', 'CD2', 'HIS', 13.79), ('CB', 'SER', 'CE1', 'HIS', 12.75), ('CB', 'SER', 'NE2', 'HIS', 12.98)], [('OG', 'SER', 'CB', 'HIS', 14.71), ('OG', 'SER', 'CG', 'HIS', 13.65), ('OG', 'SER', 'ND1', 'HIS', 12.98), ('OG', 'SER', 'CD2', 'HIS', 13.31), ('OG', 'SER', 'CE1', 'HIS', 12.2), ('OG', 'SER', 'NE2', 'HIS', 12.39)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LYS_HIS, d, 'A_1hy3_2_8_2_4')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(SER_LYS, d, 'A_1hy3_2_8_2_4')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(SER_HIS, d, 'A_1hy3_2_8_2_4')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'LYS_HIS' :  match1,
		'SER_LYS' :  match2,
		'SER_HIS' :  match3}