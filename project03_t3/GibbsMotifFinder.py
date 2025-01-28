import numpy as np
import seqlogo
from data_readers import *
from seq_ops import get_seq
from motif_ops import *

def GibbsMotifFinder(seqs, k, seed=42, iterations=1000):
    '''
    Function to find a pfm from a list of strings using a Gibbs sampler
    
    Args: 
        seqs (str list): a list of sequences, not necessarily in same lengths
        k (int): the length of motif to find
        seed (int, default=42): seed for np.random

    Returns:
        pfm (numpy array): dimensions are 4xlength
        
    '''
    #Set random seed to make results reproducible.
    np.random.seed(seed)
    
    #Initialize motif positions randomly.
    positions = [np.random.randint(0, len(seq) - k + 1) for seq in seqs]
    
    for _ in range(iterations):
        #Randomly pick a sequence to leave out.
        idx = np.random.randint(len(seqs))
        removed_seq = seqs[idx]
        del positions[idx]
        
        #Build PFM excluding the removed sequence.
        selected_kmers = [seqs[j][positions[j]:positions[j] + k] for j in range(len(positions))] #Extracts the current motif from all other sequences, excluding the removed sequence.
        pfm = build_pfm(selected_kmers, k) #Build a Position Frequency Matrix (PFM) from the selected kmers.
        pwm = build_pwm(pfm) #Convert the PFM to a PWM.
        
        #Scan removed sequence for best motif position.
        best_score = float('-inf') #Initializing "best score" to negative infinity allows us to track the highest scoring position.
        best_position = 0 #Initialize the best position.
        for i in range(len(removed_seq) - k + 1): #Iterate over all possible k-mers in the removed sequence.
            kmer = removed_seq[i:i + k]
            score, _, _ = score_sequence(kmer, pwm) #Score each kmer against PWM.
            if score > best_score: #Update the best position to the position with the highest motif score. 
                best_score = score
                best_position = i
        
        #Reinsert best position.
        positions.insert(idx, best_position)
    
    #Build final PFM.
    final_kmers = [seqs[i][positions[i]:positions[i] + k] for i in range(len(seqs))] #Extract the final set of motifs.
    pfm = build_pfm(final_kmers, k) #Constructs a final pfm.
    
    return pfm

# Here we test your Gibbs sampler.
# You do not need to edit this or the section below. This is the Driver program

#read promoters, store in a list of strings
seq_file="GCF_000009045.1_ASM904v1_genomic.fna"
gff_file="GCF_000009045.1_ASM904v1_genomic.gff"

seqs = []

for name, seq in get_fasta(seq_file): # For each entry in our FASTA file
    for gff_entry in get_gff(gff_file): # For each entry in our GFF file
        if gff_entry.type == 'CDS': # If this is a coding sequence
            promoter_seq = get_seq(seq, gff_entry.start, gff_entry.end, gff_entry.strand, 50) # Extract 50 bp as a promoter
    
            """
            Because the gibbs sampling assumption is broken in just using promoters,
            and because it takes very long time to randomly progress through so many
            regions, for this example we will pre-filter for sequences that all contain
            part of the shine-dalgarno motif:
            """
            if "AGGAGG" in promoter_seq:
                seqs.append(promoter_seq)

# Run the gibbs sampler:
promoter_pfm = GibbsMotifFinder(seqs,10)

# Plot the final pfm that is generated: 
seqlogo.seqlogo(seqlogo.CompletePm(pfm=promoter_pfm.T), format='png', filename="motif_logo.png")
