import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


def page_summary_body():
    st.write("### Project Summary & Objectives")

    st.info(
        f"**Introduction**\n\n"
        f"Lydia Doe has recently inherited four properties located in Ames, "
        f"Iowa, USA, from her late great-grandfather. While she is well-versed "
        f"in the real estate market of her home country, Belgium, she is "
        f"concerned that her understanding may not apply to the housing market "
        f"in Iowa. Factors that increase a property's value in Belgium may not "
        f"hold the same influence in Ames.\n\n"
        f"In order to make informed decisions and ensure the best possible "
        f"return on the properties, Lydia seeks help from a Data Practitioner. "
        f"Her primary goal is to accurately estimate the value of these homes "
        f"and avoid financial loss due to mispricing.\n\n"
        f"**Dataset Content**\n\n"
        f"* The dataset is sourced from "
        f"[Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data). "
        f"A fictitious user story has been created to demonstrate how "
        f"predictive analytics can be applied in a real-world project.\n"
        f"* The dataset contains almost 1,500 rows and represents housing "
        f"records from Ames, Iowa, detailing house profiles such as Floor "
        f"Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built, "
        f"along with the respective sale prices for houses built between 1872 "
        f"and 2010."
    )

    st.success(
        f"**Business Requirements**\n\n"
        f"Lydia's objectives for this data-driven project are twofold:\n\n"
        f"* Business Requirement 1 - She wants to understand which housing "
        f"attributes most strongly influence sale prices in Ames. To achieve "
        f"this, she expects clear visualizations that show the correlation "
        f"between house features and their final selling price.\n\n"
        f"* Business Requirement 2 - She needs to predict the expected sale "
        f"price for her four inherited houses based on their characteristics. "
        f"Additionally, she wishes to use this tool to estimate the price of any "
        f"other property in Ames she might consider buying in the future."
    )

    # Link to README file, allowing users to explore the full project
    # documentation
    
    st.write(
        f"* To learn more about this project, please visit the "
        f"[README file](https://github.com/micmic210/heritage-housing.git) "
        f"available on GitHub.\n"
        f"* This project was developed by Michiko Inoue."
    )
