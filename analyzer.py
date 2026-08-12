import pandas as pd
import streamlit as st
import plotly as px

def show_size(df):     
    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.metric("Row:",len(df))
    with col2:
        st.metric("Columns:",len(df.columns))
    with col3:
        st.metric("Null Values", df.isnull().sum().sum())
    with col4:
        st.metric("Duplicates:",df.duplicated().sum())

def Dataset_Information(df):
    st.write("📋 Dataset Information ")
    info=pd.DataFrame(
        {
            "Columns":df.columns,
            "DataType":df.dtypes.astype(str),
            "Null Values":df.isnull().sum()
        }
    )
    st.dataframe(info,hide_index=True)
     

def fill_missing_values(df):
    st.subheader("🧹 Clean Dataset")
    #Replacing NAN values with mean/meadian(User choise)
    ch2 = st.selectbox(
        "Replace missing numeric values with:",
        ["Mean", "Median"]
        )
    but=st.button("Clean Missing Values")
    if but:
        for col in df.columns:
            if pd.api.types.is_numeric_dtype(df[col]):
                if ch2=="Mean":
                    df[col]=df[col].fillna(df[col].mean())
                elif ch2=="Median":
                    df[col]=df[col].fillna(df[col].median())
            else:
                #Replacing NAN text with Unknown
                df[col] = df[col].fillna("Unknown")
        st.success("Data Cleaned Sucessefuly")
    st.session_state["df"]=df

def col_type(df):
    nc=0
    tc=0
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            nc+=1
        else:
            tc+=1
    print(f"\nNumeric column : {nc}")
    print(f"Categorical column : {tc}\n")

def save_file(df):
    st.subheader("💾 Export")
    filename = st.text_input(
        label="Filename:",
        value="cleaned_data.df"
    )
    if not filename.endswith(".df"):
        filename += ".df"
    df_data=df.to_csv(index=False)
    st.download_button(
        label="⬇️ Download Cleaned df",
        data=df_data,
        file_name=filename,
        mime="text/df"
    )
    

def preview_data(df):
    st.subheader("👀 Preview Dataset")
    st.dataframe(df.head(8),use_container_width=True)

def key_ststs(df):
    col1,col2,col3=st.columns(3)
    with col1:
        st.write("total Sales")
