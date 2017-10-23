'''
FUNC:A_1l1l_1_17_4_2
PDB:1l1l
EC:1.17.4.2
RESI:cys,asn,cys,glu,cys
LOCI:a-119,406,408,410,419;
'''
import motifFunctions as cmd
CYS_CYS = { 
	'distances':
		[[5.85, 5.03], [5.05, 4.03], [9.17, 9.31], [8.8, 8.95], [5.85, 5.05], [5.03, 4.03], [10.47, 11.13], [10.56, 10.86], [9.17, 8.8], [9.31, 8.95]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'CYS', 5.85), ('CB', 'CYS', 'SG', 'CYS', 5.03)], [('SG', 'CYS', 'CB', 'CYS', 5.05), ('SG', 'CYS', 'SG', 'CYS', 4.03)], [('CB', 'CYS', 'CB', 'CYS', 9.17), ('CB', 'CYS', 'SG', 'CYS', 9.31)], [('SG', 'CYS', 'CB', 'CYS', 8.8), ('SG', 'CYS', 'SG', 'CYS', 8.95)], [('CB', 'CYS', 'CB', 'CYS', 5.85), ('CB', 'CYS', 'SG', 'CYS', 5.05)], [('SG', 'CYS', 'CB', 'CYS', 5.03), ('SG', 'CYS', 'SG', 'CYS', 4.03)], [('CB', 'CYS', 'CB', 'CYS', 10.47), ('CB', 'CYS', 'SG', 'CYS', 11.13)], [('SG', 'CYS', 'CB', 'CYS', 10.56), ('SG', 'CYS', 'SG', 'CYS', 10.86)], [('CB', 'CYS', 'CB', 'CYS', 9.17), ('CB', 'CYS', 'SG', 'CYS', 8.8)], [('SG', 'CYS', 'CB', 'CYS', 9.31), ('SG', 'CYS', 'SG', 'CYS', 8.95)]]}
ASN_GLU = { 
	'distances':
		[[8.99, 8.36, 7.62, 7.04, 7.97], [7.49, 6.89, 6.19, 5.6, 6.69], [6.85, 6.43, 6.1, 5.6, 6.83], [7.17, 6.47, 5.42, 4.78, 5.75]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'GLU', 8.99), ('CB', 'ASN', 'CG', 'GLU', 8.36), ('CB', 'ASN', 'CD', 'GLU', 7.62), ('CB', 'ASN', 'OE1', 'GLU', 7.04), ('CB', 'ASN', 'OE2', 'GLU', 7.97)], [('CG', 'ASN', 'CB', 'GLU', 7.49), ('CG', 'ASN', 'CG', 'GLU', 6.89), ('CG', 'ASN', 'CD', 'GLU', 6.19), ('CG', 'ASN', 'OE1', 'GLU', 5.6), ('CG', 'ASN', 'OE2', 'GLU', 6.69)], [('OD1', 'ASN', 'CB', 'GLU', 6.85), ('OD1', 'ASN', 'CG', 'GLU', 6.43), ('OD1', 'ASN', 'CD', 'GLU', 6.1), ('OD1', 'ASN', 'OE1', 'GLU', 5.6), ('OD1', 'ASN', 'OE2', 'GLU', 6.83)], [('ND2', 'ASN', 'CB', 'GLU', 7.17), ('ND2', 'ASN', 'CG', 'GLU', 6.47), ('ND2', 'ASN', 'CD', 'GLU', 5.42), ('ND2', 'ASN', 'OE1', 'GLU', 4.78), ('ND2', 'ASN', 'OE2', 'GLU', 5.75)]]}
CYS_ASN = { 
	'distances':
		[[5.67, 6.39, 7.48, 6.21], [6.44, 6.58, 7.56, 6.04], [7.03, 6.98, 7.4, 7.01], [7.53, 7.7, 8.42, 7.45], [7.81, 6.87, 7.34, 5.86], [8.72, 8.04, 8.75, 6.93]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'ASN', 5.67), ('CB', 'CYS', 'CG', 'ASN', 6.39), ('CB', 'CYS', 'OD1', 'ASN', 7.48), ('CB', 'CYS', 'ND2', 'ASN', 6.21)], [('SG', 'CYS', 'CB', 'ASN', 6.44), ('SG', 'CYS', 'CG', 'ASN', 6.58), ('SG', 'CYS', 'OD1', 'ASN', 7.56), ('SG', 'CYS', 'ND2', 'ASN', 6.04)], [('CB', 'CYS', 'CB', 'ASN', 7.03), ('CB', 'CYS', 'CG', 'ASN', 6.98), ('CB', 'CYS', 'OD1', 'ASN', 7.4), ('CB', 'CYS', 'ND2', 'ASN', 7.01)], [('SG', 'CYS', 'CB', 'ASN', 7.53), ('SG', 'CYS', 'CG', 'ASN', 7.7), ('SG', 'CYS', 'OD1', 'ASN', 8.42), ('SG', 'CYS', 'ND2', 'ASN', 7.45)], [('CB', 'CYS', 'CB', 'ASN', 7.81), ('CB', 'CYS', 'CG', 'ASN', 6.87), ('CB', 'CYS', 'OD1', 'ASN', 7.34), ('CB', 'CYS', 'ND2', 'ASN', 5.86)], [('SG', 'CYS', 'CB', 'ASN', 8.72), ('SG', 'CYS', 'CG', 'ASN', 8.04), ('SG', 'CYS', 'OD1', 'ASN', 8.75), ('SG', 'CYS', 'ND2', 'ASN', 6.93)]]}
GLU_CYSII = { 
	'distances':
		[[7.46, 9.07], [7.46, 8.91], [6.24, 7.56], [5.16, 6.66], [6.66, 7.64]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'CYSII', 7.46), ('CB', 'GLU', 'SG', 'CYSII', 9.07)], [('CG', 'GLU', 'CB', 'CYSII', 7.46), ('CG', 'GLU', 'SG', 'CYSII', 8.91)], [('CD', 'GLU', 'CB', 'CYSII', 6.24), ('CD', 'GLU', 'SG', 'CYSII', 7.56)], [('OE1', 'GLU', 'CB', 'CYSII', 5.16), ('OE1', 'GLU', 'SG', 'CYSII', 6.66)], [('OE2', 'GLU', 'CB', 'CYSII', 6.66), ('OE2', 'GLU', 'SG', 'CYSII', 7.64)]]}
CYS_CYSI = { 
	'distances':
		[[10.47, 10.56], [11.13, 10.86]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'CYSI', 10.47), ('CB', 'CYS', 'SG', 'CYSI', 10.56)], [('SG', 'CYS', 'CB', 'CYSI', 11.13), ('SG', 'CYS', 'SG', 'CYSI', 10.86)]]}
GLU_CYSI = { 
	'distances':
		[[9.82, 10.89], [8.46, 9.51], [8.0, 8.74], [8.46, 9.1], [7.51, 8.05]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'CYSI', 9.82), ('CB', 'GLU', 'SG', 'CYSI', 10.89)], [('CG', 'GLU', 'CB', 'CYSI', 8.46), ('CG', 'GLU', 'SG', 'CYSI', 9.51)], [('CD', 'GLU', 'CB', 'CYSI', 8.0), ('CD', 'GLU', 'SG', 'CYSI', 8.74)], [('OE1', 'GLU', 'CB', 'CYSI', 8.46), ('OE1', 'GLU', 'SG', 'CYSI', 9.1)], [('OE2', 'GLU', 'CB', 'CYSI', 7.51), ('OE2', 'GLU', 'SG', 'CYSI', 8.05)]]}
CYS_GLU = { 
	'distances':
		[[11.01, 9.91, 8.86, 8.67, 8.49], [10.17, 8.91, 7.83, 7.91, 7.21], [9.82, 8.46, 8.0, 8.46, 7.51], [10.89, 9.51, 8.74, 9.1, 8.05], [7.46, 7.46, 6.24, 5.16, 6.66], [9.07, 8.91, 7.56, 6.66, 7.64]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'GLU', 11.01), ('CB', 'CYS', 'CG', 'GLU', 9.91), ('CB', 'CYS', 'CD', 'GLU', 8.86), ('CB', 'CYS', 'OE1', 'GLU', 8.67), ('CB', 'CYS', 'OE2', 'GLU', 8.49)], [('SG', 'CYS', 'CB', 'GLU', 10.17), ('SG', 'CYS', 'CG', 'GLU', 8.91), ('SG', 'CYS', 'CD', 'GLU', 7.83), ('SG', 'CYS', 'OE1', 'GLU', 7.91), ('SG', 'CYS', 'OE2', 'GLU', 7.21)], [('CB', 'CYS', 'CB', 'GLU', 9.82), ('CB', 'CYS', 'CG', 'GLU', 8.46), ('CB', 'CYS', 'CD', 'GLU', 8.0), ('CB', 'CYS', 'OE1', 'GLU', 8.46), ('CB', 'CYS', 'OE2', 'GLU', 7.51)], [('SG', 'CYS', 'CB', 'GLU', 10.89), ('SG', 'CYS', 'CG', 'GLU', 9.51), ('SG', 'CYS', 'CD', 'GLU', 8.74), ('SG', 'CYS', 'OE1', 'GLU', 9.1), ('SG', 'CYS', 'OE2', 'GLU', 8.05)], [('CB', 'CYS', 'CB', 'GLU', 7.46), ('CB', 'CYS', 'CG', 'GLU', 7.46), ('CB', 'CYS', 'CD', 'GLU', 6.24), ('CB', 'CYS', 'OE1', 'GLU', 5.16), ('CB', 'CYS', 'OE2', 'GLU', 6.66)], [('SG', 'CYS', 'CB', 'GLU', 9.07), ('SG', 'CYS', 'CG', 'GLU', 8.91), ('SG', 'CYS', 'CD', 'GLU', 7.56), ('SG', 'CYS', 'OE1', 'GLU', 6.66), ('SG', 'CYS', 'OE2', 'GLU', 7.64)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(CYS_CYS, d, 'A_1l1l_1_17_4_2')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASN_GLU, d, 'A_1l1l_1_17_4_2')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(CYS_ASN, d, 'A_1l1l_1_17_4_2')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(GLU_CYSII, d, 'A_1l1l_1_17_4_2')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(CYS_CYSI, d, 'A_1l1l_1_17_4_2')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(GLU_CYSI, d, 'A_1l1l_1_17_4_2')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(CYS_GLU, d, 'A_1l1l_1_17_4_2')
	if match7 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'CYS_CYS' :  match1,
		'ASN_GLU' :  match2,
		'CYS_ASN' :  match3,
		'GLU_CYSII' :  match4,
		'CYS_CYSI' :  match5,
		'GLU_CYSI' :  match6,
		'CYS_GLU' :  match7}