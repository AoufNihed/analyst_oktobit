import pandas as pd
import numpy as np
from sqlalchemy import create_engine
# Initialize connection to PostgreSQL
engine = create_engine('postgresql://postgres:aoufnihed@localhost/oktobit_database')
query = 'SELECT * FROM laptops'
df = pd.read_sql(query, engine)
###############################################################################################################################################################################

#make 4 image in same layouts !!
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

# Filter data for category
df['category'] = df['category'].str.replace(r'\s+', '', regex=True)  # Remove extra spaces
df_filtered = df[df['category'] != 'Asus']
category_counts = df_filtered['category'].value_counts()

# RAM data
df['ram'] = df['ram'].str.replace(r'\s+', '', regex=True)  # Remove extra spaces
ram_counts = df['ram'].value_counts()

# Batterie data
batterie_counts = df['batterie'].value_counts()

# OS data
data = {'os': ['Windows11Original.', 'Windows10Original.', 'Windows11Original', 'Windows11Original.']}
df_os = pd.DataFrame(data)
df_os['os'] = df_os['os'].str.replace(r'\.$', '', regex=True)  # Normalize 'os' values
os_counts = df_os['os'].value_counts()

# Define the color palette
colors = ['#1f2d6f', '#2f45a3', '#3e5ed7', '#5e48b7', '#321c60']

# Create subplots: 2 rows and 2 columns, reduce space with 'horizontal_spacing' and 'vertical_spacing'
fig = make_subplots(rows=2, cols=2, specs=[[{'type': 'domain'}, {'type': 'domain'}],
                                        [{'type': 'domain'}, {'type': 'domain'}]],
                    horizontal_spacing=0.05, vertical_spacing=0.05)

# Add pie charts to the subplots
fig.add_trace(go.Pie(labels=category_counts.index, values=category_counts.values, hole=.5,
                        marker=dict(colors=colors), name='Category'), row=1, col=1)

fig.add_trace(go.Pie(labels=ram_counts.index, values=ram_counts.values, hole=.5,
                    marker=dict(colors=colors), name='RAM'), row=1, col=2)

fig.add_trace(go.Pie(labels=batterie_counts.index, values=batterie_counts.values, hole=.5,
                    marker=dict(colors=colors), name='Batterie'), row=2, col=1)

fig.add_trace(go.Pie(labels=os_counts.index, values=os_counts.values, hole=.5,
                    marker=dict(colors=colors), name='OS'), row=2, col=2)

# Update layout: Set empty text in the center and reduce space between charts
fig.update_layout(
    title_text="📊 Device Analysis: Categories, RAM, Batterie, and OS",
    annotations=[
        dict(text='', x=0.5, y=0.5, font_size=12, font=dict(weight='bold'), showarrow=False) , # Bold text for Category
        dict(text='', x=0.82, y=0.82, font_size=12, font=dict(weight='bold'), showarrow=False),  # Bold text for RAM
        dict(text='',  x=0.18, y=0.18, font_size=12, font=dict(weight='bold'), showarrow=False),  # Bold text for Batterie
        dict(text='', x=0.82, y=0.18, font_size=12, font=dict(weight='bold'), showarrow=False)  # Bold text for OS
    ],
    
    showlegend=False
)
# Show the figure
fig.show()
##################################################################################################################################################################################

# Create the plots

histogram = px.histogram(df, x="price", title="Price Distribution of Laptops", color_discrete_sequence=colors)

df['RAM_value'] = df['RAM'].apply(lambda x: int(x.split()[0]))  # Convert '8 GO' -> 8
bubble_chart = px.scatter(df, x="price", y="Poids", size="RAM_value", color="category", 
                            title="Price vs Weight (Bubble Size by RAM)", color_discrete_sequence=colors)

bar_chart_1 = px.bar(df, x="category", y="price", title="Price by Category", color_discrete_sequence=colors)
bar_chart_2 = px.bar(df, x="RAM", y="price", title="Price by RAM", color_discrete_sequence=colors)
