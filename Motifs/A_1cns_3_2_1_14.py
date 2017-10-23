'''
FUNC:A_1cns_3_2_1_14
PDB:1cns
EC:3.2.1.14
RESI:glu,glu,ser
LOCI:a-67,89,120;
'''
import motifFunctions as cmd
GLU_SER = { 
	'distances':
		[[9.43, 8.05], [9.65, 8.24], [8.56, 7.18], [7.36, 5.96], [9.08, 7.77], [12.0, 11.59], [11.89, 11.66], [11.38, 11.15], [10.57, 10.23], [11.95, 11.84]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'SER', 9.43), ('CB', 'GLU', 'OG', 'SER', 8.05)], [('CG', 'GLU', 'CB', 'SER', 9.65), ('CG', 'GLU', 'OG', 'SER', 8.24)], [('CD', 'GLU', 'CB', 'SER', 8.56), ('CD', 'GLU', 'OG', 'SER', 7.18)], [('OE1', 'GLU', 'CB', 'SER', 7.36), ('OE1', 'GLU', 'OG', 'SER', 5.96)], [('OE2', 'GLU', 'CB', 'SER', 9.08), ('OE2', 'GLU', 'OG', 'SER', 7.77)], [('CB', 'GLU', 'CB', 'SER', 12.0), ('CB', 'GLU', 'OG', 'SER', 11.59)], [('CG', 'GLU', 'CB', 'SER', 11.89), ('CG', 'GLU', 'OG', 'SER', 11.66)], [('CD', 'GLU', 'CB', 'SER', 11.38), ('CD', 'GLU', 'OG', 'SER', 11.15)], [('OE1', 'GLU', 'CB', 'SER', 10.57), ('OE1', 'GLU', 'OG', 'SER', 10.23)], [('OE2', 'GLU', 'CB', 'SER', 11.95), ('OE2', 'GLU', 'OG', 'SER', 11.84)]]}
GLU_GLU = { 
	'distances':
		[[11.48, 12.38, 12.14, 11.05, 13.2], [12.01, 12.81, 12.38, 11.2, 13.35], [12.24, 12.85, 12.27, 11.07, 13.15], [11.86, 12.38, 11.84, 10.67, 12.71], [12.94, 13.48, 12.76, 11.53, 13.55], [11.48, 12.01, 12.24, 11.86, 12.94], [12.38, 12.81, 12.85, 12.38, 13.48], [12.14, 12.38, 12.27, 11.84, 12.76], [11.05, 11.2, 11.07, 10.67, 11.53], [13.2, 13.35, 13.15, 12.71, 13.55]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'GLU', 11.48), ('CB', 'GLU', 'CG', 'GLU', 12.38), ('CB', 'GLU', 'CD', 'GLU', 12.14), ('CB', 'GLU', 'OE1', 'GLU', 11.05), ('CB', 'GLU', 'OE2', 'GLU', 13.2)], [('CG', 'GLU', 'CB', 'GLU', 12.01), ('CG', 'GLU', 'CG', 'GLU', 12.81), ('CG', 'GLU', 'CD', 'GLU', 12.38), ('CG', 'GLU', 'OE1', 'GLU', 11.2), ('CG', 'GLU', 'OE2', 'GLU', 13.35)], [('CD', 'GLU', 'CB', 'GLU', 12.24), ('CD', 'GLU', 'CG', 'GLU', 12.85), ('CD', 'GLU', 'CD', 'GLU', 12.27), ('CD', 'GLU', 'OE1', 'GLU', 11.07), ('CD', 'GLU', 'OE2', 'GLU', 13.15)], [('OE1', 'GLU', 'CB', 'GLU', 11.86), ('OE1', 'GLU', 'CG', 'GLU', 12.38), ('OE1', 'GLU', 'CD', 'GLU', 11.84), ('OE1', 'GLU', 'OE1', 'GLU', 10.67), ('OE1', 'GLU', 'OE2', 'GLU', 12.71)], [('OE2', 'GLU', 'CB', 'GLU', 12.94), ('OE2', 'GLU', 'CG', 'GLU', 13.48), ('OE2', 'GLU', 'CD', 'GLU', 12.76), ('OE2', 'GLU', 'OE1', 'GLU', 11.53), ('OE2', 'GLU', 'OE2', 'GLU', 13.55)], [('CB', 'GLU', 'CB', 'GLU', 11.48), ('CB', 'GLU', 'CG', 'GLU', 12.01), ('CB', 'GLU', 'CD', 'GLU', 12.24), ('CB', 'GLU', 'OE1', 'GLU', 11.86), ('CB', 'GLU', 'OE2', 'GLU', 12.94)], [('CG', 'GLU', 'CB', 'GLU', 12.38), ('CG', 'GLU', 'CG', 'GLU', 12.81), ('CG', 'GLU', 'CD', 'GLU', 12.85), ('CG', 'GLU', 'OE1', 'GLU', 12.38), ('CG', 'GLU', 'OE2', 'GLU', 13.48)], [('CD', 'GLU', 'CB', 'GLU', 12.14), ('CD', 'GLU', 'CG', 'GLU', 12.38), ('CD', 'GLU', 'CD', 'GLU', 12.27), ('CD', 'GLU', 'OE1', 'GLU', 11.84), ('CD', 'GLU', 'OE2', 'GLU', 12.76)], [('OE1', 'GLU', 'CB', 'GLU', 11.05), ('OE1', 'GLU', 'CG', 'GLU', 11.2), ('OE1', 'GLU', 'CD', 'GLU', 11.07), ('OE1', 'GLU', 'OE1', 'GLU', 10.67), ('OE1', 'GLU', 'OE2', 'GLU', 11.53)], [('OE2', 'GLU', 'CB', 'GLU', 13.2), ('OE2', 'GLU', 'CG', 'GLU', 13.35), ('OE2', 'GLU', 'CD', 'GLU', 13.15), ('OE2', 'GLU', 'OE1', 'GLU', 12.71), ('OE2', 'GLU', 'OE2', 'GLU', 13.55)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_SER, d, 'A_1cns_3_2_1_14')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_GLU, d, 'A_1cns_3_2_1_14')
	if match2 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_SER' :  match1,
		'GLU_GLU' :  match2}