'''
FUNC:M_1ca2_4_2_1_1
PDB:1ca2
EC:4.2.1.1
RESI:his,glu,thr,zn
LOCI:a-64,106,199,262;
'''
import motifFunctions as cmd
HIS_ZN = { 
	'distances':
		[[11.3], [10.73], [11.65], [9.55], [11.18], [9.92]],
	'comparisons':
		[[('CB', 'HIS', 'ZN', 'ZN', 11.3)], [('CG', 'HIS', 'ZN', 'ZN', 10.73)], [('ND1', 'HIS', 'ZN', 'ZN', 11.65)], [('CD2', 'HIS', 'ZN', 'ZN', 9.55)], [('CE1', 'HIS', 'ZN', 'ZN', 11.18)], [('NE2', 'HIS', 'ZN', 'ZN', 9.92)]]}
THR_ZN = { 
	'distances':
		[[7.18], [5.83], [7.69]],
	'comparisons':
		[[('CB', 'THR', 'ZN', 'ZN', 7.18)], [('OG1', 'THR', 'ZN', 'ZN', 5.83)], [('CG2', 'THR', 'ZN', 'ZN', 7.69)]]}
THR_HIS = { 
	'distances':
		[[12.66, 12.3, 13.06, 11.52, 12.79, 11.88], [11.7, 11.31, 12.15, 10.44, 11.86, 10.85], [14.14, 13.75, 14.5, 12.9, 14.17, 13.21]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'HIS', 12.66), ('CB', 'THR', 'CG', 'HIS', 12.3), ('CB', 'THR', 'ND1', 'HIS', 13.06), ('CB', 'THR', 'CD2', 'HIS', 11.52), ('CB', 'THR', 'CE1', 'HIS', 12.79), ('CB', 'THR', 'NE2', 'HIS', 11.88)], [('OG1', 'THR', 'CB', 'HIS', 11.7), ('OG1', 'THR', 'CG', 'HIS', 11.31), ('OG1', 'THR', 'ND1', 'HIS', 12.15), ('OG1', 'THR', 'CD2', 'HIS', 10.44), ('OG1', 'THR', 'CE1', 'HIS', 11.86), ('OG1', 'THR', 'NE2', 'HIS', 10.85)], [('CG2', 'THR', 'CB', 'HIS', 14.14), ('CG2', 'THR', 'CG', 'HIS', 13.75), ('CG2', 'THR', 'ND1', 'HIS', 14.5), ('CG2', 'THR', 'CD2', 'HIS', 12.9), ('CG2', 'THR', 'CE1', 'HIS', 14.17), ('CG2', 'THR', 'NE2', 'HIS', 13.21)]]}
GLU_ZN = { 
	'distances':
		[[8.63], [7.82], [6.87], [6.06], [7.46]],
	'comparisons':
		[[('CB', 'GLU', 'ZN', 'ZN', 8.63)], [('CG', 'GLU', 'ZN', 'ZN', 7.82)], [('CD', 'GLU', 'ZN', 'ZN', 6.87)], [('OE1', 'GLU', 'ZN', 'ZN', 6.06)], [('OE2', 'GLU', 'ZN', 'ZN', 7.46)]]}
GLU_THR = { 
	'distances':
		[[7.38, 7.29, 7.21], [7.16, 6.75, 7.43], [5.73, 5.23, 6.26], [5.06, 4.43, 5.44], [5.88, 5.46, 6.74]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'THR', 7.38), ('CB', 'GLU', 'OG1', 'THR', 7.29), ('CB', 'GLU', 'CG2', 'THR', 7.21)], [('CG', 'GLU', 'CB', 'THR', 7.16), ('CG', 'GLU', 'OG1', 'THR', 6.75), ('CG', 'GLU', 'CG2', 'THR', 7.43)], [('CD', 'GLU', 'CB', 'THR', 5.73), ('CD', 'GLU', 'OG1', 'THR', 5.23), ('CD', 'GLU', 'CG2', 'THR', 6.26)], [('OE1', 'GLU', 'CB', 'THR', 5.06), ('OE1', 'GLU', 'OG1', 'THR', 4.43), ('OE1', 'GLU', 'CG2', 'THR', 5.44)], [('OE2', 'GLU', 'CB', 'THR', 5.88), ('OE2', 'GLU', 'OG1', 'THR', 5.46), ('OE2', 'GLU', 'CG2', 'THR', 6.74)]]}
GLU_HIS = { 
	'distances':
		[[14.67, 14.8, 15.95, 14.1, 15.96, 14.9], [13.17, 13.35, 14.54, 12.7, 14.62, 13.57], [12.25, 12.3, 13.41, 11.6, 13.42, 12.38], [12.48, 12.36, 13.4, 11.54, 13.27, 12.19], [11.48, 11.64, 12.75, 11.07, 12.87, 11.92]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'HIS', 14.67), ('CB', 'GLU', 'CG', 'HIS', 14.8), ('CB', 'GLU', 'ND1', 'HIS', 15.95), ('CB', 'GLU', 'CD2', 'HIS', 14.1), ('CB', 'GLU', 'CE1', 'HIS', 15.96), ('CB', 'GLU', 'NE2', 'HIS', 14.9)], [('CG', 'GLU', 'CB', 'HIS', 13.17), ('CG', 'GLU', 'CG', 'HIS', 13.35), ('CG', 'GLU', 'ND1', 'HIS', 14.54), ('CG', 'GLU', 'CD2', 'HIS', 12.7), ('CG', 'GLU', 'CE1', 'HIS', 14.62), ('CG', 'GLU', 'NE2', 'HIS', 13.57)], [('CD', 'GLU', 'CB', 'HIS', 12.25), ('CD', 'GLU', 'CG', 'HIS', 12.3), ('CD', 'GLU', 'ND1', 'HIS', 13.41), ('CD', 'GLU', 'CD2', 'HIS', 11.6), ('CD', 'GLU', 'CE1', 'HIS', 13.42), ('CD', 'GLU', 'NE2', 'HIS', 12.38)], [('OE1', 'GLU', 'CB', 'HIS', 12.48), ('OE1', 'GLU', 'CG', 'HIS', 12.36), ('OE1', 'GLU', 'ND1', 'HIS', 13.4), ('OE1', 'GLU', 'CD2', 'HIS', 11.54), ('OE1', 'GLU', 'CE1', 'HIS', 13.27), ('OE1', 'GLU', 'NE2', 'HIS', 12.19)], [('OE2', 'GLU', 'CB', 'HIS', 11.48), ('OE2', 'GLU', 'CG', 'HIS', 11.64), ('OE2', 'GLU', 'ND1', 'HIS', 12.75), ('OE2', 'GLU', 'CD2', 'HIS', 11.07), ('OE2', 'GLU', 'CE1', 'HIS', 12.87), ('OE2', 'GLU', 'NE2', 'HIS', 11.92)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_ZN, d, 'M_1ca2_4_2_1_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(THR_ZN, d, 'M_1ca2_4_2_1_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(THR_HIS, d, 'M_1ca2_4_2_1_1')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(GLU_ZN, d, 'M_1ca2_4_2_1_1')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(GLU_THR, d, 'M_1ca2_4_2_1_1')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(GLU_HIS, d, 'M_1ca2_4_2_1_1')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_ZN' :  match1,
		'THR_ZN' :  match2,
		'THR_HIS' :  match3,
		'GLU_ZN' :  match4,
		'GLU_THR' :  match5,
		'GLU_HIS' :  match6}