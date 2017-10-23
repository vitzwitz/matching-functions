'''
FUNC:A_2f61_3_2_1_45
PDB:2f61
EC:3.2.1.45
RESI:glu,glu,cys
LOCI:a-235,340,342;
'''
import motifFunctions as cmd
GLU_GLU = { 
	'distances':
		[[10.13, 8.73, 8.75, 8.91, 8.97], [10.34, 8.92, 8.62, 8.57, 8.83], [9.23, 7.88, 7.46, 7.23, 7.8], [8.79, 7.57, 7.35, 7.01, 7.94], [9.08, 7.72, 7.01, 6.72, 7.18], [10.13, 10.34, 9.23, 8.79, 9.08], [8.73, 8.92, 7.88, 7.57, 7.72], [8.75, 8.62, 7.46, 7.35, 7.01], [8.91, 8.57, 7.23, 7.01, 6.72], [8.97, 8.83, 7.8, 7.94, 7.18]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'GLU', 10.13), ('CB', 'GLU', 'CG', 'GLU', 8.73), ('CB', 'GLU', 'CD', 'GLU', 8.75), ('CB', 'GLU', 'OE1', 'GLU', 8.91), ('CB', 'GLU', 'OE2', 'GLU', 8.97)], [('CG', 'GLU', 'CB', 'GLU', 10.34), ('CG', 'GLU', 'CG', 'GLU', 8.92), ('CG', 'GLU', 'CD', 'GLU', 8.62), ('CG', 'GLU', 'OE1', 'GLU', 8.57), ('CG', 'GLU', 'OE2', 'GLU', 8.83)], [('CD', 'GLU', 'CB', 'GLU', 9.23), ('CD', 'GLU', 'CG', 'GLU', 7.88), ('CD', 'GLU', 'CD', 'GLU', 7.46), ('CD', 'GLU', 'OE1', 'GLU', 7.23), ('CD', 'GLU', 'OE2', 'GLU', 7.8)], [('OE1', 'GLU', 'CB', 'GLU', 8.79), ('OE1', 'GLU', 'CG', 'GLU', 7.57), ('OE1', 'GLU', 'CD', 'GLU', 7.35), ('OE1', 'GLU', 'OE1', 'GLU', 7.01), ('OE1', 'GLU', 'OE2', 'GLU', 7.94)], [('OE2', 'GLU', 'CB', 'GLU', 9.08), ('OE2', 'GLU', 'CG', 'GLU', 7.72), ('OE2', 'GLU', 'CD', 'GLU', 7.01), ('OE2', 'GLU', 'OE1', 'GLU', 6.72), ('OE2', 'GLU', 'OE2', 'GLU', 7.18)], [('CB', 'GLU', 'CB', 'GLU', 10.13), ('CB', 'GLU', 'CG', 'GLU', 10.34), ('CB', 'GLU', 'CD', 'GLU', 9.23), ('CB', 'GLU', 'OE1', 'GLU', 8.79), ('CB', 'GLU', 'OE2', 'GLU', 9.08)], [('CG', 'GLU', 'CB', 'GLU', 8.73), ('CG', 'GLU', 'CG', 'GLU', 8.92), ('CG', 'GLU', 'CD', 'GLU', 7.88), ('CG', 'GLU', 'OE1', 'GLU', 7.57), ('CG', 'GLU', 'OE2', 'GLU', 7.72)], [('CD', 'GLU', 'CB', 'GLU', 8.75), ('CD', 'GLU', 'CG', 'GLU', 8.62), ('CD', 'GLU', 'CD', 'GLU', 7.46), ('CD', 'GLU', 'OE1', 'GLU', 7.35), ('CD', 'GLU', 'OE2', 'GLU', 7.01)], [('OE1', 'GLU', 'CB', 'GLU', 8.91), ('OE1', 'GLU', 'CG', 'GLU', 8.57), ('OE1', 'GLU', 'CD', 'GLU', 7.23), ('OE1', 'GLU', 'OE1', 'GLU', 7.01), ('OE1', 'GLU', 'OE2', 'GLU', 6.72)], [('OE2', 'GLU', 'CB', 'GLU', 8.97), ('OE2', 'GLU', 'CG', 'GLU', 8.83), ('OE2', 'GLU', 'CD', 'GLU', 7.8), ('OE2', 'GLU', 'OE1', 'GLU', 7.94), ('OE2', 'GLU', 'OE2', 'GLU', 7.18)]]}
GLU_CYS = { 
	'distances':
		[[8.54, 8.41], [7.29, 7.15], [7.72, 7.21], [8.85, 8.37], [7.21, 6.37], [14.02, 12.7], [12.62, 11.34], [11.68, 10.27], [11.45, 10.06], [11.4, 9.89]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'CYS', 8.54), ('CB', 'GLU', 'SG', 'CYS', 8.41)], [('CG', 'GLU', 'CB', 'CYS', 7.29), ('CG', 'GLU', 'SG', 'CYS', 7.15)], [('CD', 'GLU', 'CB', 'CYS', 7.72), ('CD', 'GLU', 'SG', 'CYS', 7.21)], [('OE1', 'GLU', 'CB', 'CYS', 8.85), ('OE1', 'GLU', 'SG', 'CYS', 8.37)], [('OE2', 'GLU', 'CB', 'CYS', 7.21), ('OE2', 'GLU', 'SG', 'CYS', 6.37)], [('CB', 'GLU', 'CB', 'CYS', 14.02), ('CB', 'GLU', 'SG', 'CYS', 12.7)], [('CG', 'GLU', 'CB', 'CYS', 12.62), ('CG', 'GLU', 'SG', 'CYS', 11.34)], [('CD', 'GLU', 'CB', 'CYS', 11.68), ('CD', 'GLU', 'SG', 'CYS', 10.27)], [('OE1', 'GLU', 'CB', 'CYS', 11.45), ('OE1', 'GLU', 'SG', 'CYS', 10.06)], [('OE2', 'GLU', 'CB', 'CYS', 11.4), ('OE2', 'GLU', 'SG', 'CYS', 9.89)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_GLU, d, 'A_2f61_3_2_1_45')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_CYS, d, 'A_2f61_3_2_1_45')
	if match2 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_GLU' :  match1,
		'GLU_CYS' :  match2}