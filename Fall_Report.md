# Fall Final Report &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![N|Solid](https://urlscan.io/logo/github.com?size=40)](https://github.com/vitzwitz/matching-functions) 
&nbsp;&nbsp;&nbsp;&nbsp; Bri Miskovitz


> Re-formatted the atom comparisons that find the catalytic sites in the protein structures to a residue
comparison  matrix. Implemented principal components analysis and other statistical methods. 
Devloped methods to convert all motif files into more appropriate format.  Wrote techniques that
store the results of the search algorithm, created an entity relationship diagram, and began
connecting a MySQL database in order to compare said results.  Testing search algorithm and PCA
implementation onto part of the serine protease protein family led to a major issue in the motif 
files: ill-formed matrices.  Developed extensive tests, methods to detect specific issues, and processes 
to predict and monitor significant information necessary to properly construct the matrices and 
rewrite the motif files.  After the continuous production of ill-formed matrices, analyzed the most
directory of motif files, determined which motifs are still not properly made, and developed and 
tested methods to split aforementioned matrices. 


#### From Comparing Atoms to Comparing Residues
ProMOL originally implemented PyMOL's select and delete functions and uses PyMOL's selection algebra, and an example is seen in the first motif representation below.  It searched for the necessary constraints individually, but the files that held the constraints were not user-friendly and were very hard to read.  Changed ProMOL's representation of catalytic sites from comparing atoms individually to compared pairs of residues as matrices. One matrix represents all of the distance constraints between two residues and the other matrix contains all the necessary information for a comparison: names of atoms and residues and the distance between them.  The words 'comparisons' and 'distances' map to the matrix it relates to, so each residue pair has a distances matrix and a comparisons matrix, e.g. seen in the second representation below.   Matrix representation allows implementation of linear algebra techniques such as principal components analysis.

##### Motif Representations

Comparing Atoms
 ```sh
cmd.select('his25', 'n. CB&r. his w. %s of n. CB&r. ser'%(d*8.66))
```

Comparing Residues
```sh
HIS_SER = { 
	'distances':
		[[8.66, 8.85],
		[7.2, 7.34],
		[6.65, 6.76],
		[6.55, 6.59],
		[5.48, 5.46],
		[5.4, 5.31]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'SER', 8.66), ('CB', 'HIS', 'OG', 'SER', 8.85)],
		[('CG', 'HIS', 'CB', 'SER', 7.2), ('CG', 'HIS', 'OG', 'SER', 7.34)],
		[('ND1', 'HIS', 'CB', 'SER', 6.65), ('ND1', 'HIS', 'OG', 'SER', 6.76)],
		[('CD2', 'HIS', 'CB', 'SER', 6.55), ('CD2', 'HIS', 'OG', 'SER', 6.59)],
		[('CE1', 'HIS', 'CB', 'SER', 5.48), ('CE1', 'HIS', 'OG', 'SER', 5.46)],
		[('NE2', 'HIS', 'CB', 'SER', 5.4), ('NE2', 'HIS', 'OG', 'SER', 5.31)]]}

```

#### Principal Components Analysis
Modified principal components analysis and implemented process onto motif files in order to shorten search process.  Wrote method to standardize matrices by subtracting it by its mean and dividing it by it's standard deviation, and created method to find matrix's covariance matrix by finding the average of the columns, subtracting the average column from the matrix, and taking the dot product of the results and its transpose. Found and scaled the real positive eigenvalues of the covariance matrix between 0 and 1, and then removed the eigenvalues that are seen as 0 to only allow the components with the largest eigenvalues to exist.  Scaled the eigenvalues by finding the range, subtracting the mean from each value, and dividing the value of said subtraction by the range.  Apply the indices for the matrix and its transpose to the comparison and distance matrices, removes unwanted from those matrices, and allows ProMOL to skip those comparisons.  

#### Updating Motif Files
Parsed motif files, ignored all delete implementations, utilized the select implementations, and included the initial information at the top of the motif files.  Split PyMOL's selection algebra into two atoms, two residues, and a distance between two said atoms.  Constructed a dictionary that maps a residue pair name to the matrix of the distances the pair affiliates with and another that maps that same name to a matrix that contains tuples of its individual comparisons.  Both dictionaries accumulate all of the data found in the original motif files (it at least should, but this issue will be discussed later).  After all of the information is gathered, the two maps are transformed into a map for each individual residue pair, similar to the motif representation that compares residues above. The motif function, the Protein Data Bank (pdb) ID, the emission commision, and the location from the original motif files is included into the new files as well.  For each residue pair, an implementation of the search algorithm and new dictionary that maps the names of the residue pairs to the results from the aforementioned implementation if the motif's execution is successful are incorporated into the files.  

[Talk about now? Or after issue?]: # (Because of later issues, answers to two binary questions are added to the beginning of the files that provide information)


#### Testing Search Algorithm by Implementing it onto Serine Protease 

The search algorithm worked on individual protein structures, and it could use certain motif files to find catalytic sites in the structures.  It is also important to study an entire protein family because after implementing the search algorithm to the structures, the comparison of the results will provide sufficient information, such as what motif files that pass for similar structures, what atoms are choosen that consist of the necessary catalytic sites, and the differences in the atoms that were choosen for similar structures.  However, the search process should be able to utilize all of the given catalytic sites, but when all of the motifs attempted to be implemented, a major issue occurred.  

#### Re-occuring Error




#### Saving the Results of the Search Algorithm





#### Extensive Testing



#### Devlopment as a Developer
















| Plugin | README |
| ------ | ------ |
| Dropbox | [plugins/dropbox/README.md] [PlDb] |
| Github | [plugins/github/README.md] [PlGh] |
| Google Drive | [plugins/googledrive/README.md] [PlGd] |
| OneDrive | [plugins/onedrive/README.md] [PlOd] |
| Medium | [plugins/medium/README.md] [PlMe] |
| Google Analytics | [plugins/googleanalytics/README.md] [PlGa] |

[//]: # (Git, VCS, Markdown, importance of testing edge cases, PCA, effects of small errors, handling inconsistent data)
[//]: # (Parsing files, Pandas, AWS, importance of comments)

[//]: # (References)

   [Standardizing Data]: <https://stackoverflow.com/questions/4544292/how-do-i-standardize-a-matrix>
   [Scaling in PCA]: <https://www.researchgate.net/post/What_is_the_best_way_to_scale_parameters_before_running_a_Principal_Component_Analysis_PCA>
   [PCA1]: <http://www.vision.jhu.edu/teaching/vision08/Handouts/case_study_pca1.pdf>
   [PCA2]: <http://www.cs.toronto.edu/~guerzhoy/320/lec/pca.pdf>
   [Scaling Data]: <https://docs.tibco.com/pub/spotfire/7.0.0/doc/html/norm/norm_scale_between_0_and_1.htm>


   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
