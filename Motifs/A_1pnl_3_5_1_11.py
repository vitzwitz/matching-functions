'''
FUNC:A_1pnl_3_5_1_11
PDB:1pnl
EC:3.5.1.11
RESI:ser,ala,asn
LOCI:b-1,69,241;
'''
import motifFunctions as cmd
ASN_ALA = { 
	'distances':
		[[7.43, 6.27, 7.27, 7.72, 7.65], [6.54, 6.09, 6.93, 6.97, 6.7], [7.09, 7.22, 7.95, 7.76, 7.43], [5.6, 5.14, 5.9, 5.81, 5.38]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'ALA', 7.43), ('CB', 'ASN', 'O', 'ALA', 6.27), ('CB', 'ASN', 'C', 'ALA', 7.27), ('CB', 'ASN', 'CA', 'ALA', 7.72), ('CB', 'ASN', 'N', 'ALA', 7.65)], [('CG', 'ASN', 'CB', 'ALA', 6.54), ('CG', 'ASN', 'O', 'ALA', 6.09), ('CG', 'ASN', 'C', 'ALA', 6.93), ('CG', 'ASN', 'CA', 'ALA', 6.97), ('CG', 'ASN', 'N', 'ALA', 6.7)], [('OD1', 'ASN', 'CB', 'ALA', 7.09), ('OD1', 'ASN', 'O', 'ALA', 7.22), ('OD1', 'ASN', 'C', 'ALA', 7.95), ('OD1', 'ASN', 'CA', 'ALA', 7.76), ('OD1', 'ASN', 'N', 'ALA', 7.43)], [('ND2', 'ASN', 'CB', 'ALA', 5.6), ('ND2', 'ASN', 'O', 'ALA', 5.14), ('ND2', 'ASN', 'C', 'ALA', 5.9), ('ND2', 'ASN', 'CA', 'ALA', 5.81), ('ND2', 'ASN', 'N', 'ALA', 5.38)]]}
ALA_SER = { 
	'distances':
		[[7.45, 7.09], [8.22, 8.57], [8.55, 8.67], [7.63, 7.52], [6.41, 6.49]],
	'comparisons':
		[[('CB', 'ALA', 'CB', 'SER', 7.45), ('CB', 'ALA', 'OG', 'SER', 7.09)], [('O', 'ALA', 'CB', 'SER', 8.22), ('O', 'ALA', 'OG', 'SER', 8.57)], [('C', 'ALA', 'CB', 'SER', 8.55), ('C', 'ALA', 'OG', 'SER', 8.67)], [('CA', 'ALA', 'CB', 'SER', 7.63), ('CA', 'ALA', 'OG', 'SER', 7.52)], [('N', 'ALA', 'CB', 'SER', 6.41), ('N', 'ALA', 'OG', 'SER', 6.49)]]}
ASN_SER = { 
	'distances':
		[[8.15, 8.7], [6.74, 7.21], [6.57, 6.91], [6.04, 6.51]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'SER', 8.15), ('CB', 'ASN', 'OG', 'SER', 8.7)], [('CG', 'ASN', 'CB', 'SER', 6.74), ('CG', 'ASN', 'OG', 'SER', 7.21)], [('OD1', 'ASN', 'CB', 'SER', 6.57), ('OD1', 'ASN', 'OG', 'SER', 6.91)], [('ND2', 'ASN', 'CB', 'SER', 6.04), ('ND2', 'ASN', 'OG', 'SER', 6.51)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASN_ALA, d, 'A_1pnl_3_5_1_11')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ALA_SER, d, 'A_1pnl_3_5_1_11')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASN_SER, d, 'A_1pnl_3_5_1_11')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASN_ALA' :  match1,
		'ALA_SER' :  match2,
		'ASN_SER' :  match3}