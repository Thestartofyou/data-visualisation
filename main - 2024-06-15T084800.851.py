import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Sample Data
data = {
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Value': [10, 20, 15, 25, 30],
    'Change': [5, -2, 3, 8, -1]
}

df = pd.DataFrame(data)

# Matplotlib and Seaborn Visualization
def static_visualization(df):
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Category', y='Value', data=df, palette='viridis')
    plt.title('Category vs Value')
    plt.xlabel('Category')
    plt.ylabel('Value')
    plt.show()

# Plotly Interactive Visualization
def interactive_visualization(df):
    fig = px.bar(df, x='Category', y='Value', title='Category vs Value',
                 hover_data=['Change'], labels={'Value':'Value in Units'},
                 template='plotly_dark')
    fig.update_traces(marker_color='turquoise', marker_line_width=1.5)
    fig.show()

# Call Visualization Functions
static_visualization(df)
interactive_visualization(df)

