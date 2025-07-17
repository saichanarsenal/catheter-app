import streamlit as st

st.title("💉 自己導尿カテーテル支給シミュレーター（カナリハ・他院対応）")

# 使用パターン
usage_pattern = st.radio(
    "① 使用カテーテルの種類を選んでください",
    ("セルフカテーテルのみ", "ネラトンカテーテル使用（併用含む）")
)

# 使用月数
months = st.selectbox("② 何か月分希望ですか？", [1, 2, 3])

# 各物品の希望数（入力）
st.markdown("#### 各物品の希望数を入力してください")

num_self = st.number_input("セルフカテーテル（本）", min_value=0, step=1)

if usage_pattern == "セルフカテーテルのみ":
    num_neraton = 0
    st.markdown("※ ネラトンカテーテルは使用不可（セルフカテーテルのみ選択中）")
else:
    num_neraton = st.n_
