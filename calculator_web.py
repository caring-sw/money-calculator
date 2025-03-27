import streamlit as st

st.set_page_config(page_title="금전 ↔ 현금 계산기", page_icon="💰")

st.title("🎮 금전 ↔ 현금 계산기")

# 시세 입력
rate = st.number_input("💱 금전 100만원당 현금 시세 (원)", min_value=1.0, value=150.0)

# 모드 선택
mode = st.radio("계산 모드 선택", ["금전 → 현금", "현금 → 금전"])

# 입력 값
if mode == "금전 → 현금":
    gm = st.number_input("💰 내가 가진 금전 (예: 30000000)", min_value=0)
    if gm:
        result = (gm / 1_000_000) * rate
        st.success(f"💵 현금으로 약 {result:,.0f}원입니다.")
else:
    cash = st.number_input("💵 내가 원하는 현금 (예: 10000)", min_value=0.0)
    if cash:
        result = (cash / rate) * 1_000_000
        st.success(f"💰 필요한 금전은 약 {result:,.0f}원입니다.")
