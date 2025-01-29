# Description of the project

Gibs sampling provides a method to identify reoccuring motifs in the DNA sequence using an algorithm with random sampling. The program initializes with the sequencing from a randomly positioned motif to once again pick sequences to exclude randomly. The position weight matrix (PWM), the model that weight nucleotides accordingly to transcription, is then calculated with the position frequency matrix (PFM) with the selected kmer. Then the best motif position is measured using the kmer against PWM with the highest motif score with the complementary strand. 

# Pertinent documentation and usage write-up

Python ver. 3.11
Packages: numpy, seqlogo

Run the program via an IDE or python in the terminal. Recommended to use a bioconda environment opposed to assembling a local virtual environment.

### Required Data
"GCF_000009045.1_ASM904v1_genomic.fna"
"GCF_000009045.1_ASM904v1_genomic.gff"

# Pseudocode

The functions provided needs a careful read through to see how the motifs and kmers are interacted with a for loop to first get the number of initial runs to build the GibbsMotifFinder. Review the documentation in seqlogo. Once the program runs and the randomly selected DNAs pass through the build_pfm and build_pwm function considering how to aquire the best score from the negative and positive level must also be considered. The number of iteration once the program runs would also be tested ranging from 1000 to 5000.

# Reflection 

Using a local environment ran into an OS error for seqlogo, a bioconda environment with initialized replacing the local virtual environment to run smoothly. Another issue would be Window operating systeming being unable to identify the gswin32c.exe which led to the path to the file to be set by user. Testing for convergence, the iteration would end very quickly within around 50 iterations on average until it met the threshold score 0.001. There was also uncertaintly setting the iteration number however the problem quickly ran 1000 cycles. Setting the convergence threshold was also uncertain as we didn't know what should be set.

# Appendix 

Tang, D. (2013, October 1). Position weight matrix. Dave Tang's blog. https://davetang.org/muse/2013/10/01/position-weight-matrix/




