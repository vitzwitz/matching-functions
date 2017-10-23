'''
FUNC:A_1og1_2_4_2_31
PDB:1og1
EC:2.4.2.31
RESI:ser,glu,arg,glu
LOCI:a-147,159,184,189;
'''
import motifFunctions as cmd
SER_ARG = { 
	'distances':
		[[12.43, 11.31, 11.98, 12.83, 13.79, 14.06, 14.61], [12.36, 11.22, 11.91, 12.59, 13.56, 13.96, 14.26]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ARG', 12.43), ('CB', 'SER', 'CG', 'ARG', 11.31), ('CB', 'SER', 'CD', 'ARG', 11.98), ('CB', 'SER', 'NE', 'ARG', 12.83), ('CB', 'SER', 'CZ', 'ARG', 13.79), ('CB', 'SER', 'NH1', 'ARG', 14.06), ('CB', 'SER', 'NH2', 'ARG', 14.61)], [('OG', 'SER', 'CB', 'ARG', 12.36), ('OG', 'SER', 'CG', 'ARG', 11.22), ('OG', 'SER', 'CD', 'ARG', 11.91), ('OG', 'SER', 'NE', 'ARG', 12.59), ('OG', 'SER', 'CZ', 'ARG', 13.56), ('OG', 'SER', 'NH1', 'ARG', 13.96), ('OG', 'SER', 'NH2', 'ARG', 14.26)]]}
GLU_ARG = { 
	'distances':
		[[8.73, 8.32, 9.59, 10.63, 11.89, 12.33, 12.84], [9.8, 9.22, 10.43, 11.36, 12.61, 13.1, 13.48], [9.54, 8.73, 9.82, 10.63, 11.82, 12.36, 12.62], [8.48, 7.63, 8.72, 9.46, 10.66, 11.26, 11.42], [10.6, 9.67, 10.64, 11.39, 12.52, 13.04, 13.28], [12.51, 11.56, 10.64, 11.46, 11.26, 10.21, 12.28], [12.4, 11.61, 10.59, 11.37, 11.06, 9.88, 12.06], [12.93, 12.14, 10.96, 11.53, 11.01, 9.78, 11.86], [12.74, 11.84, 10.6, 11.04, 10.47, 9.28, 11.23], [13.7, 13.02, 11.8, 12.32, 11.72, 10.44, 12.52]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ARG', 8.73), ('CB', 'GLU', 'CG', 'ARG', 8.32), ('CB', 'GLU', 'CD', 'ARG', 9.59), ('CB', 'GLU', 'NE', 'ARG', 10.63), ('CB', 'GLU', 'CZ', 'ARG', 11.89), ('CB', 'GLU', 'NH1', 'ARG', 12.33), ('CB', 'GLU', 'NH2', 'ARG', 12.84)], [('CG', 'GLU', 'CB', 'ARG', 9.8), ('CG', 'GLU', 'CG', 'ARG', 9.22), ('CG', 'GLU', 'CD', 'ARG', 10.43), ('CG', 'GLU', 'NE', 'ARG', 11.36), ('CG', 'GLU', 'CZ', 'ARG', 12.61), ('CG', 'GLU', 'NH1', 'ARG', 13.1), ('CG', 'GLU', 'NH2', 'ARG', 13.48)], [('CD', 'GLU', 'CB', 'ARG', 9.54), ('CD', 'GLU', 'CG', 'ARG', 8.73), ('CD', 'GLU', 'CD', 'ARG', 9.82), ('CD', 'GLU', 'NE', 'ARG', 10.63), ('CD', 'GLU', 'CZ', 'ARG', 11.82), ('CD', 'GLU', 'NH1', 'ARG', 12.36), ('CD', 'GLU', 'NH2', 'ARG', 12.62)], [('OE1', 'GLU', 'CB', 'ARG', 8.48), ('OE1', 'GLU', 'CG', 'ARG', 7.63), ('OE1', 'GLU', 'CD', 'ARG', 8.72), ('OE1', 'GLU', 'NE', 'ARG', 9.46), ('OE1', 'GLU', 'CZ', 'ARG', 10.66), ('OE1', 'GLU', 'NH1', 'ARG', 11.26), ('OE1', 'GLU', 'NH2', 'ARG', 11.42)], [('OE2', 'GLU', 'CB', 'ARG', 10.6), ('OE2', 'GLU', 'CG', 'ARG', 9.67), ('OE2', 'GLU', 'CD', 'ARG', 10.64), ('OE2', 'GLU', 'NE', 'ARG', 11.39), ('OE2', 'GLU', 'CZ', 'ARG', 12.52), ('OE2', 'GLU', 'NH1', 'ARG', 13.04), ('OE2', 'GLU', 'NH2', 'ARG', 13.28)], [('CB', 'GLU', 'CB', 'ARG', 12.51), ('CB', 'GLU', 'CG', 'ARG', 11.56), ('CB', 'GLU', 'CD', 'ARG', 10.64), ('CB', 'GLU', 'NE', 'ARG', 11.46), ('CB', 'GLU', 'CZ', 'ARG', 11.26), ('CB', 'GLU', 'NH1', 'ARG', 10.21), ('CB', 'GLU', 'NH2', 'ARG', 12.28)], [('CG', 'GLU', 'CB', 'ARG', 12.4), ('CG', 'GLU', 'CG', 'ARG', 11.61), ('CG', 'GLU', 'CD', 'ARG', 10.59), ('CG', 'GLU', 'NE', 'ARG', 11.37), ('CG', 'GLU', 'CZ', 'ARG', 11.06), ('CG', 'GLU', 'NH1', 'ARG', 9.88), ('CG', 'GLU', 'NH2', 'ARG', 12.06)], [('CD', 'GLU', 'CB', 'ARG', 12.93), ('CD', 'GLU', 'CG', 'ARG', 12.14), ('CD', 'GLU', 'CD', 'ARG', 10.96), ('CD', 'GLU', 'NE', 'ARG', 11.53), ('CD', 'GLU', 'CZ', 'ARG', 11.01), ('CD', 'GLU', 'NH1', 'ARG', 9.78), ('CD', 'GLU', 'NH2', 'ARG', 11.86)], [('OE1', 'GLU', 'CB', 'ARG', 12.74), ('OE1', 'GLU', 'CG', 'ARG', 11.84), ('OE1', 'GLU', 'CD', 'ARG', 10.6), ('OE1', 'GLU', 'NE', 'ARG', 11.04), ('OE1', 'GLU', 'CZ', 'ARG', 10.47), ('OE1', 'GLU', 'NH1', 'ARG', 9.28), ('OE1', 'GLU', 'NH2', 'ARG', 11.23)], [('OE2', 'GLU', 'CB', 'ARG', 13.7), ('OE2', 'GLU', 'CG', 'ARG', 13.02), ('OE2', 'GLU', 'CD', 'ARG', 11.8), ('OE2', 'GLU', 'NE', 'ARG', 12.32), ('OE2', 'GLU', 'CZ', 'ARG', 11.72), ('OE2', 'GLU', 'NH1', 'ARG', 10.44), ('OE2', 'GLU', 'NH2', 'ARG', 12.52)]]}
GLU_SER = { 
	'distances':
		[[7.63, 7.93], [6.53, 6.69], [5.78, 5.63], [6.59, 6.29], [4.77, 4.43], [13.45, 14.09], [14.61, 15.23], [15.58, 16.09], [15.2, 15.61], [16.8, 17.33]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'SER', 7.63), ('CB', 'GLU', 'OG', 'SER', 7.93)], [('CG', 'GLU', 'CB', 'SER', 6.53), ('CG', 'GLU', 'OG', 'SER', 6.69)], [('CD', 'GLU', 'CB', 'SER', 5.78), ('CD', 'GLU', 'OG', 'SER', 5.63)], [('OE1', 'GLU', 'CB', 'SER', 6.59), ('OE1', 'GLU', 'OG', 'SER', 6.29)], [('OE2', 'GLU', 'CB', 'SER', 4.77), ('OE2', 'GLU', 'OG', 'SER', 4.43)], [('CB', 'GLU', 'CB', 'SER', 13.45), ('CB', 'GLU', 'OG', 'SER', 14.09)], [('CG', 'GLU', 'CB', 'SER', 14.61), ('CG', 'GLU', 'OG', 'SER', 15.23)], [('CD', 'GLU', 'CB', 'SER', 15.58), ('CD', 'GLU', 'OG', 'SER', 16.09)], [('OE1', 'GLU', 'CB', 'SER', 15.2), ('OE1', 'GLU', 'OG', 'SER', 15.61)], [('OE2', 'GLU', 'CB', 'SER', 16.8), ('OE2', 'GLU', 'OG', 'SER', 17.33)]]}
GLU_GLU = { 
	'distances':
		[[14.04, 14.63, 15.7, 15.58, 16.75], [14.57, 15.31, 16.36, 16.15, 17.46], [14.03, 14.83, 15.77, 15.44, 16.92], [13.61, 14.33, 15.18, 14.81, 16.31], [14.24, 15.16, 16.08, 15.7, 17.27], [14.04, 14.57, 14.03, 13.61, 14.24], [14.63, 15.31, 14.83, 14.33, 15.16], [15.7, 16.36, 15.77, 15.18, 16.08], [15.58, 16.15, 15.44, 14.81, 15.7], [16.75, 17.46, 16.92, 16.31, 17.27]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'GLU', 14.04), ('CB', 'GLU', 'CG', 'GLU', 14.63), ('CB', 'GLU', 'CD', 'GLU', 15.7), ('CB', 'GLU', 'OE1', 'GLU', 15.58), ('CB', 'GLU', 'OE2', 'GLU', 16.75)], [('CG', 'GLU', 'CB', 'GLU', 14.57), ('CG', 'GLU', 'CG', 'GLU', 15.31), ('CG', 'GLU', 'CD', 'GLU', 16.36), ('CG', 'GLU', 'OE1', 'GLU', 16.15), ('CG', 'GLU', 'OE2', 'GLU', 17.46)], [('CD', 'GLU', 'CB', 'GLU', 14.03), ('CD', 'GLU', 'CG', 'GLU', 14.83), ('CD', 'GLU', 'CD', 'GLU', 15.77), ('CD', 'GLU', 'OE1', 'GLU', 15.44), ('CD', 'GLU', 'OE2', 'GLU', 16.92)], [('OE1', 'GLU', 'CB', 'GLU', 13.61), ('OE1', 'GLU', 'CG', 'GLU', 14.33), ('OE1', 'GLU', 'CD', 'GLU', 15.18), ('OE1', 'GLU', 'OE1', 'GLU', 14.81), ('OE1', 'GLU', 'OE2', 'GLU', 16.31)], [('OE2', 'GLU', 'CB', 'GLU', 14.24), ('OE2', 'GLU', 'CG', 'GLU', 15.16), ('OE2', 'GLU', 'CD', 'GLU', 16.08), ('OE2', 'GLU', 'OE1', 'GLU', 15.7), ('OE2', 'GLU', 'OE2', 'GLU', 17.27)], [('CB', 'GLU', 'CB', 'GLU', 14.04), ('CB', 'GLU', 'CG', 'GLU', 14.57), ('CB', 'GLU', 'CD', 'GLU', 14.03), ('CB', 'GLU', 'OE1', 'GLU', 13.61), ('CB', 'GLU', 'OE2', 'GLU', 14.24)], [('CG', 'GLU', 'CB', 'GLU', 14.63), ('CG', 'GLU', 'CG', 'GLU', 15.31), ('CG', 'GLU', 'CD', 'GLU', 14.83), ('CG', 'GLU', 'OE1', 'GLU', 14.33), ('CG', 'GLU', 'OE2', 'GLU', 15.16)], [('CD', 'GLU', 'CB', 'GLU', 15.7), ('CD', 'GLU', 'CG', 'GLU', 16.36), ('CD', 'GLU', 'CD', 'GLU', 15.77), ('CD', 'GLU', 'OE1', 'GLU', 15.18), ('CD', 'GLU', 'OE2', 'GLU', 16.08)], [('OE1', 'GLU', 'CB', 'GLU', 15.58), ('OE1', 'GLU', 'CG', 'GLU', 16.15), ('OE1', 'GLU', 'CD', 'GLU', 15.44), ('OE1', 'GLU', 'OE1', 'GLU', 14.81), ('OE1', 'GLU', 'OE2', 'GLU', 15.7)], [('OE2', 'GLU', 'CB', 'GLU', 16.75), ('OE2', 'GLU', 'CG', 'GLU', 17.46), ('OE2', 'GLU', 'CD', 'GLU', 16.92), ('OE2', 'GLU', 'OE1', 'GLU', 16.31), ('OE2', 'GLU', 'OE2', 'GLU', 17.27)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(SER_ARG, d, 'A_1og1_2_4_2_31')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_ARG, d, 'A_1og1_2_4_2_31')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_SER, d, 'A_1og1_2_4_2_31')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(GLU_GLU, d, 'A_1og1_2_4_2_31')
	if match4 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'SER_ARG' :  match1,
		'GLU_ARG' :  match2,
		'GLU_SER' :  match3,
		'GLU_GLU' :  match4}