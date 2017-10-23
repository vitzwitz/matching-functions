'''
FUNC:M_1w2n_1_14_20_1
PDB:1w2n
EC:1.14.20.1
RESI:arg,fe
LOCI:a-74,312;
'''
import motifFunctions as cmd
ARG_FE = { 
	'distances':
		[[16.32], [16.21], [17.06], [16.55], [17.33], [18.61], [16.91]],
	'comparisons':
		[[('CB', 'ARG', 'FE', 'FE', 16.32)], [('CG', 'ARG', 'FE', 'FE', 16.21)], [('CD', 'ARG', 'FE', 'FE', 17.06)], [('NE', 'ARG', 'FE', 'FE', 16.55)], [('CZ', 'ARG', 'FE', 'FE', 17.33)], [('NH1', 'ARG', 'FE', 'FE', 18.61)], [('NH2', 'ARG', 'FE', 'FE', 16.91)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ARG_FE, d, 'M_1w2n_1_14_20_1')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ARG_FE' :  match1}