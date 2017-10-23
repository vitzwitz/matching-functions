'''
FUNC:M_1j53_2_7_7_7
PDB:1j53
EC:2.7.7.7
RESI:glu,glu,his,mn,mn
LOCI:a-14,61,162;a-3000,3001;
'''
import motifFunctions as cmd
GLU_GLU = { 
	'distances':
		[[14.33, 15.02, 14.46, 13.26, 15.33], [14.25, 14.82, 14.09, 12.87, 14.85], [14.96, 15.57, 14.79, 13.55, 15.52], [16.15, 16.79, 16.03, 14.78, 16.77], [14.45, 15.04, 14.2, 12.95, 14.9], [14.33, 14.25, 14.96, 16.15, 14.45], [15.02, 14.82, 15.57, 16.79, 15.04], [14.46, 14.09, 14.79, 16.03, 14.2], [13.26, 12.87, 13.55, 14.78, 12.95], [15.33, 14.85, 15.52, 16.77, 14.9]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'GLU', 14.33), ('CB', 'GLU', 'CG', 'GLU', 15.02), ('CB', 'GLU', 'CD', 'GLU', 14.46), ('CB', 'GLU', 'OE1', 'GLU', 13.26), ('CB', 'GLU', 'OE2', 'GLU', 15.33)], [('CG', 'GLU', 'CB', 'GLU', 14.25), ('CG', 'GLU', 'CG', 'GLU', 14.82), ('CG', 'GLU', 'CD', 'GLU', 14.09), ('CG', 'GLU', 'OE1', 'GLU', 12.87), ('CG', 'GLU', 'OE2', 'GLU', 14.85)], [('CD', 'GLU', 'CB', 'GLU', 14.96), ('CD', 'GLU', 'CG', 'GLU', 15.57), ('CD', 'GLU', 'CD', 'GLU', 14.79), ('CD', 'GLU', 'OE1', 'GLU', 13.55), ('CD', 'GLU', 'OE2', 'GLU', 15.52)], [('OE1', 'GLU', 'CB', 'GLU', 16.15), ('OE1', 'GLU', 'CG', 'GLU', 16.79), ('OE1', 'GLU', 'CD', 'GLU', 16.03), ('OE1', 'GLU', 'OE1', 'GLU', 14.78), ('OE1', 'GLU', 'OE2', 'GLU', 16.77)], [('OE2', 'GLU', 'CB', 'GLU', 14.45), ('OE2', 'GLU', 'CG', 'GLU', 15.04), ('OE2', 'GLU', 'CD', 'GLU', 14.2), ('OE2', 'GLU', 'OE1', 'GLU', 12.95), ('OE2', 'GLU', 'OE2', 'GLU', 14.9)], [('CB', 'GLU', 'CB', 'GLU', 14.33), ('CB', 'GLU', 'CG', 'GLU', 14.25), ('CB', 'GLU', 'CD', 'GLU', 14.96), ('CB', 'GLU', 'OE1', 'GLU', 16.15), ('CB', 'GLU', 'OE2', 'GLU', 14.45)], [('CG', 'GLU', 'CB', 'GLU', 15.02), ('CG', 'GLU', 'CG', 'GLU', 14.82), ('CG', 'GLU', 'CD', 'GLU', 15.57), ('CG', 'GLU', 'OE1', 'GLU', 16.79), ('CG', 'GLU', 'OE2', 'GLU', 15.04)], [('CD', 'GLU', 'CB', 'GLU', 14.46), ('CD', 'GLU', 'CG', 'GLU', 14.09), ('CD', 'GLU', 'CD', 'GLU', 14.79), ('CD', 'GLU', 'OE1', 'GLU', 16.03), ('CD', 'GLU', 'OE2', 'GLU', 14.2)], [('OE1', 'GLU', 'CB', 'GLU', 13.26), ('OE1', 'GLU', 'CG', 'GLU', 12.87), ('OE1', 'GLU', 'CD', 'GLU', 13.55), ('OE1', 'GLU', 'OE1', 'GLU', 14.78), ('OE1', 'GLU', 'OE2', 'GLU', 12.95)], [('OE2', 'GLU', 'CB', 'GLU', 15.33), ('OE2', 'GLU', 'CG', 'GLU', 14.85), ('OE2', 'GLU', 'CD', 'GLU', 15.52), ('OE2', 'GLU', 'OE1', 'GLU', 16.77), ('OE2', 'GLU', 'OE2', 'GLU', 14.9)]]}
HIS_GLUI = { 
	'distances':
		[[8.81, 7.71, 6.55, 6.5, 6.08], [10.05, 9.05, 7.77, 7.53, 7.29], [10.23, 9.37, 7.96, 7.52, 7.55], [11.32, 10.3, 9.07, 8.86, 8.57], [11.53, 10.69, 9.28, 8.8, 8.85], [12.13, 11.2, 9.88, 9.52, 9.39]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLUI', 8.81), ('CB', 'HIS', 'CG', 'GLUI', 7.71), ('CB', 'HIS', 'CD', 'GLUI', 6.55), ('CB', 'HIS', 'OE1', 'GLUI', 6.5), ('CB', 'HIS', 'OE2', 'GLUI', 6.08)], [('CG', 'HIS', 'CB', 'GLUI', 10.05), ('CG', 'HIS', 'CG', 'GLUI', 9.05), ('CG', 'HIS', 'CD', 'GLUI', 7.77), ('CG', 'HIS', 'OE1', 'GLUI', 7.53), ('CG', 'HIS', 'OE2', 'GLUI', 7.29)], [('ND1', 'HIS', 'CB', 'GLUI', 10.23), ('ND1', 'HIS', 'CG', 'GLUI', 9.37), ('ND1', 'HIS', 'CD', 'GLUI', 7.96), ('ND1', 'HIS', 'OE1', 'GLUI', 7.52), ('ND1', 'HIS', 'OE2', 'GLUI', 7.55)], [('CD2', 'HIS', 'CB', 'GLUI', 11.32), ('CD2', 'HIS', 'CG', 'GLUI', 10.3), ('CD2', 'HIS', 'CD', 'GLUI', 9.07), ('CD2', 'HIS', 'OE1', 'GLUI', 8.86), ('CD2', 'HIS', 'OE2', 'GLUI', 8.57)], [('CE1', 'HIS', 'CB', 'GLUI', 11.53), ('CE1', 'HIS', 'CG', 'GLUI', 10.69), ('CE1', 'HIS', 'CD', 'GLUI', 9.28), ('CE1', 'HIS', 'OE1', 'GLUI', 8.8), ('CE1', 'HIS', 'OE2', 'GLUI', 8.85)], [('NE2', 'HIS', 'CB', 'GLUI', 12.13), ('NE2', 'HIS', 'CG', 'GLUI', 11.2), ('NE2', 'HIS', 'CD', 'GLUI', 9.88), ('NE2', 'HIS', 'OE1', 'GLUI', 9.52), ('NE2', 'HIS', 'OE2', 'GLUI', 9.39)]]}
HIS_MN = { 
	'distances':
		[[6.07], [6.81], [6.71], [8.06], [7.89], [8.61], [9.27], [9.47], [8.74], [10.59], [9.53], [10.6]],
	'comparisons':
		[[('CB', 'HIS', 'MN', 'MN', 6.07)], [('CG', 'HIS', 'MN', 'MN', 6.81)], [('ND1', 'HIS', 'MN', 'MN', 6.71)], [('CD2', 'HIS', 'MN', 'MN', 8.06)], [('CE1', 'HIS', 'MN', 'MN', 7.89)], [('NE2', 'HIS', 'MN', 'MN', 8.61)], [('CB', 'HIS', 'MN', 'MN', 9.27)], [('CG', 'HIS', 'MN', 'MN', 9.47)], [('ND1', 'HIS', 'MN', 'MN', 8.74)], [('CD2', 'HIS', 'MN', 'MN', 10.59)], [('CE1', 'HIS', 'MN', 'MN', 9.53)], [('NE2', 'HIS', 'MN', 'MN', 10.6)]]}
GLU_MN = { 
	'distances':
		[[15.61], [14.93], [15.44], [16.68], [14.69], [16.28], [15.44], [15.53], [16.7], [14.53], [7.34], [6.29], [4.96], [5.3], [4.02], [9.52], [9.02], [7.87], [7.78], [7.37]],
	'comparisons':
		[[('CB', 'GLU', 'MN', 'MN', 15.61)], [('CG', 'GLU', 'MN', 'MN', 14.93)], [('CD', 'GLU', 'MN', 'MN', 15.44)], [('OE1', 'GLU', 'MN', 'MN', 16.68)], [('OE2', 'GLU', 'MN', 'MN', 14.69)], [('CB', 'GLU', 'MN', 'MN', 16.28)], [('CG', 'GLU', 'MN', 'MN', 15.44)], [('CD', 'GLU', 'MN', 'MN', 15.53)], [('OE1', 'GLU', 'MN', 'MN', 16.7)], [('OE2', 'GLU', 'MN', 'MN', 14.53)], [('CB', 'GLU', 'MN', 'MN', 7.34)], [('CG', 'GLU', 'MN', 'MN', 6.29)], [('CD', 'GLU', 'MN', 'MN', 4.96)], [('OE1', 'GLU', 'MN', 'MN', 5.3)], [('OE2', 'GLU', 'MN', 'MN', 4.02)], [('CB', 'GLU', 'MN', 'MN', 9.52)], [('CG', 'GLU', 'MN', 'MN', 9.02)], [('CD', 'GLU', 'MN', 'MN', 7.87)], [('OE1', 'GLU', 'MN', 'MN', 7.78)], [('OE2', 'GLU', 'MN', 'MN', 7.37)]]}
MN_GLUI = { 
	'distances':
		[7.34, 6.29, 4.96, 5.3, 4.02, 9.52, 9.02, 7.87, 7.78, 7.37],
	'comparisons':
		[('MN', 'MN', 'CB', 'GLUI', 7.34), ('MN', 'MN', 'CG', 'GLUI', 6.29), ('MN', 'MN', 'CD', 'GLUI', 4.96), ('MN', 'MN', 'OE1', 'GLUI', 5.3), ('MN', 'MN', 'OE2', 'GLUI', 4.02), ('MN', 'MN', 'CB', 'GLUI', 9.52), ('MN', 'MN', 'CG', 'GLUI', 9.02), ('MN', 'MN', 'CD', 'GLUI', 7.87), ('MN', 'MN', 'OE1', 'GLUI', 7.78), ('MN', 'MN', 'OE2', 'GLUI', 7.37)]}
GLU_HIS = { 
	'distances':
		[[14.39, 14.16, 13.58, 14.63, 13.72, 14.36], [13.71, 13.33, 12.64, 13.77, 12.68, 13.36], [14.55, 14.11, 13.28, 14.57, 13.27, 14.06], [15.76, 15.29, 14.46, 15.71, 14.4, 15.16], [14.11, 13.66, 12.74, 14.19, 12.75, 13.64], [8.81, 10.05, 10.23, 11.32, 11.53, 12.13], [7.71, 9.05, 9.37, 10.3, 10.69, 11.2], [6.55, 7.77, 7.96, 9.07, 9.28, 9.88], [6.5, 7.53, 7.52, 8.86, 8.8, 9.52], [6.08, 7.29, 7.55, 8.57, 8.85, 9.39]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'HIS', 14.39), ('CB', 'GLU', 'CG', 'HIS', 14.16), ('CB', 'GLU', 'ND1', 'HIS', 13.58), ('CB', 'GLU', 'CD2', 'HIS', 14.63), ('CB', 'GLU', 'CE1', 'HIS', 13.72), ('CB', 'GLU', 'NE2', 'HIS', 14.36)], [('CG', 'GLU', 'CB', 'HIS', 13.71), ('CG', 'GLU', 'CG', 'HIS', 13.33), ('CG', 'GLU', 'ND1', 'HIS', 12.64), ('CG', 'GLU', 'CD2', 'HIS', 13.77), ('CG', 'GLU', 'CE1', 'HIS', 12.68), ('CG', 'GLU', 'NE2', 'HIS', 13.36)], [('CD', 'GLU', 'CB', 'HIS', 14.55), ('CD', 'GLU', 'CG', 'HIS', 14.11), ('CD', 'GLU', 'ND1', 'HIS', 13.28), ('CD', 'GLU', 'CD2', 'HIS', 14.57), ('CD', 'GLU', 'CE1', 'HIS', 13.27), ('CD', 'GLU', 'NE2', 'HIS', 14.06)], [('OE1', 'GLU', 'CB', 'HIS', 15.76), ('OE1', 'GLU', 'CG', 'HIS', 15.29), ('OE1', 'GLU', 'ND1', 'HIS', 14.46), ('OE1', 'GLU', 'CD2', 'HIS', 15.71), ('OE1', 'GLU', 'CE1', 'HIS', 14.4), ('OE1', 'GLU', 'NE2', 'HIS', 15.16)], [('OE2', 'GLU', 'CB', 'HIS', 14.11), ('OE2', 'GLU', 'CG', 'HIS', 13.66), ('OE2', 'GLU', 'ND1', 'HIS', 12.74), ('OE2', 'GLU', 'CD2', 'HIS', 14.19), ('OE2', 'GLU', 'CE1', 'HIS', 12.75), ('OE2', 'GLU', 'NE2', 'HIS', 13.64)], [('CB', 'GLU', 'CB', 'HIS', 8.81), ('CB', 'GLU', 'CG', 'HIS', 10.05), ('CB', 'GLU', 'ND1', 'HIS', 10.23), ('CB', 'GLU', 'CD2', 'HIS', 11.32), ('CB', 'GLU', 'CE1', 'HIS', 11.53), ('CB', 'GLU', 'NE2', 'HIS', 12.13)], [('CG', 'GLU', 'CB', 'HIS', 7.71), ('CG', 'GLU', 'CG', 'HIS', 9.05), ('CG', 'GLU', 'ND1', 'HIS', 9.37), ('CG', 'GLU', 'CD2', 'HIS', 10.3), ('CG', 'GLU', 'CE1', 'HIS', 10.69), ('CG', 'GLU', 'NE2', 'HIS', 11.2)], [('CD', 'GLU', 'CB', 'HIS', 6.55), ('CD', 'GLU', 'CG', 'HIS', 7.77), ('CD', 'GLU', 'ND1', 'HIS', 7.96), ('CD', 'GLU', 'CD2', 'HIS', 9.07), ('CD', 'GLU', 'CE1', 'HIS', 9.28), ('CD', 'GLU', 'NE2', 'HIS', 9.88)], [('OE1', 'GLU', 'CB', 'HIS', 6.5), ('OE1', 'GLU', 'CG', 'HIS', 7.53), ('OE1', 'GLU', 'ND1', 'HIS', 7.52), ('OE1', 'GLU', 'CD2', 'HIS', 8.86), ('OE1', 'GLU', 'CE1', 'HIS', 8.8), ('OE1', 'GLU', 'NE2', 'HIS', 9.52)], [('OE2', 'GLU', 'CB', 'HIS', 6.08), ('OE2', 'GLU', 'CG', 'HIS', 7.29), ('OE2', 'GLU', 'ND1', 'HIS', 7.55), ('OE2', 'GLU', 'CD2', 'HIS', 8.57), ('OE2', 'GLU', 'CE1', 'HIS', 8.85), ('OE2', 'GLU', 'NE2', 'HIS', 9.39)]]}
MN_MN = { 
	'distances':
		[5.73, 5.73],
	'comparisons':
		[('MN', 'MN', 'MN', 'MN', 5.73), ('MN', 'MN', 'MN', 'MN', 5.73)]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_GLU, d, 'M_1j53_2_7_7_7')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_GLUI, d, 'M_1j53_2_7_7_7')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_MN, d, 'M_1j53_2_7_7_7')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(GLU_MN, d, 'M_1j53_2_7_7_7')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(MN_GLUI, d, 'M_1j53_2_7_7_7')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(GLU_HIS, d, 'M_1j53_2_7_7_7')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(MN_MN, d, 'M_1j53_2_7_7_7')
	if match7 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_GLU' :  match1,
		'HIS_GLUI' :  match2,
		'HIS_MN' :  match3,
		'GLU_MN' :  match4,
		'MN_GLUI' :  match5,
		'GLU_HIS' :  match6,
		'MN_MN' :  match7}