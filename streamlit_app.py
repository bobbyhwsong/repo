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
    st.title("기획서 및 대시보드")
    st.markdown("**- 기획서 :** Introduction & References")
    st.markdown("**- 대시보드 :** Text elements & st.write method")

VIEW_PROPOSAL = 'Proposal'
VIEW_DASHBOARD = 'Dashboard'

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
    st.header('기획서')
    st.write(DIVIDER)
    st.subheader('Github Repo Available!')
    url1 = 'https://github.com/jhbale11/All-About-Streamlit'
    url1 

    st.write(DIVIDER)
    st.subheader('Install & Import')

    st.markdown('#### Pre-release Features')
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
