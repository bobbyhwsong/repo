import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
	
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')
DIVIDER = '--------------------------------------------------------------------------------'

@st.cache
def load_data():
        data = pd.read_csv('Superstore.csv')
        data2 = pd.read_excel('Super.xls',sheet_name='반품 정리')
        data2 = data2.drop_duplicates()
        df_merge = pd.merge(data, data2, how='left', on='주문 ID')
        df_merge = df_merge.drop(['행 ID','고객 이름','제품 이름'],axis=1)
        df = df_merge
        
        df.rename(columns={'주문 날짜':'OrderDate'},inplace=True)
        df.rename(columns={'배송 날짜':'ShipDate'},inplace=True)

        df['주문 ID']= df['주문 ID'].astype('str')
        df['OrderDate'] = pd.to_datetime(df['OrderDate'])
        df['ShipDate'] = pd.to_datetime(df['ShipDate'])
        df['배송 형태']= df['배송 형태'].astype('str')
        df['고객 ID']= df['고객 ID'].astype('str')
        df['세그먼트'] = df['세그먼트'].astype('str')
        df['도시'] = df['도시'].astype('str')
        df['시/도'] = df['시/도'].astype('str')
        df['국가/지역'] = df['국가/지역'].astype('str')
        df['지역'] = df['지역'].astype('str')
        df['제품 ID'] = df['제품 ID'].astype('str')
        df['범주'] = df['범주'].astype('str')
        df['하위 범주'] = df['하위 범주'].astype('str')
        
        df.fillna('no',inplace=True)
        df = df[df['반품']=='no']
        return df

####################################
# - Sidebar
####################################
with st.sidebar:
    st.title("비저블 지원")
    st.markdown("**- 기획서 :** 기획서 프로세스")
    st.markdown("**- 대시보드 :** 대시보드 스케치")
    
VIEW_PROPOSAL = '기획서'
VIEW_DASHBOARD = '대시보드'

sidebar = [VIEW_PROPOSAL, 
        VIEW_DASHBOARD]
add_sidebar = st.sidebar.selectbox('Choose Page You Want to See', sidebar)

with st.sidebar:
    add_radio = st.radio(
        "Choose a language (not working)",
        ("English", "Korean")
    )
    
data_load_state = st.text('Loading data...')
df = load_data()
data_load_state.text("데이터 불러오기 완료!")

if st.checkbox('데이터 보기'):
        st.subheader('Superstore.csv')
        st.write(df)
        
####################################
# - VIEW_PROPOSAL
####################################
if add_sidebar == VIEW_PROPOSAL:
    st.title(add_sidebar)
    st.write(DIVIDER)
    
    st.subheader('1. 문제 정의')
    st.markdown('###### 매출액은 크지만 이익은 크지 않은 동남아시아 수익 구조 개선')
    st.write('''동남아시아 지역에서 발생하는 매출이 840,428.9613인데 비해 수익은 17,552.6913으로 현저히 적은 것을 볼 수 있다.
                아래 비중 그래프를 봐도, 매출의 25%를 차지하는 동남아시아가 수익에서는 4.55%밖에 되지 않는 것을 볼 수 있다.
                이에 동남아시아 지역에서의 수익구조를 개선할 필요가 있다. ''')
    
    fig = px.pie(df,values='매출',names='지역', title='지역 별 매출 비중', color_discrete_sequence=px.colors.sequential.RdBu, category_orders={'지역':['동남아시아','오세아니아','북아시아','중앙아시아']})
    fig.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig)
    
    fig = px.pie(df,values='수익',names='지역', title='지역 별 수익 비중', color_discrete_sequence=px.colors.sequential.RdBu, category_orders={'지역':['동남아시아','오세아니아','북아시아','중앙아시아']})
    fig.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig)
    st.write(DIVIDER)
    
    st.subheader('2. 지표 설정')
    st.markdown('##### 동남아시아 지역의 수익, 매출, 매출액 순이익률(ROS)')
    st.write('''동남아시아의 수익 구조를 개선하는 것이기에 동남아시아의 수익이 중요한 지표가 될 것이다.
                또한, 수익만 증가하는 것보다는 매출이 증가하는 것이 의미가 있을 것이기에 매출도 중요한 지표가 될 것이며,
                매출 중에 수익이 차지하는 비율도 중요한 지표가 될 것이다. ''')
    st.write(DIVIDER)
    
    st.subheader('3. 현황 파악')
    st.markdown('##### 동남아시아 지역의 수익')
    st.write(17552.6913)
    st.markdown('##### 동남아시아 지역의 매출')
    st.write(840428.9613) 
    st.markdown('##### 동남아시아 지역의 매출액 순이익률(ROS)')
    ROS = 17552.6913/840428.9613
    st.write(ROS)
    st.write(DIVIDER)
    
    st.subheader('4. 평가')
    st.markdown('##### 그 결과에 대한 평가 기준과 비교 대상')
    
    st.write(DIVIDER)
    
    st.subheader('5. 원인 분석')
    st.markdown('##### 문제와 원인의 관련성 분석')
    
    st.write(DIVIDER)
    
    st.subheader('6. 해결 방안')
    st.markdown('##### 원인에 대한 해결 방안')
    
    st.write(DIVIDER)

    st.subheader('7. 결론')
    st.markdown('##### 결론 요약, 분석 목적에 어떤 의미가 있는지 설명')
    
    st.write(DIVIDER)

####################################
# - VIEW_DASHBOARD
####################################
elif add_sidebar == VIEW_DASHBOARD:
    st.title('Uber pickups in NYC')

    @st.cache
    def load_data(nrows):
        data = pd.read_csv(DATA_URL, nrows=nrows)
        lowercase = lambda x: str(x).lower()
        data.rename(lowercase, axis='columns', inplace=True)
        data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
        return data
	
    data_load_state = st.text('Loading data...')
    data = load_data(10000)
    data_load_state.text("Done! (using st.cache)")

    if st.checkbox('Show raw data'):
        st.subheader('Raw data')
        st.write(data)
	
    st.subheader('Number of pickups by hour')
    hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
    st.bar_chart(hist_values)

    hour_to_filter = st.slider('hour', 0, 23, 17)
    filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
	
    st.subheader('Map of all pickups at %s:00' % hour_to_filter)
    st.map(filtered_data)
