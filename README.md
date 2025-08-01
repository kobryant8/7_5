# 7_5
# 0801📘 오늘 수업 요약 (2000자 이내)

오늘은 Pandas, Matplotlib, Streamlit을 활용한 데이터 시각화 실습을 진행함.

✅ 1~2교시: 데이터 분석 및 기본 시각화
- uv init → uv add pandas matplotlib streamlit
- pd.read_csv()로 csv 파일 불러오기
- .plot(kind='line'/'bar'/'hist'/'scatter'/'pie')로 다양한 그래프 그리기
- 마커(marker), 라인스타일, 색상 지정 등 시각화 옵션 실습
- matplotlib 한글 폰트 문제 해결: Malgun Gothic

✅ 3~4교시: 웹 데이터 수집 및 파이차트 시각화
- pd.read_html()로 e나라지표 통계 데이터 불러오기
- .drop(), .iloc[::2], .set_index()로 전처리
- 특정 연도 필터링 후 .transpose()로 시계열 구성
- Streamlit st.dataframe(), st.table(), plt.subplots()로 pie chart 구현
- 연도별 사망자 비율 시각화

✅ 5교시: Streamlit UI 구성 요소 실습
- st.button(), st.text_input(), st.radio(), st.selectbox(), st.multiselect()
- st.form()으로 로그인 폼 구성 → st.success() 출력
- st.download_button()으로 DataFrame csv 다운로드 구현

✅ 6교시: 페이지 설정 및 고급 위젯
- st.set_page_config()으로 제목, 아이콘 설정
- datetime slider로 시간 선택 UI 구성
- HTML 마크업을 통한 텍스트 커스터마이징 시도

🎯 핵심: 웹에서 데이터 수집 → 전처리 → 분석 → 시각화 → Streamlit 대시보드 구성까지의 전체 흐름 실습

오늘 수업을 통해 단순 데이터 출력이 아니라, 데이터 기반의 사용자 친화적 시각화 웹앱 제작이 가능해졌음.

📘 오늘 수업에서 꼭 알아야 할 추가 개념 요약

1️⃣ index_col vs set_index 차이
# CSV 읽을 때 바로 인덱스 지정
df = pd.read_csv('file.csv', index_col=0)

# 읽은 후 나중에 인덱스 지정
df = pd.read_csv('file.csv')
df = df.set_index('컬럼명')

2️⃣ .transpose() 사용 이유
# 열 ↔ 행 구조 전환 (예: 연도별 데이터를 행으로 만들 때)
data2 = data1.filter(items=["2021", "2022", "2023"]).transpose()

3️⃣ Streamlit session_state 사용
# 사용자 선택값을 기억하는 저장소
if 'slider_value' not in st.session_state:
    st.session_state.slider_value = (2019, 2023)

# 슬라이더와 버튼 연동
slider = st.slider("년도 범위", 1980, 2023, value=st.session_state.slider_value)
if st.button("확인"):
    st.session_state.slider_value = slider

4️⃣ Pie Chart에서 squeeze 사용
# 행이 1개인 DataFrame → Series로 바꿔야 pie가 그려짐
fig, ax = plt.subplots()
ax.pie(data2.loc["2023"].squeeze(), labels=data2.columns, autopct='%1.1f%%')

5️⃣ 파일 다운로드 시 MIME 설정
# 브라우저가 csv 형식으로 정확히 인식하게 해줌
st.download_button(
    label="CSV 다운로드",
    data=df.to_csv(),
    file_name="data.csv",
    mime="text/csv"
)