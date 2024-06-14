##################################################################################################
# Created by Prajyot Birajdar
##################################################################################################
##################################################################################################
# import required library
##################################################################################################
import io
import re
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
from datetime import datetime
import matplotlib.pyplot as plt

##################################################################################################
# AutoDataAnalytics class 
##################################################################################################

class AutoDataAnalytics:
    def __init__(self) -> None:
        pass

    @staticmethod
    def funny_welcome():
        current_hour = datetime.now().hour

        if 5 <= current_hour < 12:
            return "Welcome, Good morning🌞"
        elif 12 <= current_hour < 18:
            return "Welcome, Good afternoon! "
        else:
            return "Welcome, Good evening! 🌙"
        

    @staticmethod
    def dataset_info(df):
        if "button1_clicked" not in st.session_state:
            st.session_state["button1_clicked"] = False
        if st.button("First Five row",type="primary"):
            st.session_state["button1_clicked"] = not st.session_state["button1_clicked"]

        if st.session_state["button1_clicked"]:
            st.header(" First Five row:")
            st.dataframe(df.head(),hide_index=True)
            st.header(" ", divider="rainbow")

     
        # tail
        if "b1" not in st.session_state:
            st.session_state["b1"] = False
        if st.button("Last Five row",type="primary"):
            st.session_state["b1"] = not st.session_state["b1"]
        if st.session_state["b1"]:
            st.header(" Last Five row:")
            st.dataframe(df.tail(),hide_index=True)
            st.header(" ", divider="rainbow")

        # shape
        if "b2" not in st.session_state:
            st.session_state["b2"] = False
        if st.button("Shape of Dataset",type="primary"):
            st.session_state["b2"] = not st.session_state["b2"]
        if st.session_state["b2"]:
            st.header("Dataset Shape:")
            st.write(f"**{df.shape}**")
            st.header(" ", divider="rainbow")

        # info
        if "b3" not in st.session_state:
            st.session_state["b3"] = False
        if st.button("Full information about dataset",type="primary"):
            st.session_state["b3"] = not st.session_state["b3"]
        if st.session_state["b3"]:
            st.header("Dataset all inforamtion:")
            buffer = io.StringIO()
            df.info(buf=buffer)
            info_string = buffer.getvalue()
            st.text(info_string)
            st.header(" ", divider="rainbow")

        # all columns
        if "b4" not in st.session_state:
            st.session_state["b4"] = False
        if st.button("All columns Name",type="primary"):
            st.session_state["b4"] = not st.session_state["b4"]
        if st.session_state["b4"]:
            st.header("\nColumn Names:")
            st.write(f"**{str(df.columns)**")
            st.header(" ", divider="rainbow")

        
        if "b5" not in st.session_state:
            st.session_state["b5"] = False
        if st.button("Data type of each column",type="primary"):
            st.session_state["b5"] = not st.session_state["b5"]
        if st.session_state["b5"]:
            st.header("\nData Types:")
            st.dataframe(df.dtypes)
            st.header(" ", divider="rainbow")
        

        # Summary statistics
        if "b6" not in st.session_state:
            st.session_state["b6"] = False
        if st.button("Summary Statistics",type="primary"):
            st.session_state["b6"] = not st.session_state["b6"]
        if st.session_state["b6"]:
            st.header("\nSummary Statistics:")
            st.write(df.describe())
            st.header(" ", divider="rainbow")
        
        # Missing values
        if "b7" not in st.session_state:
            st.session_state["b7"] = False
        if st.button("Missing Values",type="primary"):
            st.session_state["b7"] = not st.session_state["b7"]
        if st.session_state["b7"]:
            st.header("\nMissing Values:")
            st.write(df.isnull().sum())
            st.header(" ", divider="rainbow")
        
        # Correlation matrix
        if "b8" not in st.session_state:
            st.session_state["b8"] = False
        if st.button("Correlation Matrix and Heatmap",type="primary"):
            st.session_state["b8"] = not st.session_state["b8"]
        if st.session_state["b8"]:
            numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
            if not numeric_cols.empty:
                st.header("\nCorrelation Matrix:")
                st.write(df[numeric_cols].corr())
                st.header(" ", divider="rainbow")
                st.header("HEATMAP")
                st.header(" ", divider="rainbow")

                # heatmap
                if "b9" not in st.session_state:
                    st.session_state["b9"] = False
                if st.button("HeatMap",type="primary"):
                    st.session_state["b9"] = not st.session_state["b9"]
                if st.session_state["b9"]:
                    corr_matrix = df[numeric_cols].corr()
                    fig, ax = plt.subplots(figsize=(20, 16))
                    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax)
                    # Add labels and title
                    ax.set_title('Correlation Heatmap')
                    ax.set_xlabel('Features')
                    ax.set_ylabel('Features')
                    st.pyplot(fig)
                    st.header(" ", divider="rainbow")
        # Unique values in each column
        if "b10" not in st.session_state:
            st.session_state["b10"] = False
        if st.button("Unique Values in Each Column",type="primary"):
            st.session_state["b10"] = not st.session_state["b10"]
        if st.session_state["b10"]:
            st.header("\nUnique Values in Each Column:")
            for col in df.columns:
                st.write(f"{col}: {df[col].nunique()} unique values")
            st.header(" ", divider="rainbow")
        
        # Value counts for categorical columns

        if "b11" not in st.session_state:
            st.session_state["b11"] = False
        if st.button("Value Counts for Categorical Columns",type="primary"):
            st.session_state["b11"] = not st.session_state["b11"]
        if st.session_state["b11"]:
            st.header("\nValue Counts for Categorical Columns:")
            for col in df.select_dtypes(include='object').columns:
                st.write(f"{col}:")
                st.write(df[col].value_counts())
            st.header(" ", divider="rainbow")

        if "b12" not in st.session_state:
            st.session_state["b12"] = False
        if st.button("Number of Duplicate rows",type="primary"):
            st.session_state["b12"] = not st.session_state["b12"]
        if st.session_state["b12"]:
            st.header("\n Number of Duplicate rows:")
            st.write(df.duplicated().sum())
    
    @staticmethod
    def univariate_data_analysis(df):
        # num cat
        numerical_columns_univariate_analysis,categorical_columns_univariate_analysis = st.tabs(["Numerical Columns Univariate Analysis","Categorical Columns Univariate Analysis"])
        with numerical_columns_univariate_analysis:
            if "num" not in st.session_state:
                st.session_state["num"] = False
            if st.button("Numerical Columns Univariate Analysis",type="primary"):
                st.session_state["num"] = not st.session_state["num"]
            if st.session_state["num"]:
                numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns
                # st.write(list(numerical_columns))
                selected_option = st.selectbox(
                                            '**Select Numerical column for Univariate data analysis**',
                                            numerical_columns
                                        )
        

                if "b13" not in st.session_state:
                    st.session_state["b13"] = False
                if st.button("Column Ananlysis",type="primary"):
                    st.session_state["b13"] = not st.session_state["b13"]
                if st.session_state["b13"]:
                    st.header("\n First Five rows:")
                    st.write(df[selected_option].head())
                    st.header("\n Column Analysis:")
                    st.write(df[selected_option].describe())
                    st.header("\n Null value count:")
                    st.write(df[selected_option].isnull().sum())
                    st.header("\n Value count:")
                    st.write(df[selected_option].value_counts())


                if "b14" not in st.session_state:
                    st.session_state["b14"] = False
                if st.button("HISTOGRAM",type="primary"):
                    st.session_state["b14"] = not st.session_state["b14"]
                if st.session_state["b14"]:
                    st.write(
                        """**A histogram is used to visualize the distribution of numerical data. 
                            It consists of bars that represent the frequency or count of data points within predefined intervals (bins).
                            Histograms provide insights into the shape, central tendency, and spread of the data.**"""
                    )
                    fig, ax = plt.subplots(figsize=(20, 16))
                    sns.histplot(data=df, x=selected_option, color='red')
                    ax.set_title(f'Histogram for {selected_option}')
                    st.pyplot(fig)
                    st.header(" ", divider="rainbow")

                if "b15" not in st.session_state:
                    st.session_state["b15"] = False
                if st.button("BAR CHART",type="primary"):
                    st.session_state["b15"] = not st.session_state["b15"]
                if st.session_state["b15"]:
                    fig, ax = plt.subplots(figsize=(20, 16))
                    sns.histplot(data=df, x=selected_option, color='red')
                    ax.set_title(f'BAR CHART for {selected_option}')
                    st.pyplot(fig)
                    st.header(" ", divider="rainbow")

                if "b16" not in st.session_state:
                    st.session_state["b16"] = False
                if st.button("Frequency Polygon",type="primary"):
                    st.session_state["b16"] = not st.session_state["b16"]
                if st.session_state["b16"]:
                    fig, ax = plt.subplots(figsize=(20, 16))
                    sns.histplot(data=df, x=selected_option, kde=True, color='red', bins=20)
                    ax.set_title(f'Frequency Polygon for {selected_option}')
                    st.pyplot(fig)
                    st.header(" ", divider="rainbow")

                
                if "b17" not in st.session_state:
                    st.session_state["b17"] = False
                if st.button("Box Plot",type="primary"):
                    st.session_state["b17"] = not st.session_state["b17"]
                if st.session_state["b17"]:
                    st.write(
                        """**Box plots are effective for visualizing the distribution of numerical data and identifying outliers.**"""
                    )
                    fig, ax = plt.subplots(figsize=(20, 16))
                    sns.boxplot(data=df, x=selected_option,  color='red')
                    ax.set_title(f'Box Plot for {selected_option}')
                    st.pyplot(fig)
                    st.header(" ", divider="rainbow")

            # cat
        with categorical_columns_univariate_analysis:
            if "cat" not in st.session_state:
                st.session_state["cat"] = False
            if st.button("Categorical Columns Univariate Analysis",type="primary"):
                st.session_state["cat"] = not st.session_state["cat"]
            if st.session_state["cat"]:
                categorical_columns = df.select_dtypes(include=['object']).columns
                # st.write(list(numerical_columns))
                selected_option = st.selectbox(
                                            '**Select Categorical column for Univariate data analysis**',
                                            categorical_columns
                                        )
                
                if "b20" not in st.session_state:
                    st.session_state["b20"] = False
                if st.button("Categorical Column Ananlysis",type="primary"):
                    st.session_state["b20"] = not st.session_state["b20"]
                if st.session_state["b20"]:
                    st.header("\n First Five rows:")
                    st.write(df[selected_option].head())
                    st.header("\n Column Analysis:")
                    st.write(df[selected_option].describe())
                    st.header("\n Null value count:")
                    st.write(df[selected_option].isnull().sum())
                    st.header("\n Value count:")
                    st.write(df[selected_option].value_counts())


                
                if "b31" not in st.session_state:
                    st.session_state["b31"] = False
                if st.button("BAR CHART(C)",type="primary"):
                    st.session_state["b31"] = not st.session_state["b31"]
                if st.session_state["b31"]:
                    st.write(
                        """**Bar charts are commonly used for visualizing categorical data in univariate analysis.
                            They display the frequency or count of each category as bars, making it easy to compare the distribution of different categories.**"""
                    )
                    fig, ax = plt.subplots(figsize=(20, 16))
                    sns.histplot(data=df, x=selected_option, color='red')
                    ax.set_title(f'BAR CHART for {selected_option}')
                    st.pyplot(fig)
                    st.header(" ", divider="rainbow")

                    
                if "b32" not in st.session_state:
                    st.session_state["b32"] = False
                if st.button("PIE Chart",type="primary"):
                    st.session_state["b32"] = not st.session_state["b32"]
                if st.session_state["b32"]:
                    st.write(
                        """**Pie charts are useful for representing the proportion or percentage of each category in a dataset.
                            They provide a visual representation of the relative sizes of different categories in the data.**"""
                    )
                    value_counts = df[selected_option].value_counts()
                    fig, ax = plt.subplots(figsize=(20, 16))
                    plt.pie(value_counts, labels=value_counts.index, autopct="%1.1f%%")  # Show percentage on wedges
                    plt.title(f"Pie Chart - {selected_option}")
                    st.pyplot(fig)
                    st.header(" ", divider="rainbow")

ob = AutoDataAnalytics


##################################################################################################
# Upload csv and implement functinality
##################################################################################################
st.title("Tool For Data Exploration and Univariate Data Analysis")

st.header(
    ob.funny_welcome()
)
st.header(
    " ", divider="rainbow"
)
st.subheader(
    "PLEASE UPLOAD CSV OR EXCEL FILE"
)

file = st.file_uploader("Choose a CSV or Excel file", type=["csv","xlsx"], accept_multiple_files=False)
# excel_file = st.file_uploader('Choose Excel File',type=,accept_multiple_files=False)
try:   
    
    if file :
        
        if re.search(r'.csv',str(file)):
            df = pd.read_csv(file)
        if re.search(r'.xlsx',str(file)):
            df = pd.read_excel(file)

        Explore_data, Univariate_data_aalysis = st.tabs(["Explore Data", "univariate_data_analysis"])
        

        with Explore_data:
            st.header("Explore Data")
        # dataset_info_button = st.button("Basic Dataset information",type="primary")
        
            if "button2_clicked" not in st.session_state:
                st.session_state["button2_clicked"] = False
            if st.button("Explore Data",type="primary"):
                st.session_state["button2_clicked"] = not st.session_state["button2_clicked"]
            if st.session_state["button2_clicked"]:
                st.write("**The process of analyzing and understanding data**")
                ob.dataset_info(df)
                st.header(" ", divider="rainbow")

        with Univariate_data_aalysis:

            st.header("Univariate Data analysis")
            if "button_univariate" not in st.session_state:
                st.session_state["button_univariate"] = False
            if st.button("Univariate Data analysis",type="primary"):
                st.session_state["button_univariate"] = not st.session_state["button_univariate"]
            if st.session_state["button_univariate"]:
                st.write("**Univariate data analysis in the context of machine learning refers to the analysis of a single variable or feature in a dataset. It involves examining and summarizing the characteristics of a single variable without considering relationships with other variables**")
                ob.univariate_data_analysis(df)
            st.header(" ", divider="rainbow")
    st.title("By Prajyot Birajdar")
except UnicodeDecodeError as e:
    st.warning("Add valid csv/excel file")

