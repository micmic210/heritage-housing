import plotly.express as px
import numpy as np
import streamlit as st
from src.data_management import load_house_prices_data
import matplotlib.pyplot as plt
import seaborn as sns
import ppscore as pps

sns.set_style("whitegrid")


def page_sale_price_analysis_body():
    # Load dataset
    df = load_house_prices_data()

    # Variables selected from correlation analysis (Pearson & Spearman Top 10)
    vars_to_study = [
        "1stFlrSF",
        "BsmtFinSF1",
        "GarageArea",
        "GarageYrBlt",
        "GrLivArea",
        "LotArea",
        "MasVnrArea",
        "OpenPorchSF",
        "OverallQual",
        "TotalBsmtSF",
        "YearBuilt",
        "YearRemodAdd",
    ]

    st.write("### Sale Price Correlation Analysis")

    st.success(
        f"* One of the key goals is to explore how specific home features \n"
        f"  are associated with their final sale prices. This section aims \n"
        f"  to uncover such relationships using visual and statistical tools."
    )

    # Data inspection option
    if st.checkbox("Show Data Sample"):
        st.write(
            f"* Dataset includes {df.shape[0]} rows and {df.shape[1]} columns.\n"
            f"  Here's a preview of the first 10 entries:"
        )
        st.write(df.head(10))

    st.write("---")

    # Correlation overview
    st.write("### Correlation Overview")
    st.write(
        f"Based on both Pearson and Spearman correlations, the following \n"
        f"variables showed the strongest relationship with `SalePrice`:\n"
        f"**{vars_to_study}**"
    )

    # Pearson Correlation
    st.info(
        f"**Pearson Correlation: Heatmap & Bar Chart**\n\n"
        f"Pearson correlation measures the strength of linear associations \n"
        f"between numerical variables. The heatmap displays variables with \n"
        f"a correlation greater than 0.6. A bar chart follows with the top 5."
    )
    if st.checkbox("Show Pearson Correlation Plots"):
        calc_display_pearson_corr_heat(df)
        calc_display_pearson_corr_bar(df)

    # Spearman Correlation
    st.info(
        f"**Spearman Correlation: Heatmap & Bar Chart**\n\n"
        f"Spearman correlation evaluates monotonic relationships between \n"
        f"features. Like the Pearson method, only the strongest correlations \n"
        f"with SalePrice are shown."
    )
    if st.checkbox("Show Spearman Correlation Plots"):
        calc_display_spearman_corr_heat(df)
        calc_display_spearman_corr_bar(df)

    # Scatterplots & Histograms
    st.info(
        f"**Scatter & Histogram Plots for Top Features**\n\n"
        f"The visualizations below depict the distribution and trend of each \n"
        f"selected variable in relation to the sale price."
    )
    if st.checkbox("Show Scatter and Histogram Plots"):
        correlation_to_sale_price_hist_scat(df, vars_to_study)

    # PPS heatmap
    st.info(
        f"**Predictive Power Score (PPS)**\n\n"
        f"PPS evaluates both linear and non-linear predictive strength between \n"
        f"variables. A darker color indicates higher predictive power (scale 0-1)."
    )
    if st.checkbox("Show PPS Heatmap"):
        calc_display_pps_matrix(df)


def correlation_to_sale_price_hist_scat(df, vars_to_study):
    target_var = "SalePrice"
    for col in vars_to_study:
        fig, axes = plt.subplots(figsize=(8, 5))
        axes = sns.histplot(data=df, x=col, y=target_var)
        plt.title(f"{col}", fontsize=20, y=1.05)
        st.pyplot(fig)
        st.write("\n\n")

        fig, axes = plt.subplots(figsize=(8, 5))
        axes = sns.scatterplot(data=df, x=col, y=target_var, hue="OverallQual")
        plt.title(f"{col}", fontsize=20, y=1.05)
        st.pyplot(fig)
        st.write("\n\n")


def calc_display_pearson_corr_heat(df):
    df_corr_pearson = df.corr(method="pearson")
    heatmap_corr(df=df_corr_pearson, threshold=0.6, figsize=(12, 10), font_annot=10)


def calc_display_spearman_corr_heat(df):
    df_corr_spearman = df.corr(method="spearman")
    heatmap_corr(df=df_corr_spearman, threshold=0.6, figsize=(12, 10), font_annot=10)


def calc_display_pearson_corr_bar(df):
    corr_pearson = df.corr(method="pearson")["SalePrice"].sort_values(
        key=abs, ascending=False
    )[1:]
    fig, axes = plt.subplots(figsize=(6, 3))
    axes = plt.bar(x=corr_pearson[:5].index, height=corr_pearson[:5])
    plt.title("Top Pearson Correlations", fontsize=15, y=1.05)
    st.pyplot(fig)


def calc_display_spearman_corr_bar(df):
    corr_spearman = df.corr(method="spearman")["SalePrice"].sort_values(
        key=abs, ascending=False
    )[1:]
    fig, axes = plt.subplots(figsize=(6, 3))
    axes = plt.bar(x=corr_spearman[:5].index, height=corr_spearman[:5])
    plt.title("Top Spearman Correlations", fontsize=15, y=1.05)
    st.pyplot(fig)


def calc_display_pps_matrix(df):
    pps_matrix_raw = pps.matrix(df)
    pps_matrix = pps_matrix_raw.filter(["x", "y", "ppscore"]).pivot(
        columns="x", index="y", values="ppscore"
    )
    heatmap_pps(df=pps_matrix, threshold=0.15, figsize=(12, 10), font_annot=10)


def heatmap_corr(df, threshold, figsize=(20, 12), font_annot=8):
    if len(df.columns) > 1:
        mask = np.zeros_like(df, dtype=bool)
        mask[np.triu_indices_from(mask)] = True
        mask[abs(df) < threshold] = True
        fig, axes = plt.subplots(figsize=figsize)
        axes = sns.heatmap(
            df,
            annot=True,
            xticklabels=True,
            yticklabels=True,
            mask=mask,
            cmap="viridis",
            annot_kws={"size": font_annot},
            ax=axes,
            linewidth=0.5,
        )
        axes.set_yticklabels(df.columns, rotation=0)
        plt.ylim(len(df.columns), 0)
        st.pyplot(fig)


def heatmap_pps(df, threshold, figsize=(20, 12), font_annot=8):
    if len(df.columns) > 1:
        mask = np.zeros_like(df, dtype=bool)
        mask[abs(df) < threshold] = True
        fig, axes = plt.subplots(figsize=figsize)
        axes = sns.heatmap(
            df,
            annot=True,
            xticklabels=True,
            yticklabels=True,
            mask=mask,
            cmap="rocket_r",
            annot_kws={"size": font_annot},
            linewidth=0.05,
            linecolor="grey",
        )
        plt.ylim(len(df.columns), 0)
        st.pyplot(fig)
