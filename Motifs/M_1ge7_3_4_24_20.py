'''
FUNC:M_1ge7_3_4_24_20
PDB:1ge7
EC:3.4.24.20
RESI:glu,tyr,zn
LOCI:a-118,133,200;
'''
import motifFunctions as cmd
GLU_TYR = { 
	'distances':
		[[15.25, 14.6, 13.25, 15.45, 12.81, 15.1, 13.82, 13.66], [14.3, 13.53, 12.15, 14.31, 11.6, 13.87, 12.54, 12.31], [13.29, 12.58, 11.2, 13.43, 10.74, 13.07, 11.77, 11.64], [13.72, 13.12, 11.76, 14.05, 11.41, 13.78, 12.51, 12.48], [12.2, 11.42, 10.03, 12.23, 9.51, 11.84, 10.53, 10.4]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'TYR', 15.25), ('CB', 'GLU', 'CG', 'TYR', 14.6), ('CB', 'GLU', 'CD1', 'TYR', 13.25), ('CB', 'GLU', 'CD2', 'TYR', 15.45), ('CB', 'GLU', 'CE1', 'TYR', 12.81), ('CB', 'GLU', 'CE2', 'TYR', 15.1), ('CB', 'GLU', 'CZ', 'TYR', 13.82), ('CB', 'GLU', 'OH', 'TYR', 13.66)], [('CG', 'GLU', 'CB', 'TYR', 14.3), ('CG', 'GLU', 'CG', 'TYR', 13.53), ('CG', 'GLU', 'CD1', 'TYR', 12.15), ('CG', 'GLU', 'CD2', 'TYR', 14.31), ('CG', 'GLU', 'CE1', 'TYR', 11.6), ('CG', 'GLU', 'CE2', 'TYR', 13.87), ('CG', 'GLU', 'CZ', 'TYR', 12.54), ('CG', 'GLU', 'OH', 'TYR', 12.31)], [('CD', 'GLU', 'CB', 'TYR', 13.29), ('CD', 'GLU', 'CG', 'TYR', 12.58), ('CD', 'GLU', 'CD1', 'TYR', 11.2), ('CD', 'GLU', 'CD2', 'TYR', 13.43), ('CD', 'GLU', 'CE1', 'TYR', 10.74), ('CD', 'GLU', 'CE2', 'TYR', 13.07), ('CD', 'GLU', 'CZ', 'TYR', 11.77), ('CD', 'GLU', 'OH', 'TYR', 11.64)], [('OE1', 'GLU', 'CB', 'TYR', 13.72), ('OE1', 'GLU', 'CG', 'TYR', 13.12), ('OE1', 'GLU', 'CD1', 'TYR', 11.76), ('OE1', 'GLU', 'CD2', 'TYR', 14.05), ('OE1', 'GLU', 'CE1', 'TYR', 11.41), ('OE1', 'GLU', 'CE2', 'TYR', 13.78), ('OE1', 'GLU', 'CZ', 'TYR', 12.51), ('OE1', 'GLU', 'OH', 'TYR', 12.48)], [('OE2', 'GLU', 'CB', 'TYR', 12.2), ('OE2', 'GLU', 'CG', 'TYR', 11.42), ('OE2', 'GLU', 'CD1', 'TYR', 10.03), ('OE2', 'GLU', 'CD2', 'TYR', 12.23), ('OE2', 'GLU', 'CE1', 'TYR', 9.51), ('OE2', 'GLU', 'CE2', 'TYR', 11.84), ('OE2', 'GLU', 'CZ', 'TYR', 10.53), ('OE2', 'GLU', 'OH', 'TYR', 10.4)]]}
TYR_ZN = { 
	'distances':
		[[9.67], [9.47], [8.29], [10.68], [8.53], [10.87], [9.89], [10.44]],
	'comparisons':
		[[('CB', 'TYR', 'ZN', 'ZN', 9.67)], [('CG', 'TYR', 'ZN', 'ZN', 9.47)], [('CD1', 'TYR', 'ZN', 'ZN', 8.29)], [('CD2', 'TYR', 'ZN', 'ZN', 10.68)], [('CE1', 'TYR', 'ZN', 'ZN', 8.53)], [('CE2', 'TYR', 'ZN', 'ZN', 10.87)], [('CZ', 'TYR', 'ZN', 'ZN', 9.89)], [('OH', 'TYR', 'ZN', 'ZN', 10.44)]]}
GLU_ZN = { 
	'distances':
		[[8.49], [7.95], [6.69], [6.61], [6.14]],
	'comparisons':
		[[('CB', 'GLU', 'ZN', 'ZN', 8.49)], [('CG', 'GLU', 'ZN', 'ZN', 7.95)], [('CD', 'GLU', 'ZN', 'ZN', 6.69)], [('OE1', 'GLU', 'ZN', 'ZN', 6.61)], [('OE2', 'GLU', 'ZN', 'ZN', 6.14)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_TYR, d, 'M_1ge7_3_4_24_20')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(TYR_ZN, d, 'M_1ge7_3_4_24_20')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_ZN, d, 'M_1ge7_3_4_24_20')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_TYR' :  match1,
		'TYR_ZN' :  match2,
		'GLU_ZN' :  match3}