'''
FUNC:P_1ecg_2_4_2_14
PDB:1ecg
EC:2.4.2.14
RESI:cys,asn,gly
LOCI:a-1,101,102;
'''
import motifFunctions as cmd
CYS_GLY = { 
	'distances':
		[[7.87, 8.47, 7.94, 6.61], [7.48, 8.33, 8.17, 6.98], [9.31, 9.51, 8.49, 7.29], [9.47, 9.82, 8.94, 7.64], [8.83, 9.36, 8.71, 7.45], [8.35, 8.88, 8.26, 7.18]],
	'comparisons':
		[[('CB', 'CYS', 'O', 'GLY', 7.87), ('CB', 'CYS', 'C', 'GLY', 8.47), ('CB', 'CYS', 'CA', 'GLY', 7.94), ('CB', 'CYS', 'N', 'GLY', 6.61)], [('SG', 'CYS', 'O', 'GLY', 7.48), ('SG', 'CYS', 'C', 'GLY', 8.33), ('SG', 'CYS', 'CA', 'GLY', 8.17), ('SG', 'CYS', 'N', 'GLY', 6.98)], [('O', 'CYS', 'O', 'GLY', 9.31), ('O', 'CYS', 'C', 'GLY', 9.51), ('O', 'CYS', 'CA', 'GLY', 8.49), ('O', 'CYS', 'N', 'GLY', 7.29)], [('C', 'CYS', 'O', 'GLY', 9.47), ('C', 'CYS', 'C', 'GLY', 9.82), ('C', 'CYS', 'CA', 'GLY', 8.94), ('C', 'CYS', 'N', 'GLY', 7.64)], [('CA', 'CYS', 'O', 'GLY', 8.83), ('CA', 'CYS', 'C', 'GLY', 9.36), ('CA', 'CYS', 'CA', 'GLY', 8.71), ('CA', 'CYS', 'N', 'GLY', 7.45)], [('N', 'CYS', 'O', 'GLY', 8.35), ('N', 'CYS', 'C', 'GLY', 8.88), ('N', 'CYS', 'CA', 'GLY', 8.26), ('N', 'CYS', 'N', 'GLY', 7.18)]]}
ASN_GLY = { 
	'distances':
		[[7.22, 7.06, 5.82, 4.58], [7.14, 6.97, 5.7, 4.69], [8.12, 7.83, 6.47, 5.67], [6.3, 6.32, 5.25, 4.28]],
	'comparisons':
		[[('CB', 'ASN', 'O', 'GLY', 7.22), ('CB', 'ASN', 'C', 'GLY', 7.06), ('CB', 'ASN', 'CA', 'GLY', 5.82), ('CB', 'ASN', 'N', 'GLY', 4.58)], [('CG', 'ASN', 'O', 'GLY', 7.14), ('CG', 'ASN', 'C', 'GLY', 6.97), ('CG', 'ASN', 'CA', 'GLY', 5.7), ('CG', 'ASN', 'N', 'GLY', 4.69)], [('OD1', 'ASN', 'O', 'GLY', 8.12), ('OD1', 'ASN', 'C', 'GLY', 7.83), ('OD1', 'ASN', 'CA', 'GLY', 6.47), ('OD1', 'ASN', 'N', 'GLY', 5.67)], [('ND2', 'ASN', 'O', 'GLY', 6.3), ('ND2', 'ASN', 'C', 'GLY', 6.32), ('ND2', 'ASN', 'CA', 'GLY', 5.25), ('ND2', 'ASN', 'N', 'GLY', 4.28)]]}
CYS_ASN = { 
	'distances':
		[[5.31, 5.49, 6.44, 5.03], [6.68, 6.77, 7.81, 5.99], [4.6, 4.16, 4.37, 4.37], [5.12, 5.0, 5.45, 5.04], [5.71, 5.52, 6.2, 5.11], [5.94, 5.28, 5.87, 4.56]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'ASN', 5.31), ('CB', 'CYS', 'CG', 'ASN', 5.49), ('CB', 'CYS', 'OD1', 'ASN', 6.44), ('CB', 'CYS', 'ND2', 'ASN', 5.03)], [('SG', 'CYS', 'CB', 'ASN', 6.68), ('SG', 'CYS', 'CG', 'ASN', 6.77), ('SG', 'CYS', 'OD1', 'ASN', 7.81), ('SG', 'CYS', 'ND2', 'ASN', 5.99)], [('O', 'CYS', 'CB', 'ASN', 4.6), ('O', 'CYS', 'CG', 'ASN', 4.16), ('O', 'CYS', 'OD1', 'ASN', 4.37), ('O', 'CYS', 'ND2', 'ASN', 4.37)], [('C', 'CYS', 'CB', 'ASN', 5.12), ('C', 'CYS', 'CG', 'ASN', 5.0), ('C', 'CYS', 'OD1', 'ASN', 5.45), ('C', 'CYS', 'ND2', 'ASN', 5.04)], [('CA', 'CYS', 'CB', 'ASN', 5.71), ('CA', 'CYS', 'CG', 'ASN', 5.52), ('CA', 'CYS', 'OD1', 'ASN', 6.2), ('CA', 'CYS', 'ND2', 'ASN', 5.11)], [('N', 'CYS', 'CB', 'ASN', 5.94), ('N', 'CYS', 'CG', 'ASN', 5.28), ('N', 'CYS', 'OD1', 'ASN', 5.87), ('N', 'CYS', 'ND2', 'ASN', 4.56)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(CYS_GLY, d, 'P_1ecg_2_4_2_14')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASN_GLY, d, 'P_1ecg_2_4_2_14')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(CYS_ASN, d, 'P_1ecg_2_4_2_14')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'CYS_GLY' :  match1,
		'ASN_GLY' :  match2,
		'CYS_ASN' :  match3}