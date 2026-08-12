import pandas as pd
import streamlit as st
import analyzer as an
import charts as vi

def upload():
    file=st.file_uploader(
        "Upload CSV",
        type="csv"
    )

    if file is not None :

        df=pd.read_csv(file)
        st.success("CSV uploaded successfully!")

        row,col=st.columns(2)
        with row:
            st.metric("Rows",len(df))
        with col:
            st.metric("Columns",len(df.columns))

        st.subheader("Dataset Preview")
        st.dataframe(df.head())
        st.session_state["df"]=df

def main():
    if "df" not in st.session_state:
        st.session_state["df"] = None
    st.sidebar.title("Options")
    page=st.sidebar.radio(
        "Navigation",
        [
            "Upload CSV",
            "Analyze & Clean CSV",
            "Visualize CSV",
            "CSV Dashboard"
        ]
    )

    if page == "Upload CSV":
        st.title("Upload CSV")
        upload()

    elif page == "Analyze & Clean CSV":

        st.title("Analyze & Clean CSV")

        if "df" in st.session_state:
            df=st.session_state["df"]
            an.show_size(df)
            an.Dataset_Information(df)
            an.fill_missing_values(df)
            an.preview_data(df)
            an.save_file(df)

        else:
            st.warning("Upload a csv file first")

    elif page == "Visualize CSV":

        st.title("Visualize CSV")

        if "df" in st.session_state:
            df=st.session_state["df"]
            ch=st.selectbox(
                "Choose Chart",
                [
                    "Bar Chart",
                    "Line Chart",
                    "Pie Chart",
                    "Histogram",
                    "Scatter Plot",
                    "Box Plot",
                    "Area Chart"
                ]
            )

            if ch=="Bar Chart":
                vi.bar(df)
            elif ch=="Line Chart":
                vi.line(df)
            elif ch=="Pie Chart":
                vi.pie(df)
            elif ch=="Histogram":
                vi.hist(df)
            elif ch=="Scatter Plot":
                vi.scatter(df)
            elif ch=="Box Plot":
                vi.box(df)
            elif ch=="Area Chart":
                vi.area(df)
            
        else:
            st.warning("First Upload the CSV")

    elif page=="CSV Dashboard":
        st.title("CSV Dashboard")
        if "df" in st.session_state:
            df=st.session_state["df"]
            # an.key_stats(df)
            an.show_size(df)
            vi.Data_Visualizations(df)
            an.preview_data(df)
        else:
            st.warning("First Upload the CSV")
    
main()