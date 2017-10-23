'''
FUNC:A_1cde_2_1_2_2
PDB:1cde
EC:2.1.2.2
RESI:asn,his,asp
LOCI:a-106,108,144;
'''
import motifFunctions as cmd
ASP_ASN = { 
	'distances':
		[[9.76, 9.15, 9.89, 7.89], [9.11, 8.26, 8.83, 7.02], [7.9, 7.03, 7.62, 5.8], [9.99, 8.99, 9.39, 7.79]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASN', 9.76), ('CB', 'ASP', 'CG', 'ASN', 9.15), ('CB', 'ASP', 'OD1', 'ASN', 9.89), ('CB', 'ASP', 'ND2', 'ASN', 7.89)], [('CG', 'ASP', 'CB', 'ASN', 9.11), ('CG', 'ASP', 'CG', 'ASN', 8.26), ('CG', 'ASP', 'OD1', 'ASN', 8.83), ('CG', 'ASP', 'ND2', 'ASN', 7.02)], [('OD1', 'ASP', 'CB', 'ASN', 7.9), ('OD1', 'ASP', 'CG', 'ASN', 7.03), ('OD1', 'ASP', 'OD1', 'ASN', 7.62), ('OD1', 'ASP', 'ND2', 'ASN', 5.8)], [('OD2', 'ASP', 'CB', 'ASN', 9.99), ('OD2', 'ASP', 'CG', 'ASN', 8.99), ('OD2', 'ASP', 'OD1', 'ASN', 9.39), ('OD2', 'ASP', 'ND2', 'ASN', 7.79)]]}
HIS_ASP = { 
	'distances':
		[[7.06, 6.59, 6.1, 7.17], [6.41, 5.91, 5.79, 6.22], [6.25, 6.11, 6.36, 6.35], [6.67, 5.81, 5.76, 5.75], [6.41, 6.16, 6.64, 6.03], [6.65, 5.97, 6.3, 5.64]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 7.06), ('CB', 'HIS', 'CG', 'ASP', 6.59), ('CB', 'HIS', 'OD1', 'ASP', 6.1), ('CB', 'HIS', 'OD2', 'ASP', 7.17)], [('CG', 'HIS', 'CB', 'ASP', 6.41), ('CG', 'HIS', 'CG', 'ASP', 5.91), ('CG', 'HIS', 'OD1', 'ASP', 5.79), ('CG', 'HIS', 'OD2', 'ASP', 6.22)], [('ND1', 'HIS', 'CB', 'ASP', 6.25), ('ND1', 'HIS', 'CG', 'ASP', 6.11), ('ND1', 'HIS', 'OD1', 'ASP', 6.36), ('ND1', 'HIS', 'OD2', 'ASP', 6.35)], [('CD2', 'HIS', 'CB', 'ASP', 6.67), ('CD2', 'HIS', 'CG', 'ASP', 5.81), ('CD2', 'HIS', 'OD1', 'ASP', 5.76), ('CD2', 'HIS', 'OD2', 'ASP', 5.75)], [('CE1', 'HIS', 'CB', 'ASP', 6.41), ('CE1', 'HIS', 'CG', 'ASP', 6.16), ('CE1', 'HIS', 'OD1', 'ASP', 6.64), ('CE1', 'HIS', 'OD2', 'ASP', 6.03)], [('NE2', 'HIS', 'CB', 'ASP', 6.65), ('NE2', 'HIS', 'CG', 'ASP', 5.97), ('NE2', 'HIS', 'OD1', 'ASP', 6.3), ('NE2', 'HIS', 'OD2', 'ASP', 5.64)]]}
HIS_ASN = { 
	'distances':
		[[8.07, 7.25, 7.8, 6.12], [9.21, 8.25, 8.7, 7.02], [10.31, 9.44, 9.97, 8.17], [9.58, 8.41, 8.64, 7.23], [11.17, 10.18, 10.58, 8.91], [10.77, 9.61, 9.86, 8.4]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASN', 8.07), ('CB', 'HIS', 'CG', 'ASN', 7.25), ('CB', 'HIS', 'OD1', 'ASN', 7.8), ('CB', 'HIS', 'ND2', 'ASN', 6.12)], [('CG', 'HIS', 'CB', 'ASN', 9.21), ('CG', 'HIS', 'CG', 'ASN', 8.25), ('CG', 'HIS', 'OD1', 'ASN', 8.7), ('CG', 'HIS', 'ND2', 'ASN', 7.02)], [('ND1', 'HIS', 'CB', 'ASN', 10.31), ('ND1', 'HIS', 'CG', 'ASN', 9.44), ('ND1', 'HIS', 'OD1', 'ASN', 9.97), ('ND1', 'HIS', 'ND2', 'ASN', 8.17)], [('CD2', 'HIS', 'CB', 'ASN', 9.58), ('CD2', 'HIS', 'CG', 'ASN', 8.41), ('CD2', 'HIS', 'OD1', 'ASN', 8.64), ('CD2', 'HIS', 'ND2', 'ASN', 7.23)], [('CE1', 'HIS', 'CB', 'ASN', 11.17), ('CE1', 'HIS', 'CG', 'ASN', 10.18), ('CE1', 'HIS', 'OD1', 'ASN', 10.58), ('CE1', 'HIS', 'ND2', 'ASN', 8.91)], [('NE2', 'HIS', 'CB', 'ASN', 10.77), ('NE2', 'HIS', 'CG', 'ASN', 9.61), ('NE2', 'HIS', 'OD1', 'ASN', 9.86), ('NE2', 'HIS', 'ND2', 'ASN', 8.4)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_ASN, d, 'A_1cde_2_1_2_2')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_ASP, d, 'A_1cde_2_1_2_2')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_ASN, d, 'A_1cde_2_1_2_2')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_ASN' :  match1,
		'HIS_ASP' :  match2,
		'HIS_ASN' :  match3}