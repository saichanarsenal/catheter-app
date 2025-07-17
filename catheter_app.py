import streamlit as st

st.title("💉 自己導尿カテーテル支給シミュレーター（再改良版）")

# 使用パターン（2択）
usage_pattern = st.radio(
    "① 使用カテーテルの種類を選んでください",
    ("セルフカテーテルのみ", "ネラトンカテーテル使用（併用含む）")
)

# 使用月数（1〜3）
months = st.selectbox("② 何か月分希望ですか？", [1, 2, 3])

# 単価設定
price_self = 2000
price_neraton = 800
price_bc = 860
price_balloon = 8100  # ← 追加項目

# 支給限度額（月あたり）
limit_per_month = 4000 if usage
