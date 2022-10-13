import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
from sklearn.tree import  export_text
from sklearn.tree import plot_tree

df= pd.read_csv('diabetes.csv')

df=pd.get_dummies(data=df, drop_first=True)

explcativas=df.drop(columns="Outcome")
objetivas=df.Outcome


x_train,x_test,y_train,y_test=train_test_split(explcativas,objetivas,test_size=0.3,random_state=42)

model = DecisionTreeClassifier(criterion="gini",random_state=42,max_depth=3,min_samples_leaf=5)
model.fit(x_train,y_train)

plot_tree(decision_tree=model,feature_names=explcativas.columns,filled=True)

y_predict=model.predict(x_test)

print(accuracy_score(y_test,y_predict))

target=list(df["Pregnancies"].unique())
feature_name=list(explcativas.columns)
resultados=export_text(model,feature_names=feature_name)
print(resultados)

