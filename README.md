# AutoDataAnalytics: Data Exploration and Univariate Data Analysis Tool

## Overview
**AutoDataAnalytics** is an interactive tool designed for data exploration and univariate data analysis. It simplifies the process of analyzing and understanding datasets, providing users with key insights and visualizations through an intuitive interface built using Streamlit. Users can upload CSV or Excel files to explore dataset features, perform univariate analysis, and visualize data distributions. The tool provides essential features such as missing value detection, correlation matrices, summary statistics, and various visualization options including histograms, bar charts, and pie charts.

## Features
- **Dataset Exploration**: 
    - View the first and last 5 rows of the dataset.
    - Check the shape and basic information of the dataset.
    - View data types, column names, and the count of unique values.
    - Identify missing values and duplicates.
    - Generate summary statistics for numerical columns.

- **Univariate Data Analysis**:
    - Perform univariate analysis for both numerical and categorical columns.
    - Visualize data distribution using histograms, box plots, bar charts, and pie charts.
    - Analyze the frequency of categories for categorical variables.

- **Correlation Matrix & Heatmap**:
    - Display a correlation matrix for numerical columns.
    - Visualize the correlation using a heatmap for better insights into relationships between numerical features.

## Technologies Used
- **Python**: Core programming language.
- **Streamlit**: Web framework for building the interactive dashboard.
- **Pandas**: Data manipulation and analysis.
- **Seaborn** and **Matplotlib**: Visualization libraries for generating charts and graphs.
- **Numpy**: Numerical operations.
- **Regular Expressions (re)**: For file type validation.

## Installation

To use the tool, follow these steps:

1. **Clone the repository** (or download the code):
   ```bash
   git clone https://github.com/itsbilyatt/data_exploration_and_univariate_data_analysis
   ```

2. **Install the required dependencies**:
   - Create a virtual environment (optional but recommended):
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```bash
       venv\Scripts\activate
       ```
     - On macOS/Linux:
       ```bash
       source venv/bin/activate
       ```

   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```

3. **Run the app**:
   ```bash
   streamlit run app.py
   ```

## How to Use
1. **Upload CSV or Excel File**:
   - The tool allows users to upload either a CSV or Excel file. After selecting a file, it will be automatically read and processed.

2. **Explore Data**:
   - Once the file is uploaded, the dataset is displayed in various formats, including the first and last five rows, summary statistics, missing values, and more.
   - You can click on different buttons to view dataset details like column names, data types, and unique values.

3. **Univariate Data Analysis**:
   - After exploring the dataset, users can perform univariate analysis on both numerical and categorical columns.
   - Different visualizations are available to explore the data distribution, including histograms, box plots, bar charts, and pie charts.

4. **Visualize Data**:
   - Interactive plots and charts are generated for both numerical and categorical columns, making it easy to analyze the data visually.

## Example Usage
- **Explore Data**: Analyze basic statistics, shape of the dataset, and view the first and last few rows.
- **Univariate Data Analysis**: Select a column and explore its distribution using various charts.
- **Correlation Matrix**: Visualize the relationship between numerical features using a heatmap.

## Sample Output

### Example 1: Dataset Information
- **First 5 Rows**: Displays the first five rows of the dataset for a quick overview.
- **Summary Statistics**: Displays key metrics like mean, standard deviation, min, max, etc.
- **Missing Values**: Identifies the number of missing values in each column.

### Example 2: Univariate Analysis
- **Histogram**: Visualizes the distribution of a numerical column.
- **Bar Chart (Categorical)**: Displays the frequency of each category in a categorical column.
- **Box Plot**: Highlights data distribution and identifies outliers.

## Future Enhancements
- Support for additional file formats (e.g., JSON, Parquet).
- Extend the tool to support bivariate analysis and multivariate visualizations.
- Add advanced data preprocessing features like data imputation and scaling.

## Author
- **Prajyot Birajdar**  
  [LinkedIn Profile](https://www.linkedin.com/in/prajyot-birajdar-1b09a1173/) | [GitHub Profile](https://github.com/itsbilyatt/data_exploration_and_univariate_data_analysis)

## Live Demo
You can try the tool directly on the live Streamlit app: [AutoDataAnalytics Demo](https://dataexplorationandunivariatedataanalysis.streamlit.app/)

