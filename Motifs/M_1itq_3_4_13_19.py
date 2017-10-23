'''
FUNC:M_1itq_3_4_13_19
PDB:1itq
EC:3.4.13.19
RESI:his,asp,zn,zn
LOCI:a-152,288,401,402;
'''
import motifFunctions as cmd
HIS_ASP = { 
	'distances':
		[[14.75, 13.4, 12.92, 12.94], [13.59, 12.19, 11.68, 11.73], [13.75, 12.29, 11.81, 11.75], [12.35, 10.96, 10.4, 10.58], [12.68, 11.19, 10.69, 10.67], [11.74, 10.28, 9.72, 9.85]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 14.75), ('CB', 'HIS', 'CG', 'ASP', 13.4), ('CB', 'HIS', 'OD1', 'ASP', 12.92), ('CB', 'HIS', 'OD2', 'ASP', 12.94)], [('CG', 'HIS', 'CB', 'ASP', 13.59), ('CG', 'HIS', 'CG', 'ASP', 12.19), ('CG', 'HIS', 'OD1', 'ASP', 11.68), ('CG', 'HIS', 'OD2', 'ASP', 11.73)], [('ND1', 'HIS', 'CB', 'ASP', 13.75), ('ND1', 'HIS', 'CG', 'ASP', 12.29), ('ND1', 'HIS', 'OD1', 'ASP', 11.81), ('ND1', 'HIS', 'OD2', 'ASP', 11.75)], [('CD2', 'HIS', 'CB', 'ASP', 12.35), ('CD2', 'HIS', 'CG', 'ASP', 10.96), ('CD2', 'HIS', 'OD1', 'ASP', 10.4), ('CD2', 'HIS', 'OD2', 'ASP', 10.58)], [('CE1', 'HIS', 'CB', 'ASP', 12.68), ('CE1', 'HIS', 'CG', 'ASP', 11.19), ('CE1', 'HIS', 'OD1', 'ASP', 10.69), ('CE1', 'HIS', 'OD2', 'ASP', 10.67)], [('NE2', 'HIS', 'CB', 'ASP', 11.74), ('NE2', 'HIS', 'CG', 'ASP', 10.28), ('NE2', 'HIS', 'OD1', 'ASP', 9.72), ('NE2', 'HIS', 'OD2', 'ASP', 9.85)]]}
ASP_ZNI = { 
	'distances':
		[[8.03], [6.77], [6.51], [6.38]],
	'comparisons':
		[[('CB', 'ASP', 'ZN', 'ZNI', 8.03)], [('CG', 'ASP', 'ZN', 'ZNI', 6.77)], [('OD1', 'ASP', 'ZN', 'ZNI', 6.51)], [('OD2', 'ASP', 'ZN', 'ZNI', 6.38)]]}
ZN_ASP = { 
	'distances':
		[8.19, 6.97, 5.94, 7.31, 8.03, 6.77, 6.51, 6.38],
	'comparisons':
		[('ZN', 'ZN', 'CB', 'ASP', 8.19), ('ZN', 'ZN', 'CG', 'ASP', 6.97), ('ZN', 'ZN', 'OD1', 'ASP', 5.94), ('ZN', 'ZN', 'OD2', 'ASP', 7.31), ('ZN', 'ZN', 'CB', 'ASP', 8.03), ('ZN', 'ZN', 'CG', 'ASP', 6.77), ('ZN', 'ZN', 'OD1', 'ASP', 6.51), ('ZN', 'ZN', 'OD2', 'ASP', 6.38)]}
ZN_ZN = { 
	'distances':
		[5.38, 5.38],
	'comparisons':
		[('ZN', 'ZN', 'ZN', 'ZN', 5.38), ('ZN', 'ZN', 'ZN', 'ZN', 5.38)]}
ZN_HIS = { 
	'distances':
		[9.85, 8.68, 9.02, 7.35, 8.07, 6.9, 8.76, 7.71, 8.1, 6.51, 7.31, 6.22],
	'comparisons':
		[('ZN', 'ZN', 'CB', 'HIS', 9.85), ('ZN', 'ZN', 'CG', 'HIS', 8.68), ('ZN', 'ZN', 'ND1', 'HIS', 9.02), ('ZN', 'ZN', 'CD2', 'HIS', 7.35), ('ZN', 'ZN', 'CE1', 'HIS', 8.07), ('ZN', 'ZN', 'NE2', 'HIS', 6.9), ('ZN', 'ZN', 'CB', 'HIS', 8.76), ('ZN', 'ZN', 'CG', 'HIS', 7.71), ('ZN', 'ZN', 'ND1', 'HIS', 8.1), ('ZN', 'ZN', 'CD2', 'HIS', 6.51), ('ZN', 'ZN', 'CE1', 'HIS', 7.31), ('ZN', 'ZN', 'NE2', 'HIS', 6.22)]}
HIS_ZNI = { 
	'distances':
		[[8.76], [7.71], [8.1], [6.51], [7.31], [6.22]],
	'comparisons':
		[[('CB', 'HIS', 'ZN', 'ZNI', 8.76)], [('CG', 'HIS', 'ZN', 'ZNI', 7.71)], [('ND1', 'HIS', 'ZN', 'ZNI', 8.1)], [('CD2', 'HIS', 'ZN', 'ZNI', 6.51)], [('CE1', 'HIS', 'ZN', 'ZNI', 7.31)], [('NE2', 'HIS', 'ZN', 'ZNI', 6.22)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_ASP, d, 'M_1itq_3_4_13_19')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_ZNI, d, 'M_1itq_3_4_13_19')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ZN_ASP, d, 'M_1itq_3_4_13_19')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ZN_ZN, d, 'M_1itq_3_4_13_19')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ZN_HIS, d, 'M_1itq_3_4_13_19')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(HIS_ZNI, d, 'M_1itq_3_4_13_19')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_ASP' :  match1,
		'ASP_ZNI' :  match2,
		'ZN_ASP' :  match3,
		'ZN_ZN' :  match4,
		'ZN_HIS' :  match5,
		'HIS_ZNI' :  match6}