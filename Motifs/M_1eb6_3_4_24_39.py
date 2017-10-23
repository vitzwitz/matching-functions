'''
FUNC:M_1eb6_3_4_24_39
PDB:1eb6
EC:3.4.24.39
RESI:tyr,glu,zn
LOCI:a-106,129;a-178;
'''
import motifFunctions as cmd
TYR_ZN = { 
	'distances':
		[[14.51], [14.45], [15.65], [13.3], [15.81], [13.48], [14.77], [15.2]],
	'comparisons':
		[[('CB', 'TYR', 'ZN', 'ZN', 14.51)], [('CG', 'TYR', 'ZN', 'ZN', 14.45)], [('CD1', 'TYR', 'ZN', 'ZN', 15.65)], [('CD2', 'TYR', 'ZN', 'ZN', 13.3)], [('CE1', 'TYR', 'ZN', 'ZN', 15.81)], [('CE2', 'TYR', 'ZN', 'ZN', 13.48)], [('CZ', 'TYR', 'ZN', 'ZN', 14.77)], [('OH', 'TYR', 'ZN', 'ZN', 15.2)]]}
GLU_ZN = { 
	'distances':
		[[8.45], [7.82], [6.53], [6.54], [5.84]],
	'comparisons':
		[[('CB', 'GLU', 'ZN', 'ZN', 8.45)], [('CG', 'GLU', 'ZN', 'ZN', 7.82)], [('CD', 'GLU', 'ZN', 'ZN', 6.53)], [('OE1', 'GLU', 'ZN', 'ZN', 6.54)], [('OE2', 'GLU', 'ZN', 'ZN', 5.84)]]}
TYR_GLU = { 
	'distances':
		[[11.95, 10.83, 11.43, 12.35, 11.16], [11.3, 10.32, 11.13, 12.11, 10.97], [12.05, 11.22, 12.16, 13.11, 12.1], [10.08, 9.11, 9.98, 11.01, 9.82], [11.74, 11.08, 12.18, 13.14, 12.22], [9.66, 8.91, 9.99, 11.03, 9.97], [10.56, 9.96, 11.13, 12.13, 11.21], [10.54, 10.17, 11.48, 12.44, 11.68]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'GLU', 11.95), ('CB', 'TYR', 'CG', 'GLU', 10.83), ('CB', 'TYR', 'CD', 'GLU', 11.43), ('CB', 'TYR', 'OE1', 'GLU', 12.35), ('CB', 'TYR', 'OE2', 'GLU', 11.16)], [('CG', 'TYR', 'CB', 'GLU', 11.3), ('CG', 'TYR', 'CG', 'GLU', 10.32), ('CG', 'TYR', 'CD', 'GLU', 11.13), ('CG', 'TYR', 'OE1', 'GLU', 12.11), ('CG', 'TYR', 'OE2', 'GLU', 10.97)], [('CD1', 'TYR', 'CB', 'GLU', 12.05), ('CD1', 'TYR', 'CG', 'GLU', 11.22), ('CD1', 'TYR', 'CD', 'GLU', 12.16), ('CD1', 'TYR', 'OE1', 'GLU', 13.11), ('CD1', 'TYR', 'OE2', 'GLU', 12.1)], [('CD2', 'TYR', 'CB', 'GLU', 10.08), ('CD2', 'TYR', 'CG', 'GLU', 9.11), ('CD2', 'TYR', 'CD', 'GLU', 9.98), ('CD2', 'TYR', 'OE1', 'GLU', 11.01), ('CD2', 'TYR', 'OE2', 'GLU', 9.82)], [('CE1', 'TYR', 'CB', 'GLU', 11.74), ('CE1', 'TYR', 'CG', 'GLU', 11.08), ('CE1', 'TYR', 'CD', 'GLU', 12.18), ('CE1', 'TYR', 'OE1', 'GLU', 13.14), ('CE1', 'TYR', 'OE2', 'GLU', 12.22)], [('CE2', 'TYR', 'CB', 'GLU', 9.66), ('CE2', 'TYR', 'CG', 'GLU', 8.91), ('CE2', 'TYR', 'CD', 'GLU', 9.99), ('CE2', 'TYR', 'OE1', 'GLU', 11.03), ('CE2', 'TYR', 'OE2', 'GLU', 9.97)], [('CZ', 'TYR', 'CB', 'GLU', 10.56), ('CZ', 'TYR', 'CG', 'GLU', 9.96), ('CZ', 'TYR', 'CD', 'GLU', 11.13), ('CZ', 'TYR', 'OE1', 'GLU', 12.13), ('CZ', 'TYR', 'OE2', 'GLU', 11.21)], [('OH', 'TYR', 'CB', 'GLU', 10.54), ('OH', 'TYR', 'CG', 'GLU', 10.17), ('OH', 'TYR', 'CD', 'GLU', 11.48), ('OH', 'TYR', 'OE1', 'GLU', 12.44), ('OH', 'TYR', 'OE2', 'GLU', 11.68)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(TYR_ZN, d, 'M_1eb6_3_4_24_39')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_ZN, d, 'M_1eb6_3_4_24_39')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(TYR_GLU, d, 'M_1eb6_3_4_24_39')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'TYR_ZN' :  match1,
		'GLU_ZN' :  match2,
		'TYR_GLU' :  match3}