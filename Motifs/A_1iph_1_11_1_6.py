'''
FUNC:A_1iph_1_11_1_6
PDB:1iph
EC:1.11.1.6
RESI:his,ser,asn
LOCI:a-128,167,201;
'''
import motifFunctions as cmd
HIS_ASN = { 
	'distances':
		[[11.29, 10.35, 9.16, 11.26], [9.84, 8.85, 7.66, 9.74], [8.76, 7.92, 6.78, 8.9], [9.58, 8.4, 7.2, 9.12], [7.72, 6.74, 5.57, 7.65], [8.3, 7.09, 5.92, 7.81]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASN', 11.29), ('CB', 'HIS', 'CG', 'ASN', 10.35), ('CB', 'HIS', 'OD1', 'ASN', 9.16), ('CB', 'HIS', 'ND2', 'ASN', 11.26)], [('CG', 'HIS', 'CB', 'ASN', 9.84), ('CG', 'HIS', 'CG', 'ASN', 8.85), ('CG', 'HIS', 'OD1', 'ASN', 7.66), ('CG', 'HIS', 'ND2', 'ASN', 9.74)], [('ND1', 'HIS', 'CB', 'ASN', 8.76), ('ND1', 'HIS', 'CG', 'ASN', 7.92), ('ND1', 'HIS', 'OD1', 'ASN', 6.78), ('ND1', 'HIS', 'ND2', 'ASN', 8.9)], [('CD2', 'HIS', 'CB', 'ASN', 9.58), ('CD2', 'HIS', 'CG', 'ASN', 8.4), ('CD2', 'HIS', 'OD1', 'ASN', 7.2), ('CD2', 'HIS', 'ND2', 'ASN', 9.12)], [('CE1', 'HIS', 'CB', 'ASN', 7.72), ('CE1', 'HIS', 'CG', 'ASN', 6.74), ('CE1', 'HIS', 'OD1', 'ASN', 5.57), ('CE1', 'HIS', 'ND2', 'ASN', 7.65)], [('NE2', 'HIS', 'CB', 'ASN', 8.3), ('NE2', 'HIS', 'CG', 'ASN', 7.09), ('NE2', 'HIS', 'OD1', 'ASN', 5.92), ('NE2', 'HIS', 'ND2', 'ASN', 7.81)]]}
SER_ASN = { 
	'distances':
		[[10.9, 10.59, 9.63, 11.77], [9.59, 9.27, 8.3, 10.47]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ASN', 10.9), ('CB', 'SER', 'CG', 'ASN', 10.59), ('CB', 'SER', 'OD1', 'ASN', 9.63), ('CB', 'SER', 'ND2', 'ASN', 11.77)], [('OG', 'SER', 'CB', 'ASN', 9.59), ('OG', 'SER', 'CG', 'ASN', 9.27), ('OG', 'SER', 'OD1', 'ASN', 8.3), ('OG', 'SER', 'ND2', 'ASN', 10.47)]]}
SER_HIS = { 
	'distances':
		[[6.06, 6.28, 5.75, 7.61, 6.89, 7.85], [5.88, 5.64, 4.84, 6.83, 5.8, 6.85]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'HIS', 6.06), ('CB', 'SER', 'CG', 'HIS', 6.28), ('CB', 'SER', 'ND1', 'HIS', 5.75), ('CB', 'SER', 'CD2', 'HIS', 7.61), ('CB', 'SER', 'CE1', 'HIS', 6.89), ('CB', 'SER', 'NE2', 'HIS', 7.85)], [('OG', 'SER', 'CB', 'HIS', 5.88), ('OG', 'SER', 'CG', 'HIS', 5.64), ('OG', 'SER', 'ND1', 'HIS', 4.84), ('OG', 'SER', 'CD2', 'HIS', 6.83), ('OG', 'SER', 'CE1', 'HIS', 5.8), ('OG', 'SER', 'NE2', 'HIS', 6.85)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_ASN, d, 'A_1iph_1_11_1_6')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(SER_ASN, d, 'A_1iph_1_11_1_6')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(SER_HIS, d, 'A_1iph_1_11_1_6')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_ASN' :  match1,
		'SER_ASN' :  match2,
		'SER_HIS' :  match3}