import streamlit as st
import pandas as pd

from datetime import datetime, timedelta
def my_format_func(option):
    return f'{option}'

st.set_page_config(page_title='个人简历生成器',layout='wide',page_icon="📓")

st.header('🎨个人简历生成器')
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
    
    

with c2:
    st.subheader("简历实时预览")
    st.markdown("***")
    c11,c22=st.columns([1,2])
    with c11:
        st.header(f'{xingming}')
        st.image(uploaded_file)
        st.write(f'职位：{job}')
        st.write(f'电话：{dianhua}')
        st.write(f'邮箱：{youxiang}')
        st.write(f'出生日期：{date}')
    with c22:
        st.write(f'性别：{sex}')
        st.write(f'学历：{degree}')
        st.write(f'工作经验：{numbers}年')
        st.write(f'期望薪资：{values}元')
        st.write(f'最佳联系时间：{w1}')
        st.write(f'语言能力：{languages}语')

    st.subheader("个人简介")
    st.write(f'{jianjie}')


    st.subheader("专业技能")
    st.write(f'{skills}')
    st.markdown("***")
    st.write("***代码改变世界，你改变代码***")