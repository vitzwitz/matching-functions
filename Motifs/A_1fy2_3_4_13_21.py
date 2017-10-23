'''
FUNC:A_1fy2_3_4_13_21
PDB:1fy2
EC:3.4.13.21
RESI:gly,ser,ala,his,glu
LOCI:a-88,120,121,157,192;
'''
import motifFunctions as cmd
GLY_SER = { 
	'distances':
		[[7.51, 6.55], [8.3, 7.47], [8.07, 7.45], [6.79, 6.39]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'SER', 7.51), ('O', 'GLY', 'OG', 'SER', 6.55)], [('C', 'GLY', 'CB', 'SER', 8.3), ('C', 'GLY', 'OG', 'SER', 7.47)], [('CA', 'GLY', 'CB', 'SER', 8.07), ('CA', 'GLY', 'OG', 'SER', 7.45)], [('N', 'GLY', 'CB', 'SER', 6.79), ('N', 'GLY', 'OG', 'SER', 6.39)]]}
ALA_HIS = { 
	'distances':
		[[12.18, 10.95, 11.16, 9.62, 10.08, 9.02], [13.17, 12.11, 12.49, 10.82, 11.55, 10.45], [12.5, 11.34, 11.6, 10.06, 10.59, 9.55], [11.42, 10.24, 10.53, 8.92, 9.52, 8.42], [10.36, 9.09, 9.25, 7.82, 8.19, 7.17]],
	'comparisons':
		[[('CB', 'ALA', 'CB', 'HIS', 12.18), ('CB', 'ALA', 'CG', 'HIS', 10.95), ('CB', 'ALA', 'ND1', 'HIS', 11.16), ('CB', 'ALA', 'CD2', 'HIS', 9.62), ('CB', 'ALA', 'CE1', 'HIS', 10.08), ('CB', 'ALA', 'NE2', 'HIS', 9.02)], [('O', 'ALA', 'CB', 'HIS', 13.17), ('O', 'ALA', 'CG', 'HIS', 12.11), ('O', 'ALA', 'ND1', 'HIS', 12.49), ('O', 'ALA', 'CD2', 'HIS', 10.82), ('O', 'ALA', 'CE1', 'HIS', 11.55), ('O', 'ALA', 'NE2', 'HIS', 10.45)], [('C', 'ALA', 'CB', 'HIS', 12.5), ('C', 'ALA', 'CG', 'HIS', 11.34), ('C', 'ALA', 'ND1', 'HIS', 11.6), ('C', 'ALA', 'CD2', 'HIS', 10.06), ('C', 'ALA', 'CE1', 'HIS', 10.59), ('C', 'ALA', 'NE2', 'HIS', 9.55)], [('CA', 'ALA', 'CB', 'HIS', 11.42), ('CA', 'ALA', 'CG', 'HIS', 10.24), ('CA', 'ALA', 'ND1', 'HIS', 10.53), ('CA', 'ALA', 'CD2', 'HIS', 8.92), ('CA', 'ALA', 'CE1', 'HIS', 9.52), ('CA', 'ALA', 'NE2', 'HIS', 8.42)], [('N', 'ALA', 'CB', 'HIS', 10.36), ('N', 'ALA', 'CG', 'HIS', 9.09), ('N', 'ALA', 'ND1', 'HIS', 9.25), ('N', 'ALA', 'CD2', 'HIS', 7.82), ('N', 'ALA', 'CE1', 'HIS', 8.19), ('N', 'ALA', 'NE2', 'HIS', 7.17)]]}
HIS_GLU = { 
	'distances':
		[[7.67, 6.26, 6.57, 7.65, 6.11], [7.87, 6.46, 6.58, 7.75, 5.81], [7.21, 5.84, 5.69, 6.86, 4.75], [9.0, 7.67, 7.77, 8.96, 6.9], [8.08, 6.86, 6.62, 7.74, 5.57], [9.09, 7.85, 7.77, 8.93, 6.76]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLU', 7.67), ('CB', 'HIS', 'CG', 'GLU', 6.26), ('CB', 'HIS', 'CD', 'GLU', 6.57), ('CB', 'HIS', 'OE1', 'GLU', 7.65), ('CB', 'HIS', 'OE2', 'GLU', 6.11)], [('CG', 'HIS', 'CB', 'GLU', 7.87), ('CG', 'HIS', 'CG', 'GLU', 6.46), ('CG', 'HIS', 'CD', 'GLU', 6.58), ('CG', 'HIS', 'OE1', 'GLU', 7.75), ('CG', 'HIS', 'OE2', 'GLU', 5.81)], [('ND1', 'HIS', 'CB', 'GLU', 7.21), ('ND1', 'HIS', 'CG', 'GLU', 5.84), ('ND1', 'HIS', 'CD', 'GLU', 5.69), ('ND1', 'HIS', 'OE1', 'GLU', 6.86), ('ND1', 'HIS', 'OE2', 'GLU', 4.75)], [('CD2', 'HIS', 'CB', 'GLU', 9.0), ('CD2', 'HIS', 'CG', 'GLU', 7.67), ('CD2', 'HIS', 'CD', 'GLU', 7.77), ('CD2', 'HIS', 'OE1', 'GLU', 8.96), ('CD2', 'HIS', 'OE2', 'GLU', 6.9)], [('CE1', 'HIS', 'CB', 'GLU', 8.08), ('CE1', 'HIS', 'CG', 'GLU', 6.86), ('CE1', 'HIS', 'CD', 'GLU', 6.62), ('CE1', 'HIS', 'OE1', 'GLU', 7.74), ('CE1', 'HIS', 'OE2', 'GLU', 5.57)], [('NE2', 'HIS', 'CB', 'GLU', 9.09), ('NE2', 'HIS', 'CG', 'GLU', 7.85), ('NE2', 'HIS', 'CD', 'GLU', 7.77), ('NE2', 'HIS', 'OE1', 'GLU', 8.93), ('NE2', 'HIS', 'OE2', 'GLU', 6.76)]]}
SER_GLU = { 
	'distances':
		[[11.15, 10.26, 10.24, 11.35, 9.29], [11.28, 10.2, 10.07, 11.18, 9.01]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'GLU', 11.15), ('CB', 'SER', 'CG', 'GLU', 10.26), ('CB', 'SER', 'CD', 'GLU', 10.24), ('CB', 'SER', 'OE1', 'GLU', 11.35), ('CB', 'SER', 'OE2', 'GLU', 9.29)], [('OG', 'SER', 'CB', 'GLU', 11.28), ('OG', 'SER', 'CG', 'GLU', 10.2), ('OG', 'SER', 'CD', 'GLU', 10.07), ('OG', 'SER', 'OE1', 'GLU', 11.18), ('OG', 'SER', 'OE2', 'GLU', 9.01)]]}
GLY_HIS = { 
	'distances':
		[[11.49, 10.27, 10.37, 9.1, 9.34, 8.46], [12.57, 11.33, 11.32, 10.2, 10.24, 9.47], [12.89, 11.55, 11.32, 10.5, 10.16, 9.56], [12.24, 10.83, 10.55, 9.76, 9.31, 8.73]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'HIS', 11.49), ('O', 'GLY', 'CG', 'HIS', 10.27), ('O', 'GLY', 'ND1', 'HIS', 10.37), ('O', 'GLY', 'CD2', 'HIS', 9.1), ('O', 'GLY', 'CE1', 'HIS', 9.34), ('O', 'GLY', 'NE2', 'HIS', 8.46)], [('C', 'GLY', 'CB', 'HIS', 12.57), ('C', 'GLY', 'CG', 'HIS', 11.33), ('C', 'GLY', 'ND1', 'HIS', 11.32), ('C', 'GLY', 'CD2', 'HIS', 10.2), ('C', 'GLY', 'CE1', 'HIS', 10.24), ('C', 'GLY', 'NE2', 'HIS', 9.47)], [('CA', 'GLY', 'CB', 'HIS', 12.89), ('CA', 'GLY', 'CG', 'HIS', 11.55), ('CA', 'GLY', 'ND1', 'HIS', 11.32), ('CA', 'GLY', 'CD2', 'HIS', 10.5), ('CA', 'GLY', 'CE1', 'HIS', 10.16), ('CA', 'GLY', 'NE2', 'HIS', 9.56)], [('N', 'GLY', 'CB', 'HIS', 12.24), ('N', 'GLY', 'CG', 'HIS', 10.83), ('N', 'GLY', 'ND1', 'HIS', 10.55), ('N', 'GLY', 'CD2', 'HIS', 9.76), ('N', 'GLY', 'CE1', 'HIS', 9.31), ('N', 'GLY', 'NE2', 'HIS', 8.73)]]}
GLY_GLU = { 
	'distances':
		[[15.42, 14.17, 13.76, 14.73, 12.56], [16.3, 15.08, 14.58, 15.5, 13.36], [16.07, 14.93, 14.36, 15.23, 13.14], [15.15, 14.08, 13.61, 14.53, 12.43]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'GLU', 15.42), ('O', 'GLY', 'CG', 'GLU', 14.17), ('O', 'GLY', 'CD', 'GLU', 13.76), ('O', 'GLY', 'OE1', 'GLU', 14.73), ('O', 'GLY', 'OE2', 'GLU', 12.56)], [('C', 'GLY', 'CB', 'GLU', 16.3), ('C', 'GLY', 'CG', 'GLU', 15.08), ('C', 'GLY', 'CD', 'GLU', 14.58), ('C', 'GLY', 'OE1', 'GLU', 15.5), ('C', 'GLY', 'OE2', 'GLU', 13.36)], [('CA', 'GLY', 'CB', 'GLU', 16.07), ('CA', 'GLY', 'CG', 'GLU', 14.93), ('CA', 'GLY', 'CD', 'GLU', 14.36), ('CA', 'GLY', 'OE1', 'GLU', 15.23), ('CA', 'GLY', 'OE2', 'GLU', 13.14)], [('N', 'GLY', 'CB', 'GLU', 15.15), ('N', 'GLY', 'CG', 'GLU', 14.08), ('N', 'GLY', 'CD', 'GLU', 13.61), ('N', 'GLY', 'OE1', 'GLU', 14.53), ('N', 'GLY', 'OE2', 'GLU', 12.43)]]}
ALA_SER = { 
	'distances':
		[[6.89, 6.65], [8.2, 8.43], [7.08, 7.37], [6.28, 6.23], [4.81, 4.9]],
	'comparisons':
		[[('CB', 'ALA', 'CB', 'SER', 6.89), ('CB', 'ALA', 'OG', 'SER', 6.65)], [('O', 'ALA', 'CB', 'SER', 8.2), ('O', 'ALA', 'OG', 'SER', 8.43)], [('C', 'ALA', 'CB', 'SER', 7.08), ('C', 'ALA', 'OG', 'SER', 7.37)], [('CA', 'ALA', 'CB', 'SER', 6.28), ('CA', 'ALA', 'OG', 'SER', 6.23)], [('N', 'ALA', 'CB', 'SER', 4.81), ('N', 'ALA', 'OG', 'SER', 4.9)]]}
SER_HIS = { 
	'distances':
		[[8.88, 7.45, 7.15, 6.47, 5.94, 5.36], [8.25, 6.81, 6.67, 5.7, 5.49, 4.64]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'HIS', 8.88), ('CB', 'SER', 'CG', 'HIS', 7.45), ('CB', 'SER', 'ND1', 'HIS', 7.15), ('CB', 'SER', 'CD2', 'HIS', 6.47), ('CB', 'SER', 'CE1', 'HIS', 5.94), ('CB', 'SER', 'NE2', 'HIS', 5.36)], [('OG', 'SER', 'CB', 'HIS', 8.25), ('OG', 'SER', 'CG', 'HIS', 6.81), ('OG', 'SER', 'ND1', 'HIS', 6.67), ('OG', 'SER', 'CD2', 'HIS', 5.7), ('OG', 'SER', 'CE1', 'HIS', 5.49), ('OG', 'SER', 'NE2', 'HIS', 4.64)]]}
ALA_GLU = { 
	'distances':
		[[15.77, 14.72, 14.69, 15.81, 13.63], [16.48, 15.61, 15.92, 17.12, 15.05], [15.63, 14.76, 14.99, 16.18, 14.09], [14.91, 13.92, 14.05, 15.22, 13.08], [13.54, 12.58, 12.68, 13.85, 11.72]],
	'comparisons':
		[[('CB', 'ALA', 'CB', 'GLU', 15.77), ('CB', 'ALA', 'CG', 'GLU', 14.72), ('CB', 'ALA', 'CD', 'GLU', 14.69), ('CB', 'ALA', 'OE1', 'GLU', 15.81), ('CB', 'ALA', 'OE2', 'GLU', 13.63)], [('O', 'ALA', 'CB', 'GLU', 16.48), ('O', 'ALA', 'CG', 'GLU', 15.61), ('O', 'ALA', 'CD', 'GLU', 15.92), ('O', 'ALA', 'OE1', 'GLU', 17.12), ('O', 'ALA', 'OE2', 'GLU', 15.05)], [('C', 'ALA', 'CB', 'GLU', 15.63), ('C', 'ALA', 'CG', 'GLU', 14.76), ('C', 'ALA', 'CD', 'GLU', 14.99), ('C', 'ALA', 'OE1', 'GLU', 16.18), ('C', 'ALA', 'OE2', 'GLU', 14.09)], [('CA', 'ALA', 'CB', 'GLU', 14.91), ('CA', 'ALA', 'CG', 'GLU', 13.92), ('CA', 'ALA', 'CD', 'GLU', 14.05), ('CA', 'ALA', 'OE1', 'GLU', 15.22), ('CA', 'ALA', 'OE2', 'GLU', 13.08)], [('N', 'ALA', 'CB', 'GLU', 13.54), ('N', 'ALA', 'CG', 'GLU', 12.58), ('N', 'ALA', 'CD', 'GLU', 12.68), ('N', 'ALA', 'OE1', 'GLU', 13.85), ('N', 'ALA', 'OE2', 'GLU', 11.72)]]}
ALA_GLY = { 
	'distances':
		[[5.55, 6.1, 6.64, 5.91], [8.69, 9.3, 9.79, 8.9], [7.93, 8.54, 8.88, 7.87], [6.58, 7.34, 7.82, 6.88], [6.58, 7.42, 7.66, 6.52]],
	'comparisons':
		[[('CB', 'ALA', 'O', 'GLY', 5.55), ('CB', 'ALA', 'C', 'GLY', 6.1), ('CB', 'ALA', 'CA', 'GLY', 6.64), ('CB', 'ALA', 'N', 'GLY', 5.91)], [('O', 'ALA', 'O', 'GLY', 8.69), ('O', 'ALA', 'C', 'GLY', 9.3), ('O', 'ALA', 'CA', 'GLY', 9.79), ('O', 'ALA', 'N', 'GLY', 8.9)], [('C', 'ALA', 'O', 'GLY', 7.93), ('C', 'ALA', 'C', 'GLY', 8.54), ('C', 'ALA', 'CA', 'GLY', 8.88), ('C', 'ALA', 'N', 'GLY', 7.87)], [('CA', 'ALA', 'O', 'GLY', 6.58), ('CA', 'ALA', 'C', 'GLY', 7.34), ('CA', 'ALA', 'CA', 'GLY', 7.82), ('CA', 'ALA', 'N', 'GLY', 6.88)], [('N', 'ALA', 'O', 'GLY', 6.58), ('N', 'ALA', 'C', 'GLY', 7.42), ('N', 'ALA', 'CA', 'GLY', 7.66), ('N', 'ALA', 'N', 'GLY', 6.52)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLY_SER, d, 'A_1fy2_3_4_13_21')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ALA_HIS, d, 'A_1fy2_3_4_13_21')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_GLU, d, 'A_1fy2_3_4_13_21')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(SER_GLU, d, 'A_1fy2_3_4_13_21')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(GLY_HIS, d, 'A_1fy2_3_4_13_21')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(GLY_GLU, d, 'A_1fy2_3_4_13_21')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(ALA_SER, d, 'A_1fy2_3_4_13_21')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(SER_HIS, d, 'A_1fy2_3_4_13_21')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(ALA_GLU, d, 'A_1fy2_3_4_13_21')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(ALA_GLY, d, 'A_1fy2_3_4_13_21')
	if match10 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLY_SER' :  match1,
		'ALA_HIS' :  match2,
		'HIS_GLU' :  match3,
		'SER_GLU' :  match4,
		'GLY_HIS' :  match5,
		'GLY_GLU' :  match6,
		'ALA_SER' :  match7,
		'SER_HIS' :  match8,
		'ALA_GLU' :  match9,
		'ALA_GLY' :  match10}