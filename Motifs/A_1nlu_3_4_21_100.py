'''
FUNC:A_1nlu_3_4_21_100
PDB:1nlu
EC:3.4.21.100
RESI:glu,asp,asp,ser
LOCI:a-80,84,170,287;
'''
import motifFunctions as cmd
ASP_ASP = { 
	'distances':
		[[16.39, 14.94, 14.25, 14.59], [15.04, 13.62, 12.91, 13.32], [15.12, 13.75, 13.03, 13.52], [14.01, 12.56, 11.85, 12.24], [16.39, 15.04, 15.12, 14.01], [14.94, 13.62, 13.75, 12.56], [14.25, 12.91, 13.03, 11.85], [14.59, 13.32, 13.52, 12.24]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASP', 16.39), ('CB', 'ASP', 'CG', 'ASP', 14.94), ('CB', 'ASP', 'OD1', 'ASP', 14.25), ('CB', 'ASP', 'OD2', 'ASP', 14.59)], [('CG', 'ASP', 'CB', 'ASP', 15.04), ('CG', 'ASP', 'CG', 'ASP', 13.62), ('CG', 'ASP', 'OD1', 'ASP', 12.91), ('CG', 'ASP', 'OD2', 'ASP', 13.32)], [('OD1', 'ASP', 'CB', 'ASP', 15.12), ('OD1', 'ASP', 'CG', 'ASP', 13.75), ('OD1', 'ASP', 'OD1', 'ASP', 13.03), ('OD1', 'ASP', 'OD2', 'ASP', 13.52)], [('OD2', 'ASP', 'CB', 'ASP', 14.01), ('OD2', 'ASP', 'CG', 'ASP', 12.56), ('OD2', 'ASP', 'OD1', 'ASP', 11.85), ('OD2', 'ASP', 'OD2', 'ASP', 12.24)], [('CB', 'ASP', 'CB', 'ASP', 16.39), ('CB', 'ASP', 'CG', 'ASP', 15.04), ('CB', 'ASP', 'OD1', 'ASP', 15.12), ('CB', 'ASP', 'OD2', 'ASP', 14.01)], [('CG', 'ASP', 'CB', 'ASP', 14.94), ('CG', 'ASP', 'CG', 'ASP', 13.62), ('CG', 'ASP', 'OD1', 'ASP', 13.75), ('CG', 'ASP', 'OD2', 'ASP', 12.56)], [('OD1', 'ASP', 'CB', 'ASP', 14.25), ('OD1', 'ASP', 'CG', 'ASP', 12.91), ('OD1', 'ASP', 'OD1', 'ASP', 13.03), ('OD1', 'ASP', 'OD2', 'ASP', 11.85)], [('OD2', 'ASP', 'CB', 'ASP', 14.59), ('OD2', 'ASP', 'CG', 'ASP', 13.32), ('OD2', 'ASP', 'OD1', 'ASP', 13.52), ('OD2', 'ASP', 'OD2', 'ASP', 12.24)]]}
SER_ASP = { 
	'distances':
		[[9.11, 7.86, 8.22, 6.72], [9.76, 8.37, 8.46, 7.4], [9.35, 7.87, 7.2, 7.61], [8.69, 7.31, 6.6, 7.2]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ASP', 9.11), ('CB', 'SER', 'CG', 'ASP', 7.86), ('CB', 'SER', 'OD1', 'ASP', 8.22), ('CB', 'SER', 'OD2', 'ASP', 6.72)], [('OG', 'SER', 'CB', 'ASP', 9.76), ('OG', 'SER', 'CG', 'ASP', 8.37), ('OG', 'SER', 'OD1', 'ASP', 8.46), ('OG', 'SER', 'OD2', 'ASP', 7.4)], [('CB', 'SER', 'CB', 'ASP', 9.35), ('CB', 'SER', 'CG', 'ASP', 7.87), ('CB', 'SER', 'OD1', 'ASP', 7.2), ('CB', 'SER', 'OD2', 'ASP', 7.61)], [('OG', 'SER', 'CB', 'ASP', 8.69), ('OG', 'SER', 'CG', 'ASP', 7.31), ('OG', 'SER', 'OD1', 'ASP', 6.6), ('OG', 'SER', 'OD2', 'ASP', 7.2)]]}
GLU_SER = { 
	'distances':
		[[8.02, 7.78], [7.23, 6.93], [5.73, 5.48], [5.42, 4.76], [5.14, 5.35]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'SER', 8.02), ('CB', 'GLU', 'OG', 'SER', 7.78)], [('CG', 'GLU', 'CB', 'SER', 7.23), ('CG', 'GLU', 'OG', 'SER', 6.93)], [('CD', 'GLU', 'CB', 'SER', 5.73), ('CD', 'GLU', 'OG', 'SER', 5.48)], [('OE1', 'GLU', 'CB', 'SER', 5.42), ('OE1', 'GLU', 'OG', 'SER', 4.76)], [('OE2', 'GLU', 'CB', 'SER', 5.14), ('OE2', 'GLU', 'OG', 'SER', 5.35)]]}
GLU_ASP = { 
	'distances':
		[[8.29, 7.16, 6.73, 7.05], [7.53, 6.2, 5.63, 6.11], [7.63, 6.2, 5.95, 5.68], [8.83, 7.37, 7.1, 6.75], [6.83, 5.43, 5.52, 4.63], [13.54, 12.4, 11.34, 12.68], [13.08, 11.88, 10.94, 12.02], [11.81, 10.55, 9.63, 10.62], [10.7, 9.5, 8.56, 9.68], [11.95, 10.59, 9.74, 10.51]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ASP', 8.29), ('CB', 'GLU', 'CG', 'ASP', 7.16), ('CB', 'GLU', 'OD1', 'ASP', 6.73), ('CB', 'GLU', 'OD2', 'ASP', 7.05)], [('CG', 'GLU', 'CB', 'ASP', 7.53), ('CG', 'GLU', 'CG', 'ASP', 6.2), ('CG', 'GLU', 'OD1', 'ASP', 5.63), ('CG', 'GLU', 'OD2', 'ASP', 6.11)], [('CD', 'GLU', 'CB', 'ASP', 7.63), ('CD', 'GLU', 'CG', 'ASP', 6.2), ('CD', 'GLU', 'OD1', 'ASP', 5.95), ('CD', 'GLU', 'OD2', 'ASP', 5.68)], [('OE1', 'GLU', 'CB', 'ASP', 8.83), ('OE1', 'GLU', 'CG', 'ASP', 7.37), ('OE1', 'GLU', 'OD1', 'ASP', 7.1), ('OE1', 'GLU', 'OD2', 'ASP', 6.75)], [('OE2', 'GLU', 'CB', 'ASP', 6.83), ('OE2', 'GLU', 'CG', 'ASP', 5.43), ('OE2', 'GLU', 'OD1', 'ASP', 5.52), ('OE2', 'GLU', 'OD2', 'ASP', 4.63)], [('CB', 'GLU', 'CB', 'ASP', 13.54), ('CB', 'GLU', 'CG', 'ASP', 12.4), ('CB', 'GLU', 'OD1', 'ASP', 11.34), ('CB', 'GLU', 'OD2', 'ASP', 12.68)], [('CG', 'GLU', 'CB', 'ASP', 13.08), ('CG', 'GLU', 'CG', 'ASP', 11.88), ('CG', 'GLU', 'OD1', 'ASP', 10.94), ('CG', 'GLU', 'OD2', 'ASP', 12.02)], [('CD', 'GLU', 'CB', 'ASP', 11.81), ('CD', 'GLU', 'CG', 'ASP', 10.55), ('CD', 'GLU', 'OD1', 'ASP', 9.63), ('CD', 'GLU', 'OD2', 'ASP', 10.62)], [('OE1', 'GLU', 'CB', 'ASP', 10.7), ('OE1', 'GLU', 'CG', 'ASP', 9.5), ('OE1', 'GLU', 'OD1', 'ASP', 8.56), ('OE1', 'GLU', 'OD2', 'ASP', 9.68)], [('OE2', 'GLU', 'CB', 'ASP', 11.95), ('OE2', 'GLU', 'CG', 'ASP', 10.59), ('OE2', 'GLU', 'OD1', 'ASP', 9.74), ('OE2', 'GLU', 'OD2', 'ASP', 10.51)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_ASP, d, 'A_1nlu_3_4_21_100')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(SER_ASP, d, 'A_1nlu_3_4_21_100')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_SER, d, 'A_1nlu_3_4_21_100')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(GLU_ASP, d, 'A_1nlu_3_4_21_100')
	if match4 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_ASP' :  match1,
		'SER_ASP' :  match2,
		'GLU_SER' :  match3,
		'GLU_ASP' :  match4}