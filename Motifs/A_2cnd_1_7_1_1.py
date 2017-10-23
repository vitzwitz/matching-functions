'''
FUNC:A_2cnd_1_7_1_1
PDB:2cnd
EC:1.7.1.1
RESI:thr,cys,phe
LOCI:a-65,242,270;
'''
import motifFunctions as cmd
CYS_THR = { 
	'distances':
		[[10.86, 9.97, 11.39], [9.92, 8.92, 10.68]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'THR', 10.86), ('CB', 'CYS', 'OG1', 'THR', 9.97), ('CB', 'CYS', 'CG2', 'THR', 11.39)], [('SG', 'CYS', 'CB', 'THR', 9.92), ('SG', 'CYS', 'OG1', 'THR', 8.92), ('SG', 'CYS', 'CG2', 'THR', 10.68)]]}
PHE_CYS = { 
	'distances':
		[[5.74, 5.82], [6.45, 6.93], [7.83, 8.19], [6.14, 7.01], [8.73, 9.27], [7.33, 8.3], [8.53, 9.33], [6.01, 5.45], [6.62, 6.14], [6.45, 6.5], [6.31, 6.84]],
	'comparisons':
		[[('CB', 'PHE', 'CB', 'CYS', 5.74), ('CB', 'PHE', 'SG', 'CYS', 5.82)], [('CG', 'PHE', 'CB', 'CYS', 6.45), ('CG', 'PHE', 'SG', 'CYS', 6.93)], [('CD1', 'PHE', 'CB', 'CYS', 7.83), ('CD1', 'PHE', 'SG', 'CYS', 8.19)], [('CD2', 'PHE', 'CB', 'CYS', 6.14), ('CD2', 'PHE', 'SG', 'CYS', 7.01)], [('CE1', 'PHE', 'CB', 'CYS', 8.73), ('CE1', 'PHE', 'SG', 'CYS', 9.27)], [('CE2', 'PHE', 'CB', 'CYS', 7.33), ('CE2', 'PHE', 'SG', 'CYS', 8.3)], [('CZ', 'PHE', 'CB', 'CYS', 8.53), ('CZ', 'PHE', 'SG', 'CYS', 9.33)], [('O', 'PHE', 'CB', 'CYS', 6.01), ('O', 'PHE', 'SG', 'CYS', 5.45)], [('C', 'PHE', 'CB', 'CYS', 6.62), ('C', 'PHE', 'SG', 'CYS', 6.14)], [('CA', 'PHE', 'CB', 'CYS', 6.45), ('CA', 'PHE', 'SG', 'CYS', 6.5)], [('N', 'PHE', 'CB', 'CYS', 6.31), ('N', 'PHE', 'SG', 'CYS', 6.84)]]}
PHE_THR = { 
	'distances':
		[[9.7, 8.57, 9.86], [9.75, 8.78, 9.65], [9.91, 8.96, 9.6], [9.94, 9.15, 9.79], [10.24, 9.47, 9.69], [10.27, 9.65, 9.88], [10.41, 9.8, 9.83], [11.41, 10.11, 11.94], [10.96, 9.64, 11.36], [10.92, 9.7, 11.11], [12.14, 10.97, 12.31]],
	'comparisons':
		[[('CB', 'PHE', 'CB', 'THR', 9.7), ('CB', 'PHE', 'OG1', 'THR', 8.57), ('CB', 'PHE', 'CG2', 'THR', 9.86)], [('CG', 'PHE', 'CB', 'THR', 9.75), ('CG', 'PHE', 'OG1', 'THR', 8.78), ('CG', 'PHE', 'CG2', 'THR', 9.65)], [('CD1', 'PHE', 'CB', 'THR', 9.91), ('CD1', 'PHE', 'OG1', 'THR', 8.96), ('CD1', 'PHE', 'CG2', 'THR', 9.6)], [('CD2', 'PHE', 'CB', 'THR', 9.94), ('CD2', 'PHE', 'OG1', 'THR', 9.15), ('CD2', 'PHE', 'CG2', 'THR', 9.79)], [('CE1', 'PHE', 'CB', 'THR', 10.24), ('CE1', 'PHE', 'OG1', 'THR', 9.47), ('CE1', 'PHE', 'CG2', 'THR', 9.69)], [('CE2', 'PHE', 'CB', 'THR', 10.27), ('CE2', 'PHE', 'OG1', 'THR', 9.65), ('CE2', 'PHE', 'CG2', 'THR', 9.88)], [('CZ', 'PHE', 'CB', 'THR', 10.41), ('CZ', 'PHE', 'OG1', 'THR', 9.8), ('CZ', 'PHE', 'CG2', 'THR', 9.83)], [('O', 'PHE', 'CB', 'THR', 11.41), ('O', 'PHE', 'OG1', 'THR', 10.11), ('O', 'PHE', 'CG2', 'THR', 11.94)], [('C', 'PHE', 'CB', 'THR', 10.96), ('C', 'PHE', 'OG1', 'THR', 9.64), ('C', 'PHE', 'CG2', 'THR', 11.36)], [('CA', 'PHE', 'CB', 'THR', 10.92), ('CA', 'PHE', 'OG1', 'THR', 9.7), ('CA', 'PHE', 'CG2', 'THR', 11.11)], [('N', 'PHE', 'CB', 'THR', 12.14), ('N', 'PHE', 'OG1', 'THR', 10.97), ('N', 'PHE', 'CG2', 'THR', 12.31)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(CYS_THR, d, 'A_2cnd_1_7_1_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(PHE_CYS, d, 'A_2cnd_1_7_1_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(PHE_THR, d, 'A_2cnd_1_7_1_1')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'CYS_THR' :  match1,
		'PHE_CYS' :  match2,
		'PHE_THR' :  match3}