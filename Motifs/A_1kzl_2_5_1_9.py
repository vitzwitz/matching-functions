'''
FUNC:A_1kzl_2_5_1_9
PDB:1kzl
EC:2.5.1.9
RESI:ser,cys,his,ser,asp
LOCI:a-41,48,97,146,185;
'''
import motifFunctions as cmd
SER_SER = { 
	'distances':
		[[19.07, 19.94], [20.08, 20.9], [19.07, 20.08], [19.94, 20.9]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'SER', 19.07), ('CB', 'SER', 'OG', 'SER', 19.94)], [('OG', 'SER', 'CB', 'SER', 20.08), ('OG', 'SER', 'OG', 'SER', 20.9)], [('CB', 'SER', 'CB', 'SER', 19.07), ('CB', 'SER', 'OG', 'SER', 20.08)], [('OG', 'SER', 'CB', 'SER', 19.94), ('OG', 'SER', 'OG', 'SER', 20.9)]]}
HIS_ASP = { 
	'distances':
		[[8.32, 7.36, 7.19, 7.16], [7.64, 6.99, 7.07, 6.85], [8.36, 7.97, 8.05, 7.97], [6.62, 6.13, 6.51, 5.92], [7.96, 7.86, 8.15, 7.9], [6.88, 6.81, 7.29, 6.76]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 8.32), ('CB', 'HIS', 'CG', 'ASP', 7.36), ('CB', 'HIS', 'OD1', 'ASP', 7.19), ('CB', 'HIS', 'OD2', 'ASP', 7.16)], [('CG', 'HIS', 'CB', 'ASP', 7.64), ('CG', 'HIS', 'CG', 'ASP', 6.99), ('CG', 'HIS', 'OD1', 'ASP', 7.07), ('CG', 'HIS', 'OD2', 'ASP', 6.85)], [('ND1', 'HIS', 'CB', 'ASP', 8.36), ('ND1', 'HIS', 'CG', 'ASP', 7.97), ('ND1', 'HIS', 'OD1', 'ASP', 8.05), ('ND1', 'HIS', 'OD2', 'ASP', 7.97)], [('CD2', 'HIS', 'CB', 'ASP', 6.62), ('CD2', 'HIS', 'CG', 'ASP', 6.13), ('CD2', 'HIS', 'OD1', 'ASP', 6.51), ('CD2', 'HIS', 'OD2', 'ASP', 5.92)], [('CE1', 'HIS', 'CB', 'ASP', 7.96), ('CE1', 'HIS', 'CG', 'ASP', 7.86), ('CE1', 'HIS', 'OD1', 'ASP', 8.15), ('CE1', 'HIS', 'OD2', 'ASP', 7.9)], [('NE2', 'HIS', 'CB', 'ASP', 6.88), ('NE2', 'HIS', 'CG', 'ASP', 6.81), ('NE2', 'HIS', 'OD1', 'ASP', 7.29), ('NE2', 'HIS', 'OD2', 'ASP', 6.76)]]}
ASP_SERI = { 
	'distances':
		[[11.52, 10.7], [11.35, 10.45], [11.37, 10.32], [11.46, 10.66]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'SERI', 11.52), ('CB', 'ASP', 'OG', 'SERI', 10.7)], [('CG', 'ASP', 'CB', 'SERI', 11.35), ('CG', 'ASP', 'OG', 'SERI', 10.45)], [('OD1', 'ASP', 'CB', 'SERI', 11.37), ('OD1', 'ASP', 'OG', 'SERI', 10.32)], [('OD2', 'ASP', 'CB', 'SERI', 11.46), ('OD2', 'ASP', 'OG', 'SERI', 10.66)]]}
SER_CYS = { 
	'distances':
		[[7.32, 5.7], [7.48, 5.7], [16.84, 17.85], [17.68, 18.68]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'CYS', 7.32), ('CB', 'SER', 'SG', 'CYS', 5.7)], [('OG', 'SER', 'CB', 'CYS', 7.48), ('OG', 'SER', 'SG', 'CYS', 5.7)], [('CB', 'SER', 'CB', 'CYS', 16.84), ('CB', 'SER', 'SG', 'CYS', 17.85)], [('OG', 'SER', 'CB', 'CYS', 17.68), ('OG', 'SER', 'SG', 'CYS', 18.68)]]}
CYS_ASP = { 
	'distances':
		[[17.86, 17.95, 19.0, 17.06], [19.01, 18.97, 19.99, 18.02]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'ASP', 17.86), ('CB', 'CYS', 'CG', 'ASP', 17.95), ('CB', 'CYS', 'OD1', 'ASP', 19.0), ('CB', 'CYS', 'OD2', 'ASP', 17.06)], [('SG', 'CYS', 'CB', 'ASP', 19.01), ('SG', 'CYS', 'CG', 'ASP', 18.97), ('SG', 'CYS', 'OD1', 'ASP', 19.99), ('SG', 'CYS', 'OD2', 'ASP', 18.02)]]}
SER_HIS = { 
	'distances':
		[[19.12, 18.67, 18.7, 18.38, 18.46, 18.26], [19.84, 19.39, 19.5, 19.03, 19.24, 18.94], [7.57, 6.87, 5.55, 7.64, 5.75, 7.06], [6.67, 6.12, 4.88, 7.03, 5.37, 6.65]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'HIS', 19.12), ('CB', 'SER', 'CG', 'HIS', 18.67), ('CB', 'SER', 'ND1', 'HIS', 18.7), ('CB', 'SER', 'CD2', 'HIS', 18.38), ('CB', 'SER', 'CE1', 'HIS', 18.46), ('CB', 'SER', 'NE2', 'HIS', 18.26)], [('OG', 'SER', 'CB', 'HIS', 19.84), ('OG', 'SER', 'CG', 'HIS', 19.39), ('OG', 'SER', 'ND1', 'HIS', 19.5), ('OG', 'SER', 'CD2', 'HIS', 19.03), ('OG', 'SER', 'CE1', 'HIS', 19.24), ('OG', 'SER', 'NE2', 'HIS', 18.94)], [('CB', 'SER', 'CB', 'HIS', 7.57), ('CB', 'SER', 'CG', 'HIS', 6.87), ('CB', 'SER', 'ND1', 'HIS', 5.55), ('CB', 'SER', 'CD2', 'HIS', 7.64), ('CB', 'SER', 'CE1', 'HIS', 5.75), ('CB', 'SER', 'NE2', 'HIS', 7.06)], [('OG', 'SER', 'CB', 'HIS', 6.67), ('OG', 'SER', 'CG', 'HIS', 6.12), ('OG', 'SER', 'ND1', 'HIS', 4.88), ('OG', 'SER', 'CD2', 'HIS', 7.03), ('OG', 'SER', 'CE1', 'HIS', 5.37), ('OG', 'SER', 'NE2', 'HIS', 6.65)]]}
CYS_HIS = { 
	'distances':
		[[17.07, 16.24, 16.2, 15.61, 15.6, 15.21], [17.85, 17.16, 17.19, 16.61, 16.71, 16.34]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'HIS', 17.07), ('CB', 'CYS', 'CG', 'HIS', 16.24), ('CB', 'CYS', 'ND1', 'HIS', 16.2), ('CB', 'CYS', 'CD2', 'HIS', 15.61), ('CB', 'CYS', 'CE1', 'HIS', 15.6), ('CB', 'CYS', 'NE2', 'HIS', 15.21)], [('SG', 'CYS', 'CB', 'HIS', 17.85), ('SG', 'CYS', 'CG', 'HIS', 17.16), ('SG', 'CYS', 'ND1', 'HIS', 17.19), ('SG', 'CYS', 'CD2', 'HIS', 16.61), ('SG', 'CYS', 'CE1', 'HIS', 16.71), ('SG', 'CYS', 'NE2', 'HIS', 16.34)]]}
SER_ASP = { 
	'distances':
		[[21.35, 21.09, 21.98, 20.08], [21.75, 21.5, 22.43, 20.46], [11.52, 11.35, 11.37, 11.46], [10.7, 10.45, 10.32, 10.66]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ASP', 21.35), ('CB', 'SER', 'CG', 'ASP', 21.09), ('CB', 'SER', 'OD1', 'ASP', 21.98), ('CB', 'SER', 'OD2', 'ASP', 20.08)], [('OG', 'SER', 'CB', 'ASP', 21.75), ('OG', 'SER', 'CG', 'ASP', 21.5), ('OG', 'SER', 'OD1', 'ASP', 22.43), ('OG', 'SER', 'OD2', 'ASP', 20.46)], [('CB', 'SER', 'CB', 'ASP', 11.52), ('CB', 'SER', 'CG', 'ASP', 11.35), ('CB', 'SER', 'OD1', 'ASP', 11.37), ('CB', 'SER', 'OD2', 'ASP', 11.46)], [('OG', 'SER', 'CB', 'ASP', 10.7), ('OG', 'SER', 'CG', 'ASP', 10.45), ('OG', 'SER', 'OD1', 'ASP', 10.32), ('OG', 'SER', 'OD2', 'ASP', 10.66)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(SER_SER, d, 'A_1kzl_2_5_1_9')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_ASP, d, 'A_1kzl_2_5_1_9')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_SERI, d, 'A_1kzl_2_5_1_9')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(SER_CYS, d, 'A_1kzl_2_5_1_9')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(CYS_ASP, d, 'A_1kzl_2_5_1_9')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(SER_HIS, d, 'A_1kzl_2_5_1_9')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(CYS_HIS, d, 'A_1kzl_2_5_1_9')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(SER_ASP, d, 'A_1kzl_2_5_1_9')
	if match8 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'SER_SER' :  match1,
		'HIS_ASP' :  match2,
		'ASP_SERI' :  match3,
		'SER_CYS' :  match4,
		'CYS_ASP' :  match5,
		'SER_HIS' :  match6,
		'CYS_HIS' :  match7,
		'SER_ASP' :  match8}