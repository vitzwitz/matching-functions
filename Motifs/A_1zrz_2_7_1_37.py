'''
FUNC:A_1zrz_2_7_1_37
PDB:1zrz
EC:2.7.1.37
RESI:asp,lys,asn
LOCI:a-369,371,374;
'''
import motifFunctions as cmd
LYS_ASP = { 
	'distances':
		[[8.78, 8.06, 7.78, 8.15], [8.5, 7.62, 7.51, 7.41], [8.36, 7.2, 6.91, 6.93], [6.99, 5.74, 5.4, 5.59], [6.31, 5.37, 4.89, 5.69]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'ASP', 8.78), ('CB', 'LYS', 'CG', 'ASP', 8.06), ('CB', 'LYS', 'OD1', 'ASP', 7.78), ('CB', 'LYS', 'OD2', 'ASP', 8.15)], [('CG', 'LYS', 'CB', 'ASP', 8.5), ('CG', 'LYS', 'CG', 'ASP', 7.62), ('CG', 'LYS', 'OD1', 'ASP', 7.51), ('CG', 'LYS', 'OD2', 'ASP', 7.41)], [('CD', 'LYS', 'CB', 'ASP', 8.36), ('CD', 'LYS', 'CG', 'ASP', 7.2), ('CD', 'LYS', 'OD1', 'ASP', 6.91), ('CD', 'LYS', 'OD2', 'ASP', 6.93)], [('CE', 'LYS', 'CB', 'ASP', 6.99), ('CE', 'LYS', 'CG', 'ASP', 5.74), ('CE', 'LYS', 'OD1', 'ASP', 5.4), ('CE', 'LYS', 'OD2', 'ASP', 5.59)], [('NZ', 'LYS', 'CB', 'ASP', 6.31), ('NZ', 'LYS', 'CG', 'ASP', 5.37), ('NZ', 'LYS', 'OD1', 'ASP', 4.89), ('NZ', 'LYS', 'OD2', 'ASP', 5.69)]]}
ASN_LYS = { 
	'distances':
		[[6.82, 5.93, 6.9, 7.05, 7.24], [6.76, 5.63, 6.17, 6.04, 6.45], [7.84, 6.58, 6.84, 6.63, 7.27], [5.86, 4.84, 5.22, 4.84, 5.13]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'LYS', 6.82), ('CB', 'ASN', 'CG', 'LYS', 5.93), ('CB', 'ASN', 'CD', 'LYS', 6.9), ('CB', 'ASN', 'CE', 'LYS', 7.05), ('CB', 'ASN', 'NZ', 'LYS', 7.24)], [('CG', 'ASN', 'CB', 'LYS', 6.76), ('CG', 'ASN', 'CG', 'LYS', 5.63), ('CG', 'ASN', 'CD', 'LYS', 6.17), ('CG', 'ASN', 'CE', 'LYS', 6.04), ('CG', 'ASN', 'NZ', 'LYS', 6.45)], [('OD1', 'ASN', 'CB', 'LYS', 7.84), ('OD1', 'ASN', 'CG', 'LYS', 6.58), ('OD1', 'ASN', 'CD', 'LYS', 6.84), ('OD1', 'ASN', 'CE', 'LYS', 6.63), ('OD1', 'ASN', 'NZ', 'LYS', 7.27)], [('ND2', 'ASN', 'CB', 'LYS', 5.86), ('ND2', 'ASN', 'CG', 'LYS', 4.84), ('ND2', 'ASN', 'CD', 'LYS', 5.22), ('ND2', 'ASN', 'CE', 'LYS', 4.84), ('ND2', 'ASN', 'NZ', 'LYS', 5.13)]]}
ASN_ASP = { 
	'distances':
		[[8.26, 7.98, 8.66, 7.43], [7.35, 6.83, 7.54, 6.11], [7.67, 7.09, 7.91, 6.14], [6.54, 5.87, 6.39, 5.34]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'ASP', 8.26), ('CB', 'ASN', 'CG', 'ASP', 7.98), ('CB', 'ASN', 'OD1', 'ASP', 8.66), ('CB', 'ASN', 'OD2', 'ASP', 7.43)], [('CG', 'ASN', 'CB', 'ASP', 7.35), ('CG', 'ASN', 'CG', 'ASP', 6.83), ('CG', 'ASN', 'OD1', 'ASP', 7.54), ('CG', 'ASN', 'OD2', 'ASP', 6.11)], [('OD1', 'ASN', 'CB', 'ASP', 7.67), ('OD1', 'ASN', 'CG', 'ASP', 7.09), ('OD1', 'ASN', 'OD1', 'ASP', 7.91), ('OD1', 'ASN', 'OD2', 'ASP', 6.14)], [('ND2', 'ASN', 'CB', 'ASP', 6.54), ('ND2', 'ASN', 'CG', 'ASP', 5.87), ('ND2', 'ASN', 'OD1', 'ASP', 6.39), ('ND2', 'ASN', 'OD2', 'ASP', 5.34)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LYS_ASP, d, 'A_1zrz_2_7_1_37')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASN_LYS, d, 'A_1zrz_2_7_1_37')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASN_ASP, d, 'A_1zrz_2_7_1_37')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'LYS_ASP' :  match1,
		'ASN_LYS' :  match2,
		'ASN_ASP' :  match3}