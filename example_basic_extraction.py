"""
Basic PDF Extraction Example

This example demonstrates the simplest way to extract data from PDFs.
"""

from pdf_extractor_final import process_pdfs
import os

def main():
    """
    Basic extraction example
    """
    # Specify your input directory
    input_directory = 'path/to/your/pdf/files'
    
    # Specify output file
    output_file = 'extracted_data.csv'
    
    # Check if directory exists
    if not os.path.exists(input_directory):
        print(f"Error: Directory not found: {input_directory}")
        print("\nPlease update the 'input_directory' variable in this script.")
        return
    
    print("Starting PDF extraction...")
    print(f"Input: {input_directory}")
    print(f"Output: {output_file}\n")
    
    # Extract data
    df = process_pdfs(input_directory, output_file)
    
    # Display summary
    print(f"\n✅ Extraction complete!")
    print(f"Total records: {len(df)}")
    print(f"\nFirst few records:")
    print(df[['Patient_ID', 'Age', 'Gender', 'City', 'Hb', 'HbA2']].head())


if __name__ == '__main__':
    main()
