
import pickle
import smogn
import copy
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBRegressor
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from sklearn.linear_model import Ridge


df = pd.read_csv(
    "~/Documents/ML/Salary Predictor/Placement_Data_Full_Class.csv")

df["salary"] = df["salary"].fillna(0)

categorical = ["gender", "ssc_b", "hsc_b", "hsc_s",
               "degree_t", "workex", "specialisation", "status"]

le = LabelEncoder()
for i in categorical:
    df[i] = le.fit_transform(df[i])

df = df.drop("sl_no", axis=1)
df_reg = copy.deepcopy(df)
df_class = copy.deepcopy(df)

df_class = df_class.drop("salary", axis=1)

df_reg_smogn = smogn.smoter(
    data=df_reg,  # dataset
    y='salary'  # label for the prediction ,i.e in our case salary
)

X = df_reg_smogn.iloc[:, :-1].values
y = df_reg_smogn.iloc[:, -1].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

xgbr = XGBRegressor(verbosity=0)
xgbr.fit(X_train, y_train)
# below is the Adjusted R-Squared for the model
# print(1 - (1-xgbr.score(X_test, y_test)) *
# (len(y_test)-1)/(len(y_test)-X_test.shape[1]-1))


pickle.dump(xgbr, open('xgbrpredict.pickle', 'wb'))


#details = [1, 67, 1, 91, 1, 1, 58, 2, 0, 55, 1, 58, 1]
# print(xgbr.predict(np.asanyarray([details])))

# gender	ssc_p	ssc_b	hsc_p	hsc_b	hsc_s	degree_p	degree_t	workex	etest_p	specialisation	mba_p	status
# male 1, others 1, commerce1 science2 arts0, sci 2,
