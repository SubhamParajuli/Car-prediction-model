import nbformat

def combine_ipynb(files, output_file):
    combined_notebook = nbformat.v4.new_notebook()

    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            notebook = nbformat.read(f, as_version=4)
            combined_notebook.cells.extend(notebook.cells)

    with open(output_file, 'w', encoding='utf-8') as f:
        nbformat.write(combined_notebook, f)

# List of input .ipynb files to combine
input_files = ['1_1Data Cleaning Car_drop_model.ipynb', '1__2Data Cleaning Car - with Model.ipynb', 'plots.ipynb','2_Checking the Assumptions with EDA.ipynb','Linear_Regression_fiaal.ipynb','Random_Forest_2_with_model_column_4241_test_error.ipynb']

# Name of the output .ipynb file
output_file = 'combined_notebook.ipynb'

# Combine the notebooks
combine_ipynb(input_files, output_file)
