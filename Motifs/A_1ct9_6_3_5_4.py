'''
FUNC:A_1ct9_6_3_5_4
PDB:1ct9
EC:6.3.5.4
RESI:ala,asn,gly
LOCI:a-1,74,75;
'''
import motifFunctions as cmd
ASN_GLY = { 
	'distances':
		[[8.3, 8.13, 6.84, 5.66], [8.39, 8.17, 6.9, 5.92], [9.37, 9.03, 7.69, 6.9], [7.64, 7.57, 6.53, 5.58], [6.77, 6.09, 4.59, 4.22], [6.08, 5.7, 4.35, 3.33], [7.02, 6.92, 5.76, 4.44], [7.54, 7.45, 6.39, 5.19]],
	'comparisons':
		[[('CB', 'ASN', 'O', 'GLY', 8.3), ('CB', 'ASN', 'C', 'GLY', 8.13), ('CB', 'ASN', 'CA', 'GLY', 6.84), ('CB', 'ASN', 'N', 'GLY', 5.66)], [('CG', 'ASN', 'O', 'GLY', 8.39), ('CG', 'ASN', 'C', 'GLY', 8.17), ('CG', 'ASN', 'CA', 'GLY', 6.9), ('CG', 'ASN', 'N', 'GLY', 5.92)], [('OD1', 'ASN', 'O', 'GLY', 9.37), ('OD1', 'ASN', 'C', 'GLY', 9.03), ('OD1', 'ASN', 'CA', 'GLY', 7.69), ('OD1', 'ASN', 'N', 'GLY', 6.9)], [('ND2', 'ASN', 'O', 'GLY', 7.64), ('ND2', 'ASN', 'C', 'GLY', 7.57), ('ND2', 'ASN', 'CA', 'GLY', 6.53), ('ND2', 'ASN', 'N', 'GLY', 5.58)], [('O', 'ASN', 'O', 'GLY', 6.77), ('O', 'ASN', 'C', 'GLY', 6.09), ('O', 'ASN', 'CA', 'GLY', 4.59), ('O', 'ASN', 'N', 'GLY', 4.22)], [('C', 'ASN', 'O', 'GLY', 6.08), ('C', 'ASN', 'C', 'GLY', 5.7), ('C', 'ASN', 'CA', 'GLY', 4.35), ('C', 'ASN', 'N', 'GLY', 3.33)], [('CA', 'ASN', 'O', 'GLY', 7.02), ('CA', 'ASN', 'C', 'GLY', 6.92), ('CA', 'ASN', 'CA', 'GLY', 5.76), ('CA', 'ASN', 'N', 'GLY', 4.44)], [('N', 'ASN', 'O', 'GLY', 7.54), ('N', 'ASN', 'C', 'GLY', 7.45), ('N', 'ASN', 'CA', 'GLY', 6.39), ('N', 'ASN', 'N', 'GLY', 5.19)]]}
ALA_ASN = { 
	'distances':
		[[6.45, 6.54, 7.5, 6.03, 8.74, 7.65, 6.52, 7.27], [5.61, 4.98, 5.21, 5.06, 8.33, 7.71, 6.73, 7.77], [6.12, 5.81, 6.29, 5.72, 8.92, 8.13, 6.98, 7.89], [6.79, 6.44, 7.14, 5.9, 9.25, 8.28, 7.25, 8.21], [6.86, 6.15, 6.81, 5.26, 8.89, 7.96, 7.25, 8.43]],
	'comparisons':
		[[('CB', 'ALA', 'CB', 'ASN', 6.45), ('CB', 'ALA', 'CG', 'ASN', 6.54), ('CB', 'ALA', 'OD1', 'ASN', 7.5), ('CB', 'ALA', 'ND2', 'ASN', 6.03), ('CB', 'ALA', 'O', 'ASN', 8.74), ('CB', 'ALA', 'C', 'ASN', 7.65), ('CB', 'ALA', 'CA', 'ASN', 6.52), ('CB', 'ALA', 'N', 'ASN', 7.27)], [('O', 'ALA', 'CB', 'ASN', 5.61), ('O', 'ALA', 'CG', 'ASN', 4.98), ('O', 'ALA', 'OD1', 'ASN', 5.21), ('O', 'ALA', 'ND2', 'ASN', 5.06), ('O', 'ALA', 'O', 'ASN', 8.33), ('O', 'ALA', 'C', 'ASN', 7.71), ('O', 'ALA', 'CA', 'ASN', 6.73), ('O', 'ALA', 'N', 'ASN', 7.77)], [('C', 'ALA', 'CB', 'ASN', 6.12), ('C', 'ALA', 'CG', 'ASN', 5.81), ('C', 'ALA', 'OD1', 'ASN', 6.29), ('C', 'ALA', 'ND2', 'ASN', 5.72), ('C', 'ALA', 'O', 'ASN', 8.92), ('C', 'ALA', 'C', 'ASN', 8.13), ('C', 'ALA', 'CA', 'ASN', 6.98), ('C', 'ALA', 'N', 'ASN', 7.89)], [('CA', 'ALA', 'CB', 'ASN', 6.79), ('CA', 'ALA', 'CG', 'ASN', 6.44), ('CA', 'ALA', 'OD1', 'ASN', 7.14), ('CA', 'ALA', 'ND2', 'ASN', 5.9), ('CA', 'ALA', 'O', 'ASN', 9.25), ('CA', 'ALA', 'C', 'ASN', 8.28), ('CA', 'ALA', 'CA', 'ASN', 7.25), ('CA', 'ALA', 'N', 'ASN', 8.21)], [('N', 'ALA', 'CB', 'ASN', 6.86), ('N', 'ALA', 'CG', 'ASN', 6.15), ('N', 'ALA', 'OD1', 'ASN', 6.81), ('N', 'ALA', 'ND2', 'ASN', 5.26), ('N', 'ALA', 'O', 'ASN', 8.89), ('N', 'ALA', 'C', 'ASN', 7.96), ('N', 'ALA', 'CA', 'ASN', 7.25), ('N', 'ALA', 'N', 'ASN', 8.43)]]}
ALA_GLY = { 
	'distances':
		[[9.07, 9.63, 9.08, 7.75], [10.36, 10.48, 9.47, 8.31], [10.47, 10.75, 9.87, 8.61], [9.88, 10.34, 9.7, 8.46], [9.2, 9.62, 9.05, 7.98]],
	'comparisons':
		[[('CB', 'ALA', 'O', 'GLY', 9.07), ('CB', 'ALA', 'C', 'GLY', 9.63), ('CB', 'ALA', 'CA', 'GLY', 9.08), ('CB', 'ALA', 'N', 'GLY', 7.75)], [('O', 'ALA', 'O', 'GLY', 10.36), ('O', 'ALA', 'C', 'GLY', 10.48), ('O', 'ALA', 'CA', 'GLY', 9.47), ('O', 'ALA', 'N', 'GLY', 8.31)], [('C', 'ALA', 'O', 'GLY', 10.47), ('C', 'ALA', 'C', 'GLY', 10.75), ('C', 'ALA', 'CA', 'GLY', 9.87), ('C', 'ALA', 'N', 'GLY', 8.61)], [('CA', 'ALA', 'O', 'GLY', 9.88), ('CA', 'ALA', 'C', 'GLY', 10.34), ('CA', 'ALA', 'CA', 'GLY', 9.7), ('CA', 'ALA', 'N', 'GLY', 8.46)], [('N', 'ALA', 'O', 'GLY', 9.2), ('N', 'ALA', 'C', 'GLY', 9.62), ('N', 'ALA', 'CA', 'GLY', 9.05), ('N', 'ALA', 'N', 'GLY', 7.98)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASN_GLY, d, 'A_1ct9_6_3_5_4')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ALA_ASN, d, 'A_1ct9_6_3_5_4')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ALA_GLY, d, 'A_1ct9_6_3_5_4')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASN_GLY' :  match1,
		'ALA_ASN' :  match2,
		'ALA_GLY' :  match3}