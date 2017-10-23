'''
FUNC:A_1pad_3_4_22_2
PDB:1pad
EC:3.4.22.2
RESI:cys,his,asn
LOCI:a-25,159,175;
'''
import motifFunctions as cmd
CYS_HIS = { 
	'distances':
		[[7.3, 6.48, 5.18, 7.13, 5.26, 6.5], [6.89, 6.57, 5.46, 7.61, 6.14, 7.36]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'HIS', 7.3), ('CB', 'CYS', 'CG', 'HIS', 6.48), ('CB', 'CYS', 'ND1', 'HIS', 5.18), ('CB', 'CYS', 'CD2', 'HIS', 7.13), ('CB', 'CYS', 'CE1', 'HIS', 5.26), ('CB', 'CYS', 'NE2', 'HIS', 6.5)], [('SG', 'CYS', 'CB', 'HIS', 6.89), ('SG', 'CYS', 'CG', 'HIS', 6.57), ('SG', 'CYS', 'ND1', 'HIS', 5.46), ('SG', 'CYS', 'CD2', 'HIS', 7.61), ('SG', 'CYS', 'CE1', 'HIS', 6.14), ('SG', 'CYS', 'NE2', 'HIS', 7.36)]]}
CYS_ASN = { 
	'distances':
		[[10.84, 9.96, 8.68, 10.43], [12.28, 11.31, 9.99, 11.72]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'ASN', 10.84), ('CB', 'CYS', 'CG', 'ASN', 9.96), ('CB', 'CYS', 'OD1', 'ASN', 8.68), ('CB', 'CYS', 'ND2', 'ASN', 10.43)], [('SG', 'CYS', 'CB', 'ASN', 12.28), ('SG', 'CYS', 'CG', 'ASN', 11.31), ('SG', 'CYS', 'OD1', 'ASN', 9.99), ('SG', 'CYS', 'ND2', 'ASN', 11.72)]]}
HIS_ASN = { 
	'distances':
		[[10.88, 9.71, 8.53, 9.93], [9.58, 8.38, 7.17, 8.6], [9.69, 8.5, 7.24, 8.75], [8.33, 7.11, 5.97, 7.32], [8.6, 7.4, 6.18, 7.66], [7.64, 6.38, 5.19, 6.62]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASN', 10.88), ('CB', 'HIS', 'CG', 'ASN', 9.71), ('CB', 'HIS', 'OD1', 'ASN', 8.53), ('CB', 'HIS', 'ND2', 'ASN', 9.93)], [('CG', 'HIS', 'CB', 'ASN', 9.58), ('CG', 'HIS', 'CG', 'ASN', 8.38), ('CG', 'HIS', 'OD1', 'ASN', 7.17), ('CG', 'HIS', 'ND2', 'ASN', 8.6)], [('ND1', 'HIS', 'CB', 'ASN', 9.69), ('ND1', 'HIS', 'CG', 'ASN', 8.5), ('ND1', 'HIS', 'OD1', 'ASN', 7.24), ('ND1', 'HIS', 'ND2', 'ASN', 8.75)], [('CD2', 'HIS', 'CB', 'ASN', 8.33), ('CD2', 'HIS', 'CG', 'ASN', 7.11), ('CD2', 'HIS', 'OD1', 'ASN', 5.97), ('CD2', 'HIS', 'ND2', 'ASN', 7.32)], [('CE1', 'HIS', 'CB', 'ASN', 8.6), ('CE1', 'HIS', 'CG', 'ASN', 7.4), ('CE1', 'HIS', 'OD1', 'ASN', 6.18), ('CE1', 'HIS', 'ND2', 'ASN', 7.66)], [('NE2', 'HIS', 'CB', 'ASN', 7.64), ('NE2', 'HIS', 'CG', 'ASN', 6.38), ('NE2', 'HIS', 'OD1', 'ASN', 5.19), ('NE2', 'HIS', 'ND2', 'ASN', 6.62)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(CYS_HIS, d, 'A_1pad_3_4_22_2')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(CYS_ASN, d, 'A_1pad_3_4_22_2')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_ASN, d, 'A_1pad_3_4_22_2')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'CYS_HIS' :  match1,
		'CYS_ASN' :  match2,
		'HIS_ASN' :  match3}