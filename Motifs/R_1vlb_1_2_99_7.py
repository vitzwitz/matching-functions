'''
FUNC:R_1vlb_1_2_99_7
PDB:1vlb
EC:1.2.99.7
RESI:glu,fes,fes
LOCI:a-869,908,909;
'''
import motifFunctions as cmd
GLU_FESI = { 
	'distances':
		[[28.83, 31.33, 30.43, 29.84], [28.01, 30.5, 29.69, 28.94], [28.84, 31.33, 30.58, 29.71], [28.52, 31.04, 30.29, 29.38], [29.84, 32.3, 31.59, 30.65]],
	'comparisons':
		[[('CB', 'GLU', 'FE1', 'FESI', 28.83), ('CB', 'GLU', 'FE2', 'FESI', 31.33), ('CB', 'GLU', 'S1', 'FESI', 30.43), ('CB', 'GLU', 'S2', 'FESI', 29.84)], [('CG', 'GLU', 'FE1', 'FESI', 28.01), ('CG', 'GLU', 'FE2', 'FESI', 30.5), ('CG', 'GLU', 'S1', 'FESI', 29.69), ('CG', 'GLU', 'S2', 'FESI', 28.94)], [('CD', 'GLU', 'FE1', 'FESI', 28.84), ('CD', 'GLU', 'FE2', 'FESI', 31.33), ('CD', 'GLU', 'S1', 'FESI', 30.58), ('CD', 'GLU', 'S2', 'FESI', 29.71)], [('OE1', 'GLU', 'FE1', 'FESI', 28.52), ('OE1', 'GLU', 'FE2', 'FESI', 31.04), ('OE1', 'GLU', 'S1', 'FESI', 30.29), ('OE1', 'GLU', 'S2', 'FESI', 29.38)], [('OE2', 'GLU', 'FE1', 'FESI', 29.84), ('OE2', 'GLU', 'FE2', 'FESI', 32.3), ('OE2', 'GLU', 'S1', 'FESI', 31.59), ('OE2', 'GLU', 'S2', 'FESI', 30.65)]]}
FES_FES = { 
	'distances':
		[[15.16, 16.99, 16.5, 15.71], [14.27, 15.97, 15.25, 15.04], [16.05, 17.64, 17.11, 16.58], [13.21, 15.15, 14.48, 13.97], [15.16, 14.27, 16.05, 13.21], [16.99, 15.97, 17.64, 15.15], [16.5, 15.25, 17.11, 14.48], [15.71, 15.04, 16.58, 13.97]],
	'comparisons':
		[[('FE1', 'FES', 'FE1', 'FES', 15.16), ('FE1', 'FES', 'FE2', 'FES', 16.99), ('FE1', 'FES', 'S1', 'FES', 16.5), ('FE1', 'FES', 'S2', 'FES', 15.71)], [('FE2', 'FES', 'FE1', 'FES', 14.27), ('FE2', 'FES', 'FE2', 'FES', 15.97), ('FE2', 'FES', 'S1', 'FES', 15.25), ('FE2', 'FES', 'S2', 'FES', 15.04)], [('S1', 'FES', 'FE1', 'FES', 16.05), ('S1', 'FES', 'FE2', 'FES', 17.64), ('S1', 'FES', 'S1', 'FES', 17.11), ('S1', 'FES', 'S2', 'FES', 16.58)], [('S2', 'FES', 'FE1', 'FES', 13.21), ('S2', 'FES', 'FE2', 'FES', 15.15), ('S2', 'FES', 'S1', 'FES', 14.48), ('S2', 'FES', 'S2', 'FES', 13.97)], [('FE1', 'FES', 'FE1', 'FES', 15.16), ('FE1', 'FES', 'FE2', 'FES', 14.27), ('FE1', 'FES', 'S1', 'FES', 16.05), ('FE1', 'FES', 'S2', 'FES', 13.21)], [('FE2', 'FES', 'FE1', 'FES', 16.99), ('FE2', 'FES', 'FE2', 'FES', 15.97), ('FE2', 'FES', 'S1', 'FES', 17.64), ('FE2', 'FES', 'S2', 'FES', 15.15)], [('S1', 'FES', 'FE1', 'FES', 16.5), ('S1', 'FES', 'FE2', 'FES', 15.25), ('S1', 'FES', 'S1', 'FES', 17.11), ('S1', 'FES', 'S2', 'FES', 14.48)], [('S2', 'FES', 'FE1', 'FES', 15.71), ('S2', 'FES', 'FE2', 'FES', 15.04), ('S2', 'FES', 'S1', 'FES', 16.58), ('S2', 'FES', 'S2', 'FES', 13.97)]]}
FES_GLU = { 
	'distances':
		[[18.43, 17.71, 18.76, 18.93, 19.46], [20.06, 19.5, 20.66, 20.86, 21.41], [19.43, 18.84, 19.98, 20.28, 20.61], [19.45, 18.76, 19.82, 19.89, 20.63], [28.83, 28.01, 28.84, 28.52, 29.84], [31.33, 30.5, 31.33, 31.04, 32.3], [30.43, 29.69, 30.58, 30.29, 31.59], [29.84, 28.94, 29.71, 29.38, 30.65]],
	'comparisons':
		[[('FE1', 'FES', 'CB', 'GLU', 18.43), ('FE1', 'FES', 'CG', 'GLU', 17.71), ('FE1', 'FES', 'CD', 'GLU', 18.76), ('FE1', 'FES', 'OE1', 'GLU', 18.93), ('FE1', 'FES', 'OE2', 'GLU', 19.46)], [('FE2', 'FES', 'CB', 'GLU', 20.06), ('FE2', 'FES', 'CG', 'GLU', 19.5), ('FE2', 'FES', 'CD', 'GLU', 20.66), ('FE2', 'FES', 'OE1', 'GLU', 20.86), ('FE2', 'FES', 'OE2', 'GLU', 21.41)], [('S1', 'FES', 'CB', 'GLU', 19.43), ('S1', 'FES', 'CG', 'GLU', 18.84), ('S1', 'FES', 'CD', 'GLU', 19.98), ('S1', 'FES', 'OE1', 'GLU', 20.28), ('S1', 'FES', 'OE2', 'GLU', 20.61)], [('S2', 'FES', 'CB', 'GLU', 19.45), ('S2', 'FES', 'CG', 'GLU', 18.76), ('S2', 'FES', 'CD', 'GLU', 19.82), ('S2', 'FES', 'OE1', 'GLU', 19.89), ('S2', 'FES', 'OE2', 'GLU', 20.63)], [('FE1', 'FES', 'CB', 'GLU', 28.83), ('FE1', 'FES', 'CG', 'GLU', 28.01), ('FE1', 'FES', 'CD', 'GLU', 28.84), ('FE1', 'FES', 'OE1', 'GLU', 28.52), ('FE1', 'FES', 'OE2', 'GLU', 29.84)], [('FE2', 'FES', 'CB', 'GLU', 31.33), ('FE2', 'FES', 'CG', 'GLU', 30.5), ('FE2', 'FES', 'CD', 'GLU', 31.33), ('FE2', 'FES', 'OE1', 'GLU', 31.04), ('FE2', 'FES', 'OE2', 'GLU', 32.3)], [('S1', 'FES', 'CB', 'GLU', 30.43), ('S1', 'FES', 'CG', 'GLU', 29.69), ('S1', 'FES', 'CD', 'GLU', 30.58), ('S1', 'FES', 'OE1', 'GLU', 30.29), ('S1', 'FES', 'OE2', 'GLU', 31.59)], [('S2', 'FES', 'CB', 'GLU', 29.84), ('S2', 'FES', 'CG', 'GLU', 28.94), ('S2', 'FES', 'CD', 'GLU', 29.71), ('S2', 'FES', 'OE1', 'GLU', 29.38), ('S2', 'FES', 'OE2', 'GLU', 30.65)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_FESI, d, 'R_1vlb_1_2_99_7')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(FES_FES, d, 'R_1vlb_1_2_99_7')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(FES_GLU, d, 'R_1vlb_1_2_99_7')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_FESI' :  match1,
		'FES_FES' :  match2,
		'FES_GLU' :  match3}