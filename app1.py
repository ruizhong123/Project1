import streamlit as st
import pandas as pd
import pydeck as pdk

import mysql.connector as con 
import pandas as pd

columns = ['鄉鎮市區', '交易標的', '土地位置建物門牌', 'Latitude', 'Longitude', '都市土地使用分區', '交易年月日', '交易筆棟數', '移轉層次', '總樓層數', '建物型態', '主要用途', '主要建材', '建物現況格局.房', '建物現況格局.廳', '建物現況格局.衛', '建物現況格局.隔間', '有無管理組織', '車位類別', '電梯', 'm', 'n', '單價(萬/坪)', '土地移轉總面積(坪).1', '建物移轉總面積(坪)', '車位移轉總面積(坪)', '車位總價元(萬)', '總價元(萬)', '主建物面積(坪)', '附屬建物面積(坪)', '陽台面積(坪)', '屋齡', '是否為預購屋', '是否夠買一層以上的房子', '購買是否有買夾層屋', '公設面積包含電梯或樓梯', '公設面積包含屋頂突出物', '附屬面積含平台', '附屬面積含露台', '購買時是否有騎樓', '是否有購地下樓層', '最低地上樓層', '主建物占比', '陽台面積占比', '附屬面積占比', '公佔比', '是否有記附屬面積', '備註']

conn = con.connect(host = '127.0.0.1',port =  3306,password = '123456',user = 'root',database = 'house')
cur = conn.cursor()

cur.execute("""select*from house""")
data = cur.fetchall()

data = pd.DataFrame(data,columns=columns)


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
