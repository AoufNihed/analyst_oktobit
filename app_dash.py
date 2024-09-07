import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sqlalchemy import create_engine

# Initialize connection to PostgreSQL
engine = create_engine('postgresql://postgres:aoufnihed@localhost/oktobit_database')

# Fetch the data from PostgreSQL
query = 'SELECT * FROM laptops LIMIT 50'  # Limit to 50 products
df = pd.read_sql(query, engine)

# Clean and process data
df['category'] = df['category'].str.replace(r'\s+', '', regex=True)  # Clean category
df['ram'] = df['ram'].str.replace(r'\s+', '', regex=True)  # Clean RAM

# Define color palette
colors = ['#1f2d6f', '#2f45a3', '#3e5ed7', '#5e48b7', '#321c60']

# -------------------- Histogram of Price Distribution --------------------
histogram = px.histogram(df, x="price", color_discrete_sequence=colors)

# -------------------- Bubble Chart: Price vs Weight --------------------
df['RAM_value'] = df['ram'].apply(lambda x: int(x.split('GO')[0]))  # Extract numeric RAM value
bubble_chart = px.scatter(df, x="price", y="poids", size="RAM_value", color="category", 
                          color_discrete_sequence=colors)

# -------------------- Bar Charts --------------------
bar_chart_1 = px.bar(df, x="category", y="price", color_discrete_sequence=colors)
bar_chart_2 = px.bar(df, x="ram", y="price", color_discrete_sequence=colors)

# -------------------- Pie Chart for Category, RAM, Batterie, OS --------------------
category_counts = df['category'].value_counts()
ram_counts = df['ram'].value_counts()
batterie_counts = df['batterie'].value_counts()
os_counts = df['os'].value_counts()

def create_pie_charts():
    fig = make_subplots(rows=2, cols=2, specs=[[{'type': 'domain'}, {'type': 'domain'}],
                                               [{'type': 'domain'}, {'type': 'domain'}]],
                        horizontal_spacing=0.05, vertical_spacing=0.05)

    # Add pie charts
    fig.add_trace(go.Pie(labels=category_counts.index, values=category_counts.values, hole=.5,
                         marker=dict(colors=colors), name='Category'), row=1, col=1)

    fig.add_trace(go.Pie(labels=ram_counts.index, values=ram_counts.values, hole=.5,
                         marker=dict(colors=colors), name='RAM'), row=1, col=2)

    fig.add_trace(go.Pie(labels=batterie_counts.index, values=batterie_counts.values, hole=.5,
                         marker=dict(colors=colors), name='Batterie'), row=2, col=1)

    fig.add_trace(go.Pie(labels=os_counts.index, values=os_counts.values, hole=.5,
                         marker=dict(colors=colors), name='OS'), row=2, col=2)

    fig.update_layout(showlegend=False, height=700)
    
    return fig

# Create the Dash app layout
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    
    # Dashboard Title and Description
    html.H1("📈 Reports of Oktobit Store", style={'text-align': 'center', 'color': '#2f45a3'}),
    html.P("Oktobit is an e-commerce store leading the Algerian market in laptop sales. "
           "This report is based on a sample of 50 products from a total of 245 scraped products.", 
           style={'text-align': 'center', 'font-style': 'italic', 'margin': '20px 0'}),
    
    # Histogram of Price Distribution
    html.Div(children=[
        html.H3("📊 Histogram of Price Distribution", style={'color': '#2f45a3'}),
        dcc.Graph(figure=histogram),
        html.P("This histogram shows the distribution of prices among the sampled laptops. "
               "It helps identify the most common price ranges and potential outliers in the dataset.",
               style={'font-style': 'italic', 'color': '#5e48b7'})
    ], style={'border': '2px solid #2f45a3', 'padding': '15px', 'margin': '20px 0'}),
    
    # Bubble Chart: Price vs Weight
    html.Div(children=[
        html.H3("💻 Price vs Weight (Bubble Size by RAM)", style={'color': '#2f45a3'}),
        dcc.Graph(figure=bubble_chart),
        html.P("This scatter plot shows the relationship between the price and weight of the laptops. "
               "Each bubble's size is determined by the RAM, giving insights into how hardware specifications affect pricing.",
               style={'font-style': 'italic', 'color': '#5e48b7'})
    ], style={'border': '2px solid #2f45a3', 'padding': '15px', 'margin': '20px 0'}),

    # Bar Charts
    html.Div(children=[
        html.H3("🛒 Price by Category", style={'color': '#2f45a3'}),
        dcc.Graph(figure=bar_chart_1),
        html.P("This bar chart shows the average price of laptops across different categories, providing insights into which categories have higher or lower average prices.",
               style={'font-style': 'italic', 'color': '#5e48b7'})
    ], style={'border': '2px solid #2f45a3', 'padding': '15px', 'margin': '20px 0'}),
    
    html.Div(children=[
        html.H3("💾 Price by RAM", style={'color': '#2f45a3'}),
        dcc.Graph(figure=bar_chart_2),
        html.P("This bar chart demonstrates how price correlates with the amount of RAM in laptops, giving an idea of whether RAM size significantly impacts pricing.",
               style={'font-style': 'italic', 'color': '#5e48b7'})
    ], style={'border': '2px solid #2f45a3', 'padding': '15px', 'margin': '20px 0'}),

    # Pie Charts for Category, RAM, Batterie, OS
    html.Div(children=[
        html.H3("📊 Device Analysis: Categories, RAM, Batterie, and OS", style={'color': '#2f45a3'}),
        dcc.Graph(figure=create_pie_charts()),
        html.P("These pie charts break down the distribution of different laptop categories, RAM sizes, battery types, and operating systems within the sample.",
               style={'font-style': 'italic', 'color': '#5e48b7'})
    ], style={'border': '2px solid #2f45a3', 'padding': '15px', 'margin': '20px 0'}),
    
    # Footer
    html.Footer("Made with ❤️ by Aouf Nihed", style={'text-align': 'center', 'color': '#2f45a3', 'padding': '10px'})
])

# Run the dashboard
if __name__ == '__main__':
    app.run_server(debug=True)
