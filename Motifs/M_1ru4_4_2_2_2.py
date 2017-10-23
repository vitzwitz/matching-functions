'''
FUNC:M_1ru4_4_2_2_2
PDB:1ru4
EC:4.2.2.2
RESI:ca,asn,lys
LOCI:a-1,268,273;
'''
import motifFunctions as cmd
LYS_ASN = { 
	'distances':
		[[9.65, 10.3, 11.26, 10.02], [9.59, 9.97, 10.86, 9.58], [8.5, 8.73, 9.65, 8.2], [7.2, 7.49, 8.35, 7.16], [6.23, 6.27, 7.2, 5.76]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'ASN', 9.65), ('CB', 'LYS', 'CG', 'ASN', 10.3), ('CB', 'LYS', 'OD1', 'ASN', 11.26), ('CB', 'LYS', 'ND2', 'ASN', 10.02)], [('CG', 'LYS', 'CB', 'ASN', 9.59), ('CG', 'LYS', 'CG', 'ASN', 9.97), ('CG', 'LYS', 'OD1', 'ASN', 10.86), ('CG', 'LYS', 'ND2', 'ASN', 9.58)], [('CD', 'LYS', 'CB', 'ASN', 8.5), ('CD', 'LYS', 'CG', 'ASN', 8.73), ('CD', 'LYS', 'OD1', 'ASN', 9.65), ('CD', 'LYS', 'ND2', 'ASN', 8.2)], [('CE', 'LYS', 'CB', 'ASN', 7.2), ('CE', 'LYS', 'CG', 'ASN', 7.49), ('CE', 'LYS', 'OD1', 'ASN', 8.35), ('CE', 'LYS', 'ND2', 'ASN', 7.16)], [('NZ', 'LYS', 'CB', 'ASN', 6.23), ('NZ', 'LYS', 'CG', 'ASN', 6.27), ('NZ', 'LYS', 'OD1', 'ASN', 7.2), ('NZ', 'LYS', 'ND2', 'ASN', 5.76)]]}
ASN_CA = { 
	'distances':
		[[8.28], [8.42], [9.6], [7.45]],
	'comparisons':
		[[('CB', 'ASN', 'CA', 'CA', 8.28)], [('CG', 'ASN', 'CA', 'CA', 8.42)], [('OD1', 'ASN', 'CA', 'CA', 9.6)], [('ND2', 'ASN', 'CA', 'CA', 7.45)]]}
LYS_CA = { 
	'distances':
		[[7.9], [7.84], [6.66], [6.99], [6.27]],
	'comparisons':
		[[('CB', 'LYS', 'CA', 'CA', 7.9)], [('CG', 'LYS', 'CA', 'CA', 7.84)], [('CD', 'LYS', 'CA', 'CA', 6.66)], [('CE', 'LYS', 'CA', 'CA', 6.99)], [('NZ', 'LYS', 'CA', 'CA', 6.27)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LYS_ASN, d, 'M_1ru4_4_2_2_2')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASN_CA, d, 'M_1ru4_4_2_2_2')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(LYS_CA, d, 'M_1ru4_4_2_2_2')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'LYS_ASN' :  match1,
		'ASN_CA' :  match2,
		'LYS_CA' :  match3}