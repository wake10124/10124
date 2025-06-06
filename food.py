import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame({'latitude':[22.811942,22.824234,22.814160,22.809728,22.813826,22.759869],
'longitude':[108.392788,108.318291,108.321510,108.324614,108.318945,108.320104]})
     
st.subheader('南宁美食地图🌏')
st.map(df)


data3 = {
    '店名':['一点点','CHAGEE霸王茶姬','海底捞火锅','舒记老友粉','煲掌柜·明火煲仔饭','爱民螺蛳粉'],
    '评分':[1,2,3,4,5,6],

}

st.subheader("⭐️餐厅评分")

df = pd.DataFrame(data3)

index = pd.Series([1,2,3,], name='序号')

st.bar_chart(df, x='店名')



data2 =  {
 
    '月份':[1,2,3,4,5,6,7,8,9,10,11,12],
    '一点点':[60, 75, 95,45,68,97,64,64,13,70,80,70],
    'CHAGEE霸王茶姬':[30, 40, 55, 95,56,54,30,45,89,12,78,51],
    '海底捞火锅':[30, 60, 70,30, 63, 55, 45,56,54,52,45,89],
    '舒记老友粉':[50, 90, 95,30, 63, 70,41, 63, 39, 45,78,54],
    '煲掌柜·明火煲仔饭':[30, 70, 85,30, 63, 75,90, 63, 26, 45,23,54],
    '爱民螺蛳粉':[40, 60, 95,30, 70, 45,30, 63,45,90, 86, 26,]
}

st.subheader("💰不同餐厅类型价格")

df = pd.DataFrame(data2)

index = pd.Series([1,2,3,4,5,6,7,8,9,10,11,12], name='序号')

st.line_chart(df, x='月份')


# 定义数据,以便创建数据框
data = {
    '时段':[10,11,12],
    '一点点':[60, 75, 95],
    'CHAGEE霸王茶姬':[30, 40, 55],
    '海底捞火锅':[30, 60, 70],
    '舒记老友粉':[50, 90, 95],
    '煲掌柜·明火煲仔饭':[30, 70, 85],
    '爱民螺蛳粉':[40, 60, 95]
}
st.subheader("🕗用餐高峰时段")
df = pd.DataFrame(data)
index = pd.Series([1, 2, 3,], name='序号')
df.index = index
st.area_chart(df, x='时段')


st.subheader('🍽️餐厅详情')
st.text('选择餐厅查看详情')

with st.expander("一点点"):
           c1,c2=st.columns(2)
           c1.markdown('## 一点点')
           c1.markdown('##### 评分')
           c1.markdown('#  4.9/5.0')
           c1.markdown('## 人均消费')
           c1.markdown('# 25元')

           c1.markdown('**推荐菜品：**')
           c1.markdown(' * &#8194:茉莉绿茶')
           c1.markdown(' * &#8194:翡翠柠檬')
           c1.markdown(' * &#8194:四季春茶')
st.subheader('当前拥挤程度')
st.progress(10,text="%40拥挤")





st.title('😍今日推荐')
st.markdown("<span style='color:red; border:2px solid red; border-radius:8px; padding:4px;'>干饭首选👍</span>", unsafe_allow_html=True)

# 初始化会话状态
if 'count' not in st.session_state:
    st.session_state.count = 0

count = 0;
if st.button(' :red[今天吃什么]'):
	st.session_state.count += 1
	if st.session_state.count % 7 == 1:
		st.markdown("<span style='border-radius: 8px; display: inline-block;width: 800px; padding: 8px 16px;background-color:green;'>今日推荐：CHAGEE霸王茶姬</span>", unsafe_allow_html=True)
		st.markdown("![CHAGEE霸王茶姬](https://l.sinaimg.cn/wx3/large/005GOYFBgy1hgtp09r1ovj313s1e84h1.jpg/original.jpg)")
	if st.session_state.count % 7 == 2:
		st.markdown("<span style='border-radius: 8px; display: inline-block;width: 800px; padding: 8px 16px;background-color:green;'>今日推荐：一点点</span>", unsafe_allow_html=True)
		st.markdown("![一点点](https://ts1.tc.mm.bing.net/th/id/R-C.814016d6de168d0911cf4c6a4a6ab8d5?rik=llM1iIZW%2f2AMFA&riu=http%3a%2f%2fn.sinaimg.cn%2fsinacn16%2f632%2fw852h580%2f20180411%2f7a67-fyzeyqa5655389.jpg&ehk=00w4grSZD%2fyIpapErzTgN3E3AY5UYNmQ%2by6mt%2f3DA%2f8%3d&risl=&pid=ImgRaw&r=0)")
	if st.session_state.count % 7 == 3:
		st.markdown("<span style='border-radius: 8px; display: inline-block;width: 800px; padding: 8px 16px;background-color:green;'>今日推荐：海底捞火锅</span>", unsafe_allow_html=True)
		st.markdown("![海底捞火锅](https://ts1.tc.mm.bing.net/th/id/R-C.3304fc57bce46fe94f44c602ede9e919?rik=gnKWDQci9ij0YQ&riu=http%3a%2f%2f5b0988e595225.cdn.sohucs.com%2fimages%2f20181105%2fc88575aed66f433b9ae513084d1fb798.jpeg&ehk=5cB3FxZoKHcexQeRoS0Vi2knRJJ0vwk7VM05GVQ8j%2fo%3d&risl=&pid=ImgRaw&r=0)")
	if st.session_state.count % 7 == 4:
		st.markdown("<span style='border-radius: 8px; display: inline-block;width: 800px; padding: 8px 16px;background-color:green;'>今日推荐：舒记老友粉</span>", unsafe_allow_html=True)
		st.markdown("![舒记老友粉](https://tse1-mm.cn.bing.net/th/id/OIP-C.og4tTMukwMr3DtcYOpc73AHaFO?rs=1&pid=ImgDetMain)")
	if st.session_state.count % 7 == 5:
		st.markdown("<span style='border-radius: 8px; display: inline-block;width: 800px; padding: 8px 16px;background-color:green;'>今日推荐：煲掌柜·明火煲仔饭</span>", unsafe_allow_html=True)
		st.markdown("![煲掌柜·明火煲仔饭](https://tse3-mm.cn.bing.net/th/id/OIP-C.vH_dRt2V-ZQr6WNlzWYyXgHaFj?rs=1&pid=ImgDetMain)")
	if st.session_state.count % 7 == 6:
		st.markdown("<span style='border-radius: 8px; display: inline-block;width: 800px; padding: 8px 16px;background-color:green;'>今日推荐：爱民螺蛳粉</span>", unsafe_allow_html=True)
		st.markdown("![爱民螺蛳粉](https://img.alicdn.com/i4/4033604411/O1CN019mcLna1iSHmU5U9lk_!!4033604411.jpg)")




