import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime


if st. sidebar.button("首页"):
    st.title("主页")
    st.write("广西职业师范学院（原广西经济管理干部学院）坐落于广西首府南宁市风景秀丽的邕江之滨、相思湖畔，是自治区人民政府直属、自治区教育厅主管的公办全日制普通本科学校，致力于培养区域经济社会发展所需要的高素质应用型、技术技能型人才和职业教育师资。")

if st. sidebar.button("个人简历生成器"):
    from datetime import datetime, timedelta
    def my_format_func(option):
         return f'{option}'

    st.header("🎨个人简历生成器")
    st.text("使用Streamlit创建你的个性化简历")

    c1,c2 = st.columns([1,2])
    with c1:
        st.subheader("个人信息表单")
        st.markdown("***")
        xingming=st.text_input('姓名')
        job=st.text_input("职位")
        dianhua=st.text_input("电话")
        youxiang=st.text_input("邮件")
        date = st.date_input("出生日期", value=None)
    
        sex = st.radio(
            '性别',
        ['男', '女', '其他'],
        horizontal=True,)
    

        degree=st.selectbox('学历',['博士','硕士','本科','大专','中专'])

        def my_format_func(language):
            return f'{language}语'
        languages = st.multiselect(
            '语言能力',
            ['汉', '英', '德', '法', '葡萄牙', '西班牙'],
            format_func=my_format_func,
            )

        def my_format_func(skill):
            return f'{skill}'
        skills = st.multiselect(
            '技能（可多选）',
            ['java', 'python', 'jupyter', '机器学习', 'HTML', 'C语言'],
            format_func=my_format_func,
        )



        my_range = range(0, 30)
        numbers = st.select_slider('工作经验（年）', options=my_range, value=5)
    
        values = st.slider(
        '选择一组范围',
        5000, 50000, (10000, 20000))
        st.write('你选择的薪资范围是：', values)

        jianjie=st.text_area(label='个人简介：', placeholder='请简要介绍您的专业背景、职业目标和个人特点...')
        from datetime import datetime, time
        w1 = st.time_input("每日最佳联系时间段")

        uploaded_file=st.file_uploader("上传个人照片",type=["jpg","jpeg","png"],key="avatar_uploader")
    

if st. sidebar.button("动物图鉴"):
    

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
    city = st.selectbox('按分类筛选：', ['全部','自然风光', '城市夜景', '动物鉴赏'],     format_func=my_format_func, index=2)
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

if st. sidebar.button("南宁美食数据"):
    df = pd.DataFrame({'latitude':    [22.811942,22.824234,22.814160,22.809728,22.813826,22.759869],
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
    st.markdown("<span style='color:red; border:2px solid red; border-radius:8px;     padding:4px;'>干饭首选👍</span>", unsafe_allow_html=True)

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

if st. sidebar.button("数字档案"):
    st.title("🕶GTI 蜂医 - 数字档案")
    st.header("🔑基础信息")
    st.subheader("干员ID：10086")
    st.subheader("注册时间：`2025-6-04` | 情绪状态：✅稳定")
    st.subheader("当前地图: `航天基地` | 安全等级：`机密`")
    st.header("📊收益矩阵")

    c1, c2, c3 = st.columns(3)
    c1.metric(label="当局收入", value="150w", delta="100w")
    c2.metric(label="当局伤害", value="100w", delta="68%")
    c3.metric(label="当局消耗", value="35w", delta="-26%")
    st.header("📝任务日志")

    data = {
        '中控楼':[568, 868, 670, 884, 144],
        '浮力室':[820, 884, 768, 524, 709],
        '状态':['✅完成','🕒进行中','✅完成','✅完成','❌未完成'],
        '难度':['★★★☆☆','★★★☆☆','★★★☆☆','★★★☆☆','★★★☆☆'],
    }
    # 定义数据框所用的索引
    index = pd.Series(['01月', '02月', '03月', '04月', '05月'], name='月份')
    # 根据上面创建的data和index，创建数据框
    df = pd.DataFrame(data, index=index)

    st.subheader('任务数据详情')
    st.dataframe(df)
    st.subheader('🔐蓝洞代码块')
    python_code = '''def hello():
        print("你好，Streamlit！")
    '''

    st.code(python_code)
    st.code(python_code, line_numbers=True)

    st.markdown(':green[`>>SYSTEM MESSAGE:`]下一个任务目标已解锁...')
    st.markdown(':green[`>>TARGET:`]仓库管理系统')
    st.markdown(':green[`>>COUNTDOWN:`]2025-06-04 16:57:31')

    st.text("系统状态：在线 连接状态：已加密")


