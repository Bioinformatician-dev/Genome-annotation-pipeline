import os
import subprocess

def run_prokka(genome_file, output_dir, strain_name):
    """Run Prokka for genome annotation."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    prokka_command = [
        "prokka",
        "--outdir", output_dir,
        "--prefix", strain_name,
        "--genus", "YourGenus",  # Replace with actual genus
        "--species", "YourSpecies",  # Replace with actual species
        genome_file
    ]

    try:
        subprocess.run(prokka_command, check=True)
        print(f"Prokka annotation completed for {strain_name}!")
    except subprocess.CalledProcessError as e:
        print(f"Error running Prokka: {e}")

def main():
    print("Welcome to the Genome Annotation Pipeline using Prokka!")
    
    genome_file = input("Enter the path to the genomic FASTA file: ")
    output_dir = input("Enter the output directory for annotations: ")
    strain_name = input("Enter the strain name (prefix for output files): ")

    # Validate input file existence
    if not os.path.isfile(genome_file):
        print("Error: The specified genomic FASTA file does not exist.")
        return

    run_prokka(genome_file, output_dir, strain_name)

if __name__ == "__main__":
    main()
