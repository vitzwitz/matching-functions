'''
FUNC:A_1cgk_2_3_1_74
PDB:1cgk
EC:2.3.1.74
RESI:cys,phe,his,asn
LOCI:a-164,215,303,336;
'''
import motifFunctions as cmd
HIS_CYS = { 
	'distances':
		[[7.54, 8.68], [6.44, 7.34], [6.51, 7.2], [5.77, 6.45], [5.9, 6.18], [5.38, 5.6]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'CYS', 7.54), ('CB', 'HIS', 'SG', 'CYS', 8.68)], [('CG', 'HIS', 'CB', 'CYS', 6.44), ('CG', 'HIS', 'SG', 'CYS', 7.34)], [('ND1', 'HIS', 'CB', 'CYS', 6.51), ('ND1', 'HIS', 'SG', 'CYS', 7.2)], [('CD2', 'HIS', 'CB', 'CYS', 5.77), ('CD2', 'HIS', 'SG', 'CYS', 6.45)], [('CE1', 'HIS', 'CB', 'CYS', 5.9), ('CE1', 'HIS', 'SG', 'CYS', 6.18)], [('NE2', 'HIS', 'CB', 'CYS', 5.38), ('NE2', 'HIS', 'SG', 'CYS', 5.6)]]}
ASN_CYS = { 
	'distances':
		[[9.14, 8.05], [7.63, 6.52], [7.02, 6.04], [7.3, 6.11]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'CYS', 9.14), ('CB', 'ASN', 'SG', 'CYS', 8.05)], [('CG', 'ASN', 'CB', 'CYS', 7.63), ('CG', 'ASN', 'SG', 'CYS', 6.52)], [('OD1', 'ASN', 'CB', 'CYS', 7.02), ('OD1', 'ASN', 'SG', 'CYS', 6.04)], [('ND2', 'ASN', 'CB', 'CYS', 7.3), ('ND2', 'ASN', 'SG', 'CYS', 6.11)]]}
PHE_CYS = { 
	'distances':
		[[11.32, 9.62], [10.21, 8.45], [8.9, 7.17], [10.64, 8.85], [7.95, 6.17], [9.93, 8.15], [8.58, 6.81]],
	'comparisons':
		[[('CB', 'PHE', 'CB', 'CYS', 11.32), ('CB', 'PHE', 'SG', 'CYS', 9.62)], [('CG', 'PHE', 'CB', 'CYS', 10.21), ('CG', 'PHE', 'SG', 'CYS', 8.45)], [('CD1', 'PHE', 'CB', 'CYS', 8.9), ('CD1', 'PHE', 'SG', 'CYS', 7.17)], [('CD2', 'PHE', 'CB', 'CYS', 10.64), ('CD2', 'PHE', 'SG', 'CYS', 8.85)], [('CE1', 'PHE', 'CB', 'CYS', 7.95), ('CE1', 'PHE', 'SG', 'CYS', 6.17)], [('CE2', 'PHE', 'CB', 'CYS', 9.93), ('CE2', 'PHE', 'SG', 'CYS', 8.15)], [('CZ', 'PHE', 'CB', 'CYS', 8.58), ('CZ', 'PHE', 'SG', 'CYS', 6.81)]]}
ASN_HIS = { 
	'distances':
		[[9.95, 8.61, 7.98, 8.01, 6.88, 6.88], [9.07, 7.63, 7.06, 6.91, 5.81, 5.67], [8.64, 7.18, 6.4, 6.64, 5.11, 5.28], [9.09, 7.66, 7.39, 6.68, 6.17, 5.59]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'HIS', 9.95), ('CB', 'ASN', 'CG', 'HIS', 8.61), ('CB', 'ASN', 'ND1', 'HIS', 7.98), ('CB', 'ASN', 'CD2', 'HIS', 8.01), ('CB', 'ASN', 'CE1', 'HIS', 6.88), ('CB', 'ASN', 'NE2', 'HIS', 6.88)], [('CG', 'ASN', 'CB', 'HIS', 9.07), ('CG', 'ASN', 'CG', 'HIS', 7.63), ('CG', 'ASN', 'ND1', 'HIS', 7.06), ('CG', 'ASN', 'CD2', 'HIS', 6.91), ('CG', 'ASN', 'CE1', 'HIS', 5.81), ('CG', 'ASN', 'NE2', 'HIS', 5.67)], [('OD1', 'ASN', 'CB', 'HIS', 8.64), ('OD1', 'ASN', 'CG', 'HIS', 7.18), ('OD1', 'ASN', 'ND1', 'HIS', 6.4), ('OD1', 'ASN', 'CD2', 'HIS', 6.64), ('OD1', 'ASN', 'CE1', 'HIS', 5.11), ('OD1', 'ASN', 'NE2', 'HIS', 5.28)], [('ND2', 'ASN', 'CB', 'HIS', 9.09), ('ND2', 'ASN', 'CG', 'HIS', 7.66), ('ND2', 'ASN', 'ND1', 'HIS', 7.39), ('ND2', 'ASN', 'CD2', 'HIS', 6.68), ('ND2', 'ASN', 'CE1', 'HIS', 6.17), ('ND2', 'ASN', 'NE2', 'HIS', 5.59)]]}
PHE_HIS = { 
	'distances':
		[[14.41, 12.92, 12.21, 12.15, 10.9, 10.84], [13.64, 12.14, 11.56, 11.25, 10.22, 9.99], [12.29, 10.79, 10.22, 9.92, 8.88, 8.64], [14.41, 12.92, 12.47, 11.93, 11.13, 10.74], [11.75, 10.26, 9.86, 9.27, 8.54, 8.09], [13.98, 12.52, 12.21, 11.44, 10.89, 10.35], [12.68, 11.22, 10.97, 10.13, 9.67, 9.07]],
	'comparisons':
		[[('CB', 'PHE', 'CB', 'HIS', 14.41), ('CB', 'PHE', 'CG', 'HIS', 12.92), ('CB', 'PHE', 'ND1', 'HIS', 12.21), ('CB', 'PHE', 'CD2', 'HIS', 12.15), ('CB', 'PHE', 'CE1', 'HIS', 10.9), ('CB', 'PHE', 'NE2', 'HIS', 10.84)], [('CG', 'PHE', 'CB', 'HIS', 13.64), ('CG', 'PHE', 'CG', 'HIS', 12.14), ('CG', 'PHE', 'ND1', 'HIS', 11.56), ('CG', 'PHE', 'CD2', 'HIS', 11.25), ('CG', 'PHE', 'CE1', 'HIS', 10.22), ('CG', 'PHE', 'NE2', 'HIS', 9.99)], [('CD1', 'PHE', 'CB', 'HIS', 12.29), ('CD1', 'PHE', 'CG', 'HIS', 10.79), ('CD1', 'PHE', 'ND1', 'HIS', 10.22), ('CD1', 'PHE', 'CD2', 'HIS', 9.92), ('CD1', 'PHE', 'CE1', 'HIS', 8.88), ('CD1', 'PHE', 'NE2', 'HIS', 8.64)], [('CD2', 'PHE', 'CB', 'HIS', 14.41), ('CD2', 'PHE', 'CG', 'HIS', 12.92), ('CD2', 'PHE', 'ND1', 'HIS', 12.47), ('CD2', 'PHE', 'CD2', 'HIS', 11.93), ('CD2', 'PHE', 'CE1', 'HIS', 11.13), ('CD2', 'PHE', 'NE2', 'HIS', 10.74)], [('CE1', 'PHE', 'CB', 'HIS', 11.75), ('CE1', 'PHE', 'CG', 'HIS', 10.26), ('CE1', 'PHE', 'ND1', 'HIS', 9.86), ('CE1', 'PHE', 'CD2', 'HIS', 9.27), ('CE1', 'PHE', 'CE1', 'HIS', 8.54), ('CE1', 'PHE', 'NE2', 'HIS', 8.09)], [('CE2', 'PHE', 'CB', 'HIS', 13.98), ('CE2', 'PHE', 'CG', 'HIS', 12.52), ('CE2', 'PHE', 'ND1', 'HIS', 12.21), ('CE2', 'PHE', 'CD2', 'HIS', 11.44), ('CE2', 'PHE', 'CE1', 'HIS', 10.89), ('CE2', 'PHE', 'NE2', 'HIS', 10.35)], [('CZ', 'PHE', 'CB', 'HIS', 12.68), ('CZ', 'PHE', 'CG', 'HIS', 11.22), ('CZ', 'PHE', 'ND1', 'HIS', 10.97), ('CZ', 'PHE', 'CD2', 'HIS', 10.13), ('CZ', 'PHE', 'CE1', 'HIS', 9.67), ('CZ', 'PHE', 'NE2', 'HIS', 9.07)]]}
PHE_ASN = { 
	'distances':
		[[7.31, 7.49, 7.82, 7.79], [7.06, 6.9, 7.28, 6.91], [6.19, 5.73, 6.01, 5.75], [8.16, 7.89, 8.34, 7.64], [6.65, 5.8, 6.07, 5.41], [8.48, 7.95, 8.39, 7.43], [7.82, 7.03, 7.4, 6.4]],
	'comparisons':
		[[('CB', 'PHE', 'CB', 'ASN', 7.31), ('CB', 'PHE', 'CG', 'ASN', 7.49), ('CB', 'PHE', 'OD1', 'ASN', 7.82), ('CB', 'PHE', 'ND2', 'ASN', 7.79)], [('CG', 'PHE', 'CB', 'ASN', 7.06), ('CG', 'PHE', 'CG', 'ASN', 6.9), ('CG', 'PHE', 'OD1', 'ASN', 7.28), ('CG', 'PHE', 'ND2', 'ASN', 6.91)], [('CD1', 'PHE', 'CB', 'ASN', 6.19), ('CD1', 'PHE', 'CG', 'ASN', 5.73), ('CD1', 'PHE', 'OD1', 'ASN', 6.01), ('CD1', 'PHE', 'ND2', 'ASN', 5.75)], [('CD2', 'PHE', 'CB', 'ASN', 8.16), ('CD2', 'PHE', 'CG', 'ASN', 7.89), ('CD2', 'PHE', 'OD1', 'ASN', 8.34), ('CD2', 'PHE', 'ND2', 'ASN', 7.64)], [('CE1', 'PHE', 'CB', 'ASN', 6.65), ('CE1', 'PHE', 'CG', 'ASN', 5.8), ('CE1', 'PHE', 'OD1', 'ASN', 6.07), ('CE1', 'PHE', 'ND2', 'ASN', 5.41)], [('CE2', 'PHE', 'CB', 'ASN', 8.48), ('CE2', 'PHE', 'CG', 'ASN', 7.95), ('CE2', 'PHE', 'OD1', 'ASN', 8.39), ('CE2', 'PHE', 'ND2', 'ASN', 7.43)], [('CZ', 'PHE', 'CB', 'ASN', 7.82), ('CZ', 'PHE', 'CG', 'ASN', 7.03), ('CZ', 'PHE', 'OD1', 'ASN', 7.4), ('CZ', 'PHE', 'ND2', 'ASN', 6.4)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_CYS, d, 'A_1cgk_2_3_1_74')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASN_CYS, d, 'A_1cgk_2_3_1_74')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(PHE_CYS, d, 'A_1cgk_2_3_1_74')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASN_HIS, d, 'A_1cgk_2_3_1_74')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(PHE_HIS, d, 'A_1cgk_2_3_1_74')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(PHE_ASN, d, 'A_1cgk_2_3_1_74')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_CYS' :  match1,
		'ASN_CYS' :  match2,
		'PHE_CYS' :  match3,
		'ASN_HIS' :  match4,
		'PHE_HIS' :  match5,
		'PHE_ASN' :  match6}