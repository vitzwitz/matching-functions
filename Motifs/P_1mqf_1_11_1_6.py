'''
FUNC:P_1mqf_1_11_1_6
PDB:1mqf
EC:1.11.1.6
RESI:his,ser,asn
LOCI:a-54,93,127;
'''
import motifFunctions as cmd
HIS_ASN = { 
	'distances':
		[[11.32, 10.0, 8.93, 10.25], [9.98, 8.61, 7.6, 8.78], [8.89, 7.62, 6.54, 7.99], [9.68, 8.21, 7.36, 8.14], [7.81, 6.46, 5.48, 6.7], [8.35, 6.87, 6.09, 6.78]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASN', 11.32), ('CB', 'HIS', 'CG', 'ASN', 10.0), ('CB', 'HIS', 'OD1', 'ASN', 8.93), ('CB', 'HIS', 'ND2', 'ASN', 10.25)], [('CG', 'HIS', 'CB', 'ASN', 9.98), ('CG', 'HIS', 'CG', 'ASN', 8.61), ('CG', 'HIS', 'OD1', 'ASN', 7.6), ('CG', 'HIS', 'ND2', 'ASN', 8.78)], [('ND1', 'HIS', 'CB', 'ASN', 8.89), ('ND1', 'HIS', 'CG', 'ASN', 7.62), ('ND1', 'HIS', 'OD1', 'ASN', 6.54), ('ND1', 'HIS', 'ND2', 'ASN', 7.99)], [('CD2', 'HIS', 'CB', 'ASN', 9.68), ('CD2', 'HIS', 'CG', 'ASN', 8.21), ('CD2', 'HIS', 'OD1', 'ASN', 7.36), ('CD2', 'HIS', 'ND2', 'ASN', 8.14)], [('CE1', 'HIS', 'CB', 'ASN', 7.81), ('CE1', 'HIS', 'CG', 'ASN', 6.46), ('CE1', 'HIS', 'OD1', 'ASN', 5.48), ('CE1', 'HIS', 'ND2', 'ASN', 6.7)], [('NE2', 'HIS', 'CB', 'ASN', 8.35), ('NE2', 'HIS', 'CG', 'ASN', 6.87), ('NE2', 'HIS', 'OD1', 'ASN', 6.09), ('NE2', 'HIS', 'ND2', 'ASN', 6.78)]]}
SER_ASN = { 
	'distances':
		[[11.48, 10.61, 9.44, 11.35], [10.25, 9.33, 8.13, 10.07]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ASN', 11.48), ('CB', 'SER', 'CG', 'ASN', 10.61), ('CB', 'SER', 'OD1', 'ASN', 9.44), ('CB', 'SER', 'ND2', 'ASN', 11.35)], [('OG', 'SER', 'CB', 'ASN', 10.25), ('OG', 'SER', 'CG', 'ASN', 9.33), ('OG', 'SER', 'OD1', 'ASN', 8.13), ('OG', 'SER', 'ND2', 'ASN', 10.07)]]}
HIS_SER = { 
	'distances':
		[[5.95, 5.37], [6.44, 5.5], [5.97, 4.82], [7.77, 6.76], [7.15, 5.93], [8.1, 6.94]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'SER', 5.95), ('CB', 'HIS', 'OG', 'SER', 5.37)], [('CG', 'HIS', 'CB', 'SER', 6.44), ('CG', 'HIS', 'OG', 'SER', 5.5)], [('ND1', 'HIS', 'CB', 'SER', 5.97), ('ND1', 'HIS', 'OG', 'SER', 4.82)], [('CD2', 'HIS', 'CB', 'SER', 7.77), ('CD2', 'HIS', 'OG', 'SER', 6.76)], [('CE1', 'HIS', 'CB', 'SER', 7.15), ('CE1', 'HIS', 'OG', 'SER', 5.93)], [('NE2', 'HIS', 'CB', 'SER', 8.1), ('NE2', 'HIS', 'OG', 'SER', 6.94)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_ASN, d, 'P_1mqf_1_11_1_6')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(SER_ASN, d, 'P_1mqf_1_11_1_6')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_SER, d, 'P_1mqf_1_11_1_6')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_ASN' :  match1,
		'SER_ASN' :  match2,
		'HIS_SER' :  match3}