import streamlit as st
st.title('Hello World')
st.header('This is a header')
st.subheader('This is a subheader')
st.write('This is a simple example of Streamlit web app')
st.text('This is a text')
st.divider()
st.caption('This is a caption')
st.divider()
st.markdown('Heading 1')
st.markdown('[AI VIETNAM](https://)')
st.markdown("""
  1. Machine Learning
  2. Deep Learning
""")
st.markdown(r'$ \sqrt{2x} $')
st.divider()
st.latex('\sqrt{2x}')
st.divider()
st.write('AI VIETNAM')
st.write('# Heading 1')
st.write('[Google](https://www.google.com.vn/)')
st.write(r'$ \sqrt{2x} $')
st.divider()
st.code("""
  import random
  value = random.randint(0, 10)
  print(value)
""")


def get_year():
    return 2021


with st.echo():
    st.write('This code will be printed')

    def get_name():
        return "Khang"
    name = get_name()
    year = get_year()
    st.write(f'Name: {name} Year: {year}')
st.divider()

st.logo('Data/Image/logo.png')
st.image('Data/Image/dog.jpeg', caption='Dog')
st.audio('Data/Audio/audio.mp4')
st.video('Data/Video/video.mp4')
st.divider()

agree = st.checkbox('I agree')
if agree:
    st.write('Great!')

status = st.radio('Your favorite color:', [
                  'Yello ', 'Blue'], captions=['Vàng', 'Xanh'])
print(status)

status = st.selectbox('Your contact', ['EMAIL', 'PHONE'])
print(status)

status = st.multiselect('Select your favorite color:', [
                        'Red', 'Green', 'Blue'], ['Red'])
print(status)

st.select_slider('Select a range of values', [0,1, 2])
st.divider()

if st.button('Say Hello'):
  st.write('Hello')
else:
  st.write('Goodbye')
  
value=st.text_input('Your Name: ',value='Khang')
st.write(value)
st.divider()

upload_files=st.file_uploader('Choose Files',accept_multiple_files=True)
for uploaded_file in upload_files:
  st.write(uploaded_file.name)

st.divider()
with st.form(key='my_form'): 
  col1,col2=st.columns(2)
  f_name=col1.text_input('Name: ')
  f_age=col2.text_input('Age: ') 
  submited=st.form_submit_button('Submit')
  if submited:
    st.write(f'Name: {f_name}, Age: {f_age}')
st.divider()
import random
value=random.randint(1,10)
if 'key' not in st.session_state:
  st.session_state['key']=value
st.write(st.session_state.key)

