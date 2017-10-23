'''
FUNC:A_2adm_2_1_1_72
PDB:2adm
EC:2.1.1.72
RESI:asn,pro,tyr
LOCI:a-105,106,108;
'''
import motifFunctions as cmd
ASN_TYR = { 
	'distances':
		[[10.79, 9.53, 8.65, 9.49, 7.63, 8.62, 7.62, 7.03], [9.62, 8.3, 7.58, 8.11, 6.54, 7.18, 6.31, 5.76], [9.88, 8.57, 8.09, 8.15, 7.1, 7.18, 6.59, 6.0], [8.54, 7.18, 6.34, 7.12, 5.25, 6.24, 5.2, 4.82]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'TYR', 10.79), ('CB', 'ASN', 'CG', 'TYR', 9.53), ('CB', 'ASN', 'CD1', 'TYR', 8.65), ('CB', 'ASN', 'CD2', 'TYR', 9.49), ('CB', 'ASN', 'CE1', 'TYR', 7.63), ('CB', 'ASN', 'CE2', 'TYR', 8.62), ('CB', 'ASN', 'CZ', 'TYR', 7.62), ('CB', 'ASN', 'OH', 'TYR', 7.03)], [('CG', 'ASN', 'CB', 'TYR', 9.62), ('CG', 'ASN', 'CG', 'TYR', 8.3), ('CG', 'ASN', 'CD1', 'TYR', 7.58), ('CG', 'ASN', 'CD2', 'TYR', 8.11), ('CG', 'ASN', 'CE1', 'TYR', 6.54), ('CG', 'ASN', 'CE2', 'TYR', 7.18), ('CG', 'ASN', 'CZ', 'TYR', 6.31), ('CG', 'ASN', 'OH', 'TYR', 5.76)], [('OD1', 'ASN', 'CB', 'TYR', 9.88), ('OD1', 'ASN', 'CG', 'TYR', 8.57), ('OD1', 'ASN', 'CD1', 'TYR', 8.09), ('OD1', 'ASN', 'CD2', 'TYR', 8.15), ('OD1', 'ASN', 'CE1', 'TYR', 7.1), ('OD1', 'ASN', 'CE2', 'TYR', 7.18), ('OD1', 'ASN', 'CZ', 'TYR', 6.59), ('OD1', 'ASN', 'OH', 'TYR', 6.0)], [('ND2', 'ASN', 'CB', 'TYR', 8.54), ('ND2', 'ASN', 'CG', 'TYR', 7.18), ('ND2', 'ASN', 'CD1', 'TYR', 6.34), ('ND2', 'ASN', 'CD2', 'TYR', 7.12), ('ND2', 'ASN', 'CE1', 'TYR', 5.25), ('ND2', 'ASN', 'CE2', 'TYR', 6.24), ('ND2', 'ASN', 'CZ', 'TYR', 5.2), ('ND2', 'ASN', 'OH', 'TYR', 4.82)]]}
PRO_ASN = { 
	'distances':
		[[7.98, 8.17, 9.32, 7.3], [7.6, 7.66, 8.83, 6.67], [6.3, 6.61, 7.83, 5.85], [6.83, 6.29, 7.14, 5.29], [7.18, 6.98, 7.92, 6.15], [6.87, 7.08, 8.19, 6.38], [5.65, 6.02, 7.22, 5.43]],
	'comparisons':
		[[('CB', 'PRO', 'CB', 'ASN', 7.98), ('CB', 'PRO', 'CG', 'ASN', 8.17), ('CB', 'PRO', 'OD1', 'ASN', 9.32), ('CB', 'PRO', 'ND2', 'ASN', 7.3)], [('CG', 'PRO', 'CB', 'ASN', 7.6), ('CG', 'PRO', 'CG', 'ASN', 7.66), ('CG', 'PRO', 'OD1', 'ASN', 8.83), ('CG', 'PRO', 'ND2', 'ASN', 6.67)], [('CD', 'PRO', 'CB', 'ASN', 6.3), ('CD', 'PRO', 'CG', 'ASN', 6.61), ('CD', 'PRO', 'OD1', 'ASN', 7.83), ('CD', 'PRO', 'ND2', 'ASN', 5.85)], [('O', 'PRO', 'CB', 'ASN', 6.83), ('O', 'PRO', 'CG', 'ASN', 6.29), ('O', 'PRO', 'OD1', 'ASN', 7.14), ('O', 'PRO', 'ND2', 'ASN', 5.29)], [('C', 'PRO', 'CB', 'ASN', 7.18), ('C', 'PRO', 'CG', 'ASN', 6.98), ('C', 'PRO', 'OD1', 'ASN', 7.92), ('C', 'PRO', 'ND2', 'ASN', 6.15)], [('CA', 'PRO', 'CB', 'ASN', 6.87), ('CA', 'PRO', 'CG', 'ASN', 7.08), ('CA', 'PRO', 'OD1', 'ASN', 8.19), ('CA', 'PRO', 'ND2', 'ASN', 6.38)], [('N', 'PRO', 'CB', 'ASN', 5.65), ('N', 'PRO', 'CG', 'ASN', 6.02), ('N', 'PRO', 'OD1', 'ASN', 7.22), ('N', 'PRO', 'ND2', 'ASN', 5.43)]]}
PRO_TYR = { 
	'distances':
		[[9.23, 8.6, 7.28, 9.58, 7.12, 9.48, 8.35, 8.69], [9.03, 8.18, 6.78, 9.01, 6.34, 8.72, 7.48, 7.66], [9.75, 8.71, 7.35, 9.32, 6.59, 8.79, 7.47, 7.34], [6.79, 5.99, 4.91, 6.8, 4.89, 6.8, 5.95, 6.63], [7.61, 7.02, 5.94, 7.95, 6.03, 8.02, 7.16, 7.77], [8.97, 8.27, 7.04, 9.13, 6.83, 8.99, 7.92, 8.25], [9.46, 8.5, 7.23, 9.12, 6.62, 8.7, 7.5, 7.51]],
	'comparisons':
		[[('CB', 'PRO', 'CB', 'TYR', 9.23), ('CB', 'PRO', 'CG', 'TYR', 8.6), ('CB', 'PRO', 'CD1', 'TYR', 7.28), ('CB', 'PRO', 'CD2', 'TYR', 9.58), ('CB', 'PRO', 'CE1', 'TYR', 7.12), ('CB', 'PRO', 'CE2', 'TYR', 9.48), ('CB', 'PRO', 'CZ', 'TYR', 8.35), ('CB', 'PRO', 'OH', 'TYR', 8.69)], [('CG', 'PRO', 'CB', 'TYR', 9.03), ('CG', 'PRO', 'CG', 'TYR', 8.18), ('CG', 'PRO', 'CD1', 'TYR', 6.78), ('CG', 'PRO', 'CD2', 'TYR', 9.01), ('CG', 'PRO', 'CE1', 'TYR', 6.34), ('CG', 'PRO', 'CE2', 'TYR', 8.72), ('CG', 'PRO', 'CZ', 'TYR', 7.48), ('CG', 'PRO', 'OH', 'TYR', 7.66)], [('CD', 'PRO', 'CB', 'TYR', 9.75), ('CD', 'PRO', 'CG', 'TYR', 8.71), ('CD', 'PRO', 'CD1', 'TYR', 7.35), ('CD', 'PRO', 'CD2', 'TYR', 9.32), ('CD', 'PRO', 'CE1', 'TYR', 6.59), ('CD', 'PRO', 'CE2', 'TYR', 8.79), ('CD', 'PRO', 'CZ', 'TYR', 7.47), ('CD', 'PRO', 'OH', 'TYR', 7.34)], [('O', 'PRO', 'CB', 'TYR', 6.79), ('O', 'PRO', 'CG', 'TYR', 5.99), ('O', 'PRO', 'CD1', 'TYR', 4.91), ('O', 'PRO', 'CD2', 'TYR', 6.8), ('O', 'PRO', 'CE1', 'TYR', 4.89), ('O', 'PRO', 'CE2', 'TYR', 6.8), ('O', 'PRO', 'CZ', 'TYR', 5.95), ('O', 'PRO', 'OH', 'TYR', 6.63)], [('C', 'PRO', 'CB', 'TYR', 7.61), ('C', 'PRO', 'CG', 'TYR', 7.02), ('C', 'PRO', 'CD1', 'TYR', 5.94), ('C', 'PRO', 'CD2', 'TYR', 7.95), ('C', 'PRO', 'CE1', 'TYR', 6.03), ('C', 'PRO', 'CE2', 'TYR', 8.02), ('C', 'PRO', 'CZ', 'TYR', 7.16), ('C', 'PRO', 'OH', 'TYR', 7.77)], [('CA', 'PRO', 'CB', 'TYR', 8.97), ('CA', 'PRO', 'CG', 'TYR', 8.27), ('CA', 'PRO', 'CD1', 'TYR', 7.04), ('CA', 'PRO', 'CD2', 'TYR', 9.13), ('CA', 'PRO', 'CE1', 'TYR', 6.83), ('CA', 'PRO', 'CE2', 'TYR', 8.99), ('CA', 'PRO', 'CZ', 'TYR', 7.92), ('CA', 'PRO', 'OH', 'TYR', 8.25)], [('N', 'PRO', 'CB', 'TYR', 9.46), ('N', 'PRO', 'CG', 'TYR', 8.5), ('N', 'PRO', 'CD1', 'TYR', 7.23), ('N', 'PRO', 'CD2', 'TYR', 9.12), ('N', 'PRO', 'CE1', 'TYR', 6.62), ('N', 'PRO', 'CE2', 'TYR', 8.7), ('N', 'PRO', 'CZ', 'TYR', 7.5), ('N', 'PRO', 'OH', 'TYR', 7.51)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASN_TYR, d, 'A_2adm_2_1_1_72')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(PRO_ASN, d, 'A_2adm_2_1_1_72')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(PRO_TYR, d, 'A_2adm_2_1_1_72')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASN_TYR' :  match1,
		'PRO_ASN' :  match2,
		'PRO_TYR' :  match3}