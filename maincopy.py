# ============================================1교시==========================================
# 설치 
# 1.uv init
# 2.uv add pandas 
# 3.uv add pandas matplotlib
# 4.아래 기본 임포트 작성
# 5.버전 확인 코드 작성 
# import pandas as pd 
# import matplotlib
# print (pd.__version__)
# print (matplotlib.__version__)

# import pandas as pd 
# import matplotlib.pyplot as plt
# #matplotlib 는 데이터를 차트로 만들어준다.
# #한글 해결하기.
# plt.rcParams['font.family'] = 'Malgun Gothic'
# plt.rcParams['axes.unicode_minus'] = False

# #데이터 만들기
# data= pd.read_csv('./data1_20220731.csv',index_col=0)
# #선차트
# # data.plot()
# # plt.show()

# #막대 차트
# # data.plot(kind='bar')
# # plt.show()

# #히스토그램
# # data.plot(kind='hist',y='세대수')
# # plt.show()

# #산점도
# # data.plot(kind='scatter',x='남',y='여')
# # plt.show()

# #원형 그래프
# # data.plot(kind='pie',y='세대수',autopct='%1.1f%%')
# # plt.show()

# #마커 사용 예시
# data.plot(kind='line', x='남(18세이상)', y='여(18세이상)', linestyle='-', color='r', marker='s')


# plt.show()

#==========================================2교시================================
# 빠른 시각화를 위한 스트림 릿 streamlit 추가하기
#uv add streamlit
#uv run streamlit hello

#uv run streamlit run main.py 메인파일로 스트림릿 사용하기.
# st.title("타이틀 입니다" ":shinto_shrine:" ":heart:" ":heart:" ":heart:" ":heart:")
# #타이틀은 h1 태그
# st.header("헤더 입니다.")
# #헤더는 h2 태그
# st.subheader("서브 헤더 입니다.")
# #서브 헤더는 h3 태그
# st.text("텍스트 입니다.")
# #텍스트는 div 태그
# st.markdown("마크다운 입니다."),('**"개졸리네"**')

# st.markdown("green [$/sqrt{x^2+y^2=15}*1$]")
# st.latex(r"\sqrt{x^2+y^2=15}*1")
# #마크 다운으로 수식 표출가능.
# #마크다운은 p 태그 강조를 위해 **"내용"** 해서 strong 적용 가능
# st.caption  ("캡션입니다.")

# #캡션은 small 태그
# st.code("st.code("",language="")",language="python")

# cd="""
# def 함수():
#     pass
# """

# st.code(cd,language="python")

# import pandas as pd
# import matplotlib.pyplot as plt 
# import streamlit as st
# st.title("테이블 화면")
# plt.rcParams['font.family'] = 'Malgun Gothic'
# plt.rcParams['axes.unicode_minus'] = False

# data = pd.read_csv('./data1_20220731.csv',index_col=0)

# st.dataframe(data)
# st.table(data)
# #파이 차트를 그리기 위한 figure,axis 객체 생성
# fig,ax = plt.subplots()

# #열을 기준으로 파이차트 그리기 ax.pie (data['열 이름'])
# #-labels:인덱스 라벨로 사용 ax.pie (data['열 이름'],labels=data.index)
# #-autopct:퍼센트 표시형식 ax.pie (data['세대수'],labels=data.index,autopct='%1.1f%%')

# ax.pie(data['세대수'],labels=data.index,autopct='%1.1f%%')
# #차트의 형태를 일그러지지 않도록 축 비율을 동일하게 설정하는 옵션 추가
# ax.axis('equal')
# #완성된 차트 출력
# st.pyplot(fig)

#=======================================3교시==================================
# 1. uv add lxml
# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# url = 'https://www.index.go.kr/unity/potal/eNara/sub/showStblGams3.do?stts_cd=277002&idx_cd=2770&freq=Y&period=N'
# data= pd.read_html(url) #url로 데이터 받아오기
# df=data[0].drop(0) #데이터 전처리 인덱스 0으로 첫번째 인자 받아온 후 필요 없는 요소 제거
# df = df.drop("Unnamed: 1", axis=1) #전처리한 데이터 재공정 필요없는 부분 제거 후 재정렬.
# # print (df)
# data1=df.iloc[::2,:].set_index(keys="Unnamed: 0") 
# # print(data1)

# data2=data1.filter(items=["2021","2022","2023"]).transpose() #배열 items = [원하는 자료] 로 정제 
# st.dataframe(data2)

# st.title("암환자 사망 차트")
# plt.rcParams['font.family'] = 'Malgun Gothic' #한글문제 해결
# plt.rcParams['axes.unicode_minus'] = False

# st.dataframe(data2) 
# st.table(data2)
# fig, ax = plt.subplots()
# ax.pie(data2,labels=data2.index,autopct='%1.1f%%')
# ax.axis('equal')
# st.pyplot(fig)
# =========================================4교시 ====
# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# plt.rcParams['font.family'] = 'Malgun Gothic'
# plt.rcParams['axes.unicode_minus'] = False

# url="https://www.index.go.kr/unity/potal/eNara/sub/showStblGams3.do?stts_cd=277002&idx_cd=2770&freq=Y&period=N"
# data = pd.read_html(url)
# df = data[0].drop(0)
# df = df.drop("Unnamed: 1", axis=1)
# data1 = df.iloc[::2, :].set_index(keys="Unnamed: 0")
# st.dataframe(data1)


# #선택 년도 기본값.
# if 'slider_value' not in st.session_state:
#     st.session_state.slider_value = (2018, 2023)

# #차트 기본값
# if 'chart_value' not in st.session_state:
#     st.session_state.chart_value = pd.DataFrame([])
    
# #선택하는 슬라이더 추가.
# sd = st.slider(label="년도 범위지정",min_value=1989,max_value=2023,value=st.session_state.slider_value,step=1)

# def makeData():
#     st.dataframe(data1)
#     #선택된 데이터 전처리.
#     # data2 = data1.filter(items=st.session_state.slider_value).transpose()
#     # st.dataframe(st.session_state.chart_value)
#     st.dataframe(st.session_state.chart_value)
    
    
# if st.button("선택한 범위 확인"):
#     st.session_state.slider_value= sd
#     st.text(f"변경한 년도{st.session_state.slider_value}")
#     makeData()




# # fig, ax = plt.subplots()
# # ax.pie(data2.squeeze(), labels=data2.squeeze().index, autopct='%1.1f%%', startangle=90)
# # ax.axis('equal')
# # st.pyplot(fig)

#=================================강사 코드================================================
# import streamlit as st # 스트림릿 임포트 as st로 변경
# import pandas as pd #pandas 임포트 as pd 로 변경.
# import matplotlib.pyplot as plt #matlotlib 임포트 as plt로 변경.

# plt.rcParams['font.family'] = 'Malgun Gothic' #한글 문제 해결.
# plt.rcParams['axes.unicode_minus'] = False

# # 선택 년도 기본값
# if 'slider_value' not in st.session_state:
#   st.session_state.slider_value = (2019,2023)
# # 차트 기본값
# if 'chart_value' not in st.session_state:
#   st.session_state.chart_value = pd.DataFrame([])

# # 데이터 1차 전처리
# url = 'https://www.index.go.kr/unity/potal/eNara/sub/showStblGams3.do?stts_cd=277002&idx_cd=2770&freq=Y&period=N'
# data = pd.read_html(url) # url로 데이터 받아오기
# df = data[0].drop(0) #필요없는 부분 제거.
# df = df.drop("Unnamed: 1", axis=1) #재가공
# data1 = df.iloc[::2, :].set_index(keys="Unnamed: 0")
# # st.dataframe(data1)

# def makeData():
#   # st.dataframe(data1)
#   # 선택한 데이터 전처리
#   st.text(f"선택한 년도 {st.session_state.slider_value}") #선택한 년도 출력.
#   ty = st.session_state.slider_value 
#   arr = []#배열에 담아주기.
#   for y in range(ty[0], ty[1] + 1): # 반복문, 레인지로 범위 시작지점부터 끝부분 출력.
#     arr.append(str(y)) #배열에 문자열로 담아주기.
#   st.session_state.chart_value = data1.filter(items=arr).transpose()
#   st.dataframe(st.session_state.chart_value)
#   st.bar_chart(st.session_state.chart_value)

# # 선택 하는 슬라이더 추가
# sd = st.slider(label="년도 범위를 변경하세요.", min_value=1989, max_value=2023, value=st.session_state.slider_value, step=1)  
# if st.button("선택한 범위 확인"):
#   st.session_state.slider_value = sd
#   # st.text(f"변경한 년도 {st.session_state.slider_value}")
#   makeData()

#=====================================5교시 ======================================
# import streamlit as st # 스트림릿 임포트 as st로 변경
# import pandas as pd
# # 버튼 이벤트 
# btn = st. button("버튼") #버튼 이용방법

# #버튼을 사용할땐 조건문으로 작동.
# if btn:
#     #write 로 글자 작성을 할 수 있다.
#     st.write(":blue[집에가고싶다.]") #(: 색상 [내용]) 하면내용물의 색상이 변함.


# #데이터   
# df= pd.DataFrame({
#     "첫번째":[1,2,3,4,],
#     "두번째":[10,20,30,40,]
# })


# #파일 다운 버튼 이벤트
# st.download_button(
#     label= "csv다운", #버튼 이름
#     data=df.to_csv(), # 다운받는 데이터.
#     file_name="sample.csv", #다운받는 파일의 이름.
#     mime="text/csv" 
# )

# #요청 버튼 이벤트.
# with st.form(key="me"):
#     id=st.text_input("아이디")
#     pw=st.text_input("비밀번호")
#     sbtn = st.form_submit_button("호출")
    
# if sbtn:
#     st.success(f"확인:{id},{pw}")
    
    
# #선택 이벤트
# r = st.radio(
#     label="밥먹음?",
#     options=("먹음","안먹음","고민중"),
#     index=1
# )

# if r =="고민중":
#     st.text("결정장애쉨")
# elif r == "먹음":
#     st.text("돼지쉨")
# elif r == "안먹음":
#     st.text("몌루취셐")
    
# #선택 이벤트 2
# select = st.selectbox (
#     label="중식메뉴",
#     options=("짬뽕","짜장","탕수육"),
#     index=1

# )

# if select == "짬뽕":
#     st.text(" 여편네야 차돌짬뽕 하나 말아온나")
# elif select == "짜장":
#     st.text("애새기 입맛이네요")
# elif select == "탕수육":
#     st.text("부먹찍먹 가리지말고좀 쳐먹어라 씨발")
    
# #선택 이벤트3

# multi=st.multiselect(
#     "좋아하는 것은 무엇?",
#     ["#사과", "#배", "#망고"],
#     ["#사과"]
# )

# st.write(f"당신의 선택은: :green[{multi}]입니다]")
# #선택 이벤트4

# from datetime import datetime as dt
# import datetime

# 점심 = st.slider(
#     "점심 시간은 언제 좋을까요?",
#     min_value=dt(2024, 12, 5, 13, 20),
#     max_value=dt(2024, 12, 5, 14, 30),
#     value=dt(2024, 12, 5, 13, 30),
#     step=datetime.timedelta(minutes=10),
#     format="MM/DD/YY HH:mm"
# )
# st.write("선택한 시간:", 점심)
#==================================6교시

# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import datetime


# st.set_page_config(
#     page_title="2기"
#     page_icon=":sunglasses:"
    
# )

# st. markdown("<hi style='text=)


#============================원형 차트
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 1. 데이터 수집 및 전처리
url = 'https://www.index.go.kr/unity/potal/eNara/sub/showStblGams3.do?stts_cd=277002&idx_cd=2770&freq=Y&period=N'
data = pd.read_html(url)
df = data[0].drop(0)  # 첫 행 제거
df = df.drop("Unnamed: 1", axis=1)  # 불필요 열 제거
data1 = df.iloc[::2, :].set_index(keys="Unnamed: 0")  # 홀수 행만 추출 후 인덱스 설정

# 2. 원하는 연도 필터링 (2021~2023)
years = ["2021", "2022", "2023"]
data2 = data1.filter(items=years).transpose()

# 3. Streamlit 화면 출력
st.title("암 사망자 통계 (연도별 Pie Chart)")
st.dataframe(data2)

# 4. 연도별 Pie Chart 시각화
for year in data2.index:
    fig, ax = plt.subplots()
    ax.pie(data2.loc[year], 
           labels=data2.columns, 
           autopct='%1.1f%%', 
           startangle=90)
    ax.axis('equal')
    st.subheader(f" {year}년 암 사망자 비율")
    st.pyplot(fig)
