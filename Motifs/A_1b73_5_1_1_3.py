'''
FUNC:A_1b73_5_1_1_3
PDB:1b73
EC:5.1.1.3
RESI:asp,ser,cys,cys
LOCI:a-7,8,70,178;
'''
import motifFunctions as cmd
ASP_CYS = { 
	'distances':
		[[7.07, 8.18], [6.42, 7.39], [5.85, 6.46], [7.04, 8.09], [13.84, 12.84], [12.35, 11.4], [11.71, 10.81], [11.96, 11.04]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'CYS', 7.07), ('CB', 'ASP', 'SG', 'CYS', 8.18)], [('CG', 'ASP', 'CB', 'CYS', 6.42), ('CG', 'ASP', 'SG', 'CYS', 7.39)], [('OD1', 'ASP', 'CB', 'CYS', 5.85), ('OD1', 'ASP', 'SG', 'CYS', 6.46)], [('OD2', 'ASP', 'CB', 'CYS', 7.04), ('OD2', 'ASP', 'SG', 'CYS', 8.09)], [('CB', 'ASP', 'CB', 'CYS', 13.84), ('CB', 'ASP', 'SG', 'CYS', 12.84)], [('CG', 'ASP', 'CB', 'CYS', 12.35), ('CG', 'ASP', 'SG', 'CYS', 11.4)], [('OD1', 'ASP', 'CB', 'CYS', 11.71), ('OD1', 'ASP', 'SG', 'CYS', 10.81)], [('OD2', 'ASP', 'CB', 'CYS', 11.96), ('OD2', 'ASP', 'SG', 'CYS', 11.04)]]}
CYS_CYS = { 
	'distances':
		[[11.16, 9.78], [10.59, 9.37], [11.16, 10.59], [9.78, 9.37]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'CYS', 11.16), ('CB', 'CYS', 'SG', 'CYS', 9.78)], [('SG', 'CYS', 'CB', 'CYS', 10.59), ('SG', 'CYS', 'SG', 'CYS', 9.37)], [('CB', 'CYS', 'CB', 'CYS', 11.16), ('CB', 'CYS', 'SG', 'CYS', 10.59)], [('SG', 'CYS', 'CB', 'CYS', 9.78), ('SG', 'CYS', 'SG', 'CYS', 9.37)]]}
CYS_SER = { 
	'distances':
		[[7.33, 6.55], [6.64, 5.85], [12.88, 11.54], [12.25, 10.89]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'SER', 7.33), ('CB', 'CYS', 'OG', 'SER', 6.55)], [('SG', 'CYS', 'CB', 'SER', 6.64), ('SG', 'CYS', 'OG', 'SER', 5.85)], [('CB', 'CYS', 'CB', 'SER', 12.88), ('CB', 'CYS', 'OG', 'SER', 11.54)], [('SG', 'CYS', 'CB', 'SER', 12.25), ('SG', 'CYS', 'OG', 'SER', 10.89)]]}
ASP_SER = { 
	'distances':
		[[7.33, 7.03], [6.94, 6.26], [5.87, 5.06], [7.97, 7.14]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'SER', 7.33), ('CB', 'ASP', 'OG', 'SER', 7.03)], [('CG', 'ASP', 'CB', 'SER', 6.94), ('CG', 'ASP', 'OG', 'SER', 6.26)], [('OD1', 'ASP', 'CB', 'SER', 5.87), ('OD1', 'ASP', 'OG', 'SER', 5.06)], [('OD2', 'ASP', 'CB', 'SER', 7.97), ('OD2', 'ASP', 'OG', 'SER', 7.14)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_CYS, d, 'A_1b73_5_1_1_3')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(CYS_CYS, d, 'A_1b73_5_1_1_3')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(CYS_SER, d, 'A_1b73_5_1_1_3')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASP_SER, d, 'A_1b73_5_1_1_3')
	if match4 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_CYS' :  match1,
		'CYS_CYS' :  match2,
		'CYS_SER' :  match3,
		'ASP_SER' :  match4}