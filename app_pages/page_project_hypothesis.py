import streamlit as st


def page_project_hypothesis_body():
    st.write("### Project Hypotheses and Validation")

    st.info(
        f"**Hypothesis 1**\n\n"
        f"Homes with larger overall living areas (`GrLivArea`), higher material "
        f"quality (`OverallQual`), and newer construction years (`YearBuilt`) "
        f"tend to have higher sale prices.\n\n"
        f" This hypothesis is supported by strong positive correlations found "
        f"in the data. Visualizations such as scatterplots and heatmaps confirm "
        f"the influence of these features on sale price."
    )

    st.info(
        f"**Hypothesis 2**\n\n"
        f"Features like garage size (`GarageArea`), kitchen quality "
        f"(`KitchenQual`), and the presence of finished basement areas "
        f"(e.g., `BsmtFinSF1`, `BsmtExposure`) significantly contribute to "
        f"a property's value.\n\n"
        f" This is supported by moderate to strong correlations, and these "
        f"features are also present among the top predictors in the machine "
        f"learning model."
    )

    st.info(
        f"**Validation Strategy**\n\n"
        f"* Used correlation analysis and visualizations to examine relationships "
        f"between each key feature and `SalePrice`.\n"
        f"* Applied Pearson and Spearman tests to validate numerical correlations.\n"
        f"* Compared distributions of `SalePrice` across categories such as "
        f"`BsmtExposure` using boxplots (instead of full statistical ANOVA).\n"
        f"* Built regression models to quantify feature importance and predict "
        f"property prices.\n"
        f"* Tested the model using Lydia's four inherited houses to ensure the "
        f"model works in real-life scenarios."
    )
