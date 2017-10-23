'''
FUNC:Pfa_1gk2_4_3_1_3
PDB:1gk2
EC:4.3.1.3
RESI:ala,ser,gly,tyr,glu
LOCI:a-142,143,144,280,414;
'''
import motifFunctions as cmd
SER_TYR = { 
	'distances':
		[[9.99, 8.52, 8.28, 7.62, 7.11, 6.27, 5.94, 4.82], [10.78, 9.27, 8.79, 8.56, 7.48, 7.2, 6.53, 5.2]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'TYR', 9.99), ('CB', 'SER', 'CG', 'TYR', 8.52), ('CB', 'SER', 'CD1', 'TYR', 8.28), ('CB', 'SER', 'CD2', 'TYR', 7.62), ('CB', 'SER', 'CE1', 'TYR', 7.11), ('CB', 'SER', 'CE2', 'TYR', 6.27), ('CB', 'SER', 'CZ', 'TYR', 5.94), ('CB', 'SER', 'OH', 'TYR', 4.82)], [('OG', 'SER', 'CB', 'TYR', 10.78), ('OG', 'SER', 'CG', 'TYR', 9.27), ('OG', 'SER', 'CD1', 'TYR', 8.79), ('OG', 'SER', 'CD2', 'TYR', 8.56), ('OG', 'SER', 'CE1', 'TYR', 7.48), ('OG', 'SER', 'CE2', 'TYR', 7.2), ('OG', 'SER', 'CZ', 'TYR', 6.53), ('OG', 'SER', 'OH', 'TYR', 5.2)]]}
SER_GLY = { 
	'distances':
		[[6.97, 7.23, 6.53, 5.17], [7.84, 7.92, 7.09, 5.9]],
	'comparisons':
		[[('CB', 'SER', 'O', 'GLY', 6.97), ('CB', 'SER', 'C', 'GLY', 7.23), ('CB', 'SER', 'CA', 'GLY', 6.53), ('CB', 'SER', 'N', 'GLY', 5.17)], [('OG', 'SER', 'O', 'GLY', 7.84), ('OG', 'SER', 'C', 'GLY', 7.92), ('OG', 'SER', 'CA', 'GLY', 7.09), ('OG', 'SER', 'N', 'GLY', 5.9)]]}
ALA_TYR = { 
	'distances':
		[9.29, 8.1, 8.47, 6.89, 7.8, 5.95, 6.52, 6.24],
	'comparisons':
		[('C', 'ALA', 'CB', 'TYR', 9.29), ('C', 'ALA', 'CG', 'TYR', 8.1), ('C', 'ALA', 'CD1', 'TYR', 8.47), ('C', 'ALA', 'CD2', 'TYR', 6.89), ('C', 'ALA', 'CE1', 'TYR', 7.8), ('C', 'ALA', 'CE2', 'TYR', 5.95), ('C', 'ALA', 'CZ', 'TYR', 6.52), ('C', 'ALA', 'OH', 'TYR', 6.24)]}
GLY_TYR = { 
	'distances':
		[[13.21, 12.02, 12.31, 10.78, 11.47, 9.77, 10.16, 9.47], [13.72, 12.51, 12.7, 11.35, 11.81, 10.31, 10.58, 9.82], [13.12, 11.87, 11.92, 10.83, 10.99, 9.76, 9.85, 9.06], [11.81, 10.52, 10.54, 9.5, 9.58, 8.38, 8.43, 7.64]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'TYR', 13.21), ('O', 'GLY', 'CG', 'TYR', 12.02), ('O', 'GLY', 'CD1', 'TYR', 12.31), ('O', 'GLY', 'CD2', 'TYR', 10.78), ('O', 'GLY', 'CE1', 'TYR', 11.47), ('O', 'GLY', 'CE2', 'TYR', 9.77), ('O', 'GLY', 'CZ', 'TYR', 10.16), ('O', 'GLY', 'OH', 'TYR', 9.47)], [('C', 'GLY', 'CB', 'TYR', 13.72), ('C', 'GLY', 'CG', 'TYR', 12.51), ('C', 'GLY', 'CD1', 'TYR', 12.7), ('C', 'GLY', 'CD2', 'TYR', 11.35), ('C', 'GLY', 'CE1', 'TYR', 11.81), ('C', 'GLY', 'CE2', 'TYR', 10.31), ('C', 'GLY', 'CZ', 'TYR', 10.58), ('C', 'GLY', 'OH', 'TYR', 9.82)], [('CA', 'GLY', 'CB', 'TYR', 13.12), ('CA', 'GLY', 'CG', 'TYR', 11.87), ('CA', 'GLY', 'CD1', 'TYR', 11.92), ('CA', 'GLY', 'CD2', 'TYR', 10.83), ('CA', 'GLY', 'CE1', 'TYR', 10.99), ('CA', 'GLY', 'CE2', 'TYR', 9.76), ('CA', 'GLY', 'CZ', 'TYR', 9.85), ('CA', 'GLY', 'OH', 'TYR', 9.06)], [('N', 'GLY', 'CB', 'TYR', 11.81), ('N', 'GLY', 'CG', 'TYR', 10.52), ('N', 'GLY', 'CD1', 'TYR', 10.54), ('N', 'GLY', 'CD2', 'TYR', 9.5), ('N', 'GLY', 'CE1', 'TYR', 9.58), ('N', 'GLY', 'CE2', 'TYR', 8.38), ('N', 'GLY', 'CZ', 'TYR', 8.43), ('N', 'GLY', 'OH', 'TYR', 7.64)]]}
TYR_GLU = { 
	'distances':
		[[7.42, 8.05, 8.6, 8.87, 9.08], [6.55, 6.9, 7.3, 7.69, 7.66], [6.96, 6.93, 7.39, 8.04, 7.49], [5.84, 6.22, 6.34, 6.53, 6.79], [6.77, 6.34, 6.6, 7.4, 6.44], [5.59, 5.51, 5.3, 5.62, 5.53], [6.11, 5.58, 5.47, 6.18, 5.3], [6.56, 5.61, 5.14, 5.99, 4.49]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'GLU', 7.42), ('CB', 'TYR', 'CG', 'GLU', 8.05), ('CB', 'TYR', 'CD', 'GLU', 8.6), ('CB', 'TYR', 'OE1', 'GLU', 8.87), ('CB', 'TYR', 'OE2', 'GLU', 9.08)], [('CG', 'TYR', 'CB', 'GLU', 6.55), ('CG', 'TYR', 'CG', 'GLU', 6.9), ('CG', 'TYR', 'CD', 'GLU', 7.3), ('CG', 'TYR', 'OE1', 'GLU', 7.69), ('CG', 'TYR', 'OE2', 'GLU', 7.66)], [('CD1', 'TYR', 'CB', 'GLU', 6.96), ('CD1', 'TYR', 'CG', 'GLU', 6.93), ('CD1', 'TYR', 'CD', 'GLU', 7.39), ('CD1', 'TYR', 'OE1', 'GLU', 8.04), ('CD1', 'TYR', 'OE2', 'GLU', 7.49)], [('CD2', 'TYR', 'CB', 'GLU', 5.84), ('CD2', 'TYR', 'CG', 'GLU', 6.22), ('CD2', 'TYR', 'CD', 'GLU', 6.34), ('CD2', 'TYR', 'OE1', 'GLU', 6.53), ('CD2', 'TYR', 'OE2', 'GLU', 6.79)], [('CE1', 'TYR', 'CB', 'GLU', 6.77), ('CE1', 'TYR', 'CG', 'GLU', 6.34), ('CE1', 'TYR', 'CD', 'GLU', 6.6), ('CE1', 'TYR', 'OE1', 'GLU', 7.4), ('CE1', 'TYR', 'OE2', 'GLU', 6.44)], [('CE2', 'TYR', 'CB', 'GLU', 5.59), ('CE2', 'TYR', 'CG', 'GLU', 5.51), ('CE2', 'TYR', 'CD', 'GLU', 5.3), ('CE2', 'TYR', 'OE1', 'GLU', 5.62), ('CE2', 'TYR', 'OE2', 'GLU', 5.53)], [('CZ', 'TYR', 'CB', 'GLU', 6.11), ('CZ', 'TYR', 'CG', 'GLU', 5.58), ('CZ', 'TYR', 'CD', 'GLU', 5.47), ('CZ', 'TYR', 'OE1', 'GLU', 6.18), ('CZ', 'TYR', 'OE2', 'GLU', 5.3)], [('OH', 'TYR', 'CB', 'GLU', 6.56), ('OH', 'TYR', 'CG', 'GLU', 5.61), ('OH', 'TYR', 'CD', 'GLU', 5.14), ('OH', 'TYR', 'OE1', 'GLU', 5.99), ('OH', 'TYR', 'OE2', 'GLU', 4.49)]]}
ALA_GLU = { 
	'distances':
		[8.13, 7.79, 6.51, 6.08, 6.31],
	'comparisons':
		[('C', 'ALA', 'CB', 'GLU', 8.13), ('C', 'ALA', 'CG', 'GLU', 7.79), ('C', 'ALA', 'CD', 'GLU', 6.51), ('C', 'ALA', 'OE1', 'GLU', 6.08), ('C', 'ALA', 'OE2', 'GLU', 6.31)]}
GLY_GLU = { 
	'distances':
		[[11.15, 10.63, 9.13, 8.51, 8.75], [12.01, 11.4, 9.9, 9.42, 9.38], [11.88, 11.17, 9.72, 9.44, 9.04], [10.56, 9.83, 8.42, 8.24, 7.72]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'GLU', 11.15), ('O', 'GLY', 'CG', 'GLU', 10.63), ('O', 'GLY', 'CD', 'GLU', 9.13), ('O', 'GLY', 'OE1', 'GLU', 8.51), ('O', 'GLY', 'OE2', 'GLU', 8.75)], [('C', 'GLY', 'CB', 'GLU', 12.01), ('C', 'GLY', 'CG', 'GLU', 11.4), ('C', 'GLY', 'CD', 'GLU', 9.9), ('C', 'GLY', 'OE1', 'GLU', 9.42), ('C', 'GLY', 'OE2', 'GLU', 9.38)], [('CA', 'GLY', 'CB', 'GLU', 11.88), ('CA', 'GLY', 'CG', 'GLU', 11.17), ('CA', 'GLY', 'CD', 'GLU', 9.72), ('CA', 'GLY', 'OE1', 'GLU', 9.44), ('CA', 'GLY', 'OE2', 'GLU', 9.04)], [('N', 'GLY', 'CB', 'GLU', 10.56), ('N', 'GLY', 'CG', 'GLU', 9.83), ('N', 'GLY', 'CD', 'GLU', 8.42), ('N', 'GLY', 'OE1', 'GLU', 8.24), ('N', 'GLY', 'OE2', 'GLU', 7.72)]]}
ALA_SER = { 
	'distances':
		[4.97, 6.36],
	'comparisons':
		[('C', 'ALA', 'CB', 'SER', 4.97), ('C', 'ALA', 'OG', 'SER', 6.36)]}
SER_GLU = { 
	'distances':
		[[8.07, 7.04, 5.77, 6.11, 4.8], [8.8, 7.57, 6.47, 7.06, 5.28]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'GLU', 8.07), ('CB', 'SER', 'CG', 'GLU', 7.04), ('CB', 'SER', 'CD', 'GLU', 5.77), ('CB', 'SER', 'OE1', 'GLU', 6.11), ('CB', 'SER', 'OE2', 'GLU', 4.8)], [('OG', 'SER', 'CB', 'GLU', 8.8), ('OG', 'SER', 'CG', 'GLU', 7.57), ('OG', 'SER', 'CD', 'GLU', 6.47), ('OG', 'SER', 'OE1', 'GLU', 7.06), ('OG', 'SER', 'OE2', 'GLU', 5.28)]]}
ALA_GLY = { 
	'distances':
		[5.93, 6.47, 6.15, 4.98],
	'comparisons':
		[('C', 'ALA', 'O', 'GLY', 5.93), ('C', 'ALA', 'C', 'GLY', 6.47), ('C', 'ALA', 'CA', 'GLY', 6.15), ('C', 'ALA', 'N', 'GLY', 4.98)]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(SER_TYR, d, 'Pfa_1gk2_4_3_1_3')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(SER_GLY, d, 'Pfa_1gk2_4_3_1_3')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ALA_TYR, d, 'Pfa_1gk2_4_3_1_3')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(GLY_TYR, d, 'Pfa_1gk2_4_3_1_3')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(TYR_GLU, d, 'Pfa_1gk2_4_3_1_3')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(ALA_GLU, d, 'Pfa_1gk2_4_3_1_3')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(GLY_GLU, d, 'Pfa_1gk2_4_3_1_3')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(ALA_SER, d, 'Pfa_1gk2_4_3_1_3')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(SER_GLU, d, 'Pfa_1gk2_4_3_1_3')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(ALA_GLY, d, 'Pfa_1gk2_4_3_1_3')
	if match10 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'SER_TYR' :  match1,
		'SER_GLY' :  match2,
		'ALA_TYR' :  match3,
		'GLY_TYR' :  match4,
		'TYR_GLU' :  match5,
		'ALA_GLU' :  match6,
		'GLY_GLU' :  match7,
		'ALA_SER' :  match8,
		'SER_GLU' :  match9,
		'ALA_GLY' :  match10}