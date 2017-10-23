'''
FUNC:A_1dhr_1_5_1_34
PDB:1dhr
EC:1.5.1.34
RESI:tyr,lys,asn
LOCI:a-146,150,186;
'''
import motifFunctions as cmd
LYS_ASN = { 
	'distances':
		[[18.85, 17.36, 17.02, 16.58], [17.55, 16.05, 15.66, 15.32], [17.47, 15.98, 15.6, 15.23], [16.16, 14.66, 14.26, 13.95], [16.42, 14.95, 14.56, 14.25]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'ASN', 18.85), ('CB', 'LYS', 'CG', 'ASN', 17.36), ('CB', 'LYS', 'OD1', 'ASN', 17.02), ('CB', 'LYS', 'ND2', 'ASN', 16.58)], [('CG', 'LYS', 'CB', 'ASN', 17.55), ('CG', 'LYS', 'CG', 'ASN', 16.05), ('CG', 'LYS', 'OD1', 'ASN', 15.66), ('CG', 'LYS', 'ND2', 'ASN', 15.32)], [('CD', 'LYS', 'CB', 'ASN', 17.47), ('CD', 'LYS', 'CG', 'ASN', 15.98), ('CD', 'LYS', 'OD1', 'ASN', 15.6), ('CD', 'LYS', 'ND2', 'ASN', 15.23)], [('CE', 'LYS', 'CB', 'ASN', 16.16), ('CE', 'LYS', 'CG', 'ASN', 14.66), ('CE', 'LYS', 'OD1', 'ASN', 14.26), ('CE', 'LYS', 'ND2', 'ASN', 13.95)], [('NZ', 'LYS', 'CB', 'ASN', 16.42), ('NZ', 'LYS', 'CG', 'ASN', 14.95), ('NZ', 'LYS', 'OD1', 'ASN', 14.56), ('NZ', 'LYS', 'ND2', 'ASN', 14.25)]]}
TYR_LYS = { 
	'distances':
		[[8.32, 7.45, 8.46, 8.41, 9.64], [7.6, 6.54, 7.51, 7.3, 8.59], [7.58, 6.26, 6.87, 6.36, 7.52], [7.42, 6.52, 7.67, 7.55, 8.96], [7.44, 6.02, 6.42, 5.63, 6.79], [7.27, 6.3, 7.29, 7.02, 8.41], [7.3, 6.05, 6.67, 6.05, 7.33], [7.66, 6.45, 6.8, 6.02, 7.14]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'LYS', 8.32), ('CB', 'TYR', 'CG', 'LYS', 7.45), ('CB', 'TYR', 'CD', 'LYS', 8.46), ('CB', 'TYR', 'CE', 'LYS', 8.41), ('CB', 'TYR', 'NZ', 'LYS', 9.64)], [('CG', 'TYR', 'CB', 'LYS', 7.6), ('CG', 'TYR', 'CG', 'LYS', 6.54), ('CG', 'TYR', 'CD', 'LYS', 7.51), ('CG', 'TYR', 'CE', 'LYS', 7.3), ('CG', 'TYR', 'NZ', 'LYS', 8.59)], [('CD1', 'TYR', 'CB', 'LYS', 7.58), ('CD1', 'TYR', 'CG', 'LYS', 6.26), ('CD1', 'TYR', 'CD', 'LYS', 6.87), ('CD1', 'TYR', 'CE', 'LYS', 6.36), ('CD1', 'TYR', 'NZ', 'LYS', 7.52)], [('CD2', 'TYR', 'CB', 'LYS', 7.42), ('CD2', 'TYR', 'CG', 'LYS', 6.52), ('CD2', 'TYR', 'CD', 'LYS', 7.67), ('CD2', 'TYR', 'CE', 'LYS', 7.55), ('CD2', 'TYR', 'NZ', 'LYS', 8.96)], [('CE1', 'TYR', 'CB', 'LYS', 7.44), ('CE1', 'TYR', 'CG', 'LYS', 6.02), ('CE1', 'TYR', 'CD', 'LYS', 6.42), ('CE1', 'TYR', 'CE', 'LYS', 5.63), ('CE1', 'TYR', 'NZ', 'LYS', 6.79)], [('CE2', 'TYR', 'CB', 'LYS', 7.27), ('CE2', 'TYR', 'CG', 'LYS', 6.3), ('CE2', 'TYR', 'CD', 'LYS', 7.29), ('CE2', 'TYR', 'CE', 'LYS', 7.02), ('CE2', 'TYR', 'NZ', 'LYS', 8.41)], [('CZ', 'TYR', 'CB', 'LYS', 7.3), ('CZ', 'TYR', 'CG', 'LYS', 6.05), ('CZ', 'TYR', 'CD', 'LYS', 6.67), ('CZ', 'TYR', 'CE', 'LYS', 6.05), ('CZ', 'TYR', 'NZ', 'LYS', 7.33)], [('OH', 'TYR', 'CB', 'LYS', 7.66), ('OH', 'TYR', 'CG', 'LYS', 6.45), ('OH', 'TYR', 'CD', 'LYS', 6.8), ('OH', 'TYR', 'CE', 'LYS', 6.02), ('OH', 'TYR', 'NZ', 'LYS', 7.14)]]}
TYR_ASN = { 
	'distances':
		[[16.64, 15.2, 14.48, 14.9], [15.59, 14.13, 13.49, 13.72], [15.01, 13.52, 12.86, 13.11], [15.38, 13.94, 13.41, 13.43], [14.14, 12.63, 12.07, 12.12], [14.54, 13.09, 12.68, 12.47], [13.89, 12.4, 11.97, 11.77], [13.23, 11.75, 11.44, 10.99]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'ASN', 16.64), ('CB', 'TYR', 'CG', 'ASN', 15.2), ('CB', 'TYR', 'OD1', 'ASN', 14.48), ('CB', 'TYR', 'ND2', 'ASN', 14.9)], [('CG', 'TYR', 'CB', 'ASN', 15.59), ('CG', 'TYR', 'CG', 'ASN', 14.13), ('CG', 'TYR', 'OD1', 'ASN', 13.49), ('CG', 'TYR', 'ND2', 'ASN', 13.72)], [('CD1', 'TYR', 'CB', 'ASN', 15.01), ('CD1', 'TYR', 'CG', 'ASN', 13.52), ('CD1', 'TYR', 'OD1', 'ASN', 12.86), ('CD1', 'TYR', 'ND2', 'ASN', 13.11)], [('CD2', 'TYR', 'CB', 'ASN', 15.38), ('CD2', 'TYR', 'CG', 'ASN', 13.94), ('CD2', 'TYR', 'OD1', 'ASN', 13.41), ('CD2', 'TYR', 'ND2', 'ASN', 13.43)], [('CE1', 'TYR', 'CB', 'ASN', 14.14), ('CE1', 'TYR', 'CG', 'ASN', 12.63), ('CE1', 'TYR', 'OD1', 'ASN', 12.07), ('CE1', 'TYR', 'ND2', 'ASN', 12.12)], [('CE2', 'TYR', 'CB', 'ASN', 14.54), ('CE2', 'TYR', 'CG', 'ASN', 13.09), ('CE2', 'TYR', 'OD1', 'ASN', 12.68), ('CE2', 'TYR', 'ND2', 'ASN', 12.47)], [('CZ', 'TYR', 'CB', 'ASN', 13.89), ('CZ', 'TYR', 'CG', 'ASN', 12.4), ('CZ', 'TYR', 'OD1', 'ASN', 11.97), ('CZ', 'TYR', 'ND2', 'ASN', 11.77)], [('OH', 'TYR', 'CB', 'ASN', 13.23), ('OH', 'TYR', 'CG', 'ASN', 11.75), ('OH', 'TYR', 'OD1', 'ASN', 11.44), ('OH', 'TYR', 'ND2', 'ASN', 10.99)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LYS_ASN, d, 'A_1dhr_1_5_1_34')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(TYR_LYS, d, 'A_1dhr_1_5_1_34')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(TYR_ASN, d, 'A_1dhr_1_5_1_34')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'LYS_ASN' :  match1,
		'TYR_LYS' :  match2,
		'TYR_ASN' :  match3}