# Fall Final Report 
&nbsp;&nbsp; [![N|Solid](https://urlscan.io/logo/github.com?size=35)](https://github.com/vitzwitz/matching-functions/blob/master/FallSemesterFinal/diagram.jpg) 
&nbsp;&nbsp; Bri Miskovitz


> The atom comparisons that find the catalytic sites in the protein structures were re-formatted to a residue comparison matrix, and principal components analysis and other mathematical methods were implemented. Methods were developed to convert all motif files into more appropriate format. Techniques that store the results of the search algorithm were written, an entity relationship diagram was created, and the connection of the program to a MySQL database began to be developed in order to have the ability to compare the said results. Testing the search algorithm and the PCA implementation onto part of the serine protease protein family led to a major issue in the motif files: ill-formed matrices.  Extensive tests, methods to detect specific issues, and processes to predict and monitor significant information necessary to properly construct the matrices and rewrite the motif files were developed.  After the continuous production of ill-formed matrices, the most recent directory of motif files was analyzed, the specific motifs that were still not properly made were found, and methods to split aforementioned matrices were developed and tested. 


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
Motif files were parsed, all delete implementations were ignored, the select implementations were utilized, and the initial information at the top of the motif files was included.  PyMOL's selection algebra was split into two atoms, two residues, and a distance between two said atoms.  Constructed a dictionary that maps a structure that represents the residue pairing identification, a tuple of the two residue names, to the matrix of the distances the pair affiliates with and another that maps that same structure of names to a matrix that contains tuples of its individual comparisons.  Both dictionaries accumulate all of the data found in the original motif files (it at least should, but this issue will be discussed later).  After all of the information is gathered, the two maps are transformed into a map for each individual residue pair, similar to the motif representation that compares residues above. The motif function, the Protein Data Bank (pdb) ID, the emission commision, and the location from the original motif files is included into the new files as well.  The search algorithm is implemented for each residue pair configuration and if it finds every required element, the motif constructs a new dictionary that maps the names of the residue pairs to the results.


#### Testing Search Algorithm using Serine Protease

The search algorithm worked on individual protein structures, and it could use certain motif files to find catalytic sites in the structures.  It is also important to study an entire protein family because after utilizing the search algorithm to find the structures, the comparison of the results will provide sufficient information, such as what motif files that pass for similar structures, what atoms are choosen that consist of the necessary catalytic sites, and the differences in the atoms that were choosen for similar structures.  However, the search process should be able to utilize all of the given catalytic sites, but when all of the motifs attempted to be implemented, a major issue occurred.  

#### Re-occuring Errors

Maps were chosen to hold the information regarding the residue comparisons because its operations have an average constant time complexity, but they need to map unique keys to values.  However, if there are more than one of the same type of amino acid in a catalytic site, there will be multiple mappings to different structures using the same key.  It will result a matrix filled of multiple structures, an ill-formed matrix in terms of data content and sometimes shape. It can still be used for comparison to protein structures, but the purpose of using matrices was so that data analytical procedures could be implemented onto these structures, the motif files were more user-friendly and readible, and most importantly, the k-nearest neighbors of each atom of a residue can be searched for and stored together.  

The old motif files can have some slight variety as well.  Suppose a catalytic site is composed of three amino acids, one glutamine, one aspartate, and one histidines; a motif can contain conditions for one or multiple glutamines, one or multiple aspartates, and one or multiple histidines, but only one each should be used to represent the site.  The search process must include deciding the residues that best fit the motif's requirements.  The latest parser that was developed asked each motif two questions, and the first relates to the aforementioned adnormality.  Does it contains more residues than expected? It predicts the expected number of residue pairs, and it compares it with the actual number of comparisons found throughout the file.  If there are more than expected, it is noted at the top of that file; when it is used during a search process, that note can trigger an application process that will compare all of the pairs with the structure and only choose the best fits.  

#### Testing in Big Data
The original parsers produced new motif files from the simple catalytic sites, but a common issue in Big Data is that the given data will not always be consistent and frequently there will be special cases.  As aforementioned, motifs sometimes contain multiple options of residue pairs; they can represent a catalytic site that has several of the same type of residue, consist of various residues with the same name and different composition, and contain residues with the same name and the same makeup.  They can also represent sites with only one residue pair, sites that consist of only residues that multiple of the same residues, sites that contain only one type of residue, residue pairs that only contain a total of two atoms, and residues that only consist of one atom.  This variation has produced specialized analyses and has strengthened the program.   The biggest difference in working with Big Data compared to other projects is that one program needs to produce the appropriate results for any possible input and the variety of input is considerably larger. It must succeed more in-depth and broad testing to ensure the program works, and it is much harder to find the source of the problem if the same strategies that other programs implement are used.  A debugger takes too long, and simply just printing the results at the location given by the IDE produces cluttered, hard-to-read, and often useless information.  

The program manages its special cases, re-occuring issues, and mysterious failures by using exceptions that inform the user the cause of the issue, methods that review the newly parsed motif files, assessments that asks the user a series of questions regarding the information they desire, and tests that inspect the generated dictionaries.  There are individual issues that continuously re-appear in the program, and it would be a waste to search for the source of those problems everytime it emerges.  Exceptions were added to inform and remind the user what the source of the problems that were already handled.  However, exceptions and errors are not the only issues the program faced.  Motifs were not produced properly the first time; over nine hundred files had to be evaluated, and if the motifs were only reviewed by the naked eye, numerous issues would be overlooked.  Assessments were developed and put in place to ensure that each motif contained its information, residue pair configurations, implementations of the search algorithm for each structure, and a map structure that consisted of the matches found from the search algorithm if all aforementioned implementations were successful.  They analyzed the results of the parser and determined how many motifs failed, which motifs failed, how many of each type of motif failed, and how many motifs had the current number of residue pair dictionaries.  Tables were utilized to portray the results of these reviews by the usage of Pandas, a data science library.  While simple parsers fixed the minor problems, such as missing lines and syntax errors in the motifs, more complicated issues, such as missing or misplaced data, required more complex parsers.  Methods were developed to monitor the individual progress of the structures necessary, incorporate new components, predict the possible residue combinations, collect the keys of the residue pair structures as they are initialized, and compare the observed list of pairs to the expected list. After all of the appropriate maps were assembled, they were inspected.  The shape, size, and content of the structures were analyzed, and if any of the tests failed, the details were printed in coherent and user-friendly formats.  It would describe which tests had failed and the reason they failed, and it would give the user options to further analyze the results of the tests.  Although these tests provide helpful information, they did not resolve the ill-produced data structures, and a new approach to parsing the files was crucial.  First, the most recently written parser asked the current motifs two essential questions:
1. Are there more residue pairs than originally predicted?
2. Does the motif contain both orientations of the residue pairs?

The parser converted the solutions into two flags near the top of the file, and they determine how the residue pairs must be handled for each motif.  If the response to both questions is no, the motifs do not need any adjustments, and they are rebuilt as the same file and stored into the new directory.  If the first solution is no, though, the parser studies each residue pair structure.  It finds the poorly produced maps by examining the lengths of rows in the distance and comparison matrices and observing the main atom for each row in the comparison matrices.  If any lengths differ, the matrix is ill-formed, and if the results of applying the test on the comparison matrices and the distance matrices differ, an exception is raised that indicates that the issue is just a manageable bug.  If the same main atom arises more than once in the same comparison matrix, the entire residue pair configuration contains multiple structures inside it.  Both assessments collect the indices of the rows that contain the beginning of a residue pair structure, splits the matrices at those indices, creates new residue pair configurations, and converts them into appropriate motif file format.  

Currently, there is only a procedure to handle the solution first question, but an appropriate approach to the second concern is to perform the search algorithm to both orientations of the residue pair structure, combines the results into a 2D array, and apply principal components analysis to that matrix to determine which orientation is a better fit if the solution to the question is yes.  If the answer is no, assemble a dictionary that maps the name of the motif to the names of missing residue pair configurations, revisit and examine the original motifs, find the missing structures, build the residue pair structures using the established system, and add the new structures to the current motif files.

#### Saving the Results of the Search Algorithm
The primary goals of the fall semester were to implement principal components analysis and to possess suitable files that portray catalytic sites through residue comparisons, implement the search algorithm produced over the summer for each comparison, and construct a map of the results of the algorithm.  Each motif has a match dictionary that maps the residue pair names to a 2D array that contains the atom objects and their locations in the KD tree.  However, the ultimate goal was to study a protein family and compare the results for each protein structure.  The comparison matrix of each residue pair structure is looped through, each row is portrayed as a cluster, and the search algorithm individually looks for each cluster in each protein structure.  After each residue pair configuration utilizes the search algorithm, the results are inserted into a dictionary that maps the names of the residue pair ID to its results to the implementation.  Methods were written to dissect the results of each implementation, store the attributes of the atoms and the time of the search for the cluster into a map, and by using Pandas, the atom map is converted into a table and stored in a pickel file.  The atom's name, x-, y- , and z-coordinate, occupany, and temperature factor, the name of residue it exists in, and the chain ID of the aforementioned residue are all essential attributes that were extracted from the original atom classes.  Pandas also can convert the tables into SQL, and the mysql module can connect the python program to MySQL server.  A relational database instance was initalized on Amazon Web Services, and the development of the test that analyzes the connection between the program and the server.  An entity relational diagram was designed in Lucidchart to portray the layout of the components of the database.  Once the implementations of the search algorithm run successfully for each protein structure, motif files can implement the methods that govern the results, and they can be converted from tables and pickle files to sql tables.  The tables can be organized by the protein structures and stored into the MySQL database on Amazon Web Services after the connection is secured.

#### Development as a Developer
A significant amount of growth occurred this semester.  Principal components analysis was studied, dissected, modified, and implemented.  Testing and handling edge cases in Big Data is a long, intricate process, exceptions and comments are crucial, and managing ill-produced and inconsistent data is also a complex, difficult job.  If a program needs to handle a large variety of input, the program must be exceedling thorough, record issues that arise, and describe each method and implemention extensively.  Several parsers were developed, and they must clearly specify how each line of a file will be handled because if seemly trivial portions are ignored, they will fail to properly produce the appropriate files.  Amazon Web Services, Pandas, and version control have been incorporated into the project.  Git, a version control system, was utilized to maintain and push the updates of the project, record and commit progress, improvements, and issues, and add new files to the respective respository on Github.  It was also connected to the program in PyCharm, powershell was used to update the repository, and draw.io and dillinger.io were connected to Github.  The final report was also written in Markdown.



___

*TODO*


-Editting-
 [ ] &nbsp;&nbsp; Fix grammer -> verb inconsistency (find way to make them active)
 [ ] &nbsp;&nbsp; Flowchart	Timeline is ugly & flowchart can be made

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
