import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="금전 ↔ 현금 계산기",
    page_icon="💰",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 스타일 커스터마이징
st.markdown("""
    <style>
    /* 전체 페이지 배경 색상 */
    .stApp {
        background-color: #f0f2f6;
    }
    /* 타이틀 텍스트 색상 및 정렬 */
    .stApp h1 {
        color: #ff4b4b;
        text-align: center;
    }
    /* 입력 위젯 스타일 */
    .stNumberInput>div>div>input {
        border-radius: 10px;
        border: 1px solid #ff4b4b;
    }
    /* 라디오 버튼 스타일 */
    .stRadio>div>label {
        color: #ff4b4b;
    }
    /* 버튼 스타일 */
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        border: none;
    }
    .stButton>button:hover {
        background-color: #ff6b6b;
    }
    /* 결과 메시지 스타일 */
    .stSuccess {
        background-color: #d4edda;
        color: #155724;
        border-radius: 10px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 앱 제목
st.title("🎮 금전 ↔ 현금 계산기")

# 시세 입력
rate = st.number_input("💱 금전 100만원당 시세 (원)", min_value=1.0, value=150.0, step=1.0)

# 모드 선택
mode = st.radio("계산 모드 선택", ["금전 → 현금", "현금 → 금전"])

# 입력 및 계산
if mode == "금전 → 현금":
    gm = st.number_input("💰 내가 가진 금전 (원)", min_value=0.0, value=0.0, step=1.0)
    if gm:
        result = (gm / 1_000_000) * rate
        st.success(f"💵 현금으로 약 {result:,.0f}원입니다.")
else:
    cash = st.number_input("💵 내가 원하는 현금 (원)", min_value=0.0, value=0.0, step=1.0)
    if cash:
        result = (cash / rate) * 1_000_000
        st.success(f"💰 필요한 금전은 약 {result:,.0f}원입니다.")
