'''
FUNC:A_1coy_1_1_3_6
PDB:1coy
EC:1.1.3.6
RESI:glu,his,asn
LOCI:a-361,447,485;
'''
import motifFunctions as cmd
HIS_GLU = { 
	'distances':
		[[13.64, 12.79, 11.73, 10.93, 11.9], [12.27, 11.42, 10.3, 9.49, 10.44], [11.14, 10.36, 9.34, 8.48, 9.64], [11.98, 11.09, 9.83, 9.09, 9.81], [10.08, 9.29, 8.16, 7.3, 8.42], [10.62, 9.75, 8.47, 7.71, 8.49]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLU', 13.64), ('CB', 'HIS', 'CG', 'GLU', 12.79), ('CB', 'HIS', 'CD', 'GLU', 11.73), ('CB', 'HIS', 'OE1', 'GLU', 10.93), ('CB', 'HIS', 'OE2', 'GLU', 11.9)], [('CG', 'HIS', 'CB', 'GLU', 12.27), ('CG', 'HIS', 'CG', 'GLU', 11.42), ('CG', 'HIS', 'CD', 'GLU', 10.3), ('CG', 'HIS', 'OE1', 'GLU', 9.49), ('CG', 'HIS', 'OE2', 'GLU', 10.44)], [('ND1', 'HIS', 'CB', 'GLU', 11.14), ('ND1', 'HIS', 'CG', 'GLU', 10.36), ('ND1', 'HIS', 'CD', 'GLU', 9.34), ('ND1', 'HIS', 'OE1', 'GLU', 8.48), ('ND1', 'HIS', 'OE2', 'GLU', 9.64)], [('CD2', 'HIS', 'CB', 'GLU', 11.98), ('CD2', 'HIS', 'CG', 'GLU', 11.09), ('CD2', 'HIS', 'CD', 'GLU', 9.83), ('CD2', 'HIS', 'OE1', 'GLU', 9.09), ('CD2', 'HIS', 'OE2', 'GLU', 9.81)], [('CE1', 'HIS', 'CB', 'GLU', 10.08), ('CE1', 'HIS', 'CG', 'GLU', 9.29), ('CE1', 'HIS', 'CD', 'GLU', 8.16), ('CE1', 'HIS', 'OE1', 'GLU', 7.3), ('CE1', 'HIS', 'OE2', 'GLU', 8.42)], [('NE2', 'HIS', 'CB', 'GLU', 10.62), ('NE2', 'HIS', 'CG', 'GLU', 9.75), ('NE2', 'HIS', 'CD', 'GLU', 8.47), ('NE2', 'HIS', 'OE1', 'GLU', 7.71), ('NE2', 'HIS', 'OE2', 'GLU', 8.49)]]}
ASN_GLU = { 
	'distances':
		[[9.7, 9.68, 8.53, 7.35, 9.01], [8.23, 8.18, 7.05, 5.86, 7.59], [7.96, 7.63, 6.34, 5.23, 6.73], [7.49, 7.73, 6.85, 5.65, 7.62]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'GLU', 9.7), ('CB', 'ASN', 'CG', 'GLU', 9.68), ('CB', 'ASN', 'CD', 'GLU', 8.53), ('CB', 'ASN', 'OE1', 'GLU', 7.35), ('CB', 'ASN', 'OE2', 'GLU', 9.01)], [('CG', 'ASN', 'CB', 'GLU', 8.23), ('CG', 'ASN', 'CG', 'GLU', 8.18), ('CG', 'ASN', 'CD', 'GLU', 7.05), ('CG', 'ASN', 'OE1', 'GLU', 5.86), ('CG', 'ASN', 'OE2', 'GLU', 7.59)], [('OD1', 'ASN', 'CB', 'GLU', 7.96), ('OD1', 'ASN', 'CG', 'GLU', 7.63), ('OD1', 'ASN', 'CD', 'GLU', 6.34), ('OD1', 'ASN', 'OE1', 'GLU', 5.23), ('OD1', 'ASN', 'OE2', 'GLU', 6.73)], [('ND2', 'ASN', 'CB', 'GLU', 7.49), ('ND2', 'ASN', 'CG', 'GLU', 7.73), ('ND2', 'ASN', 'CD', 'GLU', 6.85), ('ND2', 'ASN', 'OE1', 'GLU', 5.65), ('ND2', 'ASN', 'OE2', 'GLU', 7.62)]]}
HIS_ASN = { 
	'distances':
		[[9.26, 9.49, 8.98, 10.49], [8.07, 8.15, 7.54, 9.18], [7.44, 7.32, 6.76, 8.2], [7.72, 7.78, 7.03, 8.93], [6.66, 6.33, 5.59, 7.26], [6.83, 6.63, 5.76, 7.74]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASN', 9.26), ('CB', 'HIS', 'CG', 'ASN', 9.49), ('CB', 'HIS', 'OD1', 'ASN', 8.98), ('CB', 'HIS', 'ND2', 'ASN', 10.49)], [('CG', 'HIS', 'CB', 'ASN', 8.07), ('CG', 'HIS', 'CG', 'ASN', 8.15), ('CG', 'HIS', 'OD1', 'ASN', 7.54), ('CG', 'HIS', 'ND2', 'ASN', 9.18)], [('ND1', 'HIS', 'CB', 'ASN', 7.44), ('ND1', 'HIS', 'CG', 'ASN', 7.32), ('ND1', 'HIS', 'OD1', 'ASN', 6.76), ('ND1', 'HIS', 'ND2', 'ASN', 8.2)], [('CD2', 'HIS', 'CB', 'ASN', 7.72), ('CD2', 'HIS', 'CG', 'ASN', 7.78), ('CD2', 'HIS', 'OD1', 'ASN', 7.03), ('CD2', 'HIS', 'ND2', 'ASN', 8.93)], [('CE1', 'HIS', 'CB', 'ASN', 6.66), ('CE1', 'HIS', 'CG', 'ASN', 6.33), ('CE1', 'HIS', 'OD1', 'ASN', 5.59), ('CE1', 'HIS', 'ND2', 'ASN', 7.26)], [('NE2', 'HIS', 'CB', 'ASN', 6.83), ('NE2', 'HIS', 'CG', 'ASN', 6.63), ('NE2', 'HIS', 'OD1', 'ASN', 5.76), ('NE2', 'HIS', 'ND2', 'ASN', 7.74)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_GLU, d, 'A_1coy_1_1_3_6')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASN_GLU, d, 'A_1coy_1_1_3_6')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_ASN, d, 'A_1coy_1_1_3_6')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_GLU' :  match1,
		'ASN_GLU' :  match2,
		'HIS_ASN' :  match3}