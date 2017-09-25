# matching-functions

Where Motifs were Taken From and How they were Taken:

- Motifs were taken from the repository sbevsl_migrated under the folder:
  sbevsl_migrated/promol/ProMol/Motifs/
- Motifs were taken by:
    - copying and pasting individually
    - Cloning into zip file

What packages were used:
  - __future__
    - division
    - print_function
    - absolute_import
  - heapq
    - heappush
    - heappop
  - Numpy
    - linalg
  - SciPy
    - stats
    - misc
  - Anacondaq

Changes in Motifs:
- Changed purpose of select function
    - Parses PyMOL selection algebra and stores data into two matrices
    - No longer is used as search algorithm
- select (PyMOL selection algebra parser) calls removed & select's purpose removed and is replaced with:
    - Comparison and distance matrices for each residue pair
- Removed repeated searches
- Principal component analysis and search algorithm implemented at end using detect function


The Motifs' Parser:
- All motifs stored in directory and directory is taken as argument
- Loop through directory and edit each motif file
    - Initializes the new content as an empty string
        - Will add new content to this argument as it goes through the file
    - Adds info about motif to the new content parameter
    - Initializes a filename as an empty string, then assigns the name of the motif to it
    - Initializes 2 maps and a list
        - Calculates the number of possible residue pairs using NumPy's permutation function
        - Fills the list with empty strings until its length is equivalent to that aforementioned number
    - Convert each line to string (to achieve behavior of a text file)
    - Skip all delete calls and select calls that used to expand selection to complete residues
    - Skip repeated searches with check inside select function (i.e. select no longer stores data for the search of each atom in res1 
      near res 2 AND for the search of each atom in res 2 near res1 - only one set of comparisons )
    - Ignore names in select calls and call select for each comparison
    - Builds distance matrices and comparison matrices for each residue pair
        - Comparisons are represented as tuples that contain the first atom and residue name, the second atom and residue name, and the 
          distance limit between them respectively
        - Distances are stored as single floats
        - Stores the distance matrices into one map and the comparison matrices into the other map, where the keys for both maps are a 
          tuple of the residue pair
    - Converts matrices into strings using a tostring function
        - Adds string of matrices to the new content parameter
    - Opens a file using the file name
    - Writes the new content onto the new file
    - Stores it onto a new directory


Setting Up the Protein Structure Data

- Download PDB file from RCSB site
- Parse PDB Files into objects
- Sort atom objects into KD-Tree


Using KD-Tree Structure
- Takes in a large list of atom objects to represent the protein structure
- Data is sorted into smaller groups until it can easily be sorted by their coordinates
- Methods include:
    - Query: Search for nearest neighbors of an atom object
    - Query Pairs: Searches for a pair of atoms that fit conditions, the uses query to search for the nearest neighbors of the main atom
- Classes used:
    - Rectangle: A hyperrectange that splits tree using midpoints and merge sort algorithm to shorten search
- Other functions: 
    - Modified NumPy methods to allow atom objects to be taken in
        - all
        - max & min
        - nonzero
        - maximum
   - isQualified method to test if a comparison fits certain criteria
   - Method to return an atom's coordinate (i.e. Takes in 2 and returns z-coordinate)
   - Other methods to allow data structures that contain atom objects to have the same abilities as arrays in NumPy:
        - Allowing operations to be done between vectors and scalars 
        - Applying a list of indices onto another list to shorten original list
- Functions used in file, but exist in other:
    - Euclidean Distance: Finds the euclidean distance between two atoms and a list of distance between an atom and a list of atoms 
- Classes used outside of file
    - Argument Error
        - Source: https://docs.python.org/2/tutorial/errors.html

Applying Principal Component Analysis

- Apply PCA to each distance matrix and their transpose matrices
    - Standardize matrix by subtracting it by its mean and dividing it by it's standard deviation
    - Find matrix's covariance matrix
    - Find the eigenvalues of the covariance matrix, then take the absolute value and only the real parts
    - Scale the eigenvalues between 0 and 1, then remove the eigenvalues that are seen as 0
- Save which components that have the largest eigenvalues
- The indices for the matrix and the indices for the transpose of the matrix are applied to the object matrices
- Unwanted comparisons are removed and allows ProMOL to skip them.
- Sources:
    - https://stackoverflow.com/questions/4544292/how-do-i-standardize-a-matrix
    - https://www.researchgate.net/post/What_is_the_best_way_to_scale_parameters_before_running_a_Principal_Component_Analysis_PCA
    - http://www.vision.jhu.edu/teaching/vision08/Handouts/case_study_pca1.pdf


Solving for the Covariance Matrix

- Find the mean of the columns
- Generate the matrix of the subtraction of the original matrix and the columns' mean
- The result is the dot product between that matrix and its transpose
- Sources:
    - http://www.cs.toronto.edu/~guerzhoy/320/lec/pca.pdf
    - http://www.vision.jhu.edu/teaching/vision08/Handouts/case_study_pca1.pdf


Scaling Data

- Find the minimum and the maximum of the data
- Subtract the mean from each value
- subtract the min from the max: The range of the data
- The new data is the division between the range and the second step
- Source:
    - https://docs.tibco.com/pub/spotfire/7.0.0/doc/html/norm/norm_scale_between_0_and_1.htm


Purpose and Application of PCA:

- Lower the number of searches in each motif because the constraints themselves cannot change
- Compare the variance between one residue structure with each atom from the other residue structure by applying PCA to the distance 
  matrix
- Compare the variance between the other residue with each atom in the first residue by applying PCA to the transpose of the distance 
  matrix
- Finds which set of comparisons (columns in the matrix) to keep for comparing that residue pair


Search Algorithm
- The comparison matrix is transformed into a list of clusters - Cluster objects
- Search algorithm is applied to each cluster
- It searches for a specific atom near a cluster: 
      - Once it finds a pair between the atom and an atom from the cluster, k-nearest neighbor is implemented
      - If one atom fails to be near a cluster, the motif fails and terminates
      - If all searches are successful, motif is successful and indices for matches are stored

What Else Exists:

- Old methods and algorithms
- PDB files used
- Used methods
- Testing files


