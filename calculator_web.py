import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="💰 시세 비교 계산기", page_icon="💸")

st.title("💸 금전 ↔ 현금 시세 비교 계산기")

# 금전 or 현금 입력 선택
mode = st.radio("계산 모드 선택", ["금전 → 현금", "현금 → 금전"])

# 시세 입력 (최대 5개)
st.markdown("### 📊 비교할 시세 입력 (100만원당 현금)")
rate_inputs = []
num_rates = st.slider("비교할 시세 수", 1, 5, 3)

for i in range(num_rates):
    rate = st.number_input(f"시세 {i+1} (예: 150)", min_value=1.0, value=150.0 + i * 10)
    rate_inputs.append(rate)

# 계산 기준 값 입력
if mode == "금전 → 현금":
    gm = st.number_input("💰 내가 가진 금전 (원)", min_value=0.0, value=30_000_000.0, step=100000.0)
    results = [(gm / 1_000_000) * r for r in rate_inputs]
    df = pd.DataFrame({
        "시세 (100만당 현금)": rate_inputs,
        "계산된 현금 (원)": results
    })
else:
    cash = st.number_input("💵 내가 원하는 현금 (원)", min_value=0.0, value=10_000.0, step=1000.0)
    results = [(cash / r) * 1_000_000 for r in rate_inputs]
    df = pd.DataFrame({
        "시세 (100만당 현금)": rate_inputs,
        "필요한 금전 (원)": results
    })

# 결과 출력
st.markdown("### 📋 계산 결과")
st.dataframe(df.style.format("{:,.0f}"))

# 그래프 출력
st.markdown("### 📈 시각화")
fig, ax = plt.subplots()
if mode == "금전 → 현금":
    ax.bar([str(r) for r in rate_inputs], results, color="green")
    ax.set_ylabel("얻는 현금 (원)")
else:
    ax.bar([str(r) for r in rate_inputs], results, color="blue")
    ax.set_ylabel("필요한 금전 (원)")
ax.set_xlabel("시세 (100만당)")
ax.set_title("시세 비교 결과")
st.pyplot(fig)

st.markdown("---")
st.caption("ⓒ 2024. 시세 비교 계산기 made with ❤️ by caring-sw")
