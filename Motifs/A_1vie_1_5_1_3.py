'''
FUNC:A_1vie_1_5_1_3
PDB:1vie
EC:1.5.1.3
RESI:lys,gln,ile,tyr
LOCI:a-32,67,68,69;
'''
import motifFunctions as cmd
GLN_LYS = { 
	'distances':
		[[10.69, 9.83, 9.05, 9.92, 11.07], [10.9, 10.0, 8.99, 9.65, 10.73], [11.86, 11.1, 10.01, 10.65, 11.6], [12.81, 12.08, 11.08, 11.8, 12.76], [11.64, 11.0, 9.8, 10.37, 11.14]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'LYS', 10.69), ('CB', 'GLN', 'CG', 'LYS', 9.83), ('CB', 'GLN', 'CD', 'LYS', 9.05), ('CB', 'GLN', 'CE', 'LYS', 9.92), ('CB', 'GLN', 'NZ', 'LYS', 11.07)], [('CG', 'GLN', 'CB', 'LYS', 10.9), ('CG', 'GLN', 'CG', 'LYS', 10.0), ('CG', 'GLN', 'CD', 'LYS', 8.99), ('CG', 'GLN', 'CE', 'LYS', 9.65), ('CG', 'GLN', 'NZ', 'LYS', 10.73)], [('CD', 'GLN', 'CB', 'LYS', 11.86), ('CD', 'GLN', 'CG', 'LYS', 11.1), ('CD', 'GLN', 'CD', 'LYS', 10.01), ('CD', 'GLN', 'CE', 'LYS', 10.65), ('CD', 'GLN', 'NZ', 'LYS', 11.6)], [('OE1', 'GLN', 'CB', 'LYS', 12.81), ('OE1', 'GLN', 'CG', 'LYS', 12.08), ('OE1', 'GLN', 'CD', 'LYS', 11.08), ('OE1', 'GLN', 'CE', 'LYS', 11.8), ('OE1', 'GLN', 'NZ', 'LYS', 12.76)], [('NE2', 'GLN', 'CB', 'LYS', 11.64), ('NE2', 'GLN', 'CG', 'LYS', 11.0), ('NE2', 'GLN', 'CD', 'LYS', 9.8), ('NE2', 'GLN', 'CE', 'LYS', 10.37), ('NE2', 'GLN', 'NZ', 'LYS', 11.14)]]}
TYR_ILE = { 
	'distances':
		[[7.68, 8.41, 8.88, 9.59], [7.75, 8.34, 8.92, 9.7], [8.26, 8.53, 9.53, 9.89], [7.84, 8.59, 8.77, 10.04], [8.77, 8.92, 9.93, 10.36], [8.44, 9.03, 9.27, 10.55], [8.87, 9.17, 9.83, 10.69], [9.76, 9.93, 10.6, 11.46]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'ILE', 7.68), ('CB', 'TYR', 'CG1', 'ILE', 8.41), ('CB', 'TYR', 'CG2', 'ILE', 8.88), ('CB', 'TYR', 'CD1', 'ILE', 9.59)], [('CG', 'TYR', 'CB', 'ILE', 7.75), ('CG', 'TYR', 'CG1', 'ILE', 8.34), ('CG', 'TYR', 'CG2', 'ILE', 8.92), ('CG', 'TYR', 'CD1', 'ILE', 9.7)], [('CD1', 'TYR', 'CB', 'ILE', 8.26), ('CD1', 'TYR', 'CG1', 'ILE', 8.53), ('CD1', 'TYR', 'CG2', 'ILE', 9.53), ('CD1', 'TYR', 'CD1', 'ILE', 9.89)], [('CD2', 'TYR', 'CB', 'ILE', 7.84), ('CD2', 'TYR', 'CG1', 'ILE', 8.59), ('CD2', 'TYR', 'CG2', 'ILE', 8.77), ('CD2', 'TYR', 'CD1', 'ILE', 10.04)], [('CE1', 'TYR', 'CB', 'ILE', 8.77), ('CE1', 'TYR', 'CG1', 'ILE', 8.92), ('CE1', 'TYR', 'CG2', 'ILE', 9.93), ('CE1', 'TYR', 'CD1', 'ILE', 10.36)], [('CE2', 'TYR', 'CB', 'ILE', 8.44), ('CE2', 'TYR', 'CG1', 'ILE', 9.03), ('CE2', 'TYR', 'CG2', 'ILE', 9.27), ('CE2', 'TYR', 'CD1', 'ILE', 10.55)], [('CZ', 'TYR', 'CB', 'ILE', 8.87), ('CZ', 'TYR', 'CG1', 'ILE', 9.17), ('CZ', 'TYR', 'CG2', 'ILE', 9.83), ('CZ', 'TYR', 'CD1', 'ILE', 10.69)], [('OH', 'TYR', 'CB', 'ILE', 9.76), ('OH', 'TYR', 'CG1', 'ILE', 9.93), ('OH', 'TYR', 'CG2', 'ILE', 10.6), ('OH', 'TYR', 'CD1', 'ILE', 11.46)]]}
ILE_GLN = { 
	'distances':
		[[7.84, 8.19, 9.34, 9.49, 10.51], [8.08, 8.07, 9.06, 9.25, 10.16], [8.17, 8.7, 9.7, 9.61, 10.98], [9.55, 9.51, 10.39, 10.5, 11.48]],
	'comparisons':
		[[('CB', 'ILE', 'CB', 'GLN', 7.84), ('CB', 'ILE', 'CG', 'GLN', 8.19), ('CB', 'ILE', 'CD', 'GLN', 9.34), ('CB', 'ILE', 'OE1', 'GLN', 9.49), ('CB', 'ILE', 'NE2', 'GLN', 10.51)], [('CG1', 'ILE', 'CB', 'GLN', 8.08), ('CG1', 'ILE', 'CG', 'GLN', 8.07), ('CG1', 'ILE', 'CD', 'GLN', 9.06), ('CG1', 'ILE', 'OE1', 'GLN', 9.25), ('CG1', 'ILE', 'NE2', 'GLN', 10.16)], [('CG2', 'ILE', 'CB', 'GLN', 8.17), ('CG2', 'ILE', 'CG', 'GLN', 8.7), ('CG2', 'ILE', 'CD', 'GLN', 9.7), ('CG2', 'ILE', 'OE1', 'GLN', 9.61), ('CG2', 'ILE', 'NE2', 'GLN', 10.98)], [('CD1', 'ILE', 'CB', 'GLN', 9.55), ('CD1', 'ILE', 'CG', 'GLN', 9.51), ('CD1', 'ILE', 'CD', 'GLN', 10.39), ('CD1', 'ILE', 'OE1', 'GLN', 10.5), ('CD1', 'ILE', 'NE2', 'GLN', 11.48)]]}
ILE_LYS = { 
	'distances':
		[[13.57, 12.22, 11.73, 12.07, 13.51], [14.12, 12.75, 12.08, 12.26, 13.66], [14.55, 13.27, 12.84, 13.31, 14.75], [15.56, 14.16, 13.5, 13.6, 14.99]],
	'comparisons':
		[[('CB', 'ILE', 'CB', 'LYS', 13.57), ('CB', 'ILE', 'CG', 'LYS', 12.22), ('CB', 'ILE', 'CD', 'LYS', 11.73), ('CB', 'ILE', 'CE', 'LYS', 12.07), ('CB', 'ILE', 'NZ', 'LYS', 13.51)], [('CG1', 'ILE', 'CB', 'LYS', 14.12), ('CG1', 'ILE', 'CG', 'LYS', 12.75), ('CG1', 'ILE', 'CD', 'LYS', 12.08), ('CG1', 'ILE', 'CE', 'LYS', 12.26), ('CG1', 'ILE', 'NZ', 'LYS', 13.66)], [('CG2', 'ILE', 'CB', 'LYS', 14.55), ('CG2', 'ILE', 'CG', 'LYS', 13.27), ('CG2', 'ILE', 'CD', 'LYS', 12.84), ('CG2', 'ILE', 'CE', 'LYS', 13.31), ('CG2', 'ILE', 'NZ', 'LYS', 14.75)], [('CD1', 'ILE', 'CB', 'LYS', 15.56), ('CD1', 'ILE', 'CG', 'LYS', 14.16), ('CD1', 'ILE', 'CD', 'LYS', 13.5), ('CD1', 'ILE', 'CE', 'LYS', 13.6), ('CD1', 'ILE', 'NZ', 'LYS', 14.99)]]}
TYR_LYS = { 
	'distances':
		[[8.72, 7.28, 7.27, 7.51, 8.92], [7.96, 6.53, 6.23, 6.66, 8.11], [7.86, 6.41, 5.71, 5.82, 7.27], [7.78, 6.54, 6.34, 7.17, 8.55], [7.6, 6.32, 5.28, 5.59, 6.93], [7.51, 6.45, 5.99, 7.02, 8.29], [7.41, 6.33, 5.43, 6.24, 7.48], [7.68, 6.89, 5.84, 6.71, 7.7]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'LYS', 8.72), ('CB', 'TYR', 'CG', 'LYS', 7.28), ('CB', 'TYR', 'CD', 'LYS', 7.27), ('CB', 'TYR', 'CE', 'LYS', 7.51), ('CB', 'TYR', 'NZ', 'LYS', 8.92)], [('CG', 'TYR', 'CB', 'LYS', 7.96), ('CG', 'TYR', 'CG', 'LYS', 6.53), ('CG', 'TYR', 'CD', 'LYS', 6.23), ('CG', 'TYR', 'CE', 'LYS', 6.66), ('CG', 'TYR', 'NZ', 'LYS', 8.11)], [('CD1', 'TYR', 'CB', 'LYS', 7.86), ('CD1', 'TYR', 'CG', 'LYS', 6.41), ('CD1', 'TYR', 'CD', 'LYS', 5.71), ('CD1', 'TYR', 'CE', 'LYS', 5.82), ('CD1', 'TYR', 'NZ', 'LYS', 7.27)], [('CD2', 'TYR', 'CB', 'LYS', 7.78), ('CD2', 'TYR', 'CG', 'LYS', 6.54), ('CD2', 'TYR', 'CD', 'LYS', 6.34), ('CD2', 'TYR', 'CE', 'LYS', 7.17), ('CD2', 'TYR', 'NZ', 'LYS', 8.55)], [('CE1', 'TYR', 'CB', 'LYS', 7.6), ('CE1', 'TYR', 'CG', 'LYS', 6.32), ('CE1', 'TYR', 'CD', 'LYS', 5.28), ('CE1', 'TYR', 'CE', 'LYS', 5.59), ('CE1', 'TYR', 'NZ', 'LYS', 6.93)], [('CE2', 'TYR', 'CB', 'LYS', 7.51), ('CE2', 'TYR', 'CG', 'LYS', 6.45), ('CE2', 'TYR', 'CD', 'LYS', 5.99), ('CE2', 'TYR', 'CE', 'LYS', 7.02), ('CE2', 'TYR', 'NZ', 'LYS', 8.29)], [('CZ', 'TYR', 'CB', 'LYS', 7.41), ('CZ', 'TYR', 'CG', 'LYS', 6.33), ('CZ', 'TYR', 'CD', 'LYS', 5.43), ('CZ', 'TYR', 'CE', 'LYS', 6.24), ('CZ', 'TYR', 'NZ', 'LYS', 7.48)], [('OH', 'TYR', 'CB', 'LYS', 7.68), ('OH', 'TYR', 'CG', 'LYS', 6.89), ('OH', 'TYR', 'CD', 'LYS', 5.84), ('OH', 'TYR', 'CE', 'LYS', 6.71), ('OH', 'TYR', 'NZ', 'LYS', 7.7)]]}
TYR_GLN = { 
	'distances':
		[[8.61, 8.96, 10.45, 11.22, 11.04], [7.37, 7.65, 9.12, 9.95, 9.62], [7.45, 7.37, 8.74, 9.73, 9.05], [6.52, 7.09, 8.55, 9.27, 9.12], [6.68, 6.42, 7.68, 8.75, 7.83], [5.62, 6.16, 7.51, 8.28, 7.97], [5.72, 5.74, 6.99, 7.97, 7.21], [5.49, 5.29, 6.22, 7.25, 6.17]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'GLN', 8.61), ('CB', 'TYR', 'CG', 'GLN', 8.96), ('CB', 'TYR', 'CD', 'GLN', 10.45), ('CB', 'TYR', 'OE1', 'GLN', 11.22), ('CB', 'TYR', 'NE2', 'GLN', 11.04)], [('CG', 'TYR', 'CB', 'GLN', 7.37), ('CG', 'TYR', 'CG', 'GLN', 7.65), ('CG', 'TYR', 'CD', 'GLN', 9.12), ('CG', 'TYR', 'OE1', 'GLN', 9.95), ('CG', 'TYR', 'NE2', 'GLN', 9.62)], [('CD1', 'TYR', 'CB', 'GLN', 7.45), ('CD1', 'TYR', 'CG', 'GLN', 7.37), ('CD1', 'TYR', 'CD', 'GLN', 8.74), ('CD1', 'TYR', 'OE1', 'GLN', 9.73), ('CD1', 'TYR', 'NE2', 'GLN', 9.05)], [('CD2', 'TYR', 'CB', 'GLN', 6.52), ('CD2', 'TYR', 'CG', 'GLN', 7.09), ('CD2', 'TYR', 'CD', 'GLN', 8.55), ('CD2', 'TYR', 'OE1', 'GLN', 9.27), ('CD2', 'TYR', 'NE2', 'GLN', 9.12)], [('CE1', 'TYR', 'CB', 'GLN', 6.68), ('CE1', 'TYR', 'CG', 'GLN', 6.42), ('CE1', 'TYR', 'CD', 'GLN', 7.68), ('CE1', 'TYR', 'OE1', 'GLN', 8.75), ('CE1', 'TYR', 'NE2', 'GLN', 7.83)], [('CE2', 'TYR', 'CB', 'GLN', 5.62), ('CE2', 'TYR', 'CG', 'GLN', 6.16), ('CE2', 'TYR', 'CD', 'GLN', 7.51), ('CE2', 'TYR', 'OE1', 'GLN', 8.28), ('CE2', 'TYR', 'NE2', 'GLN', 7.97)], [('CZ', 'TYR', 'CB', 'GLN', 5.72), ('CZ', 'TYR', 'CG', 'GLN', 5.74), ('CZ', 'TYR', 'CD', 'GLN', 6.99), ('CZ', 'TYR', 'OE1', 'GLN', 7.97), ('CZ', 'TYR', 'NE2', 'GLN', 7.21)], [('OH', 'TYR', 'CB', 'GLN', 5.49), ('OH', 'TYR', 'CG', 'GLN', 5.29), ('OH', 'TYR', 'CD', 'GLN', 6.22), ('OH', 'TYR', 'OE1', 'GLN', 7.25), ('OH', 'TYR', 'NE2', 'GLN', 6.17)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLN_LYS, d, 'A_1vie_1_5_1_3')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(TYR_ILE, d, 'A_1vie_1_5_1_3')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ILE_GLN, d, 'A_1vie_1_5_1_3')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ILE_LYS, d, 'A_1vie_1_5_1_3')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(TYR_LYS, d, 'A_1vie_1_5_1_3')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(TYR_GLN, d, 'A_1vie_1_5_1_3')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLN_LYS' :  match1,
		'TYR_ILE' :  match2,
		'ILE_GLN' :  match3,
		'ILE_LYS' :  match4,
		'TYR_LYS' :  match5,
		'TYR_GLN' :  match6}