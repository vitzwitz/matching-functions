'''
FUNC:A_1b02_2_1_1_45
PDB:1b02
EC:2.1.1.45
RESI:cys,asn,gln
LOCI:a-161,192,195;
'''
import motifFunctions as cmd
ASN_CYS = { 
	'distances':
		[[9.34, 10.44], [8.13, 9.06], [7.46, 8.35], [8.14, 8.91]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'CYS', 9.34), ('CB', 'ASN', 'SG', 'CYS', 10.44)], [('CG', 'ASN', 'CB', 'CYS', 8.13), ('CG', 'ASN', 'SG', 'CYS', 9.06)], [('OD1', 'ASN', 'CB', 'CYS', 7.46), ('OD1', 'ASN', 'SG', 'CYS', 8.35)], [('ND2', 'ASN', 'CB', 'CYS', 8.14), ('ND2', 'ASN', 'SG', 'CYS', 8.91)]]}
GLN_CYS = { 
	'distances':
		[[13.93, 14.68], [12.48, 13.31], [11.56, 12.22], [10.34, 11.02], [12.28, 12.75]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'CYS', 13.93), ('CB', 'GLN', 'SG', 'CYS', 14.68)], [('CG', 'GLN', 'CB', 'CYS', 12.48), ('CG', 'GLN', 'SG', 'CYS', 13.31)], [('CD', 'GLN', 'CB', 'CYS', 11.56), ('CD', 'GLN', 'SG', 'CYS', 12.22)], [('OE1', 'GLN', 'CB', 'CYS', 10.34), ('OE1', 'GLN', 'SG', 'CYS', 11.02)], [('NE2', 'GLN', 'CB', 'CYS', 12.28), ('NE2', 'GLN', 'SG', 'CYS', 12.75)]]}
GLN_ASN = { 
	'distances':
		[[8.25, 8.78, 9.99, 8.13], [6.91, 7.41, 8.63, 6.75], [6.9, 6.95, 8.11, 5.99], [6.15, 5.97, 7.1, 4.91], [8.07, 7.97, 9.07, 6.91]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'ASN', 8.25), ('CB', 'GLN', 'CG', 'ASN', 8.78), ('CB', 'GLN', 'OD1', 'ASN', 9.99), ('CB', 'GLN', 'ND2', 'ASN', 8.13)], [('CG', 'GLN', 'CB', 'ASN', 6.91), ('CG', 'GLN', 'CG', 'ASN', 7.41), ('CG', 'GLN', 'OD1', 'ASN', 8.63), ('CG', 'GLN', 'ND2', 'ASN', 6.75)], [('CD', 'GLN', 'CB', 'ASN', 6.9), ('CD', 'GLN', 'CG', 'ASN', 6.95), ('CD', 'GLN', 'OD1', 'ASN', 8.11), ('CD', 'GLN', 'ND2', 'ASN', 5.99)], [('OE1', 'GLN', 'CB', 'ASN', 6.15), ('OE1', 'GLN', 'CG', 'ASN', 5.97), ('OE1', 'GLN', 'OD1', 'ASN', 7.1), ('OE1', 'GLN', 'ND2', 'ASN', 4.91)], [('NE2', 'GLN', 'CB', 'ASN', 8.07), ('NE2', 'GLN', 'CG', 'ASN', 7.97), ('NE2', 'GLN', 'OD1', 'ASN', 9.07), ('NE2', 'GLN', 'ND2', 'ASN', 6.91)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASN_CYS, d, 'A_1b02_2_1_1_45')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLN_CYS, d, 'A_1b02_2_1_1_45')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLN_ASN, d, 'A_1b02_2_1_1_45')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASN_CYS' :  match1,
		'GLN_CYS' :  match2,
		'GLN_ASN' :  match3}