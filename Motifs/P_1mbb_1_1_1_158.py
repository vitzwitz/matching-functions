'''
FUNC:P_1mbb_1_1_1_158
PDB:1mbb
EC:1.1.1.158
RESI:arg,ser,glu
LOCI:a-159,229,325;
'''
import motifFunctions as cmd
ARG_SER = { 
	'distances':
		[[10.64, 11.27], [9.48, 9.97], [9.36, 9.8], [8.36, 8.62], [8.7, 8.68], [9.91, 9.82], [8.01, 7.77]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'SER', 10.64), ('CB', 'ARG', 'OG', 'SER', 11.27)], [('CG', 'ARG', 'CB', 'SER', 9.48), ('CG', 'ARG', 'OG', 'SER', 9.97)], [('CD', 'ARG', 'CB', 'SER', 9.36), ('CD', 'ARG', 'OG', 'SER', 9.8)], [('NE', 'ARG', 'CB', 'SER', 8.36), ('NE', 'ARG', 'OG', 'SER', 8.62)], [('CZ', 'ARG', 'CB', 'SER', 8.7), ('CZ', 'ARG', 'OG', 'SER', 8.68)], [('NH1', 'ARG', 'CB', 'SER', 9.91), ('NH1', 'ARG', 'OG', 'SER', 9.82)], [('NH2', 'ARG', 'CB', 'SER', 8.01), ('NH2', 'ARG', 'OG', 'SER', 7.77)]]}
ARG_GLU = { 
	'distances':
		[[7.46, 6.46, 6.9, 7.03, 7.55], [7.22, 6.16, 6.14, 6.01, 6.77], [7.51, 6.18, 5.85, 5.94, 6.09], [7.67, 6.42, 5.58, 5.4, 5.69], [8.82, 7.66, 6.71, 6.3, 6.78], [9.82, 8.66, 7.87, 7.47, 8.0], [9.18, 8.14, 6.94, 6.37, 6.9]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'GLU', 7.46), ('CB', 'ARG', 'CG', 'GLU', 6.46), ('CB', 'ARG', 'CD', 'GLU', 6.9), ('CB', 'ARG', 'OE1', 'GLU', 7.03), ('CB', 'ARG', 'OE2', 'GLU', 7.55)], [('CG', 'ARG', 'CB', 'GLU', 7.22), ('CG', 'ARG', 'CG', 'GLU', 6.16), ('CG', 'ARG', 'CD', 'GLU', 6.14), ('CG', 'ARG', 'OE1', 'GLU', 6.01), ('CG', 'ARG', 'OE2', 'GLU', 6.77)], [('CD', 'ARG', 'CB', 'GLU', 7.51), ('CD', 'ARG', 'CG', 'GLU', 6.18), ('CD', 'ARG', 'CD', 'GLU', 5.85), ('CD', 'ARG', 'OE1', 'GLU', 5.94), ('CD', 'ARG', 'OE2', 'GLU', 6.09)], [('NE', 'ARG', 'CB', 'GLU', 7.67), ('NE', 'ARG', 'CG', 'GLU', 6.42), ('NE', 'ARG', 'CD', 'GLU', 5.58), ('NE', 'ARG', 'OE1', 'GLU', 5.4), ('NE', 'ARG', 'OE2', 'GLU', 5.69)], [('CZ', 'ARG', 'CB', 'GLU', 8.82), ('CZ', 'ARG', 'CG', 'GLU', 7.66), ('CZ', 'ARG', 'CD', 'GLU', 6.71), ('CZ', 'ARG', 'OE1', 'GLU', 6.3), ('CZ', 'ARG', 'OE2', 'GLU', 6.78)], [('NH1', 'ARG', 'CB', 'GLU', 9.82), ('NH1', 'ARG', 'CG', 'GLU', 8.66), ('NH1', 'ARG', 'CD', 'GLU', 7.87), ('NH1', 'ARG', 'OE1', 'GLU', 7.47), ('NH1', 'ARG', 'OE2', 'GLU', 8.0)], [('NH2', 'ARG', 'CB', 'GLU', 9.18), ('NH2', 'ARG', 'CG', 'GLU', 8.14), ('NH2', 'ARG', 'CD', 'GLU', 6.94), ('NH2', 'ARG', 'OE1', 'GLU', 6.37), ('NH2', 'ARG', 'OE2', 'GLU', 6.9)]]}
SER_GLU = { 
	'distances':
		[[7.38, 7.6, 6.49, 5.73, 6.74], [8.64, 8.7, 7.46, 6.59, 7.62]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'GLU', 7.38), ('CB', 'SER', 'CG', 'GLU', 7.6), ('CB', 'SER', 'CD', 'GLU', 6.49), ('CB', 'SER', 'OE1', 'GLU', 5.73), ('CB', 'SER', 'OE2', 'GLU', 6.74)], [('OG', 'SER', 'CB', 'GLU', 8.64), ('OG', 'SER', 'CG', 'GLU', 8.7), ('OG', 'SER', 'CD', 'GLU', 7.46), ('OG', 'SER', 'OE1', 'GLU', 6.59), ('OG', 'SER', 'OE2', 'GLU', 7.62)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ARG_SER, d, 'P_1mbb_1_1_1_158')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ARG_GLU, d, 'P_1mbb_1_1_1_158')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(SER_GLU, d, 'P_1mbb_1_1_1_158')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ARG_SER' :  match1,
		'ARG_GLU' :  match2,
		'SER_GLU' :  match3}