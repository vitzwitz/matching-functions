'''
FUNC:A_1h7o_4_2_1_24
PDB:1h7o
EC:4.2.1.24
RESI:asp,ser,lys,lys
LOCI:a-131,179,210,263;
'''
import motifFunctions as cmd
LYS_ASP = { 
	'distances':
		[[13.35, 12.05, 10.99, 12.24], [12.78, 11.44, 10.43, 11.56], [11.54, 10.15, 9.22, 10.17], [11.9, 10.44, 9.67, 10.26], [10.82, 9.35, 8.72, 9.05], [13.08, 12.15, 10.96, 12.72], [12.7, 11.72, 10.61, 12.2], [11.25, 10.22, 9.13, 10.68], [10.68, 10.68, 10.68, 10.68], [10.68, 10.68, 10.68, 10.68]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'ASP', 13.35), ('CB', 'LYS', 'CG', 'ASP', 12.05), ('CB', 'LYS', 'OD1', 'ASP', 10.99), ('CB', 'LYS', 'OD2', 'ASP', 12.24)], [('CG', 'LYS', 'CB', 'ASP', 12.78), ('CG', 'LYS', 'CG', 'ASP', 11.44), ('CG', 'LYS', 'OD1', 'ASP', 10.43), ('CG', 'LYS', 'OD2', 'ASP', 11.56)], [('CD', 'LYS', 'CB', 'ASP', 11.54), ('CD', 'LYS', 'CG', 'ASP', 10.15), ('CD', 'LYS', 'OD1', 'ASP', 9.22), ('CD', 'LYS', 'OD2', 'ASP', 10.17)], [('CE', 'LYS', 'CB', 'ASP', 11.9), ('CE', 'LYS', 'CG', 'ASP', 10.44), ('CE', 'LYS', 'OD1', 'ASP', 9.67), ('CE', 'LYS', 'OD2', 'ASP', 10.26)], [('NZ', 'LYS', 'CB', 'ASP', 10.82), ('NZ', 'LYS', 'CG', 'ASP', 9.35), ('NZ', 'LYS', 'OD1', 'ASP', 8.72), ('NZ', 'LYS', 'OD2', 'ASP', 9.05)], [('CB', 'LYS', 'CB', 'ASP', 13.08), ('CB', 'LYS', 'CG', 'ASP', 12.15), ('CB', 'LYS', 'OD1', 'ASP', 10.96), ('CB', 'LYS', 'OD2', 'ASP', 12.72)], [('CG', 'LYS', 'CB', 'ASP', 12.7), ('CG', 'LYS', 'CG', 'ASP', 11.72), ('CG', 'LYS', 'OD1', 'ASP', 10.61), ('CG', 'LYS', 'OD2', 'ASP', 12.2)], [('CD', 'LYS', 'CB', 'ASP', 11.25), ('CD', 'LYS', 'CG', 'ASP', 10.22), ('CD', 'LYS', 'OD1', 'ASP', 9.13), ('CD', 'LYS', 'OD2', 'ASP', 10.68)], [('CE', 'LYS', 'CB', 'ASP', 10.68), ('CE', 'LYS', 'CG', 'ASP', 10.68), ('CE', 'LYS', 'OD1', 'ASP', 10.68), ('CE', 'LYS', 'OD2', 'ASP', 10.68)], [('NZ', 'LYS', 'CB', 'ASP', 10.68), ('NZ', 'LYS', 'CG', 'ASP', 10.68), ('NZ', 'LYS', 'OD1', 'ASP', 10.68), ('NZ', 'LYS', 'OD2', 'ASP', 10.68)]]}
ASP_LYSI = { 
	'distances':
		[[13.08, 12.7, 11.25, 11.25, 11.25], [12.15, 11.72, 10.22, 10.22, 10.22], [10.96, 10.61, 9.13, 9.13, 9.13], [12.72, 12.2, 10.68, 10.68, 10.68]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'LYSI', 13.08), ('CB', 'ASP', 'CG', 'LYSI', 12.7), ('CB', 'ASP', 'CD', 'LYSI', 11.25), ('CB', 'ASP', 'CE', 'LYSI', 11.25), ('CB', 'ASP', 'NZ', 'LYSI', 11.25)], [('CG', 'ASP', 'CB', 'LYSI', 12.15), ('CG', 'ASP', 'CG', 'LYSI', 11.72), ('CG', 'ASP', 'CD', 'LYSI', 10.22), ('CG', 'ASP', 'CE', 'LYSI', 10.22), ('CG', 'ASP', 'NZ', 'LYSI', 10.22)], [('OD1', 'ASP', 'CB', 'LYSI', 10.96), ('OD1', 'ASP', 'CG', 'LYSI', 10.61), ('OD1', 'ASP', 'CD', 'LYSI', 9.13), ('OD1', 'ASP', 'CE', 'LYSI', 9.13), ('OD1', 'ASP', 'NZ', 'LYSI', 9.13)], [('OD2', 'ASP', 'CB', 'LYSI', 12.72), ('OD2', 'ASP', 'CG', 'LYSI', 12.2), ('OD2', 'ASP', 'CD', 'LYSI', 10.68), ('OD2', 'ASP', 'CE', 'LYSI', 10.68), ('OD2', 'ASP', 'NZ', 'LYSI', 10.68)]]}
LYS_LYS = { 
	'distances':
		[[6.51, 6.85, 6.72, 6.72, 6.72], [6.31, 6.15, 5.83, 5.83, 5.83], [7.17, 6.85, 6.03, 6.03, 6.03], [8.21, 7.59, 6.76, 6.76, 6.76], [8.98, 8.21, 7.1, 7.1, 7.1], [6.51, 6.31, 7.17, 8.21, 8.98], [6.85, 6.15, 6.85, 7.59, 8.21], [6.72, 5.83, 6.03, 6.76, 7.1], [7.1, 7.1, 7.1, 7.1, 7.1], [7.1, 7.1, 7.1, 7.1, 7.1]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'LYS', 6.51), ('CB', 'LYS', 'CG', 'LYS', 6.85), ('CB', 'LYS', 'CD', 'LYS', 6.72), ('CB', 'LYS', 'CE', 'LYS', 6.72), ('CB', 'LYS', 'NZ', 'LYS', 6.72)], [('CG', 'LYS', 'CB', 'LYS', 6.31), ('CG', 'LYS', 'CG', 'LYS', 6.15), ('CG', 'LYS', 'CD', 'LYS', 5.83), ('CG', 'LYS', 'CE', 'LYS', 5.83), ('CG', 'LYS', 'NZ', 'LYS', 5.83)], [('CD', 'LYS', 'CB', 'LYS', 7.17), ('CD', 'LYS', 'CG', 'LYS', 6.85), ('CD', 'LYS', 'CD', 'LYS', 6.03), ('CD', 'LYS', 'CE', 'LYS', 6.03), ('CD', 'LYS', 'NZ', 'LYS', 6.03)], [('CE', 'LYS', 'CB', 'LYS', 8.21), ('CE', 'LYS', 'CG', 'LYS', 7.59), ('CE', 'LYS', 'CD', 'LYS', 6.76), ('CE', 'LYS', 'CE', 'LYS', 6.76), ('CE', 'LYS', 'NZ', 'LYS', 6.76)], [('NZ', 'LYS', 'CB', 'LYS', 8.98), ('NZ', 'LYS', 'CG', 'LYS', 8.21), ('NZ', 'LYS', 'CD', 'LYS', 7.1), ('NZ', 'LYS', 'CE', 'LYS', 7.1), ('NZ', 'LYS', 'NZ', 'LYS', 7.1)], [('CB', 'LYS', 'CB', 'LYS', 6.51), ('CB', 'LYS', 'CG', 'LYS', 6.31), ('CB', 'LYS', 'CD', 'LYS', 7.17), ('CB', 'LYS', 'CE', 'LYS', 8.21), ('CB', 'LYS', 'NZ', 'LYS', 8.98)], [('CG', 'LYS', 'CB', 'LYS', 6.85), ('CG', 'LYS', 'CG', 'LYS', 6.15), ('CG', 'LYS', 'CD', 'LYS', 6.85), ('CG', 'LYS', 'CE', 'LYS', 7.59), ('CG', 'LYS', 'NZ', 'LYS', 8.21)], [('CD', 'LYS', 'CB', 'LYS', 6.72), ('CD', 'LYS', 'CG', 'LYS', 5.83), ('CD', 'LYS', 'CD', 'LYS', 6.03), ('CD', 'LYS', 'CE', 'LYS', 6.76), ('CD', 'LYS', 'NZ', 'LYS', 7.1)], [('CE', 'LYS', 'CB', 'LYS', 7.1), ('CE', 'LYS', 'CG', 'LYS', 7.1), ('CE', 'LYS', 'CD', 'LYS', 7.1), ('CE', 'LYS', 'CE', 'LYS', 7.1), ('CE', 'LYS', 'NZ', 'LYS', 7.1)], [('NZ', 'LYS', 'CB', 'LYS', 7.1), ('NZ', 'LYS', 'CG', 'LYS', 7.1), ('NZ', 'LYS', 'CD', 'LYS', 7.1), ('NZ', 'LYS', 'CE', 'LYS', 7.1), ('NZ', 'LYS', 'NZ', 'LYS', 7.1)]]}
LYS_SER = { 
	'distances':
		[[8.35, 9.39], [7.93, 8.8], [6.57, 7.32], [7.09, 7.47], [6.38, 6.43], [9.76, 10.86], [9.54, 10.45], [8.13, 8.98], [8.98, 8.98], [8.98, 8.98]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'SER', 8.35), ('CB', 'LYS', 'OG', 'SER', 9.39)], [('CG', 'LYS', 'CB', 'SER', 7.93), ('CG', 'LYS', 'OG', 'SER', 8.8)], [('CD', 'LYS', 'CB', 'SER', 6.57), ('CD', 'LYS', 'OG', 'SER', 7.32)], [('CE', 'LYS', 'CB', 'SER', 7.09), ('CE', 'LYS', 'OG', 'SER', 7.47)], [('NZ', 'LYS', 'CB', 'SER', 6.38), ('NZ', 'LYS', 'OG', 'SER', 6.43)], [('CB', 'LYS', 'CB', 'SER', 9.76), ('CB', 'LYS', 'OG', 'SER', 10.86)], [('CG', 'LYS', 'CB', 'SER', 9.54), ('CG', 'LYS', 'OG', 'SER', 10.45)], [('CD', 'LYS', 'CB', 'SER', 8.13), ('CD', 'LYS', 'OG', 'SER', 8.98)], [('CE', 'LYS', 'CB', 'SER', 8.98), ('CE', 'LYS', 'OG', 'SER', 8.98)], [('NZ', 'LYS', 'CB', 'SER', 8.98), ('NZ', 'LYS', 'OG', 'SER', 8.98)]]}
SER_LYSI = { 
	'distances':
		[[9.76, 9.54, 8.13, 8.13, 8.13], [10.86, 10.45, 8.98, 8.98, 8.98]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'LYSI', 9.76), ('CB', 'SER', 'CG', 'LYSI', 9.54), ('CB', 'SER', 'CD', 'LYSI', 8.13), ('CB', 'SER', 'CE', 'LYSI', 8.13), ('CB', 'SER', 'NZ', 'LYSI', 8.13)], [('OG', 'SER', 'CB', 'LYSI', 10.86), ('OG', 'SER', 'CG', 'LYSI', 10.45), ('OG', 'SER', 'CD', 'LYSI', 8.98), ('OG', 'SER', 'CE', 'LYSI', 8.98), ('OG', 'SER', 'NZ', 'LYSI', 8.98)]]}
SER_ASP = { 
	'distances':
		[[7.43, 6.04, 5.26, 6.08], [7.06, 5.57, 5.22, 5.2]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ASP', 7.43), ('CB', 'SER', 'CG', 'ASP', 6.04), ('CB', 'SER', 'OD1', 'ASP', 5.26), ('CB', 'SER', 'OD2', 'ASP', 6.08)], [('OG', 'SER', 'CB', 'ASP', 7.06), ('OG', 'SER', 'CG', 'ASP', 5.57), ('OG', 'SER', 'OD1', 'ASP', 5.22), ('OG', 'SER', 'OD2', 'ASP', 5.2)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LYS_ASP, d, 'A_1h7o_4_2_1_24')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_LYSI, d, 'A_1h7o_4_2_1_24')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(LYS_LYS, d, 'A_1h7o_4_2_1_24')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(LYS_SER, d, 'A_1h7o_4_2_1_24')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(SER_LYSI, d, 'A_1h7o_4_2_1_24')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(SER_ASP, d, 'A_1h7o_4_2_1_24')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'LYS_ASP' :  match1,
		'ASP_LYSI' :  match2,
		'LYS_LYS' :  match3,
		'LYS_SER' :  match4,
		'SER_LYSI' :  match5,
		'SER_ASP' :  match6}