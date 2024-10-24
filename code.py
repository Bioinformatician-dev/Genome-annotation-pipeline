import subprocess
import os

def create_output_directory(output_dir):
    """Create an output directory if it doesn't exist."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

def run_prokka(input_file, output_dir):
    """Run Prokka annotation on the input genomic data."""
    command = [
        'prokka',
        '--outdir', output_dir,
        '--prefix', os.path.basename(input_file).split('.')[0],
        input_file
    ]
    try:
        subprocess.run(command, check=True)
        print(f"Annotation completed successfully. Results are in {output_dir}.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running Prokka: {e}")

def main():
    """Main function to execute the genome annotation pipeline."""
    input_file = input("Enter the path to the genomic data file: ")
    output_dir = input("Enter the output directory for annotations: ")

    create_output_directory(output_dir)
    run_prokka(input_file, output_dir)

if __name__ == "__main__":
    main()
