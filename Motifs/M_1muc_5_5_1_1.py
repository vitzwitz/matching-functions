'''
FUNC:M_1muc_5_5_1_1
PDB:1muc
EC:5.5.1.1
RESI:lys,lys,glu,mn
LOCI:a-167,169,327,374;
'''
import motifFunctions as cmd
LYS_LYS = { 
	'distances':
		[[9.11, 8.33, 8.78, 8.2, 9.17], [8.24, 7.44, 7.64, 7.06, 7.92], [9.16, 8.47, 8.42, 7.84, 8.43], [10.47, 9.63, 9.48, 8.66, 9.07], [11.51, 10.75, 10.47, 9.69, 9.92], [9.11, 8.24, 9.16, 10.47, 11.51], [8.33, 7.44, 8.47, 9.63, 10.75], [8.78, 7.64, 8.42, 9.48, 10.47], [8.2, 7.06, 7.84, 8.66, 9.69], [9.17, 7.92, 8.43, 9.07, 9.92]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'LYS', 9.11), ('CB', 'LYS', 'CG', 'LYS', 8.33), ('CB', 'LYS', 'CD', 'LYS', 8.78), ('CB', 'LYS', 'CE', 'LYS', 8.2), ('CB', 'LYS', 'NZ', 'LYS', 9.17)], [('CG', 'LYS', 'CB', 'LYS', 8.24), ('CG', 'LYS', 'CG', 'LYS', 7.44), ('CG', 'LYS', 'CD', 'LYS', 7.64), ('CG', 'LYS', 'CE', 'LYS', 7.06), ('CG', 'LYS', 'NZ', 'LYS', 7.92)], [('CD', 'LYS', 'CB', 'LYS', 9.16), ('CD', 'LYS', 'CG', 'LYS', 8.47), ('CD', 'LYS', 'CD', 'LYS', 8.42), ('CD', 'LYS', 'CE', 'LYS', 7.84), ('CD', 'LYS', 'NZ', 'LYS', 8.43)], [('CE', 'LYS', 'CB', 'LYS', 10.47), ('CE', 'LYS', 'CG', 'LYS', 9.63), ('CE', 'LYS', 'CD', 'LYS', 9.48), ('CE', 'LYS', 'CE', 'LYS', 8.66), ('CE', 'LYS', 'NZ', 'LYS', 9.07)], [('NZ', 'LYS', 'CB', 'LYS', 11.51), ('NZ', 'LYS', 'CG', 'LYS', 10.75), ('NZ', 'LYS', 'CD', 'LYS', 10.47), ('NZ', 'LYS', 'CE', 'LYS', 9.69), ('NZ', 'LYS', 'NZ', 'LYS', 9.92)], [('CB', 'LYS', 'CB', 'LYS', 9.11), ('CB', 'LYS', 'CG', 'LYS', 8.24), ('CB', 'LYS', 'CD', 'LYS', 9.16), ('CB', 'LYS', 'CE', 'LYS', 10.47), ('CB', 'LYS', 'NZ', 'LYS', 11.51)], [('CG', 'LYS', 'CB', 'LYS', 8.33), ('CG', 'LYS', 'CG', 'LYS', 7.44), ('CG', 'LYS', 'CD', 'LYS', 8.47), ('CG', 'LYS', 'CE', 'LYS', 9.63), ('CG', 'LYS', 'NZ', 'LYS', 10.75)], [('CD', 'LYS', 'CB', 'LYS', 8.78), ('CD', 'LYS', 'CG', 'LYS', 7.64), ('CD', 'LYS', 'CD', 'LYS', 8.42), ('CD', 'LYS', 'CE', 'LYS', 9.48), ('CD', 'LYS', 'NZ', 'LYS', 10.47)], [('CE', 'LYS', 'CB', 'LYS', 8.2), ('CE', 'LYS', 'CG', 'LYS', 7.06), ('CE', 'LYS', 'CD', 'LYS', 7.84), ('CE', 'LYS', 'CE', 'LYS', 8.66), ('CE', 'LYS', 'NZ', 'LYS', 9.69)], [('NZ', 'LYS', 'CB', 'LYS', 9.17), ('NZ', 'LYS', 'CG', 'LYS', 7.92), ('NZ', 'LYS', 'CD', 'LYS', 8.43), ('NZ', 'LYS', 'CE', 'LYS', 9.07), ('NZ', 'LYS', 'NZ', 'LYS', 9.92)]]}
GLU_MN = { 
	'distances':
		[[10.24], [9.29], [7.83], [7.6], [7.14]],
	'comparisons':
		[[('CB', 'GLU', 'MN', 'MN', 10.24)], [('CG', 'GLU', 'MN', 'MN', 9.29)], [('CD', 'GLU', 'MN', 'MN', 7.83)], [('OE1', 'GLU', 'MN', 'MN', 7.6)], [('OE2', 'GLU', 'MN', 'MN', 7.14)]]}
GLU_LYSI = { 
	'distances':
		[[8.28, 8.39, 7.16, 7.84, 7.21], [9.08, 8.88, 7.49, 7.8, 6.83], [8.49, 8.01, 6.53, 6.55, 5.42], [7.31, 6.78, 5.32, 5.46, 4.54], [9.39, 8.74, 7.24, 6.91, 5.57]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'LYSI', 8.28), ('CB', 'GLU', 'CG', 'LYSI', 8.39), ('CB', 'GLU', 'CD', 'LYSI', 7.16), ('CB', 'GLU', 'CE', 'LYSI', 7.84), ('CB', 'GLU', 'NZ', 'LYSI', 7.21)], [('CG', 'GLU', 'CB', 'LYSI', 9.08), ('CG', 'GLU', 'CG', 'LYSI', 8.88), ('CG', 'GLU', 'CD', 'LYSI', 7.49), ('CG', 'GLU', 'CE', 'LYSI', 7.8), ('CG', 'GLU', 'NZ', 'LYSI', 6.83)], [('CD', 'GLU', 'CB', 'LYSI', 8.49), ('CD', 'GLU', 'CG', 'LYSI', 8.01), ('CD', 'GLU', 'CD', 'LYSI', 6.53), ('CD', 'GLU', 'CE', 'LYSI', 6.55), ('CD', 'GLU', 'NZ', 'LYSI', 5.42)], [('OE1', 'GLU', 'CB', 'LYSI', 7.31), ('OE1', 'GLU', 'CG', 'LYSI', 6.78), ('OE1', 'GLU', 'CD', 'LYSI', 5.32), ('OE1', 'GLU', 'CE', 'LYSI', 5.46), ('OE1', 'GLU', 'NZ', 'LYSI', 4.54)], [('OE2', 'GLU', 'CB', 'LYSI', 9.39), ('OE2', 'GLU', 'CG', 'LYSI', 8.74), ('OE2', 'GLU', 'CD', 'LYSI', 7.24), ('OE2', 'GLU', 'CE', 'LYSI', 6.91), ('OE2', 'GLU', 'NZ', 'LYSI', 5.57)]]}
MN_LYSI = { 
	'distances':
		[10.47, 9.11, 8.14, 6.75, 5.84],
	'comparisons':
		[('MN', 'MN', 'CB', 'LYSI', 10.47), ('MN', 'MN', 'CG', 'LYSI', 9.11), ('MN', 'MN', 'CD', 'LYSI', 8.14), ('MN', 'MN', 'CE', 'LYSI', 6.75), ('MN', 'MN', 'NZ', 'LYSI', 5.84)]}
LYS_MN = { 
	'distances':
		[[10.32], [9.41], [9.77], [9.65], [10.39], [10.47], [9.11], [8.14], [6.75], [5.84]],
	'comparisons':
		[[('CB', 'LYS', 'MN', 'MN', 10.32)], [('CG', 'LYS', 'MN', 'MN', 9.41)], [('CD', 'LYS', 'MN', 'MN', 9.77)], [('CE', 'LYS', 'MN', 'MN', 9.65)], [('NZ', 'LYS', 'MN', 'MN', 10.39)], [('CB', 'LYS', 'MN', 'MN', 10.47)], [('CG', 'LYS', 'MN', 'MN', 9.11)], [('CD', 'LYS', 'MN', 'MN', 8.14)], [('CE', 'LYS', 'MN', 'MN', 6.75)], [('NZ', 'LYS', 'MN', 'MN', 5.84)]]}
LYS_GLU = { 
	'distances':
		[[13.24, 13.37, 12.15, 11.28, 12.22], [11.83, 11.94, 10.74, 9.92, 10.82], [11.97, 12.03, 10.89, 10.23, 10.85], [12.93, 12.82, 11.59, 11.03, 11.37], [13.36, 13.21, 12.06, 11.66, 11.75], [8.28, 9.08, 8.49, 7.31, 9.39], [8.39, 8.88, 8.01, 6.78, 8.74], [7.16, 7.49, 6.53, 5.32, 7.24], [7.84, 7.8, 6.55, 5.46, 6.91], [7.21, 6.83, 5.42, 4.54, 5.57]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'GLU', 13.24), ('CB', 'LYS', 'CG', 'GLU', 13.37), ('CB', 'LYS', 'CD', 'GLU', 12.15), ('CB', 'LYS', 'OE1', 'GLU', 11.28), ('CB', 'LYS', 'OE2', 'GLU', 12.22)], [('CG', 'LYS', 'CB', 'GLU', 11.83), ('CG', 'LYS', 'CG', 'GLU', 11.94), ('CG', 'LYS', 'CD', 'GLU', 10.74), ('CG', 'LYS', 'OE1', 'GLU', 9.92), ('CG', 'LYS', 'OE2', 'GLU', 10.82)], [('CD', 'LYS', 'CB', 'GLU', 11.97), ('CD', 'LYS', 'CG', 'GLU', 12.03), ('CD', 'LYS', 'CD', 'GLU', 10.89), ('CD', 'LYS', 'OE1', 'GLU', 10.23), ('CD', 'LYS', 'OE2', 'GLU', 10.85)], [('CE', 'LYS', 'CB', 'GLU', 12.93), ('CE', 'LYS', 'CG', 'GLU', 12.82), ('CE', 'LYS', 'CD', 'GLU', 11.59), ('CE', 'LYS', 'OE1', 'GLU', 11.03), ('CE', 'LYS', 'OE2', 'GLU', 11.37)], [('NZ', 'LYS', 'CB', 'GLU', 13.36), ('NZ', 'LYS', 'CG', 'GLU', 13.21), ('NZ', 'LYS', 'CD', 'GLU', 12.06), ('NZ', 'LYS', 'OE1', 'GLU', 11.66), ('NZ', 'LYS', 'OE2', 'GLU', 11.75)], [('CB', 'LYS', 'CB', 'GLU', 8.28), ('CB', 'LYS', 'CG', 'GLU', 9.08), ('CB', 'LYS', 'CD', 'GLU', 8.49), ('CB', 'LYS', 'OE1', 'GLU', 7.31), ('CB', 'LYS', 'OE2', 'GLU', 9.39)], [('CG', 'LYS', 'CB', 'GLU', 8.39), ('CG', 'LYS', 'CG', 'GLU', 8.88), ('CG', 'LYS', 'CD', 'GLU', 8.01), ('CG', 'LYS', 'OE1', 'GLU', 6.78), ('CG', 'LYS', 'OE2', 'GLU', 8.74)], [('CD', 'LYS', 'CB', 'GLU', 7.16), ('CD', 'LYS', 'CG', 'GLU', 7.49), ('CD', 'LYS', 'CD', 'GLU', 6.53), ('CD', 'LYS', 'OE1', 'GLU', 5.32), ('CD', 'LYS', 'OE2', 'GLU', 7.24)], [('CE', 'LYS', 'CB', 'GLU', 7.84), ('CE', 'LYS', 'CG', 'GLU', 7.8), ('CE', 'LYS', 'CD', 'GLU', 6.55), ('CE', 'LYS', 'OE1', 'GLU', 5.46), ('CE', 'LYS', 'OE2', 'GLU', 6.91)], [('NZ', 'LYS', 'CB', 'GLU', 7.21), ('NZ', 'LYS', 'CG', 'GLU', 6.83), ('NZ', 'LYS', 'CD', 'GLU', 5.42), ('NZ', 'LYS', 'OE1', 'GLU', 4.54), ('NZ', 'LYS', 'OE2', 'GLU', 5.57)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LYS_LYS, d, 'M_1muc_5_5_1_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_MN, d, 'M_1muc_5_5_1_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_LYSI, d, 'M_1muc_5_5_1_1')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(MN_LYSI, d, 'M_1muc_5_5_1_1')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(LYS_MN, d, 'M_1muc_5_5_1_1')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(LYS_GLU, d, 'M_1muc_5_5_1_1')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'LYS_LYS' :  match1,
		'GLU_MN' :  match2,
		'GLU_LYSI' :  match3,
		'MN_LYSI' :  match4,
		'LYS_MN' :  match5,
		'LYS_GLU' :  match6}