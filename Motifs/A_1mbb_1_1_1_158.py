'''
FUNC:A_1mbb_1_1_1_158
PDB:1mbb
EC:1.1.1.158
RESI:arg,ser,glu
LOCI:a-159,229,325;
'''
import motifFunctions as cmd
SER_ARG = { 
	'distances':
		[[10.64, 9.48, 9.36, 8.36, 8.7, 9.91, 8.01], [11.27, 9.97, 9.8, 8.62, 8.68, 9.82, 7.77]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ARG', 10.64), ('CB', 'SER', 'CG', 'ARG', 9.48), ('CB', 'SER', 'CD', 'ARG', 9.36), ('CB', 'SER', 'NE', 'ARG', 8.36), ('CB', 'SER', 'CZ', 'ARG', 8.7), ('CB', 'SER', 'NH1', 'ARG', 9.91), ('CB', 'SER', 'NH2', 'ARG', 8.01)], [('OG', 'SER', 'CB', 'ARG', 11.27), ('OG', 'SER', 'CG', 'ARG', 9.97), ('OG', 'SER', 'CD', 'ARG', 9.8), ('OG', 'SER', 'NE', 'ARG', 8.62), ('OG', 'SER', 'CZ', 'ARG', 8.68), ('OG', 'SER', 'NH1', 'ARG', 9.82), ('OG', 'SER', 'NH2', 'ARG', 7.77)]]}
GLU_ARG = { 
	'distances':
		[[7.46, 7.22, 7.51, 7.67, 8.82, 9.82, 9.18], [6.46, 6.16, 6.18, 6.42, 7.66, 8.66, 8.14], [6.9, 6.14, 5.85, 5.58, 6.71, 7.87, 6.94], [7.03, 6.01, 5.94, 5.4, 6.3, 7.47, 6.37], [7.55, 6.77, 6.09, 5.69, 6.78, 8.0, 6.9]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ARG', 7.46), ('CB', 'GLU', 'CG', 'ARG', 7.22), ('CB', 'GLU', 'CD', 'ARG', 7.51), ('CB', 'GLU', 'NE', 'ARG', 7.67), ('CB', 'GLU', 'CZ', 'ARG', 8.82), ('CB', 'GLU', 'NH1', 'ARG', 9.82), ('CB', 'GLU', 'NH2', 'ARG', 9.18)], [('CG', 'GLU', 'CB', 'ARG', 6.46), ('CG', 'GLU', 'CG', 'ARG', 6.16), ('CG', 'GLU', 'CD', 'ARG', 6.18), ('CG', 'GLU', 'NE', 'ARG', 6.42), ('CG', 'GLU', 'CZ', 'ARG', 7.66), ('CG', 'GLU', 'NH1', 'ARG', 8.66), ('CG', 'GLU', 'NH2', 'ARG', 8.14)], [('CD', 'GLU', 'CB', 'ARG', 6.9), ('CD', 'GLU', 'CG', 'ARG', 6.14), ('CD', 'GLU', 'CD', 'ARG', 5.85), ('CD', 'GLU', 'NE', 'ARG', 5.58), ('CD', 'GLU', 'CZ', 'ARG', 6.71), ('CD', 'GLU', 'NH1', 'ARG', 7.87), ('CD', 'GLU', 'NH2', 'ARG', 6.94)], [('OE1', 'GLU', 'CB', 'ARG', 7.03), ('OE1', 'GLU', 'CG', 'ARG', 6.01), ('OE1', 'GLU', 'CD', 'ARG', 5.94), ('OE1', 'GLU', 'NE', 'ARG', 5.4), ('OE1', 'GLU', 'CZ', 'ARG', 6.3), ('OE1', 'GLU', 'NH1', 'ARG', 7.47), ('OE1', 'GLU', 'NH2', 'ARG', 6.37)], [('OE2', 'GLU', 'CB', 'ARG', 7.55), ('OE2', 'GLU', 'CG', 'ARG', 6.77), ('OE2', 'GLU', 'CD', 'ARG', 6.09), ('OE2', 'GLU', 'NE', 'ARG', 5.69), ('OE2', 'GLU', 'CZ', 'ARG', 6.78), ('OE2', 'GLU', 'NH1', 'ARG', 8.0), ('OE2', 'GLU', 'NH2', 'ARG', 6.9)]]}
GLU_SER = { 
	'distances':
		[[7.38, 8.64], [7.6, 8.7], [6.49, 7.46], [5.73, 6.59], [6.74, 7.62]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'SER', 7.38), ('CB', 'GLU', 'OG', 'SER', 8.64)], [('CG', 'GLU', 'CB', 'SER', 7.6), ('CG', 'GLU', 'OG', 'SER', 8.7)], [('CD', 'GLU', 'CB', 'SER', 6.49), ('CD', 'GLU', 'OG', 'SER', 7.46)], [('OE1', 'GLU', 'CB', 'SER', 5.73), ('OE1', 'GLU', 'OG', 'SER', 6.59)], [('OE2', 'GLU', 'CB', 'SER', 6.74), ('OE2', 'GLU', 'OG', 'SER', 7.62)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(SER_ARG, d, 'A_1mbb_1_1_1_158')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_ARG, d, 'A_1mbb_1_1_1_158')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_SER, d, 'A_1mbb_1_1_1_158')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'SER_ARG' :  match1,
		'GLU_ARG' :  match2,
		'GLU_SER' :  match3}