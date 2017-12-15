# Fall Final Report 
&nbsp;&nbsp;&nbsp;&nbsp; [![N|Solid](https://urlscan.io/logo/github.com?size=35)](https://github.com/vitzwitz/matching-functions/blob/master/FallSemesterFinal/diagram.jpg) 
&nbsp;&nbsp;&nbsp;&nbsp; Bri Miskovitz


> The atom comparisons that find the catalytic sites in the protein structures were re-formatted to a residue comparison matrix, 
and principal components analysis and other mathematical methods were implemented. Methods were developed to convert
all motif files into more appropriate format. Techniques that store the results of the search algorithm were written, an entity
relationship diagram was created, and the connection of the program to a MySQL database began to be developed in order to
have the ability to compare the said results.  Testing the search algorithm and the PCA implementation onto part of the serine
protease protein family led to a major issue in the motif files: ill-formed matrices.  Extensive tests, methods to detect specific
issues, and processes to predict and monitor significant information necessary to properly construct the matrices and rewrite
the motif files were developed.  After the continuous production of ill-formed matrices, the most recent directory of motif files
was analyzed, the specific motifs that were still not properly made were found, and methods to split aforementioned matrices
were developed and tested. 


#### From Comparing Atoms to Comparing Residues
ProMOL originally implemented PyMOL's select and delete functions and uses PyMOL's selection algebra, and an example is seen in the first motif representation below.  It searched for the necessary constraints individually, but the files that held the constraints were not user-friendly and were very hard to read.  ProMOL's representation of catalytic sites changed from comparing atoms individually to compared pairs of residues as matrices. One matrix represents all of the distance constraints between two residues and the other matrix contains all the necessary information for a comparison: names of atoms and residues and the distance between them.  The words 'comparisons' and 'distances' map to the matrix it relates to, so each residue pair has a distances matrix and a comparisons matrix, e.g. seen in the second representation below.   Matrix representation allows implementation of data analytical techniques such as k-nearest neighbor and principal components analysis.

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
Principal components analysis was modified and implemented process onto motif files in order to shorten search process.  A method to standardize matrices was written, and it subtracts the matrix by its mean and divides it by it's standard deviation. A method to find matrix's covariance matrix was created, and it finds the average of the columns, subtracts the average column from the matrix, and takes the dot product of the results and its transpose. The real positive eigenvalues of the covariance matrix were scaled between 0 and 1, and then the eigenvalues that are seen as 0 were removed to only allow the components with the largest eigenvalues to exist.  The eigenvalues were scaled by finding the range, subtracting the mean from each value, and dividing the value of said subtraction by the range.  The indices for the matrix and its transpose were applied to the comparison and distance matrices, the unwanted indices were removed from those matrices, and it allows ProMOL to skip those comparisons.  

#### Updating Motif Files
Motif files were parsed, all delete implementations were ignored, the select implementations were utilized, and the initial information at the top of the motif files was included.  PyMOL's selection algebra was split into two atoms, two residues, and a distance between two said atoms.  Constructed a dictionary that maps a structure that represents the residue pairing identification, a tuple of the two residue names, to the matrix of the distances the pair affiliates with and another that maps that same structure of names to a matrix that contains tuples of its individual comparisons.  Both dictionaries accumulate all of the data found in the original motif files (it at least should, but this issue will be discussed later).  After all of the information is gathered, the two maps are transformed into a map for each individual residue pair, similar to the motif representation that compares residues above. The motif function, the Protein Data Bank (pdb) ID, the emission commision, and the location from the original motif files is included into the new files as well.  For each residue pair, an implementation of the search algorithm and new dictionary that maps the names of the residue pairs to the results from the aforementioned implementation if the motif's execution is successful are incorporated into the files.  

[Talk about now? Or after issue?]: # (Because of later issues, answers to two binary questions are added to the beginning of the files that provide information)


#### Testing Search Algorithm by Implementing it onto Serine Protease 

The search algorithm worked on individual protein structures, and it could use certain motif files to find catalytic sites in the structures.  It is also important to study an entire protein family because after implementing the search algorithm to the structures, the comparison of the results will provide sufficient information, such as what motif files that pass for similar structures, what atoms are choosen that consist of the necessary catalytic sites, and the differences in the atoms that were choosen for similar structures.  However, the search process should be able to utilize all of the given catalytic sites, but when all of the motifs attempted to be implemented, a major issue occurred.  

#### Re-occuring Errors

Maps were chosen to hold the information regarding the residue comparisons because its operations have an average constant time complexity, but they need to map unique keys to values.  However, if there are more than one of the same type of amino acid in a catalytic site, there will be multiple mappings to different structures using the same key.  It will result a matrix filled of multiple structures, an ill-formed matrix in terms of data content and sometimes shape. It can still be used for comparison to protein structures, but the purpose of using matrices was so that data analytical procedures could be implemented onto these structures, the motif files were more user-friendly and readible, and most importantly, the k-nearest neighbors of each atom of a residue can be searched for and stored together.  

The old motif files can have some slight variety as well.  Suppose a catalytic site is composed of three amino acids, one glutamine, one aspartate, and one histidines; a motif can contain conditions for one or multiple glutamines, one or multiple aspartates, and one or multiple histidines, but only one each should be used to represent the site.  The search process must include deciding the residues that best fit the motif's requirements.  The latest parser that was developed asked each motif two questions, and the first relates to the aforementioned adnormality.  Does it contains more residues than expected? It predicts the expected number of residue pairs, and it compares it with the actual number of comparisons found throughout the file.  If there are more than expected, it is noted at the top of that file; when it is used during a search process, that note can trigger an application process that will compare all of the pairs with the structure and only choose the best fits.  

#### Testing in Big Data
The original parsers produced new motif files from the simple catalytic sites, but a common issue in Big Data is that the given data will not always be consistent and frequently there will be special cases.  As aforementioned, motifs sometimes contain multiple options of residue pairs; they can represent a catalytic site that has several of the same type of residue, consist of various residues with the same name and different composition, and contain residues with the same name and the same makeup.  They can also represent sites with only one residue pair, sites that consist of only residues that multiple of the same residues, sites that contain only one type of residue, residue pairs that only contain a total of two atoms, and residues that only consist of one atom.  This variation has produced specialized analyses and has strengthened the program.   The biggest difference in working with Big Data compared to other projects is that one program needs to produce the appropriate results for any possible input and the variety of input is considerably larger. It must succeed more in-depth and broad testing to ensure the program works, and it is much harder to find the source of the problem if the same strategies that other programs implement are used.  A debugger takes too long, and simply just printing the results at the location given by the IDE produces cluttered, hard-to-read, and often useless information.  The program manages its special cases, re-occuring issues, and mysterious failures by using methods that review the newly parsed motif files, exceptions that inform the user the cause of the issue, tests that inspect the generated dictionaries, and assessments that asks the user a series of questions regarding the information they desire.  

#### Saving the Results of the Search Algorithm

#### Development as a Developer















___

*TODO*

 [ ] &nbsp;&nbsp; Error	- The major error that was worked on during the semester
 [ ] &nbsp;&nbsp; Storing Results - AWS, ERD, Pandas, MySQL, Pickle
 [ ] &nbsp;&nbsp;Testing - Pretty print, user friendly testing, edge cases, using actual data and beyond
 [ ] &nbsp;&nbsp; Growth - Seen in comments
 [ ] &nbsp;&nbsp; Fix grammer -> verb inconsistency (find way to make them active)
 [ ] &nbsp;&nbsp; Flowchart	Timeline is ugly & flowchart can be made


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
