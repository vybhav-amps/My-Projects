import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
#reading data
data=pd.read_csv('kc_house_data.csv')
data=data.rename(columns={"long":"lon"})

data.drop('id',axis=1,inplace=True)
data.drop('date',axis=1,inplace=True)
data.drop('sqft_living',axis=1,inplace=True)
data.drop('waterfront',axis=1,inplace=True)
data.drop('view',axis=1,inplace=True)
data.drop('sqft_above',axis=1,inplace=True)
data.drop('sqft_basement',axis=1,inplace=True)
data.drop('yr_renovated',axis=1,inplace=True)
data.drop('sqft_living15',axis=1,inplace=True)
data.drop('sqft_lot15',axis=1,inplace=True)

st.write('## predicting house prices at KING COUNTY,Washington')
st.write(data)
st.write('### houses on map')
st.map(data)

x1=data['bedrooms'].values
x2=data['bathrooms'].values
x3=data['floors'].values
x4=data['condition'].values
y=data['price'].values

st.sidebar.header('check your choice')

st.write('### select maximum area you choose (sqft lot)',50000)
area_sqft=st.number_input('between 500sqft to 1,660,000sqft')
min_price=st.sidebar.slider('min price (x 10^3 $)',70,7700,1000,10)
max_price=st.sidebar.slider('max price (x 10^3 $)',70,7700,5000,10)
bedroom=st.sidebar.slider('bedrooms',0,40,3)
bathroom=st.sidebar.slider('bathrooms',0.0,10.0,2.5,0.25)
floor=st.sidebar.slider('floors',0.0,4.0,2.0,0.5)
cond=st.sidebar.slider('condition',0,5,3)

X=data[['yr_built','sqft_lot']]
y=data['price'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)
lm = LinearRegression()
lm.fit(X_train,y_train)
m=lm.coef_
c=lm.intercept_

def area():
    n1=0
    x_area=data['sqft_lot']
    for i in range(len(x_area)):
        if x_area[i]<=area_sqft:
            n1+=1
    st.write('### Number of houses within',area_sqft,'sqft : ',n1)
    st.plotly_chart(px.scatter(data, x='sqft_lot', y='price'))

def year():
    n0=0
    m0=m[0]
    a=st.selectbox('From',range(1900,2015),1)
    b=st.selectbox('To',range(1905,2050),1)
    x0=np.linspace(a,b,b-a+1)
    y0=m0*x0+c
    plt.plot(x0,y0,color='red',label='predicted values')
    plt.scatter(X['yr_built'],y,color='blue',label='actual values')
    plt.legend()
    st.pyplot(plt.show())
    data1={'year':x0,'price':y0}
    st.write('### predicted price')
    st.plotly_chart(px.line(data1, x='year', y='price'))
    st.write('### actual values')
    st.plotly_chart(px.scatter(data, x='yr_built', y='price'))

    yb=data['yr_built'].values
    for i in range(len(yb)):
        if a<=yb[i]<=b:
            n0+=1        
    st.write('number of houses with your choice:',n0)
    


def bedrooms():
    k=0
    c=0
    for i in range(len(x1)):
        if x1[i]==bedroom:
            k=k+y[i]
            c+=1

    try:
        st.write('the average price on ',bedroom,'bedrooms:',k/c)
        st.write('number of houses with',bedroom,'bedrooms are',c)
    except:
        st.write('no houses available')

    

def bathrooms():
    k=0
    c=0
    for i in range(len(x2)):
        if x2[i]==bathroom:
            k=k+y[i]
            c+=1

    try:
        st.write('the average price on ',bathroom,'bathrooms:',k/c)
        st.write('number of houses with',bathroom,'bathrooms are',c)
    except:
        st.write('no houses available')

    
def floors():
    k=0
    c=0
    for i in range(len(x3)):
        if x3[i]==floor:
            k=k+y[i]
            c+=1

    try:
        st.write('the average price on ',floor,'floors:',k/c)
        st.write('number of houses with',floor,'floors are',c)
    except:
        st.write('no houses available')

    
def condition():
    k=0
    c=0
    for i in range(len(x4)):
        if x4[i]==cond:
            k=k+y[i]
            c+=1

    try:
        st.write('the average price on ',cond,'condition:',k/c)
        st.write('number of houses with',cond,'/5 condition are',c)
    except:
        st.write('no houses available')

    
def total():
    y=data['price'].values
    st.write("""
     ## price for your total choice
    """)
    k=0
    c=0
    l1=[]
    l2=[]
    p=[]
    z=[]
    area_sq=X['sqft_lot']
    for i in range(len(y)):
        if min_price*1000<=y[i]<=max_price*1000:
            if area_sq[i]<=area_sqft:
                if x1[i]==bedroom and x2[i]==bathroom and x3[i]==floor and x4[i]==cond:
                    k=k+y[i]
                    c+=1
                    p.append(data['price'][i])
                    z.append(data['zipcode'][i])
                    l1.append(data['lat'][i])
                    l2.append(data['lon'][i])
            

    try:
        st.write('average house price with your choice',k/c)
        st.write('total number of houses with your choice :',c)
    except:
        st.write('no houses')

    d={"price":p,"zipcode":z,"lat":l1,"lon":l2}
    df=pd.DataFrame(d)
    length=len(df)
    st.write('### houses of your choice on map')
    st.map(df)
    st.write('### houses of your choice')
    st.write(df)
    
    
        
st.write('--------------------------------------------------------')
df_area=area()
st.write('--------------------------------------------------------')
df0=year()
st.write('--------------------------------------------------------')
df1=bedrooms()
st.write('--------------------------------------------------------')
df2=bathrooms()
st.write('--------------------------------------------------------')
df3=floors()
st.write('--------------------------------------------------------')
df4=condition()
st.write('--------------------------------------------------------')
t=total()
st.write('--------------------------------------------------------')