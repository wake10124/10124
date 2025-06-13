import streamlit as st

st.set_page_config(page_title='Streamlit 视频播放器', page_icon='🎬️')

st.header("🎬️Streamlit 视频播放器")
st.text("点击下方视频封面选择要播放的视频")


# 读取视频数据
video_file = 'https://www.w3school.com.cn/example/html5/mov_bbb.mp4'

# 显示视频
st.subheader("视频播放")
st.video(video_file)


def my_format_func(option):
    return f'{option}'


st.subheader('视频库')
st.text("点击图片选择视频")
city = st.selectbox('按分类筛选：', ['全部','自然风光', '城市夜景', '动物鉴赏'], format_func=my_format_func, index=2)
# 根据返回值不同，选择不同的特色回答
# 同时应注意返回值不受自定义my_format_func
if city == '自然风光':
    st.subheader("自然风光")
    st.text("**描述**：美丽的自然景观，山川湖海")
    st.text("时长2:15 | 分类：自然")
if city == '城市夜景':
    st.subheader("城市夜景")
    st.text("**描述**：壮丽的城市景观，霓虹闪烁")
    st.text("时长2:15 | 分类：城市")
if city == '动物鉴赏':
    st.subheader("动物鉴赏")
    st.text("**描述**：美丽的自然景观，山川湖海")
    st.text("时长2:15 | 分类：动物")

if city == '全部':
    
    
    
    

    st.image('https://www.2008php.com/2012_Website_appreciate/2012-02-18/20120218154042.jpg')
    st.write("自然风光")
    st.text("时长2:15 | 分类：自然")

    st.image('https://seopic.699pic.com/photo/50089/8786.jpg_wh1200.jpg')
    st.write("城市夜景")
    st.text("时长2:15 | 分类：城市")

    st.image('https://www.2008php.com/2017_Website_appreciate/2017-07-02/20170702001646.jpg')
    st.write("动物鉴赏")
    st.text("时长2:15 | 分类：动物")

    






