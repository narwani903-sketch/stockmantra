import streamlit as st
import pandas as pd
import plotly.express as px
from data_fetcher import *
from ratio_calculator import *

st.set_page_config(layout="wide")

st.title("📊 Ultimate Stock Fundamental Analyzer")

# Sidebar
st.sidebar.header("🔍 Search Stock")
symbol = st.sidebar.text_input("Enter Symbol", "RELIANCE.NS")

if symbol:

    info = get_stock_info(symbol)
    price_data = get_price_data(symbol)
    financials = get_financials(symbol)
    ratios = calculate_ratios(info)
    holding = get_shareholding_pattern()

    # -------------------------
    # 🔥 BASIC INFO
    # -------------------------
    st.header(info.get("longName", symbol))

    col1, col2, col3 = st.columns(3)
    col1.metric("Price", info.get("currentPrice"))
    col2.metric("Market Cap", info.get("marketCap"))
    col3.metric("PE Ratio", info.get("trailingPE"))

    # -------------------------
    # 📈 CHART
    # -------------------------
    st.subheader("📈 Price Chart")
    fig = px.line(price_data, x=price_data.index, y="Close")
    st.plotly_chart(fig, use_container_width=True)

    # -------------------------
    # 📊 RATIOS
    # -------------------------
    st.subheader("📊 Key Ratios")
    st.table(pd.DataFrame(ratios.items(), columns=["Metric", "Value"]))

    # -------------------------
    # 🧾 FINANCIALS
    # -------------------------
    st.subheader("📄 Financial Statements")

    tab1, tab2, tab3 = st.tabs(["Income Statement", "Balance Sheet", "Cash Flow"])

    with tab1:
        st.dataframe(financials["income"])

    with tab2:
        st.dataframe(financials["balance"])

    with tab3:
        st.dataframe(financials["cashflow"])

    # -------------------------
    # 🏦 SHAREHOLDING
    # -------------------------
    st.subheader("🏦 Shareholding Pattern")

    fig2 = px.pie(holding, names="Category", values="Holding %")
    st.plotly_chart(fig2)

    # -------------------------
    # ⚖️ COMPARISON
    # -------------------------
    st.sidebar.subheader("Compare with")
    comp_symbol = st.sidebar.text_input("Second Stock", "TCS.NS")

    if comp_symbol:
        info2 = get_stock_info(comp_symbol)

        comp_df = pd.DataFrame({
            "Metric": ["Price", "PE", "ROE"],
            symbol: [
                info.get("currentPrice"),
                info.get("trailingPE"),
                info.get("returnOnEquity")
            ],
            comp_symbol: [
                info2.get("currentPrice"),
                info2.get("trailingPE"),
                info2.get("returnOnEquity")
            ]
        })

        st.subheader("⚔️ Comparison")
        st.table(comp_df)