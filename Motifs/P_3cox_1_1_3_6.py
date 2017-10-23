'''
FUNC:P_3cox_1_1_3_6
PDB:3cox
EC:1.1.3.6
RESI:glu,his,asn
LOCI:a-361,447,485;
'''
import motifFunctions as cmd
HIS_ASN = { 
	'distances':
		[[9.39, 9.13, 8.41, 9.95], [8.22, 7.78, 7.0, 8.56], [7.64, 7.11, 6.51, 7.69], [7.84, 7.27, 6.28, 8.14], [6.87, 6.08, 5.4, 6.6], [6.99, 6.17, 5.17, 6.91]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASN', 9.39), ('CB', 'HIS', 'CG', 'ASN', 9.13), ('CB', 'HIS', 'OD1', 'ASN', 8.41), ('CB', 'HIS', 'ND2', 'ASN', 9.95)], [('CG', 'HIS', 'CB', 'ASN', 8.22), ('CG', 'HIS', 'CG', 'ASN', 7.78), ('CG', 'HIS', 'OD1', 'ASN', 7.0), ('CG', 'HIS', 'ND2', 'ASN', 8.56)], [('ND1', 'HIS', 'CB', 'ASN', 7.64), ('ND1', 'HIS', 'CG', 'ASN', 7.11), ('ND1', 'HIS', 'OD1', 'ASN', 6.51), ('ND1', 'HIS', 'ND2', 'ASN', 7.69)], [('CD2', 'HIS', 'CB', 'ASN', 7.84), ('CD2', 'HIS', 'CG', 'ASN', 7.27), ('CD2', 'HIS', 'OD1', 'ASN', 6.28), ('CD2', 'HIS', 'ND2', 'ASN', 8.14)], [('CE1', 'HIS', 'CB', 'ASN', 6.87), ('CE1', 'HIS', 'CG', 'ASN', 6.08), ('CE1', 'HIS', 'OD1', 'ASN', 5.4), ('CE1', 'HIS', 'ND2', 'ASN', 6.6)], [('NE2', 'HIS', 'CB', 'ASN', 6.99), ('NE2', 'HIS', 'CG', 'ASN', 6.17), ('NE2', 'HIS', 'OD1', 'ASN', 5.17), ('NE2', 'HIS', 'ND2', 'ASN', 6.91)]]}
GLU_ASN = { 
	'distances':
		[[9.56, 8.35, 8.71, 7.14], [9.75, 8.39, 8.48, 7.34], [8.9, 7.44, 7.34, 6.59], [7.75, 6.28, 6.14, 5.51], [9.59, 8.11, 7.87, 7.39]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ASN', 9.56), ('CB', 'GLU', 'CG', 'ASN', 8.35), ('CB', 'GLU', 'OD1', 'ASN', 8.71), ('CB', 'GLU', 'ND2', 'ASN', 7.14)], [('CG', 'GLU', 'CB', 'ASN', 9.75), ('CG', 'GLU', 'CG', 'ASN', 8.39), ('CG', 'GLU', 'OD1', 'ASN', 8.48), ('CG', 'GLU', 'ND2', 'ASN', 7.34)], [('CD', 'GLU', 'CB', 'ASN', 8.9), ('CD', 'GLU', 'CG', 'ASN', 7.44), ('CD', 'GLU', 'OD1', 'ASN', 7.34), ('CD', 'GLU', 'ND2', 'ASN', 6.59)], [('OE1', 'GLU', 'CB', 'ASN', 7.75), ('OE1', 'GLU', 'CG', 'ASN', 6.28), ('OE1', 'GLU', 'OD1', 'ASN', 6.14), ('OE1', 'GLU', 'ND2', 'ASN', 5.51)], [('OE2', 'GLU', 'CB', 'ASN', 9.59), ('OE2', 'GLU', 'CG', 'ASN', 8.11), ('OE2', 'GLU', 'OD1', 'ASN', 7.87), ('OE2', 'GLU', 'ND2', 'ASN', 7.39)]]}
GLU_HIS = { 
	'distances':
		[[13.3, 11.9, 10.82, 11.54, 9.72, 10.19], [12.55, 11.16, 10.14, 10.76, 9.04, 9.45], [11.69, 10.24, 9.37, 9.68, 8.16, 8.36], [10.58, 9.12, 8.23, 8.57, 7.0, 7.23], [12.31, 10.85, 10.12, 10.13, 8.88, 8.86]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'HIS', 13.3), ('CB', 'GLU', 'CG', 'HIS', 11.9), ('CB', 'GLU', 'ND1', 'HIS', 10.82), ('CB', 'GLU', 'CD2', 'HIS', 11.54), ('CB', 'GLU', 'CE1', 'HIS', 9.72), ('CB', 'GLU', 'NE2', 'HIS', 10.19)], [('CG', 'GLU', 'CB', 'HIS', 12.55), ('CG', 'GLU', 'CG', 'HIS', 11.16), ('CG', 'GLU', 'ND1', 'HIS', 10.14), ('CG', 'GLU', 'CD2', 'HIS', 10.76), ('CG', 'GLU', 'CE1', 'HIS', 9.04), ('CG', 'GLU', 'NE2', 'HIS', 9.45)], [('CD', 'GLU', 'CB', 'HIS', 11.69), ('CD', 'GLU', 'CG', 'HIS', 10.24), ('CD', 'GLU', 'ND1', 'HIS', 9.37), ('CD', 'GLU', 'CD2', 'HIS', 9.68), ('CD', 'GLU', 'CE1', 'HIS', 8.16), ('CD', 'GLU', 'NE2', 'HIS', 8.36)], [('OE1', 'GLU', 'CB', 'HIS', 10.58), ('OE1', 'GLU', 'CG', 'HIS', 9.12), ('OE1', 'GLU', 'ND1', 'HIS', 8.23), ('OE1', 'GLU', 'CD2', 'HIS', 8.57), ('OE1', 'GLU', 'CE1', 'HIS', 7.0), ('OE1', 'GLU', 'NE2', 'HIS', 7.23)], [('OE2', 'GLU', 'CB', 'HIS', 12.31), ('OE2', 'GLU', 'CG', 'HIS', 10.85), ('OE2', 'GLU', 'ND1', 'HIS', 10.12), ('OE2', 'GLU', 'CD2', 'HIS', 10.13), ('OE2', 'GLU', 'CE1', 'HIS', 8.88), ('OE2', 'GLU', 'NE2', 'HIS', 8.86)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_ASN, d, 'P_3cox_1_1_3_6')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_ASN, d, 'P_3cox_1_1_3_6')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_HIS, d, 'P_3cox_1_1_3_6')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_ASN' :  match1,
		'GLU_ASN' :  match2,
		'GLU_HIS' :  match3}