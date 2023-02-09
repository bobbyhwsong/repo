import streamlit as st
import pandas as pd
import numpy as np
	
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')
DIVIDER = '--------------------------------------------------------------------------------'

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

####################################
# - VIEW_PROPOSAL
####################################
if add_sidebar == VIEW_PROPOSAL:
    st.title(add_sidebar)
    st.write(DIVIDER)
    
    st.subheader('1. 문제 정의')
    st.markdown('##### 풀고자하는 문제와 목적을 명확하게')
    st.write('''
             북아시아에서의 매출 증진
             ''')
    st.write(DIVIDER)
    
    st.subheader('2. 지표 설정')
    st.markdown('##### 어떤 지표가 목적에 부합하는가')
    
    st.write(DIVIDER)
    
    st.subheader('3. 현황 파악')
    st.markdown('##### 현재 성과 및 결과 파악')
    
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
    
    code = '''
        pip uninstall streamlit
        pip install streamlit-nightly --upgrade
        '''
    st.code(code, language='bash')


    st.markdown('#### Run streamlit server')
    code = '''
            streamlit run streamlit_test.py'''
    st.code(code, language='bash')
    

    st.markdown('#### Command Line')
    code = '''
        streamlit --help
        streamlit run your_script.py
        streamlit hello
        streamlit config show
        streamlit cache clear
        streamlit docs
        streamlit --version
        '''
    st.code(code, language='bash')

    st.markdown('#### Import Convention')
    code = '''
            # Import Convention
            import streamlit as st'''
    st.code(code, language='python')

    st.write(DIVIDER)
    
    st.subheader('Template')    

    code = '''
        #<Sample code for the template>
        
        import streamlit as st
        import pandas as pd
        
        ####################################
        # 1_ Define Functions
        # - Load data
        # - Clean data
        ####################################
        @st.cache
        def load_data():
            #filepath = 'some_filepath.csv'
            #df = pd.read_csv(filepath)
            df = pd.DataFrame({
                'first column': [1, 2, 3, 4],
                'second column': [10, 20, 30, 50],
            })
            return df
        df = load_data()
        ####################################
        # 2_ Engineer Data
        # - prepare data for output
        ####################################
        df.column = ['Number', 'Scores']
        df['Level'] = ['C', 'B', 'B', 'A']
        ####################################
        # 3_Build Dashboard using Streamlit
        ####################################
        st.title('You can build Streamlit Webapp')
        add_sidebar = st.sidebar.selectbox('Select Method', 'First','Second')
        if add_sidebar == 'First':
            # View for s'First'- show matrix, graph etc.
        else :
            # View for 'Second' - show matrix, graph etc.
        '''
    st.code(code, language='python')


    st.write(DIVIDER)
    st.subheader('References')
    url1 = 'https://docs.streamlit.io/'
    url2 = 'https://bittersweet-match-49f.notion.site/Streamlit-5ca73e87f96a443a902eefc5c721e3d0'

    url1
    url2

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
