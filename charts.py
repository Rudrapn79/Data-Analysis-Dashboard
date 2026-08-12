import plotly.express as px
import streamlit as st

def save_image(fig):
    img=fig.to_image(format="png")
    f_name = st.text_input(
        "Enter file name",
        value="chart.png"
    )

    if not f_name.endswith(".png"):
        f_name += ".png"

    st.download_button(
        "⬇️ Download Plot",
        data=img,
        file_name=f_name,
        mime="image/png"
    )

def bar(csv):

    col1, col2, col3 = st.columns(3)
    with col1:
        cx = st.selectbox(
            "X column",
            csv.columns
        )
    with col2:
        cy = st.selectbox(
            "Y column",
            csv.columns
        )
    with col3:
        cc=st.selectbox(
            "Column colour",
            csv.columns
        )
    col1, col2, col3 = st.columns([2, 1, 2])
    # tit=st.text_input(label="Enter Title",value="Sales Analysis")
    with col2:
        ch=st.button("Generate Chart")

    if ch:
        st.success("Chart Generated")
        fig=px.bar(
        csv,
        x=cx,
        y=cy,
        title="Sales Analysis",
        template="plotly_dark",
        color=cc
        )

        st.plotly_chart(fig, use_container_width=True)

        save_image(fig)


def line(csv):

    col1, col2 = st.columns(2)
    with col1:
        cx = st.selectbox(
            "X column",
            csv.columns
        )
    with col2:
        cy = st.selectbox(
            "Y column",
            csv.columns
        )

    col1, col2, col3 = st.columns([2, 1, 2])
    # tit=st.text_input(label="Enter Title",value="Sales Analysis")
    with col2:
        ch=st.button("Generate Chart")

    if ch:
        st.success("Chart Generated")
        fig=px.line(
        csv,
        x=cx,
        y=cy,
        title="Sales Analysis",
        template="plotly_dark"
        )

        st.plotly_chart(fig, use_container_width=True)

        save_image(fig)

def pie(csv):

    col1, col2= st.columns(2)
    with col1:
        cx = st.selectbox(
            "Name",
            csv.columns
        )
    with col2:
        cy = st.selectbox(
            "Values",
            csv.columns
        )

    col1, col2, col3 = st.columns([2, 1, 2])
    # tit=st.text_input(label="Enter Title",value="Sales Analysis")
    with col2:
        ch=st.button("Generate Chart")

    if ch:
        st.success("Chart Generated")
        fig=px.pie(
        csv,
        names=cx,
        values=cy,
        title="Sales Analysis",
        template="plotly_dark"
        )

        st.plotly_chart(fig, use_container_width=True)

        save_image(fig)

def hist(csv):

    cx = st.selectbox(
        "X column",
        csv.columns
    )

    col1, col2, col3 = st.columns([2, 1, 2])
    # tit=st.text_input(label="Enter Title",value="Sales Analysis")
    with col2:
        ch=st.button("Generate Chart")

    if ch:
        st.success("Chart Generated")
        fig=px.histogram(
        csv,
        x=cx,
        nbins=20,
        title="Sales Analysis",
        template="plotly_dark"
        )

        st.plotly_chart(fig, use_container_width=True)

        save_image(fig)

def scatter(csv):

    col1, col2 = st.columns(2)
    with col1:
        cx = st.selectbox(
            "X column",
            csv.columns
        )
    with col2:
        cy = st.selectbox(
            "Y column",
            csv.columns
        )
    col1, col2, col3 = st.columns([2, 1, 2])
    # tit=st.text_input(label="Enter Title",value="Sales Analysis")
    with col2:
        ch=st.button("Generate Chart")

    if ch:
        st.success("Chart Generated")
        fig=px.scatter(
        csv,
        x=cx,
        y=cy,
        title="Sales Analysis",
        template="plotly_dark"
        )

        st.plotly_chart(fig, use_container_width=True)

        save_image(fig)

def box(csv):

    c = st.selectbox(
        "Y column",
        csv.columns
    )
    col1, col2, col3 = st.columns([2, 1, 2])
    # tit=st.text_input(label="Enter Title",value="Sales Analysis")
    with col2:
        ch=st.button("Generate Chart")

    if ch:
        st.success("Chart Generated")
        fig=px.box(
        csv,
        x=c,
        title="Sales Analysis",
        template="plotly_dark"
        )

        st.plotly_chart(fig, use_container_width=True)

        save_image(fig)

def area(csv):

    col1, col2 = st.columns(2)
    with col1:
        cx = st.selectbox(
            "X column",
            csv.columns
        )
    with col2:
        cy = st.selectbox(
            "Y column",
            csv.columns
        )
    col1, col2, col3 = st.columns([2, 1, 2])
    # tit=st.text_input(label="Enter Title",value="Sales Analysis")
    with col2:
        ch=st.button("Generate Chart")

    if ch:
        st.success("Chart Generated")
        fig=px.area(
        csv,
        x=cx,
        y=cy,
        title="Sales Analysis",
        template="plotly_dark"
        )

        st.plotly_chart(fig, use_container_width=True)

        save_image(fig)

def Data_Visualizations(df):
    st.subheader(" Data Visualizations")
    # First row
    col1, col2 = st.columns(2)

    with col1:
        st.write("### 📊 Sales by Category")

        fig1 = px.bar(
            df,
            x="Category",
            y="Sales"
        )

        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.write("### 📈 Sales by Year")

        fig2 = px.line(
            df,
            x="Year",
            y="Sales",
            markers=True
        )

        st.plotly_chart(fig2, use_container_width=True)


    # Second row
    col3, col4 = st.columns(2)

    with col3:
        st.write("### 🥧 Category Distribution")

        category_sales = df.groupby("Category")["Sales"].sum().reset_index()

        fig3 = px.pie(
            category_sales,
            names="Category",
            values="Sales"
        )

        st.plotly_chart(fig3, use_container_width=True)

    with col4:
        st.write("### 🔥 Correlation")

        numeric_df = df.select_dtypes(include="number")

        fig4 = px.imshow(
            numeric_df.corr(),
            text_auto=True
        )

        st.plotly_chart(fig4, use_container_width=True)