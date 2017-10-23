'''
FUNC:Pab_1b8f_4_3_1_3
PDB:1b8f
EC:4.3.1.3
RESI:ala,ser,gly,tyr,glu
LOCI:a-142,143,144,280,414;
'''
import motifFunctions as cmd
SER_TYR = { 
	'distances':
		[10.62, 9.17, 8.92, 8.22, 7.73, 6.86, 6.55, 5.37],
	'comparisons':
		[('CB', 'SER', 'CB', 'TYR', 10.62), ('CB', 'SER', 'CG', 'TYR', 9.17), ('CB', 'SER', 'CD1', 'TYR', 8.92), ('CB', 'SER', 'CD2', 'TYR', 8.22), ('CB', 'SER', 'CE1', 'TYR', 7.73), ('CB', 'SER', 'CE2', 'TYR', 6.86), ('CB', 'SER', 'CZ', 'TYR', 6.55), ('CB', 'SER', 'OH', 'TYR', 5.37)]}
SER_GLY = { 
	'distances':
		[7.27, 7.37, 6.65, 5.63],
	'comparisons':
		[('CB', 'SER', 'O', 'GLY', 7.27), ('CB', 'SER', 'C', 'GLY', 7.37), ('CB', 'SER', 'CA', 'GLY', 6.65), ('CB', 'SER', 'N', 'GLY', 5.63)]}
ALA_TYR = { 
	'distances':
		[9.92, 8.81, 9.14, 7.57, 8.46, 6.63, 7.17, 6.8],
	'comparisons':
		[('C', 'ALA', 'CB', 'TYR', 9.92), ('C', 'ALA', 'CG', 'TYR', 8.81), ('C', 'ALA', 'CD1', 'TYR', 9.14), ('C', 'ALA', 'CD2', 'TYR', 7.57), ('C', 'ALA', 'CE1', 'TYR', 8.46), ('C', 'ALA', 'CE2', 'TYR', 6.63), ('C', 'ALA', 'CZ', 'TYR', 7.17), ('C', 'ALA', 'OH', 'TYR', 6.8)]}
GLY_TYR = { 
	'distances':
		[[13.27, 12.2, 12.57, 10.86, 11.81, 9.91, 10.45, 9.84], [13.43, 12.35, 12.67, 11.08, 11.89, 10.12, 10.58, 9.95], [12.23, 11.14, 11.42, 9.94, 10.66, 9.0, 9.41, 8.85], [10.94, 9.79, 9.98, 8.65, 9.2, 7.66, 7.98, 7.44]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'TYR', 13.27), ('O', 'GLY', 'CG', 'TYR', 12.2), ('O', 'GLY', 'CD1', 'TYR', 12.57), ('O', 'GLY', 'CD2', 'TYR', 10.86), ('O', 'GLY', 'CE1', 'TYR', 11.81), ('O', 'GLY', 'CE2', 'TYR', 9.91), ('O', 'GLY', 'CZ', 'TYR', 10.45), ('O', 'GLY', 'OH', 'TYR', 9.84)], [('C', 'GLY', 'CB', 'TYR', 13.43), ('C', 'GLY', 'CG', 'TYR', 12.35), ('C', 'GLY', 'CD1', 'TYR', 12.67), ('C', 'GLY', 'CD2', 'TYR', 11.08), ('C', 'GLY', 'CE1', 'TYR', 11.89), ('C', 'GLY', 'CE2', 'TYR', 10.12), ('C', 'GLY', 'CZ', 'TYR', 10.58), ('C', 'GLY', 'OH', 'TYR', 9.95)], [('CA', 'GLY', 'CB', 'TYR', 12.23), ('CA', 'GLY', 'CG', 'TYR', 11.14), ('CA', 'GLY', 'CD1', 'TYR', 11.42), ('CA', 'GLY', 'CD2', 'TYR', 9.94), ('CA', 'GLY', 'CE1', 'TYR', 10.66), ('CA', 'GLY', 'CE2', 'TYR', 9.0), ('CA', 'GLY', 'CZ', 'TYR', 9.41), ('CA', 'GLY', 'OH', 'TYR', 8.85)], [('N', 'GLY', 'CB', 'TYR', 10.94), ('N', 'GLY', 'CG', 'TYR', 9.79), ('N', 'GLY', 'CD1', 'TYR', 9.98), ('N', 'GLY', 'CD2', 'TYR', 8.65), ('N', 'GLY', 'CE1', 'TYR', 9.2), ('N', 'GLY', 'CE2', 'TYR', 7.66), ('N', 'GLY', 'CZ', 'TYR', 7.98), ('N', 'GLY', 'OH', 'TYR', 7.44)]]}
TYR_GLU = { 
	'distances':
		[[7.65, 7.78, 9.02, 9.31, 9.93], [6.73, 6.56, 7.74, 8.14, 8.58], [6.94, 6.5, 7.73, 8.38, 8.34], [6.11, 5.85, 6.81, 7.0, 7.75], [6.65, 5.83, 6.89, 7.66, 7.3], [5.78, 5.05, 5.78, 6.06, 6.6], [6.08, 5.04, 5.83, 6.48, 6.32], [6.4, 5.02, 5.35, 6.12, 5.49]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'GLU', 7.65), ('CB', 'TYR', 'CG', 'GLU', 7.78), ('CB', 'TYR', 'CD', 'GLU', 9.02), ('CB', 'TYR', 'OE1', 'GLU', 9.31), ('CB', 'TYR', 'OE2', 'GLU', 9.93)], [('CG', 'TYR', 'CB', 'GLU', 6.73), ('CG', 'TYR', 'CG', 'GLU', 6.56), ('CG', 'TYR', 'CD', 'GLU', 7.74), ('CG', 'TYR', 'OE1', 'GLU', 8.14), ('CG', 'TYR', 'OE2', 'GLU', 8.58)], [('CD1', 'TYR', 'CB', 'GLU', 6.94), ('CD1', 'TYR', 'CG', 'GLU', 6.5), ('CD1', 'TYR', 'CD', 'GLU', 7.73), ('CD1', 'TYR', 'OE1', 'GLU', 8.38), ('CD1', 'TYR', 'OE2', 'GLU', 8.34)], [('CD2', 'TYR', 'CB', 'GLU', 6.11), ('CD2', 'TYR', 'CG', 'GLU', 5.85), ('CD2', 'TYR', 'CD', 'GLU', 6.81), ('CD2', 'TYR', 'OE1', 'GLU', 7.0), ('CD2', 'TYR', 'OE2', 'GLU', 7.75)], [('CE1', 'TYR', 'CB', 'GLU', 6.65), ('CE1', 'TYR', 'CG', 'GLU', 5.83), ('CE1', 'TYR', 'CD', 'GLU', 6.89), ('CE1', 'TYR', 'OE1', 'GLU', 7.66), ('CE1', 'TYR', 'OE2', 'GLU', 7.3)], [('CE2', 'TYR', 'CB', 'GLU', 5.78), ('CE2', 'TYR', 'CG', 'GLU', 5.05), ('CE2', 'TYR', 'CD', 'GLU', 5.78), ('CE2', 'TYR', 'OE1', 'GLU', 6.06), ('CE2', 'TYR', 'OE2', 'GLU', 6.6)], [('CZ', 'TYR', 'CB', 'GLU', 6.08), ('CZ', 'TYR', 'CG', 'GLU', 5.04), ('CZ', 'TYR', 'CD', 'GLU', 5.83), ('CZ', 'TYR', 'OE1', 'GLU', 6.48), ('CZ', 'TYR', 'OE2', 'GLU', 6.32)], [('OH', 'TYR', 'CB', 'GLU', 6.4), ('OH', 'TYR', 'CG', 'GLU', 5.02), ('OH', 'TYR', 'CD', 'GLU', 5.35), ('OH', 'TYR', 'OE1', 'GLU', 6.12), ('OH', 'TYR', 'OE2', 'GLU', 5.49)]]}
ALA_GLU = { 
	'distances':
		[8.92, 7.94, 7.26, 6.74, 7.66],
	'comparisons':
		[('C', 'ALA', 'CB', 'GLU', 8.92), ('C', 'ALA', 'CG', 'GLU', 7.94), ('C', 'ALA', 'CD', 'GLU', 7.26), ('C', 'ALA', 'OE1', 'GLU', 6.74), ('C', 'ALA', 'OE2', 'GLU', 7.66)]}
GLY_GLU = { 
	'distances':
		[[11.11, 10.29, 9.12, 8.26, 9.27], [11.75, 10.82, 9.73, 8.99, 9.83], [11.11, 10.1, 9.19, 8.59, 9.35], [10.06, 8.96, 8.21, 7.79, 8.39]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'GLU', 11.11), ('O', 'GLY', 'CG', 'GLU', 10.29), ('O', 'GLY', 'CD', 'GLU', 9.12), ('O', 'GLY', 'OE1', 'GLU', 8.26), ('O', 'GLY', 'OE2', 'GLU', 9.27)], [('C', 'GLY', 'CB', 'GLU', 11.75), ('C', 'GLY', 'CG', 'GLU', 10.82), ('C', 'GLY', 'CD', 'GLU', 9.73), ('C', 'GLY', 'OE1', 'GLU', 8.99), ('C', 'GLY', 'OE2', 'GLU', 9.83)], [('CA', 'GLY', 'CB', 'GLU', 11.11), ('CA', 'GLY', 'CG', 'GLU', 10.1), ('CA', 'GLY', 'CD', 'GLU', 9.19), ('CA', 'GLY', 'OE1', 'GLU', 8.59), ('CA', 'GLY', 'OE2', 'GLU', 9.35)], [('N', 'GLY', 'CB', 'GLU', 10.06), ('N', 'GLY', 'CG', 'GLU', 8.96), ('N', 'GLY', 'CD', 'GLU', 8.21), ('N', 'GLY', 'OE1', 'GLU', 7.79), ('N', 'GLY', 'OE2', 'GLU', 8.39)]]}
ALA_SER = { 
	'distances':
		[5.51],
	'comparisons':
		[('C', 'ALA', 'CB', 'SER', 5.51)]}
SER_GLU = { 
	'distances':
		[8.12, 6.73, 5.78, 5.97, 5.35],
	'comparisons':
		[('CB', 'SER', 'CB', 'GLU', 8.12), ('CB', 'SER', 'CG', 'GLU', 6.73), ('CB', 'SER', 'CD', 'GLU', 5.78), ('CB', 'SER', 'OE1', 'GLU', 5.97), ('CB', 'SER', 'OE2', 'GLU', 5.35)]}
ALA_GLY = { 
	'distances':
		[5.63, 5.56, 4.39, 3.34],
	'comparisons':
		[('C', 'ALA', 'O', 'GLY', 5.63), ('C', 'ALA', 'C', 'GLY', 5.56), ('C', 'ALA', 'CA', 'GLY', 4.39), ('C', 'ALA', 'N', 'GLY', 3.34)]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(SER_TYR, d, 'Pab_1b8f_4_3_1_3')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(SER_GLY, d, 'Pab_1b8f_4_3_1_3')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ALA_TYR, d, 'Pab_1b8f_4_3_1_3')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(GLY_TYR, d, 'Pab_1b8f_4_3_1_3')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(TYR_GLU, d, 'Pab_1b8f_4_3_1_3')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(ALA_GLU, d, 'Pab_1b8f_4_3_1_3')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(GLY_GLU, d, 'Pab_1b8f_4_3_1_3')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(ALA_SER, d, 'Pab_1b8f_4_3_1_3')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(SER_GLU, d, 'Pab_1b8f_4_3_1_3')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(ALA_GLY, d, 'Pab_1b8f_4_3_1_3')
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