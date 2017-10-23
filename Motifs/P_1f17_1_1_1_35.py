'''
FUNC:P_1f17_1_1_1_35
PDB:1f17
EC:1.1.1.35
RESI:ser,his,asn
LOCI:a-137,158,208;
'''
import motifFunctions as cmd
HIS_ASN = { 
	'distances':
		[[10.72, 10.01, 10.58, 8.99], [9.51, 8.68, 9.24, 7.62], [8.31, 7.52, 8.08, 6.58], [9.49, 8.53, 9.07, 7.34], [7.48, 6.52, 7.06, 5.47], [8.29, 7.24, 7.76, 6.04]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASN', 10.72), ('CB', 'HIS', 'CG', 'ASN', 10.01), ('CB', 'HIS', 'OD1', 'ASN', 10.58), ('CB', 'HIS', 'ND2', 'ASN', 8.99)], [('CG', 'HIS', 'CB', 'ASN', 9.51), ('CG', 'HIS', 'CG', 'ASN', 8.68), ('CG', 'HIS', 'OD1', 'ASN', 9.24), ('CG', 'HIS', 'ND2', 'ASN', 7.62)], [('ND1', 'HIS', 'CB', 'ASN', 8.31), ('ND1', 'HIS', 'CG', 'ASN', 7.52), ('ND1', 'HIS', 'OD1', 'ASN', 8.08), ('ND1', 'HIS', 'ND2', 'ASN', 6.58)], [('CD2', 'HIS', 'CB', 'ASN', 9.49), ('CD2', 'HIS', 'CG', 'ASN', 8.53), ('CD2', 'HIS', 'OD1', 'ASN', 9.07), ('CD2', 'HIS', 'ND2', 'ASN', 7.34)], [('CE1', 'HIS', 'CB', 'ASN', 7.48), ('CE1', 'HIS', 'CG', 'ASN', 6.52), ('CE1', 'HIS', 'OD1', 'ASN', 7.06), ('CE1', 'HIS', 'ND2', 'ASN', 5.47)], [('NE2', 'HIS', 'CB', 'ASN', 8.29), ('NE2', 'HIS', 'CG', 'ASN', 7.24), ('NE2', 'HIS', 'OD1', 'ASN', 7.76), ('NE2', 'HIS', 'ND2', 'ASN', 6.04)]]}
SER_ASN = { 
	'distances':
		[[8.04, 7.25, 7.96, 6.05], [8.32, 7.26, 7.77, 6.03]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ASN', 8.04), ('CB', 'SER', 'CG', 'ASN', 7.25), ('CB', 'SER', 'OD1', 'ASN', 7.96), ('CB', 'SER', 'ND2', 'ASN', 6.05)], [('OG', 'SER', 'CB', 'ASN', 8.32), ('OG', 'SER', 'CG', 'ASN', 7.26), ('OG', 'SER', 'OD1', 'ASN', 7.77), ('OG', 'SER', 'ND2', 'ASN', 6.03)]]}
SER_HIS = { 
	'distances':
		[[8.93, 7.61, 7.5, 6.59, 6.43, 5.72], [8.25, 6.87, 6.83, 5.72, 5.72, 4.8]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'HIS', 8.93), ('CB', 'SER', 'CG', 'HIS', 7.61), ('CB', 'SER', 'ND1', 'HIS', 7.5), ('CB', 'SER', 'CD2', 'HIS', 6.59), ('CB', 'SER', 'CE1', 'HIS', 6.43), ('CB', 'SER', 'NE2', 'HIS', 5.72)], [('OG', 'SER', 'CB', 'HIS', 8.25), ('OG', 'SER', 'CG', 'HIS', 6.87), ('OG', 'SER', 'ND1', 'HIS', 6.83), ('OG', 'SER', 'CD2', 'HIS', 5.72), ('OG', 'SER', 'CE1', 'HIS', 5.72), ('OG', 'SER', 'NE2', 'HIS', 4.8)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_ASN, d, 'P_1f17_1_1_1_35')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(SER_ASN, d, 'P_1f17_1_1_1_35')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(SER_HIS, d, 'P_1f17_1_1_1_35')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_ASN' :  match1,
		'SER_ASN' :  match2,
		'SER_HIS' :  match3}