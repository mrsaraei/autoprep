# AutoPrep
**Automated CSV Clinical Data Preprocessing**

**پیش پردازش اتوماتیک داده های بالینی مبتنی بر فرمت CSV**

![VisualizePreprocessedData](AutoPrep.jpg)(docs/README.md)

This project has been modified in following steps on October 20, 2023:

* Step 1 [Done]: The required Python libraries would be imported.
* Step 2 [Done]: All object values in DataFrame would be encoded.
* Step 3 [Done]: All raw values in DataFrame would be normalized.
* Step 4 [Done]: All duplicate values in DataFrame would be removed.
* Step 5 [Done]: All unknown values in DataFrame would be replaced by NaN.
* Step 6 [Done]: All missing values in DataFrame would be replaced by mean.
* Step 7 [Done]: All preprocessed values in DataFrame would be reordered.
* Step 8 [Done]: All outliers in DataFrame would be removed.
* Step 9 [Done]: All values in DataFrame would be visualized.
* Step 10 [Done]: The preprocessed data would be saved as 'PreprocessedData.csv'.
* Step 11 [Done]: The feature names would be saved as 'FeatureName.csv'.

**How to install and use AutoPrep**

# install AutoPrep Python Package from PyPI
pip install autoprep

# Import PreProcessCSV from AutoPrep Python Package
from autoprep import PreProcessCSV

# Call the AutoPrep function with the file path as an argument
preprocessed_df = PreProcessCSV('data_sample/[YourDataName].csv')

The following is a step-by-step explanation of what the code does:

1. The first line, `# install AutoPrep Python Package from PyPI`, is a comment. Python comments are ignored by the interpreter, so they are used to document the code.
2. The second line, `# pip install AutoPrep`, is a command that tells Python to install the AutoPrep Python package.
3. The third line, `from autoprep import PreProcessCSV`, tells Python to import the `PreProcessCSV` function from the AutoPrep Python package.
4. The fourth line, `preprocessed_df = PreProcessCSV('Dataset/[YourDataName].csv')`, calls the `PreProcessCSV` function with the file path to your dataset as the argument.
5. The `PreProcessCSV` function preprocesses the dataset and returns a Pandas DataFrame containing the preprocessed data. The `preprocessed_df` variable will contain the preprocessed data.

Once you have preprocessed the dataset, you can use it to train your machine learning model. 

For more information about how to install AutoPrep Python Package on your custom dataset, please check the [documentation](docs/README.md).

If you have any questions, please feel free to contact mrsaraei3@gmail.com.
