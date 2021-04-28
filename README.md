# Redcoat annotations processing

A simple script to convert Redcoat annotations into true JSON and CSV.

## Running the script

First, open `process_annotations.py` and set the three variables:


   INPUT_FILE - The path to your annotations file, e.g. 'example_annotations.json'
   OUTPUT_FILE_JSON - The path to save the exported JSON annotations, e.g. 'output.json'
   OUTPUT_FILE_CSV - The path to save the exported CSV annotations, e.g. 'output.csv'

Then, run `process_annotations.py`. Two files will be created - a JSON export, and a CSV export. The CSV is designed to be human readable, as each mention is in a new column.
