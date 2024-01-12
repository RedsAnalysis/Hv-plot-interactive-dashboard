#!/usr/bin/env python
# coding: utf-8

# In[167]:


import pandas as pd
import numpy as np
import panel as pn
import hvplot.pandas
pn.extension('tabulator')


# In[168]:


# Loading the data frame
df =pd.read_csv("annual-co2-emissions-per-country.csv")
df


# In[169]:


# EDA
df[df['Entity'] == 'North America']


# In[170]:


df[df['Entity'] == 'World'] 


# In[171]:


df[df['Entity'] == 'Asia'] 


# In[172]:


# Extracting unique continents from the 'Entity' column
continents = ['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America', 'World']

def create_dashboard():
    # Check buttons for selecting continents
    continent_selector = pn.widgets.CheckButtonGroup(options=continents, value=[continents[0]])

    # Year slider
    year_slider = pn.widgets.IntSlider(name='Select Year', start=1750, end=2020, step=5, value=1850)

    # Function to update the plot based on user selection
    def update_plot(selected_continents, year):
        plot_data = df[df['Entity'].isin(selected_continents) & (df['Year'] <= year)]
        plot = plot_data.hvplot.line(x='Year', y='Annual CO₂ emissions', by='Entity', xlabel='Year',
                                     ylabel='Annual CO2 Emission', title='Annual CO2 Emission Comparison',
                                     legend='top_left', width=800, height=400)
        return plot

    # Dynamic plot based on user interaction
    dashboard = pn.interact(update_plot, selected_continents=continent_selector, year=year_slider)

    return pn.Column("# Annual CO2 Emission Comparison", dashboard)

# Show the dashboard
create_dashboard().servable()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




