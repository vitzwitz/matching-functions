'''
FUNC:M_2ag0_4_1_2_38
PDB:2ag0
EC:4.1.2.38
RESI:his,glu,gln,mg
LOCI:a-29,50,113,601;
'''
import motifFunctions as cmd
HIS_MG = { 
	'distances':
		[[40.4], [40.71], [41.44], [40.42], [41.61], [41.0]],
	'comparisons':
		[[('CB', 'HIS', 'MG', 'MG', 40.4)], [('CG', 'HIS', 'MG', 'MG', 40.71)], [('ND1', 'HIS', 'MG', 'MG', 41.44)], [('CD2', 'HIS', 'MG', 'MG', 40.42)], [('CE1', 'HIS', 'MG', 'MG', 41.61)], [('NE2', 'HIS', 'MG', 'MG', 41.0)]]}
GLN_GLU = { 
	'distances':
		[[14.98, 13.92, 13.32, 13.76, 12.59], [14.54, 13.45, 12.68, 13.03, 11.89], [14.01, 12.8, 12.0, 12.45, 11.09], [12.88, 11.64, 10.9, 11.43, 9.98], [14.93, 13.66, 12.79, 13.24, 11.8]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'GLU', 14.98), ('CB', 'GLN', 'CG', 'GLU', 13.92), ('CB', 'GLN', 'CD', 'GLU', 13.32), ('CB', 'GLN', 'OE1', 'GLU', 13.76), ('CB', 'GLN', 'OE2', 'GLU', 12.59)], [('CG', 'GLN', 'CB', 'GLU', 14.54), ('CG', 'GLN', 'CG', 'GLU', 13.45), ('CG', 'GLN', 'CD', 'GLU', 12.68), ('CG', 'GLN', 'OE1', 'GLU', 13.03), ('CG', 'GLN', 'OE2', 'GLU', 11.89)], [('CD', 'GLN', 'CB', 'GLU', 14.01), ('CD', 'GLN', 'CG', 'GLU', 12.8), ('CD', 'GLN', 'CD', 'GLU', 12.0), ('CD', 'GLN', 'OE1', 'GLU', 12.45), ('CD', 'GLN', 'OE2', 'GLU', 11.09)], [('OE1', 'GLN', 'CB', 'GLU', 12.88), ('OE1', 'GLN', 'CG', 'GLU', 11.64), ('OE1', 'GLN', 'CD', 'GLU', 10.9), ('OE1', 'GLN', 'OE1', 'GLU', 11.43), ('OE1', 'GLN', 'OE2', 'GLU', 9.98)], [('NE2', 'GLN', 'CB', 'GLU', 14.93), ('NE2', 'GLN', 'CG', 'GLU', 13.66), ('NE2', 'GLN', 'CD', 'GLU', 12.79), ('NE2', 'GLN', 'OE1', 'GLU', 13.24), ('NE2', 'GLN', 'OE2', 'GLU', 11.8)]]}
GLN_HIS = { 
	'distances':
		[[8.92, 7.74, 7.45, 7.13, 6.64, 6.38], [9.33, 8.2, 8.21, 7.32, 7.39, 6.76], [8.37, 7.34, 7.65, 6.33, 6.98, 6.08], [7.86, 7.07, 7.58, 6.23, 7.18, 6.33], [8.48, 7.37, 7.75, 6.15, 6.96, 5.85]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'HIS', 8.92), ('CB', 'GLN', 'CG', 'HIS', 7.74), ('CB', 'GLN', 'ND1', 'HIS', 7.45), ('CB', 'GLN', 'CD2', 'HIS', 7.13), ('CB', 'GLN', 'CE1', 'HIS', 6.64), ('CB', 'GLN', 'NE2', 'HIS', 6.38)], [('CG', 'GLN', 'CB', 'HIS', 9.33), ('CG', 'GLN', 'CG', 'HIS', 8.2), ('CG', 'GLN', 'ND1', 'HIS', 8.21), ('CG', 'GLN', 'CD2', 'HIS', 7.32), ('CG', 'GLN', 'CE1', 'HIS', 7.39), ('CG', 'GLN', 'NE2', 'HIS', 6.76)], [('CD', 'GLN', 'CB', 'HIS', 8.37), ('CD', 'GLN', 'CG', 'HIS', 7.34), ('CD', 'GLN', 'ND1', 'HIS', 7.65), ('CD', 'GLN', 'CD2', 'HIS', 6.33), ('CD', 'GLN', 'CE1', 'HIS', 6.98), ('CD', 'GLN', 'NE2', 'HIS', 6.08)], [('OE1', 'GLN', 'CB', 'HIS', 7.86), ('OE1', 'GLN', 'CG', 'HIS', 7.07), ('OE1', 'GLN', 'ND1', 'HIS', 7.58), ('OE1', 'GLN', 'CD2', 'HIS', 6.23), ('OE1', 'GLN', 'CE1', 'HIS', 7.18), ('OE1', 'GLN', 'NE2', 'HIS', 6.33)], [('NE2', 'GLN', 'CB', 'HIS', 8.48), ('NE2', 'GLN', 'CG', 'HIS', 7.37), ('NE2', 'GLN', 'ND1', 'HIS', 7.75), ('NE2', 'GLN', 'CD2', 'HIS', 6.15), ('NE2', 'GLN', 'CE1', 'HIS', 6.96), ('NE2', 'GLN', 'NE2', 'HIS', 5.85)]]}
GLN_MG = { 
	'distances':
		[[38.45], [37.72], [37.62], [36.85], [38.44]],
	'comparisons':
		[[('CB', 'GLN', 'MG', 'MG', 38.45)], [('CG', 'GLN', 'MG', 'MG', 37.72)], [('CD', 'GLN', 'MG', 'MG', 37.62)], [('OE1', 'GLN', 'MG', 'MG', 36.85)], [('NE2', 'GLN', 'MG', 'MG', 38.44)]]}
GLU_MG = { 
	'distances':
		[[27.53], [28.88], [28.96], [28.0], [30.06]],
	'comparisons':
		[[('CB', 'GLU', 'MG', 'MG', 27.53)], [('CG', 'GLU', 'MG', 'MG', 28.88)], [('CD', 'GLU', 'MG', 'MG', 28.96)], [('OE1', 'GLU', 'MG', 'MG', 28.0)], [('OE2', 'GLU', 'MG', 'MG', 30.06)]]}
GLU_HIS = { 
	'distances':
		[[15.02, 15.54, 16.35, 15.53, 16.8, 16.33], [13.64, 14.17, 15.05, 14.14, 15.5, 14.99], [13.51, 13.9, 14.81, 13.7, 15.15, 14.51], [14.51, 14.81, 15.68, 14.52, 15.93, 15.25], [12.52, 12.91, 13.88, 12.65, 14.2, 13.5]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'HIS', 15.02), ('CB', 'GLU', 'CG', 'HIS', 15.54), ('CB', 'GLU', 'ND1', 'HIS', 16.35), ('CB', 'GLU', 'CD2', 'HIS', 15.53), ('CB', 'GLU', 'CE1', 'HIS', 16.8), ('CB', 'GLU', 'NE2', 'HIS', 16.33)], [('CG', 'GLU', 'CB', 'HIS', 13.64), ('CG', 'GLU', 'CG', 'HIS', 14.17), ('CG', 'GLU', 'ND1', 'HIS', 15.05), ('CG', 'GLU', 'CD2', 'HIS', 14.14), ('CG', 'GLU', 'CE1', 'HIS', 15.5), ('CG', 'GLU', 'NE2', 'HIS', 14.99)], [('CD', 'GLU', 'CB', 'HIS', 13.51), ('CD', 'GLU', 'CG', 'HIS', 13.9), ('CD', 'GLU', 'ND1', 'HIS', 14.81), ('CD', 'GLU', 'CD2', 'HIS', 13.7), ('CD', 'GLU', 'CE1', 'HIS', 15.15), ('CD', 'GLU', 'NE2', 'HIS', 14.51)], [('OE1', 'GLU', 'CB', 'HIS', 14.51), ('OE1', 'GLU', 'CG', 'HIS', 14.81), ('OE1', 'GLU', 'ND1', 'HIS', 15.68), ('OE1', 'GLU', 'CD2', 'HIS', 14.52), ('OE1', 'GLU', 'CE1', 'HIS', 15.93), ('OE1', 'GLU', 'NE2', 'HIS', 15.25)], [('OE2', 'GLU', 'CB', 'HIS', 12.52), ('OE2', 'GLU', 'CG', 'HIS', 12.91), ('OE2', 'GLU', 'ND1', 'HIS', 13.88), ('OE2', 'GLU', 'CD2', 'HIS', 12.65), ('OE2', 'GLU', 'CE1', 'HIS', 14.2), ('OE2', 'GLU', 'NE2', 'HIS', 13.5)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_MG, d, 'M_2ag0_4_1_2_38')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLN_GLU, d, 'M_2ag0_4_1_2_38')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLN_HIS, d, 'M_2ag0_4_1_2_38')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(GLN_MG, d, 'M_2ag0_4_1_2_38')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(GLU_MG, d, 'M_2ag0_4_1_2_38')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(GLU_HIS, d, 'M_2ag0_4_1_2_38')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_MG' :  match1,
		'GLN_GLU' :  match2,
		'GLN_HIS' :  match3,
		'GLN_MG' :  match4,
		'GLU_MG' :  match5,
		'GLU_HIS' :  match6}