'''
FUNC:A_1ecf_2_4_2_14
PDB:1ecf
EC:2.4.2.14
RESI:cys,asn,gly
LOCI:a-1,101,102;
'''
import motifFunctions as cmd
CYS_GLY = { 
	'distances':
		[[8.75, 9.35, 8.79, 7.44], [8.09, 8.92, 8.74, 7.54], [10.4, 10.6, 9.57, 8.37], [10.54, 10.89, 10.01, 8.7], [9.87, 10.39, 9.73, 8.45], [9.51, 10.0, 9.35, 8.24]],
	'comparisons':
		[[('CB', 'CYS', 'O', 'GLY', 8.75), ('CB', 'CYS', 'C', 'GLY', 9.35), ('CB', 'CYS', 'CA', 'GLY', 8.79), ('CB', 'CYS', 'N', 'GLY', 7.44)], [('SG', 'CYS', 'O', 'GLY', 8.09), ('SG', 'CYS', 'C', 'GLY', 8.92), ('SG', 'CYS', 'CA', 'GLY', 8.74), ('SG', 'CYS', 'N', 'GLY', 7.54)], [('O', 'CYS', 'O', 'GLY', 10.4), ('O', 'CYS', 'C', 'GLY', 10.6), ('O', 'CYS', 'CA', 'GLY', 9.57), ('O', 'CYS', 'N', 'GLY', 8.37)], [('C', 'CYS', 'O', 'GLY', 10.54), ('C', 'CYS', 'C', 'GLY', 10.89), ('C', 'CYS', 'CA', 'GLY', 10.01), ('C', 'CYS', 'N', 'GLY', 8.7)], [('CA', 'CYS', 'O', 'GLY', 9.87), ('CA', 'CYS', 'C', 'GLY', 10.39), ('CA', 'CYS', 'CA', 'GLY', 9.73), ('CA', 'CYS', 'N', 'GLY', 8.45)], [('N', 'CYS', 'O', 'GLY', 9.51), ('N', 'CYS', 'C', 'GLY', 10.0), ('N', 'CYS', 'CA', 'GLY', 9.35), ('N', 'CYS', 'N', 'GLY', 8.24)]]}
ASN_GLY = { 
	'distances':
		[[8.17, 8.03, 6.78, 5.57], [8.17, 7.99, 6.7, 5.7], [9.18, 8.88, 7.5, 6.7], [7.38, 7.36, 6.25, 5.3], [6.75, 6.11, 4.73, 4.25], [6.02, 5.66, 4.41, 3.33], [6.93, 6.89, 5.82, 4.46], [7.55, 7.48, 6.54, 5.33]],
	'comparisons':
		[[('CB', 'ASN', 'O', 'GLY', 8.17), ('CB', 'ASN', 'C', 'GLY', 8.03), ('CB', 'ASN', 'CA', 'GLY', 6.78), ('CB', 'ASN', 'N', 'GLY', 5.57)], [('CG', 'ASN', 'O', 'GLY', 8.17), ('CG', 'ASN', 'C', 'GLY', 7.99), ('CG', 'ASN', 'CA', 'GLY', 6.7), ('CG', 'ASN', 'N', 'GLY', 5.7)], [('OD1', 'ASN', 'O', 'GLY', 9.18), ('OD1', 'ASN', 'C', 'GLY', 8.88), ('OD1', 'ASN', 'CA', 'GLY', 7.5), ('OD1', 'ASN', 'N', 'GLY', 6.7)], [('ND2', 'ASN', 'O', 'GLY', 7.38), ('ND2', 'ASN', 'C', 'GLY', 7.36), ('ND2', 'ASN', 'CA', 'GLY', 6.25), ('ND2', 'ASN', 'N', 'GLY', 5.3)], [('O', 'ASN', 'O', 'GLY', 6.75), ('O', 'ASN', 'C', 'GLY', 6.11), ('O', 'ASN', 'CA', 'GLY', 4.73), ('O', 'ASN', 'N', 'GLY', 4.25)], [('C', 'ASN', 'O', 'GLY', 6.02), ('C', 'ASN', 'C', 'GLY', 5.66), ('C', 'ASN', 'CA', 'GLY', 4.41), ('C', 'ASN', 'N', 'GLY', 3.33)], [('CA', 'ASN', 'O', 'GLY', 6.93), ('CA', 'ASN', 'C', 'GLY', 6.89), ('CA', 'ASN', 'CA', 'GLY', 5.82), ('CA', 'ASN', 'N', 'GLY', 4.46)], [('N', 'ASN', 'O', 'GLY', 7.55), ('N', 'ASN', 'C', 'GLY', 7.48), ('N', 'ASN', 'CA', 'GLY', 6.54), ('N', 'ASN', 'N', 'GLY', 5.33)]]}
CYS_ASN = { 
	'distances':
		[[6.19, 6.36, 7.31, 5.94, 8.42, 7.34, 6.16, 7.0], [7.44, 7.49, 8.54, 6.7, 9.07, 7.86, 7.0, 7.84], [5.74, 5.29, 5.49, 5.48, 8.52, 7.84, 6.78, 7.81], [6.25, 6.12, 6.55, 6.16, 9.06, 8.25, 7.02, 7.91], [6.78, 6.59, 7.26, 6.19, 9.28, 8.29, 7.15, 8.12], [7.02, 6.37, 6.94, 5.67, 9.23, 8.26, 7.43, 8.65]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'ASN', 6.19), ('CB', 'CYS', 'CG', 'ASN', 6.36), ('CB', 'CYS', 'OD1', 'ASN', 7.31), ('CB', 'CYS', 'ND2', 'ASN', 5.94), ('CB', 'CYS', 'O', 'ASN', 8.42), ('CB', 'CYS', 'C', 'ASN', 7.34), ('CB', 'CYS', 'CA', 'ASN', 6.16), ('CB', 'CYS', 'N', 'ASN', 7.0)], [('SG', 'CYS', 'CB', 'ASN', 7.44), ('SG', 'CYS', 'CG', 'ASN', 7.49), ('SG', 'CYS', 'OD1', 'ASN', 8.54), ('SG', 'CYS', 'ND2', 'ASN', 6.7), ('SG', 'CYS', 'O', 'ASN', 9.07), ('SG', 'CYS', 'C', 'ASN', 7.86), ('SG', 'CYS', 'CA', 'ASN', 7.0), ('SG', 'CYS', 'N', 'ASN', 7.84)], [('O', 'CYS', 'CB', 'ASN', 5.74), ('O', 'CYS', 'CG', 'ASN', 5.29), ('O', 'CYS', 'OD1', 'ASN', 5.49), ('O', 'CYS', 'ND2', 'ASN', 5.48), ('O', 'CYS', 'O', 'ASN', 8.52), ('O', 'CYS', 'C', 'ASN', 7.84), ('O', 'CYS', 'CA', 'ASN', 6.78), ('O', 'CYS', 'N', 'ASN', 7.81)], [('C', 'CYS', 'CB', 'ASN', 6.25), ('C', 'CYS', 'CG', 'ASN', 6.12), ('C', 'CYS', 'OD1', 'ASN', 6.55), ('C', 'CYS', 'ND2', 'ASN', 6.16), ('C', 'CYS', 'O', 'ASN', 9.06), ('C', 'CYS', 'C', 'ASN', 8.25), ('C', 'CYS', 'CA', 'ASN', 7.02), ('C', 'CYS', 'N', 'ASN', 7.91)], [('CA', 'CYS', 'CB', 'ASN', 6.78), ('CA', 'CYS', 'CG', 'ASN', 6.59), ('CA', 'CYS', 'OD1', 'ASN', 7.26), ('CA', 'CYS', 'ND2', 'ASN', 6.19), ('CA', 'CYS', 'O', 'ASN', 9.28), ('CA', 'CYS', 'C', 'ASN', 8.29), ('CA', 'CYS', 'CA', 'ASN', 7.15), ('CA', 'CYS', 'N', 'ASN', 8.12)], [('N', 'CYS', 'CB', 'ASN', 7.02), ('N', 'CYS', 'CG', 'ASN', 6.37), ('N', 'CYS', 'OD1', 'ASN', 6.94), ('N', 'CYS', 'ND2', 'ASN', 5.67), ('N', 'CYS', 'O', 'ASN', 9.23), ('N', 'CYS', 'C', 'ASN', 8.26), ('N', 'CYS', 'CA', 'ASN', 7.43), ('N', 'CYS', 'N', 'ASN', 8.65)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(CYS_GLY, d, 'A_1ecf_2_4_2_14')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASN_GLY, d, 'A_1ecf_2_4_2_14')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(CYS_ASN, d, 'A_1ecf_2_4_2_14')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'CYS_GLY' :  match1,
		'ASN_GLY' :  match2,
		'CYS_ASN' :  match3}