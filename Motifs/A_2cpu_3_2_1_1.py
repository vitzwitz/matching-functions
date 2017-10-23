'''
FUNC:A_2cpu_3_2_1_1
PDB:2cpu
EC:3.2.1.1
RESI:asp,glu,asn
LOCI:a-197,233,300;
'''
import motifFunctions as cmd
ASP_ASN = { 
	'distances':
		[[11.9, 12.09, 12.99, 11.44], [10.84, 10.86, 11.74, 10.14], [9.64, 9.74, 10.64, 9.07], [11.33, 11.16, 11.97, 10.33]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASN', 11.9), ('CB', 'ASP', 'CG', 'ASN', 12.09), ('CB', 'ASP', 'OD1', 'ASN', 12.99), ('CB', 'ASP', 'ND2', 'ASN', 11.44)], [('CG', 'ASP', 'CB', 'ASN', 10.84), ('CG', 'ASP', 'CG', 'ASN', 10.86), ('CG', 'ASP', 'OD1', 'ASN', 11.74), ('CG', 'ASP', 'ND2', 'ASN', 10.14)], [('OD1', 'ASP', 'CB', 'ASN', 9.64), ('OD1', 'ASP', 'CG', 'ASN', 9.74), ('OD1', 'ASP', 'OD1', 'ASN', 10.64), ('OD1', 'ASP', 'ND2', 'ASN', 9.07)], [('OD2', 'ASP', 'CB', 'ASN', 11.33), ('OD2', 'ASP', 'CG', 'ASN', 11.16), ('OD2', 'ASP', 'OD1', 'ASN', 11.97), ('OD2', 'ASP', 'ND2', 'ASN', 10.33)]]}
GLU_ASN = { 
	'distances':
		[[10.87, 11.62, 12.83, 11.07], [9.7, 10.46, 11.69, 9.91], [8.77, 9.33, 10.55, 8.65], [9.37, 9.74, 10.92, 8.94], [7.61, 8.19, 9.42, 7.55]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ASN', 10.87), ('CB', 'GLU', 'CG', 'ASN', 11.62), ('CB', 'GLU', 'OD1', 'ASN', 12.83), ('CB', 'GLU', 'ND2', 'ASN', 11.07)], [('CG', 'GLU', 'CB', 'ASN', 9.7), ('CG', 'GLU', 'CG', 'ASN', 10.46), ('CG', 'GLU', 'OD1', 'ASN', 11.69), ('CG', 'GLU', 'ND2', 'ASN', 9.91)], [('CD', 'GLU', 'CB', 'ASN', 8.77), ('CD', 'GLU', 'CG', 'ASN', 9.33), ('CD', 'GLU', 'OD1', 'ASN', 10.55), ('CD', 'GLU', 'ND2', 'ASN', 8.65)], [('OE1', 'GLU', 'CB', 'ASN', 9.37), ('OE1', 'GLU', 'CG', 'ASN', 9.74), ('OE1', 'GLU', 'OD1', 'ASN', 10.92), ('OE1', 'GLU', 'ND2', 'ASN', 8.94)], [('OE2', 'GLU', 'CB', 'ASN', 7.61), ('OE2', 'GLU', 'CG', 'ASN', 8.19), ('OE2', 'GLU', 'OD1', 'ASN', 9.42), ('OE2', 'GLU', 'ND2', 'ASN', 7.55)]]}
ASP_GLU = { 
	'distances':
		[[7.74, 8.47, 7.85, 6.9, 8.57], [7.96, 8.34, 7.4, 6.41, 7.91], [7.49, 7.65, 6.61, 5.8, 6.95], [8.89, 9.2, 8.14, 7.07, 8.6]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLU', 7.74), ('CB', 'ASP', 'CG', 'GLU', 8.47), ('CB', 'ASP', 'CD', 'GLU', 7.85), ('CB', 'ASP', 'OE1', 'GLU', 6.9), ('CB', 'ASP', 'OE2', 'GLU', 8.57)], [('CG', 'ASP', 'CB', 'GLU', 7.96), ('CG', 'ASP', 'CG', 'GLU', 8.34), ('CG', 'ASP', 'CD', 'GLU', 7.4), ('CG', 'ASP', 'OE1', 'GLU', 6.41), ('CG', 'ASP', 'OE2', 'GLU', 7.91)], [('OD1', 'ASP', 'CB', 'GLU', 7.49), ('OD1', 'ASP', 'CG', 'GLU', 7.65), ('OD1', 'ASP', 'CD', 'GLU', 6.61), ('OD1', 'ASP', 'OE1', 'GLU', 5.8), ('OD1', 'ASP', 'OE2', 'GLU', 6.95)], [('OD2', 'ASP', 'CB', 'GLU', 8.89), ('OD2', 'ASP', 'CG', 'GLU', 9.2), ('OD2', 'ASP', 'CD', 'GLU', 8.14), ('OD2', 'ASP', 'OE1', 'GLU', 7.07), ('OD2', 'ASP', 'OE2', 'GLU', 8.6)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_ASN, d, 'A_2cpu_3_2_1_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_ASN, d, 'A_2cpu_3_2_1_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_GLU, d, 'A_2cpu_3_2_1_1')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_ASN' :  match1,
		'GLU_ASN' :  match2,
		'ASP_GLU' :  match3}