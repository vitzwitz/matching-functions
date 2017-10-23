'''
FUNC:P_3lip_3_1_1_3
PDB:3lip
EC:3.1.1.3
RESI:ser,asp,his
LOCI:a-87,264,286;
'''
import motifFunctions as cmd
SER_HIS = { 
	'distances':
		[[8.99, 7.52, 7.05, 6.63, 5.83, 5.44], [8.45, 6.97, 6.61, 5.99, 5.37, 4.78]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'HIS', 8.99), ('CB', 'SER', 'CG', 'HIS', 7.52), ('CB', 'SER', 'ND1', 'HIS', 7.05), ('CB', 'SER', 'CD2', 'HIS', 6.63), ('CB', 'SER', 'CE1', 'HIS', 5.83), ('CB', 'SER', 'NE2', 'HIS', 5.44)], [('OG', 'SER', 'CB', 'HIS', 8.45), ('OG', 'SER', 'CG', 'HIS', 6.97), ('OG', 'SER', 'ND1', 'HIS', 6.61), ('OG', 'SER', 'CD2', 'HIS', 5.99), ('OG', 'SER', 'CE1', 'HIS', 5.37), ('OG', 'SER', 'NE2', 'HIS', 4.78)]]}
ASP_HIS = { 
	'distances':
		[[6.45, 7.14, 6.76, 8.46, 7.92, 8.85], [5.75, 6.07, 5.49, 7.31, 6.56, 7.54], [5.75, 6.02, 5.57, 7.14, 6.53, 7.38], [5.87, 5.82, 4.9, 6.97, 5.83, 6.97]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 6.45), ('CB', 'ASP', 'CG', 'HIS', 7.14), ('CB', 'ASP', 'ND1', 'HIS', 6.76), ('CB', 'ASP', 'CD2', 'HIS', 8.46), ('CB', 'ASP', 'CE1', 'HIS', 7.92), ('CB', 'ASP', 'NE2', 'HIS', 8.85)], [('CG', 'ASP', 'CB', 'HIS', 5.75), ('CG', 'ASP', 'CG', 'HIS', 6.07), ('CG', 'ASP', 'ND1', 'HIS', 5.49), ('CG', 'ASP', 'CD2', 'HIS', 7.31), ('CG', 'ASP', 'CE1', 'HIS', 6.56), ('CG', 'ASP', 'NE2', 'HIS', 7.54)], [('OD1', 'ASP', 'CB', 'HIS', 5.75), ('OD1', 'ASP', 'CG', 'HIS', 6.02), ('OD1', 'ASP', 'ND1', 'HIS', 5.57), ('OD1', 'ASP', 'CD2', 'HIS', 7.14), ('OD1', 'ASP', 'CE1', 'HIS', 6.53), ('OD1', 'ASP', 'NE2', 'HIS', 7.38)], [('OD2', 'ASP', 'CB', 'HIS', 5.87), ('OD2', 'ASP', 'CG', 'HIS', 5.82), ('OD2', 'ASP', 'ND1', 'HIS', 4.9), ('OD2', 'ASP', 'CD2', 'HIS', 6.97), ('OD2', 'ASP', 'CE1', 'HIS', 5.83), ('OD2', 'ASP', 'NE2', 'HIS', 6.97)]]}
SER_ASP = { 
	'distances':
		[[11.66, 10.31, 10.29, 9.41], [11.25, 9.83, 9.61, 9.09]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ASP', 11.66), ('CB', 'SER', 'CG', 'ASP', 10.31), ('CB', 'SER', 'OD1', 'ASP', 10.29), ('CB', 'SER', 'OD2', 'ASP', 9.41)], [('OG', 'SER', 'CB', 'ASP', 11.25), ('OG', 'SER', 'CG', 'ASP', 9.83), ('OG', 'SER', 'OD1', 'ASP', 9.61), ('OG', 'SER', 'OD2', 'ASP', 9.09)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(SER_HIS, d, 'P_3lip_3_1_1_3')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_HIS, d, 'P_3lip_3_1_1_3')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(SER_ASP, d, 'P_3lip_3_1_1_3')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'SER_HIS' :  match1,
		'ASP_HIS' :  match2,
		'SER_ASP' :  match3}