'''
FUNC:M_1ir3_2_7_10_1
PDB:1ir3
EC:2.7.10.1
RESI:mg,mg,asp,arg
LOCI:a-301,302,1132,1136;
'''
import motifFunctions as cmd
ASP_ARG = { 
	'distances':
		[[10.88, 9.44, 9.4, 8.2, 8.15, 9.22, 7.24], [9.79, 8.31, 8.06, 6.8, 6.8, 7.97, 5.93], [9.44, 7.91, 7.58, 6.21, 5.92, 7.0, 4.87], [9.52, 8.11, 7.76, 6.62, 6.93, 8.21, 6.27]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ARG', 10.88), ('CB', 'ASP', 'CG', 'ARG', 9.44), ('CB', 'ASP', 'CD', 'ARG', 9.4), ('CB', 'ASP', 'NE', 'ARG', 8.2), ('CB', 'ASP', 'CZ', 'ARG', 8.15), ('CB', 'ASP', 'NH1', 'ARG', 9.22), ('CB', 'ASP', 'NH2', 'ARG', 7.24)], [('CG', 'ASP', 'CB', 'ARG', 9.79), ('CG', 'ASP', 'CG', 'ARG', 8.31), ('CG', 'ASP', 'CD', 'ARG', 8.06), ('CG', 'ASP', 'NE', 'ARG', 6.8), ('CG', 'ASP', 'CZ', 'ARG', 6.8), ('CG', 'ASP', 'NH1', 'ARG', 7.97), ('CG', 'ASP', 'NH2', 'ARG', 5.93)], [('OD1', 'ASP', 'CB', 'ARG', 9.44), ('OD1', 'ASP', 'CG', 'ARG', 7.91), ('OD1', 'ASP', 'CD', 'ARG', 7.58), ('OD1', 'ASP', 'NE', 'ARG', 6.21), ('OD1', 'ASP', 'CZ', 'ARG', 5.92), ('OD1', 'ASP', 'NH1', 'ARG', 7.0), ('OD1', 'ASP', 'NH2', 'ARG', 4.87)], [('OD2', 'ASP', 'CB', 'ARG', 9.52), ('OD2', 'ASP', 'CG', 'ARG', 8.11), ('OD2', 'ASP', 'CD', 'ARG', 7.76), ('OD2', 'ASP', 'NE', 'ARG', 6.62), ('OD2', 'ASP', 'CZ', 'ARG', 6.93), ('OD2', 'ASP', 'NH1', 'ARG', 8.21), ('OD2', 'ASP', 'NH2', 'ARG', 6.27)]]}
ASP_MG = { 
	'distances':
		[[8.85], [7.97], [8.49], [6.98], [9.02], [8.46], [9.38], [7.25]],
	'comparisons':
		[[('CB', 'ASP', 'MG', 'MG', 8.85)], [('CG', 'ASP', 'MG', 'MG', 7.97)], [('OD1', 'ASP', 'MG', 'MG', 8.49)], [('OD2', 'ASP', 'MG', 'MG', 6.98)], [('CB', 'ASP', 'MG', 'MG', 9.02)], [('CG', 'ASP', 'MG', 'MG', 8.46)], [('OD1', 'ASP', 'MG', 'MG', 9.38)], [('OD2', 'ASP', 'MG', 'MG', 7.25)]]}
ARG_MG = { 
	'distances':
		[[7.39], [6.87], [6.88], [7.06], [8.29], [9.28], [8.74], [10.89], [10.14], [9.81], [9.5], [10.54], [11.77], [10.52]],
	'comparisons':
		[[('CB', 'ARG', 'MG', 'MG', 7.39)], [('CG', 'ARG', 'MG', 'MG', 6.87)], [('CD', 'ARG', 'MG', 'MG', 6.88)], [('NE', 'ARG', 'MG', 'MG', 7.06)], [('CZ', 'ARG', 'MG', 'MG', 8.29)], [('NH1', 'ARG', 'MG', 'MG', 9.28)], [('NH2', 'ARG', 'MG', 'MG', 8.74)], [('CB', 'ARG', 'MG', 'MG', 10.89)], [('CG', 'ARG', 'MG', 'MG', 10.14)], [('CD', 'ARG', 'MG', 'MG', 9.81)], [('NE', 'ARG', 'MG', 'MG', 9.5)], [('CZ', 'ARG', 'MG', 'MG', 10.54)], [('NH1', 'ARG', 'MG', 'MG', 11.77)], [('NH2', 'ARG', 'MG', 'MG', 10.52)]]}
MG_MG = { 
	'distances':
		[5.62, 5.62],
	'comparisons':
		[('MG', 'MG', 'MG', 'MG', 5.62), ('MG', 'MG', 'MG', 'MG', 5.62)]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_ARG, d, 'M_1ir3_2_7_10_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_MG, d, 'M_1ir3_2_7_10_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ARG_MG, d, 'M_1ir3_2_7_10_1')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(MG_MG, d, 'M_1ir3_2_7_10_1')
	if match4 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_ARG' :  match1,
		'ASP_MG' :  match2,
		'ARG_MG' :  match3,
		'MG_MG' :  match4}