'''
FUNC:A_1bvv_3_2_1_8
PDB:1bvv
EC:3.2.1.8
RESI:glu,glu
LOCI:a-78,172;
'''
import motifFunctions as cmd
GLU_GLU = { 
	'distances':
		[[12.72, 11.27, 10.52, 10.69, 10.02], [12.38, 10.98, 10.01, 10.06, 9.46], [10.95, 9.6, 8.58, 8.56, 8.09], [10.15, 8.77, 7.92, 7.97, 7.57], [10.78, 9.52, 8.32, 8.18, 7.79], [12.72, 12.38, 10.95, 10.15, 10.78], [11.27, 10.98, 9.6, 8.77, 9.52], [10.52, 10.01, 8.58, 7.92, 8.32], [10.69, 10.06, 8.56, 7.97, 8.18], [10.02, 9.46, 8.09, 7.57, 7.79]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'GLU', 12.72), ('CB', 'GLU', 'CG', 'GLU', 11.27), ('CB', 'GLU', 'CD', 'GLU', 10.52), ('CB', 'GLU', 'OE1', 'GLU', 10.69), ('CB', 'GLU', 'OE2', 'GLU', 10.02)], [('CG', 'GLU', 'CB', 'GLU', 12.38), ('CG', 'GLU', 'CG', 'GLU', 10.98), ('CG', 'GLU', 'CD', 'GLU', 10.01), ('CG', 'GLU', 'OE1', 'GLU', 10.06), ('CG', 'GLU', 'OE2', 'GLU', 9.46)], [('CD', 'GLU', 'CB', 'GLU', 10.95), ('CD', 'GLU', 'CG', 'GLU', 9.6), ('CD', 'GLU', 'CD', 'GLU', 8.58), ('CD', 'GLU', 'OE1', 'GLU', 8.56), ('CD', 'GLU', 'OE2', 'GLU', 8.09)], [('OE1', 'GLU', 'CB', 'GLU', 10.15), ('OE1', 'GLU', 'CG', 'GLU', 8.77), ('OE1', 'GLU', 'CD', 'GLU', 7.92), ('OE1', 'GLU', 'OE1', 'GLU', 7.97), ('OE1', 'GLU', 'OE2', 'GLU', 7.57)], [('OE2', 'GLU', 'CB', 'GLU', 10.78), ('OE2', 'GLU', 'CG', 'GLU', 9.52), ('OE2', 'GLU', 'CD', 'GLU', 8.32), ('OE2', 'GLU', 'OE1', 'GLU', 8.18), ('OE2', 'GLU', 'OE2', 'GLU', 7.79)], [('CB', 'GLU', 'CB', 'GLU', 12.72), ('CB', 'GLU', 'CG', 'GLU', 12.38), ('CB', 'GLU', 'CD', 'GLU', 10.95), ('CB', 'GLU', 'OE1', 'GLU', 10.15), ('CB', 'GLU', 'OE2', 'GLU', 10.78)], [('CG', 'GLU', 'CB', 'GLU', 11.27), ('CG', 'GLU', 'CG', 'GLU', 10.98), ('CG', 'GLU', 'CD', 'GLU', 9.6), ('CG', 'GLU', 'OE1', 'GLU', 8.77), ('CG', 'GLU', 'OE2', 'GLU', 9.52)], [('CD', 'GLU', 'CB', 'GLU', 10.52), ('CD', 'GLU', 'CG', 'GLU', 10.01), ('CD', 'GLU', 'CD', 'GLU', 8.58), ('CD', 'GLU', 'OE1', 'GLU', 7.92), ('CD', 'GLU', 'OE2', 'GLU', 8.32)], [('OE1', 'GLU', 'CB', 'GLU', 10.69), ('OE1', 'GLU', 'CG', 'GLU', 10.06), ('OE1', 'GLU', 'CD', 'GLU', 8.56), ('OE1', 'GLU', 'OE1', 'GLU', 7.97), ('OE1', 'GLU', 'OE2', 'GLU', 8.18)], [('OE2', 'GLU', 'CB', 'GLU', 10.02), ('OE2', 'GLU', 'CG', 'GLU', 9.46), ('OE2', 'GLU', 'CD', 'GLU', 8.09), ('OE2', 'GLU', 'OE1', 'GLU', 7.57), ('OE2', 'GLU', 'OE2', 'GLU', 7.79)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_GLU, d, 'A_1bvv_3_2_1_8')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_GLU' :  match1}