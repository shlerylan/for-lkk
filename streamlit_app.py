import streamlit as st
import numpy as np
import pandas as pd
import pydeck as pdk

# def init_state(session_state):
    
#     if 'y' not in session_state:
#         session_state.y = 5
#     else:
#         print(session_state.y)
#         print('y is already in session state.1')


# FUNCTION FOR MAPS
def map(data, lat, lon, zoom):
    '''
    画扎点儿的地图
    '''
    st.write(
        pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v9",
            initial_view_state={
                "latitude": lat,
                "longitude": lon,
                "zoom": zoom,
                "pitch": 50,
            },
            layers=[
                pdk.Layer(
                    "HexagonLayer",
                    data=data,
                    get_position=["lon", "lat"],
                    radius=50,
                    elevation_scale=4,
                    elevation_range=[0, 500],
                    pickable=True,
                    extruded=True,
                ),
            ],
        )
    )



def run():
    '''
    主体部分
    '''
    #标题
    st.set_page_config(
        page_title="Happy birthday LKK!",
        page_icon=":heartbeat:",
        layout="wide",
    )    
    # 使用 markdown 添加一些样式和介绍文本
    st.markdown("""
        <style>
                
        /* 调整页面宽度 */
        .main {
            max-width: 100%;
            margin: 0 auto;
            padding: 1rem;
        }
                

        .title {
            text-align: center;
            font-size: 3em;
            color: black;
        }
        .button {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
        .birthday-wish {
            font-size: 1.5em;
            color: #ff69b4;
            text-align: center;
            margin-top: 20px;
        }
        </style>
        <div class="title">
            🎂 李可，生日快乐！🎂
        </div>
    """, unsafe_allow_html=True)

    map_data = pd.DataFrame({
        'City': ['萨克雷高原', '深圳'],
        'lat': [48.7321,  22.5985],
        'lon': [2.1661, 113.9986]
    })



    st.balloons()

    # init_state(st.session_state)
    # st.write("# 生日快乐，李可！:birthday:")

    #左部选择框
    cities = ['深圳','北京','萨克雷高原']
    st.sidebar.title("点击查看李可的足迹 ")
    la = st.sidebar.selectbox(" ",cities)

    if la == '深圳':

        #说明语
        st.markdown(
            """
            <h1 style='text-align: center; font-size: 25px;'>
                2024年，李可是在深圳的一名CS博士生，正在积极写paper中。
            </div>
            
        """, 
        unsafe_allow_html=True
        )

        # st.markdown("Here's a bouquet &mdash;\
        # :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

        #World Map，带有下拉框
        #st.map(map_data[map_data.City == la])
        # 添加一个按钮
        if st.button('-------------------------------------点击我，为李可的科研助力！----------------------------------'):
            # 如果按钮被点击，则显示图片
            st.image("./pic/keyanzhishen.png", caption='@copyright qrr', use_column_width=True)
            st.markdown("""
                    <div class="birthday-wish">
                        WOW！ 您已经得到了科研之神の助力！
                    </div>
                """, unsafe_allow_html=True)            

    if la == '萨克雷高原':
        
        #说明语
        st.markdown(
            """
            李可曾就读于巴黎南大，在萨克雷高原上度过了幸福的两年。2023年，网页制作者追随李可的脚步，也来到了萨克雷高原。
            
        """
        )      
      

        #标识
        col1, col2,col3 = st.columns(3)
        col1.metric("捕捉到野生李可已经", "825天", "稀有度：SSSSS")
        col2.metric("与李可相距", "9094 km", "飞行时长12h")
        col3.metric("李可今天", "27岁啦！", "茁壮成长中")

        st.map(map_data)
        st.write(""" <h1 style='text-align: center; font-size: 25px;'> 2024年6月27日，我好想你。""", unsafe_allow_html=True) 

    if la == '北京':
        st.write(
            """
        <h1 style='text-align: center; font-size: 22px; font-weight: normal;'>
            李可在华子度过了充实的五年，取得学士和硕士学位。啊，华子。啊，北京。     
        """, unsafe_allow_html=True)   

        st.write(
            """
        <h1 style='text-align: center; font-size: 20px;'>
            点击查看百变李可👇        
        """, unsafe_allow_html=True)          

        if st.button('--------------------------------------------------------------她，是摄影师。------------------------------------------------------------'):
            st.image("./pic/photo.jpg")

        if st.button('--------------------------------------------------------------她，能尝百草。------------------------------------------------------------'):
            st.image("./pic/baicao.jpg")

        if st.button('--------------------------------------------------------------她，是环境第一后卫。------------------------------------------------------------'):

            st.image("./pic/basket.jpg")
        if st.button('--------------------------------------------------------------她，也会一点魔法。------------------------------------------------------------'):
            st.image("./pic/magic.jpg")


        st.markdown("""
                    <div class="birthday-wish">
                        WOW！ 让我们为十项全能的李可欢呼！
                    </div>
                """, unsafe_allow_html=True)   
if __name__ == '__main__':
    run()
