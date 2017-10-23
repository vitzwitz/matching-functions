'''
FUNC:A_1tyf_3_4_21_92
PDB:1tyf
EC:3.4.21.92
RESI:gly,ser,met,his,asp
LOCI:a-68,97,98,122,171;
'''
import motifFunctions as cmd
ASP_MET = { 
	'distances':
		[[15.72, 17.14, 17.45, 17.7, 16.48, 15.48, 14.89, 13.48], [14.9, 16.33, 16.73, 16.9, 15.96, 14.9, 14.21, 12.77], [13.99, 15.4, 15.74, 15.83, 15.18, 14.13, 13.34, 11.92], [15.29, 16.75, 17.29, 17.46, 16.47, 15.36, 14.69, 13.24]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'MET', 15.72), ('CB', 'ASP', 'CG', 'MET', 17.14), ('CB', 'ASP', 'SD', 'MET', 17.45), ('CB', 'ASP', 'CE', 'MET', 17.7), ('CB', 'ASP', 'O', 'MET', 16.48), ('CB', 'ASP', 'C', 'MET', 15.48), ('CB', 'ASP', 'CA', 'MET', 14.89), ('CB', 'ASP', 'N', 'MET', 13.48)], [('CG', 'ASP', 'CB', 'MET', 14.9), ('CG', 'ASP', 'CG', 'MET', 16.33), ('CG', 'ASP', 'SD', 'MET', 16.73), ('CG', 'ASP', 'CE', 'MET', 16.9), ('CG', 'ASP', 'O', 'MET', 15.96), ('CG', 'ASP', 'C', 'MET', 14.9), ('CG', 'ASP', 'CA', 'MET', 14.21), ('CG', 'ASP', 'N', 'MET', 12.77)], [('OD1', 'ASP', 'CB', 'MET', 13.99), ('OD1', 'ASP', 'CG', 'MET', 15.4), ('OD1', 'ASP', 'SD', 'MET', 15.74), ('OD1', 'ASP', 'CE', 'MET', 15.83), ('OD1', 'ASP', 'O', 'MET', 15.18), ('OD1', 'ASP', 'C', 'MET', 14.13), ('OD1', 'ASP', 'CA', 'MET', 13.34), ('OD1', 'ASP', 'N', 'MET', 11.92)], [('OD2', 'ASP', 'CB', 'MET', 15.29), ('OD2', 'ASP', 'CG', 'MET', 16.75), ('OD2', 'ASP', 'SD', 'MET', 17.29), ('OD2', 'ASP', 'CE', 'MET', 17.46), ('OD2', 'ASP', 'O', 'MET', 16.47), ('OD2', 'ASP', 'C', 'MET', 15.36), ('OD2', 'ASP', 'CA', 'MET', 14.69), ('OD2', 'ASP', 'N', 'MET', 13.24)]]}
HIS_MET = { 
	'distances':
		[[12.2, 13.47, 13.49, 13.53, 13.26, 12.33, 11.43, 10.14], [11.13, 12.44, 12.63, 12.63, 12.5, 11.49, 10.5, 9.18], [11.46, 12.85, 13.25, 13.25, 13.02, 11.92, 10.97, 9.58], [9.92, 11.2, 11.37, 11.31, 11.49, 10.48, 9.38, 8.11], [10.58, 11.97, 12.51, 12.45, 12.43, 11.28, 10.26, 8.9], [9.56, 10.89, 11.31, 11.21, 11.46, 10.36, 9.23, 7.94]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'MET', 12.2), ('CB', 'HIS', 'CG', 'MET', 13.47), ('CB', 'HIS', 'SD', 'MET', 13.49), ('CB', 'HIS', 'CE', 'MET', 13.53), ('CB', 'HIS', 'O', 'MET', 13.26), ('CB', 'HIS', 'C', 'MET', 12.33), ('CB', 'HIS', 'CA', 'MET', 11.43), ('CB', 'HIS', 'N', 'MET', 10.14)], [('CG', 'HIS', 'CB', 'MET', 11.13), ('CG', 'HIS', 'CG', 'MET', 12.44), ('CG', 'HIS', 'SD', 'MET', 12.63), ('CG', 'HIS', 'CE', 'MET', 12.63), ('CG', 'HIS', 'O', 'MET', 12.5), ('CG', 'HIS', 'C', 'MET', 11.49), ('CG', 'HIS', 'CA', 'MET', 10.5), ('CG', 'HIS', 'N', 'MET', 9.18)], [('ND1', 'HIS', 'CB', 'MET', 11.46), ('ND1', 'HIS', 'CG', 'MET', 12.85), ('ND1', 'HIS', 'SD', 'MET', 13.25), ('ND1', 'HIS', 'CE', 'MET', 13.25), ('ND1', 'HIS', 'O', 'MET', 13.02), ('ND1', 'HIS', 'C', 'MET', 11.92), ('ND1', 'HIS', 'CA', 'MET', 10.97), ('ND1', 'HIS', 'N', 'MET', 9.58)], [('CD2', 'HIS', 'CB', 'MET', 9.92), ('CD2', 'HIS', 'CG', 'MET', 11.2), ('CD2', 'HIS', 'SD', 'MET', 11.37), ('CD2', 'HIS', 'CE', 'MET', 11.31), ('CD2', 'HIS', 'O', 'MET', 11.49), ('CD2', 'HIS', 'C', 'MET', 10.48), ('CD2', 'HIS', 'CA', 'MET', 9.38), ('CD2', 'HIS', 'N', 'MET', 8.11)], [('CE1', 'HIS', 'CB', 'MET', 10.58), ('CE1', 'HIS', 'CG', 'MET', 11.97), ('CE1', 'HIS', 'SD', 'MET', 12.51), ('CE1', 'HIS', 'CE', 'MET', 12.45), ('CE1', 'HIS', 'O', 'MET', 12.43), ('CE1', 'HIS', 'C', 'MET', 11.28), ('CE1', 'HIS', 'CA', 'MET', 10.26), ('CE1', 'HIS', 'N', 'MET', 8.9)], [('NE2', 'HIS', 'CB', 'MET', 9.56), ('NE2', 'HIS', 'CG', 'MET', 10.89), ('NE2', 'HIS', 'SD', 'MET', 11.31), ('NE2', 'HIS', 'CE', 'MET', 11.21), ('NE2', 'HIS', 'O', 'MET', 11.46), ('NE2', 'HIS', 'C', 'MET', 10.36), ('NE2', 'HIS', 'CA', 'MET', 9.23), ('NE2', 'HIS', 'N', 'MET', 7.94)]]}
ASP_HIS = { 
	'distances':
		[[6.64, 7.33, 7.01, 8.66, 8.21, 9.09], [6.13, 6.46, 5.85, 7.75, 6.96, 7.98], [5.01, 5.28, 4.76, 6.59, 5.97, 6.89], [7.17, 7.24, 6.35, 8.44, 7.25, 8.42]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 6.64), ('CB', 'ASP', 'CG', 'HIS', 7.33), ('CB', 'ASP', 'ND1', 'HIS', 7.01), ('CB', 'ASP', 'CD2', 'HIS', 8.66), ('CB', 'ASP', 'CE1', 'HIS', 8.21), ('CB', 'ASP', 'NE2', 'HIS', 9.09)], [('CG', 'ASP', 'CB', 'HIS', 6.13), ('CG', 'ASP', 'CG', 'HIS', 6.46), ('CG', 'ASP', 'ND1', 'HIS', 5.85), ('CG', 'ASP', 'CD2', 'HIS', 7.75), ('CG', 'ASP', 'CE1', 'HIS', 6.96), ('CG', 'ASP', 'NE2', 'HIS', 7.98)], [('OD1', 'ASP', 'CB', 'HIS', 5.01), ('OD1', 'ASP', 'CG', 'HIS', 5.28), ('OD1', 'ASP', 'ND1', 'HIS', 4.76), ('OD1', 'ASP', 'CD2', 'HIS', 6.59), ('OD1', 'ASP', 'CE1', 'HIS', 5.97), ('OD1', 'ASP', 'NE2', 'HIS', 6.89)], [('OD2', 'ASP', 'CB', 'HIS', 7.17), ('OD2', 'ASP', 'CG', 'HIS', 7.24), ('OD2', 'ASP', 'ND1', 'HIS', 6.35), ('OD2', 'ASP', 'CD2', 'HIS', 8.44), ('OD2', 'ASP', 'CE1', 'HIS', 7.25), ('OD2', 'ASP', 'NE2', 'HIS', 8.42)]]}
SER_MET = { 
	'distances':
		[[6.69, 8.16, 8.84, 9.3, 8.11, 6.94, 6.09, 4.65], [7.99, 9.47, 10.11, 10.47, 9.43, 8.26, 7.44, 6.0]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'MET', 6.69), ('CB', 'SER', 'CG', 'MET', 8.16), ('CB', 'SER', 'SD', 'MET', 8.84), ('CB', 'SER', 'CE', 'MET', 9.3), ('CB', 'SER', 'O', 'MET', 8.11), ('CB', 'SER', 'C', 'MET', 6.94), ('CB', 'SER', 'CA', 'MET', 6.09), ('CB', 'SER', 'N', 'MET', 4.65)], [('OG', 'SER', 'CB', 'MET', 7.99), ('OG', 'SER', 'CG', 'MET', 9.47), ('OG', 'SER', 'SD', 'MET', 10.11), ('OG', 'SER', 'CE', 'MET', 10.47), ('OG', 'SER', 'O', 'MET', 9.43), ('OG', 'SER', 'C', 'MET', 8.26), ('OG', 'SER', 'CA', 'MET', 7.44), ('OG', 'SER', 'N', 'MET', 6.0)]]}
ASP_SER = { 
	'distances':
		[[11.07, 9.83], [10.25, 8.94], [9.42, 8.12], [10.64, 9.3]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'SER', 11.07), ('CB', 'ASP', 'OG', 'SER', 9.83)], [('CG', 'ASP', 'CB', 'SER', 10.25), ('CG', 'ASP', 'OG', 'SER', 8.94)], [('OD1', 'ASP', 'CB', 'SER', 9.42), ('OD1', 'ASP', 'OG', 'SER', 8.12)], [('OD2', 'ASP', 'CB', 'SER', 10.64), ('OD2', 'ASP', 'OG', 'SER', 9.3)]]}
SER_GLY = { 
	'distances':
		[[8.08, 8.74, 8.35, 7.03], [8.81, 9.49, 9.07, 7.83]],
	'comparisons':
		[[('CB', 'SER', 'O', 'GLY', 8.08), ('CB', 'SER', 'C', 'GLY', 8.74), ('CB', 'SER', 'CA', 'GLY', 8.35), ('CB', 'SER', 'N', 'GLY', 7.03)], [('OG', 'SER', 'O', 'GLY', 8.81), ('OG', 'SER', 'C', 'GLY', 9.49), ('OG', 'SER', 'CA', 'GLY', 9.07), ('OG', 'SER', 'N', 'GLY', 7.83)]]}
HIS_GLY = { 
	'distances':
		[[12.78, 13.72, 13.63, 12.57], [11.4, 12.31, 12.2, 11.19], [11.32, 12.14, 11.91, 10.95], [10.18, 11.14, 11.13, 10.14], [10.1, 10.89, 10.66, 9.77], [9.28, 10.18, 10.1, 9.18]],
	'comparisons':
		[[('CB', 'HIS', 'O', 'GLY', 12.78), ('CB', 'HIS', 'C', 'GLY', 13.72), ('CB', 'HIS', 'CA', 'GLY', 13.63), ('CB', 'HIS', 'N', 'GLY', 12.57)], [('CG', 'HIS', 'O', 'GLY', 11.4), ('CG', 'HIS', 'C', 'GLY', 12.31), ('CG', 'HIS', 'CA', 'GLY', 12.2), ('CG', 'HIS', 'N', 'GLY', 11.19)], [('ND1', 'HIS', 'O', 'GLY', 11.32), ('ND1', 'HIS', 'C', 'GLY', 12.14), ('ND1', 'HIS', 'CA', 'GLY', 11.91), ('ND1', 'HIS', 'N', 'GLY', 10.95)], [('CD2', 'HIS', 'O', 'GLY', 10.18), ('CD2', 'HIS', 'C', 'GLY', 11.14), ('CD2', 'HIS', 'CA', 'GLY', 11.13), ('CD2', 'HIS', 'N', 'GLY', 10.14)], [('CE1', 'HIS', 'O', 'GLY', 10.1), ('CE1', 'HIS', 'C', 'GLY', 10.89), ('CE1', 'HIS', 'CA', 'GLY', 10.66), ('CE1', 'HIS', 'N', 'GLY', 9.77)], [('NE2', 'HIS', 'O', 'GLY', 9.28), ('NE2', 'HIS', 'C', 'GLY', 10.18), ('NE2', 'HIS', 'CA', 'GLY', 10.1), ('NE2', 'HIS', 'N', 'GLY', 9.18)]]}
ASP_GLY = { 
	'distances':
		[[16.17, 16.89, 16.44, 15.35], [14.99, 15.7, 15.27, 14.26], [14.04, 14.82, 14.49, 13.49], [15.13, 15.75, 15.24, 14.29]],
	'comparisons':
		[[('CB', 'ASP', 'O', 'GLY', 16.17), ('CB', 'ASP', 'C', 'GLY', 16.89), ('CB', 'ASP', 'CA', 'GLY', 16.44), ('CB', 'ASP', 'N', 'GLY', 15.35)], [('CG', 'ASP', 'O', 'GLY', 14.99), ('CG', 'ASP', 'C', 'GLY', 15.7), ('CG', 'ASP', 'CA', 'GLY', 15.27), ('CG', 'ASP', 'N', 'GLY', 14.26)], [('OD1', 'ASP', 'O', 'GLY', 14.04), ('OD1', 'ASP', 'C', 'GLY', 14.82), ('OD1', 'ASP', 'CA', 'GLY', 14.49), ('OD1', 'ASP', 'N', 'GLY', 13.49)], [('OD2', 'ASP', 'O', 'GLY', 15.13), ('OD2', 'ASP', 'C', 'GLY', 15.75), ('OD2', 'ASP', 'CA', 'GLY', 15.24), ('OD2', 'ASP', 'N', 'GLY', 14.29)]]}
MET_GLY = { 
	'distances':
		[[6.37, 6.76, 6.82, 5.91], [6.86, 7.15, 7.45, 6.87], [8.07, 8.59, 9.1, 8.52], [7.55, 8.22, 9.07, 8.73], [9.64, 9.87, 9.67, 8.61], [8.79, 9.06, 8.75, 7.59], [7.65, 8.12, 8.04, 6.91], [7.64, 8.2, 7.97, 6.68]],
	'comparisons':
		[[('CB', 'MET', 'O', 'GLY', 6.37), ('CB', 'MET', 'C', 'GLY', 6.76), ('CB', 'MET', 'CA', 'GLY', 6.82), ('CB', 'MET', 'N', 'GLY', 5.91)], [('CG', 'MET', 'O', 'GLY', 6.86), ('CG', 'MET', 'C', 'GLY', 7.15), ('CG', 'MET', 'CA', 'GLY', 7.45), ('CG', 'MET', 'N', 'GLY', 6.87)], [('SD', 'MET', 'O', 'GLY', 8.07), ('SD', 'MET', 'C', 'GLY', 8.59), ('SD', 'MET', 'CA', 'GLY', 9.1), ('SD', 'MET', 'N', 'GLY', 8.52)], [('CE', 'MET', 'O', 'GLY', 7.55), ('CE', 'MET', 'C', 'GLY', 8.22), ('CE', 'MET', 'CA', 'GLY', 9.07), ('CE', 'MET', 'N', 'GLY', 8.73)], [('O', 'MET', 'O', 'GLY', 9.64), ('O', 'MET', 'C', 'GLY', 9.87), ('O', 'MET', 'CA', 'GLY', 9.67), ('O', 'MET', 'N', 'GLY', 8.61)], [('C', 'MET', 'O', 'GLY', 8.79), ('C', 'MET', 'C', 'GLY', 9.06), ('C', 'MET', 'CA', 'GLY', 8.75), ('C', 'MET', 'N', 'GLY', 7.59)], [('CA', 'MET', 'O', 'GLY', 7.65), ('CA', 'MET', 'C', 'GLY', 8.12), ('CA', 'MET', 'CA', 'GLY', 8.04), ('CA', 'MET', 'N', 'GLY', 6.91)], [('N', 'MET', 'O', 'GLY', 7.64), ('N', 'MET', 'C', 'GLY', 8.2), ('N', 'MET', 'CA', 'GLY', 7.97), ('N', 'MET', 'N', 'GLY', 6.68)]]}
HIS_SER = { 
	'distances':
		[[8.01, 7.0], [6.89, 5.8], [7.06, 5.79], [5.97, 5.1], [6.37, 5.15], [5.6, 4.63]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'SER', 8.01), ('CB', 'HIS', 'OG', 'SER', 7.0)], [('CG', 'HIS', 'CB', 'SER', 6.89), ('CG', 'HIS', 'OG', 'SER', 5.8)], [('ND1', 'HIS', 'CB', 'SER', 7.06), ('ND1', 'HIS', 'OG', 'SER', 5.79)], [('CD2', 'HIS', 'CB', 'SER', 5.97), ('CD2', 'HIS', 'OG', 'SER', 5.1)], [('CE1', 'HIS', 'CB', 'SER', 6.37), ('CE1', 'HIS', 'OG', 'SER', 5.15)], [('NE2', 'HIS', 'CB', 'SER', 5.6), ('NE2', 'HIS', 'OG', 'SER', 4.63)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_MET, d, 'A_1tyf_3_4_21_92')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_MET, d, 'A_1tyf_3_4_21_92')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_HIS, d, 'A_1tyf_3_4_21_92')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(SER_MET, d, 'A_1tyf_3_4_21_92')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ASP_SER, d, 'A_1tyf_3_4_21_92')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(SER_GLY, d, 'A_1tyf_3_4_21_92')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(HIS_GLY, d, 'A_1tyf_3_4_21_92')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(ASP_GLY, d, 'A_1tyf_3_4_21_92')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(MET_GLY, d, 'A_1tyf_3_4_21_92')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(HIS_SER, d, 'A_1tyf_3_4_21_92')
	if match10 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_MET' :  match1,
		'HIS_MET' :  match2,
		'ASP_HIS' :  match3,
		'SER_MET' :  match4,
		'ASP_SER' :  match5,
		'SER_GLY' :  match6,
		'HIS_GLY' :  match7,
		'ASP_GLY' :  match8,
		'MET_GLY' :  match9,
		'HIS_SER' :  match10}