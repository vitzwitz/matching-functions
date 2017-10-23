'''
FUNC:M_1lws_3_6_3_14
PDB:1lws
EC:3.6.3.14
RESI:lys,lys,ca,ca
LOCI:a-301,403,501,502;
'''
import motifFunctions as cmd
CA_CA = { 
	'distances':
		[6.23, 6.23],
	'comparisons':
		[('CA', 'CA', 'CA', 'CA', 6.23), ('CA', 'CA', 'CA', 'CA', 6.23)]}
LYS_LYS = { 
	'distances':
		[[22.12, 21.92, 20.49, 20.31, 19.13], [21.44, 21.17, 19.71, 19.45, 18.2], [21.19, 20.98, 19.53, 19.17, 17.94], [20.53, 20.25, 18.78, 18.32, 17.04], [19.28, 18.95, 17.46, 17.05, 15.76], [22.12, 21.44, 21.19, 20.53, 19.28], [21.92, 21.17, 20.98, 20.25, 18.95], [20.49, 19.71, 19.53, 18.78, 17.46], [20.31, 19.45, 19.17, 18.32, 17.05], [19.13, 18.2, 17.94, 17.04, 15.76]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'LYS', 22.12), ('CB', 'LYS', 'CG', 'LYS', 21.92), ('CB', 'LYS', 'CD', 'LYS', 20.49), ('CB', 'LYS', 'CE', 'LYS', 20.31), ('CB', 'LYS', 'NZ', 'LYS', 19.13)], [('CG', 'LYS', 'CB', 'LYS', 21.44), ('CG', 'LYS', 'CG', 'LYS', 21.17), ('CG', 'LYS', 'CD', 'LYS', 19.71), ('CG', 'LYS', 'CE', 'LYS', 19.45), ('CG', 'LYS', 'NZ', 'LYS', 18.2)], [('CD', 'LYS', 'CB', 'LYS', 21.19), ('CD', 'LYS', 'CG', 'LYS', 20.98), ('CD', 'LYS', 'CD', 'LYS', 19.53), ('CD', 'LYS', 'CE', 'LYS', 19.17), ('CD', 'LYS', 'NZ', 'LYS', 17.94)], [('CE', 'LYS', 'CB', 'LYS', 20.53), ('CE', 'LYS', 'CG', 'LYS', 20.25), ('CE', 'LYS', 'CD', 'LYS', 18.78), ('CE', 'LYS', 'CE', 'LYS', 18.32), ('CE', 'LYS', 'NZ', 'LYS', 17.04)], [('NZ', 'LYS', 'CB', 'LYS', 19.28), ('NZ', 'LYS', 'CG', 'LYS', 18.95), ('NZ', 'LYS', 'CD', 'LYS', 17.46), ('NZ', 'LYS', 'CE', 'LYS', 17.05), ('NZ', 'LYS', 'NZ', 'LYS', 15.76)], [('CB', 'LYS', 'CB', 'LYS', 22.12), ('CB', 'LYS', 'CG', 'LYS', 21.44), ('CB', 'LYS', 'CD', 'LYS', 21.19), ('CB', 'LYS', 'CE', 'LYS', 20.53), ('CB', 'LYS', 'NZ', 'LYS', 19.28)], [('CG', 'LYS', 'CB', 'LYS', 21.92), ('CG', 'LYS', 'CG', 'LYS', 21.17), ('CG', 'LYS', 'CD', 'LYS', 20.98), ('CG', 'LYS', 'CE', 'LYS', 20.25), ('CG', 'LYS', 'NZ', 'LYS', 18.95)], [('CD', 'LYS', 'CB', 'LYS', 20.49), ('CD', 'LYS', 'CG', 'LYS', 19.71), ('CD', 'LYS', 'CD', 'LYS', 19.53), ('CD', 'LYS', 'CE', 'LYS', 18.78), ('CD', 'LYS', 'NZ', 'LYS', 17.46)], [('CE', 'LYS', 'CB', 'LYS', 20.31), ('CE', 'LYS', 'CG', 'LYS', 19.45), ('CE', 'LYS', 'CD', 'LYS', 19.17), ('CE', 'LYS', 'CE', 'LYS', 18.32), ('CE', 'LYS', 'NZ', 'LYS', 17.05)], [('NZ', 'LYS', 'CB', 'LYS', 19.13), ('NZ', 'LYS', 'CG', 'LYS', 18.2), ('NZ', 'LYS', 'CD', 'LYS', 17.94), ('NZ', 'LYS', 'CE', 'LYS', 17.04), ('NZ', 'LYS', 'NZ', 'LYS', 15.76)]]}
LYS_CA = { 
	'distances':
		[[15.48], [14.31], [13.72], [12.55], [11.52], [12.68], [11.3], [10.78], [9.38], [8.46], [12.02], [11.55], [10.18], [9.08], [7.81], [15.81], [15.21], [13.73], [12.84], [11.42]],
	'comparisons':
		[[('CB', 'LYS', 'CA', 'CA', 15.48)], [('CG', 'LYS', 'CA', 'CA', 14.31)], [('CD', 'LYS', 'CA', 'CA', 13.72)], [('CE', 'LYS', 'CA', 'CA', 12.55)], [('NZ', 'LYS', 'CA', 'CA', 11.52)], [('CB', 'LYS', 'CA', 'CA', 12.68)], [('CG', 'LYS', 'CA', 'CA', 11.3)], [('CD', 'LYS', 'CA', 'CA', 10.78)], [('CE', 'LYS', 'CA', 'CA', 9.38)], [('NZ', 'LYS', 'CA', 'CA', 8.46)], [('CB', 'LYS', 'CA', 'CA', 12.02)], [('CG', 'LYS', 'CA', 'CA', 11.55)], [('CD', 'LYS', 'CA', 'CA', 10.18)], [('CE', 'LYS', 'CA', 'CA', 9.08)], [('NZ', 'LYS', 'CA', 'CA', 7.81)], [('CB', 'LYS', 'CA', 'CA', 15.81)], [('CG', 'LYS', 'CA', 'CA', 15.21)], [('CD', 'LYS', 'CA', 'CA', 13.73)], [('CE', 'LYS', 'CA', 'CA', 12.84)], [('NZ', 'LYS', 'CA', 'CA', 11.42)]]}
CA_LYSI = { 
	'distances':
		[12.02, 11.55, 10.18, 9.08, 7.81, 15.81, 15.21, 13.73, 12.84, 11.42],
	'comparisons':
		[('CA', 'CA', 'CB', 'LYSI', 12.02), ('CA', 'CA', 'CG', 'LYSI', 11.55), ('CA', 'CA', 'CD', 'LYSI', 10.18), ('CA', 'CA', 'CE', 'LYSI', 9.08), ('CA', 'CA', 'NZ', 'LYSI', 7.81), ('CA', 'CA', 'CB', 'LYSI', 15.81), ('CA', 'CA', 'CG', 'LYSI', 15.21), ('CA', 'CA', 'CD', 'LYSI', 13.73), ('CA', 'CA', 'CE', 'LYSI', 12.84), ('CA', 'CA', 'NZ', 'LYSI', 11.42)]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(CA_CA, d, 'M_1lws_3_6_3_14')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(LYS_LYS, d, 'M_1lws_3_6_3_14')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(LYS_CA, d, 'M_1lws_3_6_3_14')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(CA_LYSI, d, 'M_1lws_3_6_3_14')
	if match4 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'CA_CA' :  match1,
		'LYS_LYS' :  match2,
		'LYS_CA' :  match3,
		'CA_LYSI' :  match4}