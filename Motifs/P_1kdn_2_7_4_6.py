'''
FUNC:P_1kdn_2_7_4_6
PDB:1kdn
EC:2.7.4.6
RESI:lys,asn
LOCI:a-16,119;
'''
import motifFunctions as cmd
LYS_ASN = { 
	'distances':
		[[9.41, 8.85, 7.7, 9.87], [9.01, 8.21, 7.05, 9.05], [7.73, 6.81, 5.61, 7.63], [7.62, 6.44, 5.36, 6.95], [7.01, 5.64, 4.65, 5.94]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'ASN', 9.41), ('CB', 'LYS', 'CG', 'ASN', 8.85), ('CB', 'LYS', 'OD1', 'ASN', 7.7), ('CB', 'LYS', 'ND2', 'ASN', 9.87)], [('CG', 'LYS', 'CB', 'ASN', 9.01), ('CG', 'LYS', 'CG', 'ASN', 8.21), ('CG', 'LYS', 'OD1', 'ASN', 7.05), ('CG', 'LYS', 'ND2', 'ASN', 9.05)], [('CD', 'LYS', 'CB', 'ASN', 7.73), ('CD', 'LYS', 'CG', 'ASN', 6.81), ('CD', 'LYS', 'OD1', 'ASN', 5.61), ('CD', 'LYS', 'ND2', 'ASN', 7.63)], [('CE', 'LYS', 'CB', 'ASN', 7.62), ('CE', 'LYS', 'CG', 'ASN', 6.44), ('CE', 'LYS', 'OD1', 'ASN', 5.36), ('CE', 'LYS', 'ND2', 'ASN', 6.95)], [('NZ', 'LYS', 'CB', 'ASN', 7.01), ('NZ', 'LYS', 'CG', 'ASN', 5.64), ('NZ', 'LYS', 'OD1', 'ASN', 4.65), ('NZ', 'LYS', 'ND2', 'ASN', 5.94)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LYS_ASN, d, 'P_1kdn_2_7_4_6')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'LYS_ASN' :  match1}