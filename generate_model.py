import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
pd.set_option('display.unicode.east_asian_width',True)
penguin_df=pd.read_csv(r'penguins-chinese.csv',encoding='gbk')
penguin_df.dropna(inplace=True)
output=penguin_df['企鹅的种类']
features=penguin_df[['企鹅栖息的岛屿','喙的长度','喙的深度','翅膀的长度','身体质量','性别']]
features=pd.get_dummies(features)
output_codes,output_uniques=pd.factorize(output)

x_train,x_test,y_train,y_test=train_test_split(features,output_codes,train_size=0.8)
rfc=RandomForestClassifier()
rfc.fit(x_train,y_train)
y_pred=rfc.predict(x_test)

score=accuracy_score(y_test,y_pred)
print(f'该模型的准确率是：{score}')