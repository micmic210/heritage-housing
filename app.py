import streamlit as st
from app_pages.multipage import Multipage

# Load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_sale_price_analysis import page_sale_price_analysis_body
from app_pages.page_sale_price_predictor import page_sale_price_predictor_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_predict_price_ml import page_predict_price_ml_body

# Create an intance of the app
app = Multipage(app_name="Heritage Valuater")

# Add app pages
app.add_page("Project Summary & Objectives", page_summary_body)
app.add_page("Sales Price Correlation Study", page_sale_price_analysis_body)
app.add_page("House Sales Price Predictor", page_sale_price_predictor_body)
app.add_page("Project Hypotheses and Validation", page_project_hypothesis_body)
app.add_page("ML Pipeline & Model Evaluation", page_predict_price_ml_body)

# Run the app
app.run()
