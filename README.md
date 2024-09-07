# Data Analysis of Oktobit Store Products Using PostgreSQL and SQL

## Project Overview
This project focuses on analyzing the scraped laptop product data from the Oktobit store. After collecting the data through web scraping, the data was cleaned, stored in a PostgreSQL database, and analyzed using SQL queries. Additionally, interactive visualizations were created using Plotly and Dash.

## Project Structure
```bash
|-- data_analysis/
    |-- sql/
        |-- oktobit database.sql        # SQL script to create PostgreSQL tables
        |-- oktobit databse.sql          # SQL queries for exploratory data analysis
    |-- notebooks/
        |-- daahboard.ipynb # Jupyter notebook for data visualization
        |-- app.py# Jupyter notebook for data visualization
      

    |-- dash_app/
        |-- app_dash.py                   # Dash app to visualize the data
