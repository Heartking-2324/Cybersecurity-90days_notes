# Data Visualization Dashboard

This project demonstrates how to create an interactive data visualization dashboard using Python and Dash. The dashboard allows users to filter data through a dropdown menu and visualize the results in a bar chart.

## Installation

To get started, you'll need to install the Dash library. You can do this using pip:

```bash
pip install dash
```

## Usage

1. **Import the necessary libraries in your Python script:**

```python
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
```

2. **Load your dataset:**

Ensure you have a CSV file named `your_dataset.csv` in the same directory as your script:

```python
data = pd.read_csv('your_dataset.csv')
```

3. **Create a Dash app instance:**

```python
app = dash.Dash(__name__)
```

4. **Define the layout of your dashboard:**

This layout includes a title, a dropdown menu for selecting categories, and a graph for displaying the bar chart:

```python
app.layout = html.Div([
    html.H1('Data Visualization Dashboard'),
    dcc.Dropdown(
        id='category-dropdown',
        options=[{'label': i, 'value': i} for i in data['category'].unique()],
        value=data['category'].unique()[0]
    ),
    dcc.Graph(id='price-graph')
])
```

5. **Define the callback function for updating the dashboard based on user interactions:**

The callback function updates the graph whenever a new category is selected from the dropdown menu:

```python
@app.callback(
    Output('price-graph', 'figure'),
    [Input('category-dropdown', 'value')]
)
def update_graph(selected_category):
    filtered_data = data[data['category'] == selected_category]
    fig = px.bar(filtered_data, x='product', y='price')
    return fig
```

6. **Run the Dash app:**

Start the Dash server to view the dashboard in your web browser:

```python
if __name__ == '__main__':
    app.run_server(debug=True)
```

## Example

Here's a complete example of a simple Dash app that visualizes data from a CSV file:

```python
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load the dataset
data = pd.read_csv('books_scraped_data.csv')  # Ensure the correct path to your dataset

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1('Data Visualization Dashboard'),
    dcc.Dropdown(
        id='category-dropdown',
        options=[{'label': i, 'value': i} for i in data['category'].unique()],
        value=data['category'].unique()[0]
    ),
    dcc.Graph(id='price-graph')
])

# Define the callback function
@app.callback(
    Output('price-graph', 'figure'),
    [Input('category-dropdown', 'value')]
)
def update_graph(selected_category):
    filtered_data = data[data['category'] == selected_category]
    fig = px.bar(filtered_data, x='product', y='price')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
```
To get data for the .csv then we should you could try the script in this day's file.
## Deployment

I will give the .csv file directly you can try it out by yourself!. I will also give the script to create a automated into the .csv file it is  DUMMY DATA. 

---

### Happy Coding!
