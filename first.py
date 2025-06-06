import streamlit as st

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

import pandas as pd

# 定义数据,以便创建数据框
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

# 创建一个代码块，用于展示python_code的内容
# language为默认，即该代码块以Python语法高亮
st.code(python_code)
# 创建一个代码块，用于展示python_code的内容
# language为默认，即该代码块以Python语法高亮
# 并设置line_numbers为True，即该代码块有行号
st.code(python_code, line_numbers=True)

st.markdown(':green[`>>SYSTEM MESSAGE:`]下一个任务目标已解锁...')
st.markdown(':green[`>>TARGET:`]仓库管理系统')
st.markdown(':green[`>>COUNTDOWN:`]2025-06-04 16:57:31')

st.text("系统状态：在线 连接状态：已加密")