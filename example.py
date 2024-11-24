# 1) build the map 

# 2) make filter slider for the map 

# 3) make popular selling in this slider





import streamlit as st
import pandas as pd
import pydeck as pdk

# Sample data
data = pd.DataFrame({
    "lat": [37.76, 37.77, 37.78],
    "lon": [-122.4, -122.41, -122.42],
    "name": ["Point A", "Point B", "Point C"]
})

# Create scatter layer
scatter_layer = pdk.Layer(
    "ScatterplotLayer",
    data=data,
    get_position=["lon", "lat"],
    get_color=[200, 30, 0, 160],
    get_radius=1000,
)

# Create text layer
text_layer = pdk.Layer(
    "TextLayer",
    data=data,
    get_position=["lon", "lat"],
    get_text="name",
    get_color=[0, 0, 0, 200],
    get_size=15,
    get_alignment_baseline="'bottom'"
)

# Create view state
view_state = pdk.ViewState(
    latitude=data["lat"].mean(),
    longitude=data["lon"].mean(),
    zoom=12
)

# Create deck
deck = pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state=view_state,
    layers=[scatter_layer, text_layer]
)

# Display the map in Streamlit
st.pydeck_chart(deck)