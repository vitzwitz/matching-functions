'''
FUNC:M_1b66_4_6_1_10
PDB:1b66
EC:4.6.1.10
RESI:glu,zn,asp,his
LOCI:a-133,401;b-88,89;
'''
import motifFunctions as cmd
ASP_ZN = { 
	'distances':
		[[63.55], [64.39], [64.42], [65.12]],
	'comparisons':
		[[('CB', 'ASP', 'ZN', 'ZN', 63.55)], [('CG', 'ASP', 'ZN', 'ZN', 64.39)], [('OD1', 'ASP', 'ZN', 'ZN', 64.42)], [('OD2', 'ASP', 'ZN', 'ZN', 65.12)]]}
ASP_HIS = { 
	'distances':
		[[6.95, 7.27, 6.61, 8.53, 7.63, 8.69], [6.5, 6.4, 5.46, 7.54, 6.31, 7.47], [6.75, 6.44, 5.45, 7.4, 6.05, 7.18], [6.33, 6.09, 5.05, 7.2, 5.86, 7.06]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 6.95), ('CB', 'ASP', 'CG', 'HIS', 7.27), ('CB', 'ASP', 'ND1', 'HIS', 6.61), ('CB', 'ASP', 'CD2', 'HIS', 8.53), ('CB', 'ASP', 'CE1', 'HIS', 7.63), ('CB', 'ASP', 'NE2', 'HIS', 8.69)], [('CG', 'ASP', 'CB', 'HIS', 6.5), ('CG', 'ASP', 'CG', 'HIS', 6.4), ('CG', 'ASP', 'ND1', 'HIS', 5.46), ('CG', 'ASP', 'CD2', 'HIS', 7.54), ('CG', 'ASP', 'CE1', 'HIS', 6.31), ('CG', 'ASP', 'NE2', 'HIS', 7.47)], [('OD1', 'ASP', 'CB', 'HIS', 6.75), ('OD1', 'ASP', 'CG', 'HIS', 6.44), ('OD1', 'ASP', 'ND1', 'HIS', 5.45), ('OD1', 'ASP', 'CD2', 'HIS', 7.4), ('OD1', 'ASP', 'CE1', 'HIS', 6.05), ('OD1', 'ASP', 'NE2', 'HIS', 7.18)], [('OD2', 'ASP', 'CB', 'HIS', 6.33), ('OD2', 'ASP', 'CG', 'HIS', 6.09), ('OD2', 'ASP', 'ND1', 'HIS', 5.05), ('OD2', 'ASP', 'CD2', 'HIS', 7.2), ('OD2', 'ASP', 'CE1', 'HIS', 5.86), ('OD2', 'ASP', 'NE2', 'HIS', 7.06)]]}
GLU_ASP = { 
	'distances':
		[[59.29, 60.17, 60.16, 60.97], [60.26, 61.15, 61.15, 61.92], [60.42, 61.28, 61.27, 62.04], [60.74, 61.58, 61.54, 62.35], [60.29, 61.14, 61.15, 61.88]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ASP', 59.29), ('CB', 'GLU', 'CG', 'ASP', 60.17), ('CB', 'GLU', 'OD1', 'ASP', 60.16), ('CB', 'GLU', 'OD2', 'ASP', 60.97)], [('CG', 'GLU', 'CB', 'ASP', 60.26), ('CG', 'GLU', 'CG', 'ASP', 61.15), ('CG', 'GLU', 'OD1', 'ASP', 61.15), ('CG', 'GLU', 'OD2', 'ASP', 61.92)], [('CD', 'GLU', 'CB', 'ASP', 60.42), ('CD', 'GLU', 'CG', 'ASP', 61.28), ('CD', 'GLU', 'OD1', 'ASP', 61.27), ('CD', 'GLU', 'OD2', 'ASP', 62.04)], [('OE1', 'GLU', 'CB', 'ASP', 60.74), ('OE1', 'GLU', 'CG', 'ASP', 61.58), ('OE1', 'GLU', 'OD1', 'ASP', 61.54), ('OE1', 'GLU', 'OD2', 'ASP', 62.35)], [('OE2', 'GLU', 'CB', 'ASP', 60.29), ('OE2', 'GLU', 'CG', 'ASP', 61.14), ('OE2', 'GLU', 'OD1', 'ASP', 61.15), ('OE2', 'GLU', 'OD2', 'ASP', 61.88)]]}
HIS_ZN = { 
	'distances':
		[[68.37], [68.69], [67.8], [69.79], [68.36], [69.56]],
	'comparisons':
		[[('CB', 'HIS', 'ZN', 'ZN', 68.37)], [('CG', 'HIS', 'ZN', 'ZN', 68.69)], [('ND1', 'HIS', 'ZN', 'ZN', 67.8)], [('CD2', 'HIS', 'ZN', 'ZN', 69.79)], [('CE1', 'HIS', 'ZN', 'ZN', 68.36)], [('NE2', 'HIS', 'ZN', 'ZN', 69.56)]]}
GLU_ZN = { 
	'distances':
		[[8.07], [6.6], [5.93], [6.39], [5.46]],
	'comparisons':
		[[('CB', 'GLU', 'ZN', 'ZN', 8.07)], [('CG', 'GLU', 'ZN', 'ZN', 6.6)], [('CD', 'GLU', 'ZN', 'ZN', 5.93)], [('OE1', 'GLU', 'ZN', 'ZN', 6.39)], [('OE2', 'GLU', 'ZN', 'ZN', 5.46)]]}
GLU_HIS = { 
	'distances':
		[[64.02, 64.38, 63.56, 65.48, 64.14, 65.31], [65.02, 65.38, 64.54, 66.48, 65.12, 66.3], [65.21, 65.53, 64.67, 66.62, 65.22, 66.4], [65.52, 65.82, 64.95, 66.89, 65.49, 66.66], [65.1, 65.41, 64.53, 66.5, 65.08, 66.28]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'HIS', 64.02), ('CB', 'GLU', 'CG', 'HIS', 64.38), ('CB', 'GLU', 'ND1', 'HIS', 63.56), ('CB', 'GLU', 'CD2', 'HIS', 65.48), ('CB', 'GLU', 'CE1', 'HIS', 64.14), ('CB', 'GLU', 'NE2', 'HIS', 65.31)], [('CG', 'GLU', 'CB', 'HIS', 65.02), ('CG', 'GLU', 'CG', 'HIS', 65.38), ('CG', 'GLU', 'ND1', 'HIS', 64.54), ('CG', 'GLU', 'CD2', 'HIS', 66.48), ('CG', 'GLU', 'CE1', 'HIS', 65.12), ('CG', 'GLU', 'NE2', 'HIS', 66.3)], [('CD', 'GLU', 'CB', 'HIS', 65.21), ('CD', 'GLU', 'CG', 'HIS', 65.53), ('CD', 'GLU', 'ND1', 'HIS', 64.67), ('CD', 'GLU', 'CD2', 'HIS', 66.62), ('CD', 'GLU', 'CE1', 'HIS', 65.22), ('CD', 'GLU', 'NE2', 'HIS', 66.4)], [('OE1', 'GLU', 'CB', 'HIS', 65.52), ('OE1', 'GLU', 'CG', 'HIS', 65.82), ('OE1', 'GLU', 'ND1', 'HIS', 64.95), ('OE1', 'GLU', 'CD2', 'HIS', 66.89), ('OE1', 'GLU', 'CE1', 'HIS', 65.49), ('OE1', 'GLU', 'NE2', 'HIS', 66.66)], [('OE2', 'GLU', 'CB', 'HIS', 65.1), ('OE2', 'GLU', 'CG', 'HIS', 65.41), ('OE2', 'GLU', 'ND1', 'HIS', 64.53), ('OE2', 'GLU', 'CD2', 'HIS', 66.5), ('OE2', 'GLU', 'CE1', 'HIS', 65.08), ('OE2', 'GLU', 'NE2', 'HIS', 66.28)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_ZN, d, 'M_1b66_4_6_1_10')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_HIS, d, 'M_1b66_4_6_1_10')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_ASP, d, 'M_1b66_4_6_1_10')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(HIS_ZN, d, 'M_1b66_4_6_1_10')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(GLU_ZN, d, 'M_1b66_4_6_1_10')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(GLU_HIS, d, 'M_1b66_4_6_1_10')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_ZN' :  match1,
		'ASP_HIS' :  match2,
		'GLU_ASP' :  match3,
		'HIS_ZN' :  match4,
		'GLU_ZN' :  match5,
		'GLU_HIS' :  match6}