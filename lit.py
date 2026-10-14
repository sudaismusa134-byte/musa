import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("chocolate_sales (2).csv")

st.title("Sample Dashboard")

st.markdown("### this a practice dashboard we are building with streamlit")

#for kpi@
kpi1, kpi2, kpi3 = st.columns(3)

with kpi1:
    st.metric(label="total boxes shipped", value=df["Boxes Shipped"].sum())

with kpi2:
    st.metric(label="total revenue generated",value=df["Amount"].sum())

with kpi3:
    st.metric(label="most purchased product", value=df["Product"].mode()[0])


#for charts#

chart1, chart2 = st.columns(2)

with chart2:
    product_revenue = df.groupby("Product")["Amount"].sum()

    fig, ax = plt.subplots()
    product_revenue.plot(kind="line", color="black", ax=ax)
    plt.ylabel("Total Revenue")
    plt.title("Total Revenue Per Product")
    st.pyplot(fig=fig)


with chart1:
    product_revenue = df.groupby("Product")["Amount"].sum()

    fig, ax = plt.subplots()
    product_revenue.plot(kind="bar", color="green")
    plt.ylabel("Total Revenue")
    plt.title("Total Revenue Per Product")
    st.pyplot(fig=fig)

chart3, chart4 = st.columns(2)

with chart3:
    yearly_income = df.groupby("Product")["Amount"].sum()

    fig, ax = plt.subplots()
    yearly_income.plot(kind="line", color="red", ax=ax)
    plt.ylabel("Total revenue")
    plt.title("Total income yearly")
    st.pyplot(fig=fig)


with chart4:
    dayly_income= df.groupby("Product")["Amount"].sum()

    fig, ax = plt.subplots()
    dayly_income.plot(kind="bar", color="blue", ax=ax)
    plt.ylabel("Total revenue")
    plt.title("Total income dayly")
    st.pyplot(fig=fig)


st.write("Sample Dataframe")
st.dataframe(df.head(20))

