'''
FUNC:A_1qam_2_1_1_48
PDB:1qam
EC:2.1.1.48
RESI:gly,glu,asn
LOCI:a-38,59,101;
'''
import motifFunctions as cmd
GLY_GLU = { 
	'distances':
		[[8.13, 8.64, 8.14, 6.96, 9.13], [7.04, 7.48, 6.93, 5.76, 7.91], [6.95, 7.4, 6.63, 5.53, 7.41], [7.51, 8.26, 7.68, 6.71, 8.46]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'GLU', 8.13), ('O', 'GLY', 'CG', 'GLU', 8.64), ('O', 'GLY', 'CD', 'GLU', 8.14), ('O', 'GLY', 'OE1', 'GLU', 6.96), ('O', 'GLY', 'OE2', 'GLU', 9.13)], [('C', 'GLY', 'CB', 'GLU', 7.04), ('C', 'GLY', 'CG', 'GLU', 7.48), ('C', 'GLY', 'CD', 'GLU', 6.93), ('C', 'GLY', 'OE1', 'GLU', 5.76), ('C', 'GLY', 'OE2', 'GLU', 7.91)], [('CA', 'GLY', 'CB', 'GLU', 6.95), ('CA', 'GLY', 'CG', 'GLU', 7.4), ('CA', 'GLY', 'CD', 'GLU', 6.63), ('CA', 'GLY', 'OE1', 'GLU', 5.53), ('CA', 'GLY', 'OE2', 'GLU', 7.41)], [('N', 'GLY', 'CB', 'GLU', 7.51), ('N', 'GLY', 'CG', 'GLU', 8.26), ('N', 'GLY', 'CD', 'GLU', 7.68), ('N', 'GLY', 'OE1', 'GLU', 6.71), ('N', 'GLY', 'OE2', 'GLU', 8.46)]]}
GLU_ASN = { 
	'distances':
		[[13.48, 14.2, 15.33, 13.7], [13.5, 14.05, 15.17, 13.41], [12.5, 12.96, 14.03, 12.31], [11.27, 11.78, 12.86, 11.17], [13.05, 13.39, 14.4, 12.7]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ASN', 13.48), ('CB', 'GLU', 'CG', 'ASN', 14.2), ('CB', 'GLU', 'OD1', 'ASN', 15.33), ('CB', 'GLU', 'ND2', 'ASN', 13.7)], [('CG', 'GLU', 'CB', 'ASN', 13.5), ('CG', 'GLU', 'CG', 'ASN', 14.05), ('CG', 'GLU', 'OD1', 'ASN', 15.17), ('CG', 'GLU', 'ND2', 'ASN', 13.41)], [('CD', 'GLU', 'CB', 'ASN', 12.5), ('CD', 'GLU', 'CG', 'ASN', 12.96), ('CD', 'GLU', 'OD1', 'ASN', 14.03), ('CD', 'GLU', 'ND2', 'ASN', 12.31)], [('OE1', 'GLU', 'CB', 'ASN', 11.27), ('OE1', 'GLU', 'CG', 'ASN', 11.78), ('OE1', 'GLU', 'OD1', 'ASN', 12.86), ('OE1', 'GLU', 'ND2', 'ASN', 11.17)], [('OE2', 'GLU', 'CB', 'ASN', 13.05), ('OE2', 'GLU', 'CG', 'ASN', 13.39), ('OE2', 'GLU', 'OD1', 'ASN', 14.4), ('OE2', 'GLU', 'ND2', 'ASN', 12.7)]]}
GLY_ASN = { 
	'distances':
		[[7.9, 9.02, 10.13, 8.94], [8.63, 9.59, 10.71, 9.37], [9.02, 9.92, 10.94, 9.77], [9.47, 10.53, 11.48, 10.59]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'ASN', 7.9), ('O', 'GLY', 'CG', 'ASN', 9.02), ('O', 'GLY', 'OD1', 'ASN', 10.13), ('O', 'GLY', 'ND2', 'ASN', 8.94)], [('C', 'GLY', 'CB', 'ASN', 8.63), ('C', 'GLY', 'CG', 'ASN', 9.59), ('C', 'GLY', 'OD1', 'ASN', 10.71), ('C', 'GLY', 'ND2', 'ASN', 9.37)], [('CA', 'GLY', 'CB', 'ASN', 9.02), ('CA', 'GLY', 'CG', 'ASN', 9.92), ('CA', 'GLY', 'OD1', 'ASN', 10.94), ('CA', 'GLY', 'ND2', 'ASN', 9.77)], [('N', 'GLY', 'CB', 'ASN', 9.47), ('N', 'GLY', 'CG', 'ASN', 10.53), ('N', 'GLY', 'OD1', 'ASN', 11.48), ('N', 'GLY', 'ND2', 'ASN', 10.59)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLY_GLU, d, 'A_1qam_2_1_1_48')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_ASN, d, 'A_1qam_2_1_1_48')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLY_ASN, d, 'A_1qam_2_1_1_48')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLY_GLU' :  match1,
		'GLU_ASN' :  match2,
		'GLY_ASN' :  match3}