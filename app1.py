import streamlit as st
import pandas as pd
import pydeck as pdk

data = pd.read_excel("C:\\資料探勘\\website_create\\房價113(1).xlsx")
data = data.dropna()
st.set_page_config(layout="wide")
st.title("不動產交易房屋資訊")

min,max = st.slider("每坪單價(萬)",int(round(min(data['單價(萬/坪)']))),int(round(max(data['單價(萬/坪)']))),(25,50))
house_type = st.selectbox("房屋型態",("公寓(5樓含以下無電梯)","住宅大樓(11層含以上有電梯)","華廈(10層含以下有電梯)","透天厝",None))


filter_data = data[(data["單價(萬/坪)"]>=min) & (data["單價(萬/坪)"]<=max) & (data['建物型態'] == house_type)]


event=st.pydeck_chart(
   
    pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=25,
            longitude=121.4,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                "ScatterplotLayer",
                data=filter_data,
                id="單價(萬/坪)",
                get_position="[Longitude, Latitude]",
                get_color="[255, 75, 75]",
                get_radius=200,
            ),

        ],
    )
)

event.selection