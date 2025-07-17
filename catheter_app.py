import streamlit as st

st.title("💉 自己導尿カテーテル支給シミュレーター（改良版）")

# 使用パターン
usage_pattern = st.radio(
    "① セルフカテーテルだけですか？",
    ("セルフカテーテルのみ", "ネラトン併用", "ネラトンのみ")
)

# 使用月数
months = st.selectbox("② 何か月分希望ですか？", [1, 2, 3])

# 単価設定
price_self = 2000
price_neraton = 800
price_bc = 860  # ← 修正済み

# 支給上限額
limit_per_month = 4000 if usage_pattern == "セルフカテーテルのみ" else 10000
limit_total = limit_per_month * months

# 入力フォーム
st.markdown("#### 各物品の希望本数を入力してください")

# 初期値をゼロにする（条件付き）
num_self = st.number_input("セルフカテーテル（1本 2000円）", min_value=0, step=1)

if usage_pattern == "セルフカテーテルのみ":
    num_neraton = 0
    st.markdown("ネラトンカテーテルは使用不可（セルフカテーテルのみを選択）")
else:
    num_neraton = st.number_input("ネラトンカテーテル（1本 800円）", min_value=1, step=1)

num_bc = st.number_input("グリセリンBC（1本 860円）", min_value=0, step=1)

# 支給可能性の条件判定
if usage_pattern == "セルフカテーテルのみ" and num_neraton > 0:
    status = "❌ セルフカテーテルのみを選んでいる場合は、ネラトンは使用できません。"
    feasible = False
elif usage_pattern in ["ネラトン併用", "ネラトンのみ"] and num_neraton == 0:
    status = "❌ ネラトンが0本のため、支給対象外です。"
    feasible = False
else:
    # コスト計算
    total_cost = num_self * price_self + num_neraton * price_neraton + num_bc * price_bc
    profit = limit_total - total_cost
    feasible = profit >= 0
    status = "✅ 支給可能" if feasible else "❌ 支給不可能"

# 表示
if st.button("結果を表示"):
    st.subheader("🧾 判定結果")
    st.write(f"使用パターン: {usage_pattern}")
    st.write(f"使用期間: {months}か月")
    st.write(f"支給限度額: {limit_total:,} 円")

    if feasible:
        st.write(f"総原価: {total_cost:,} 円")
        st.write(f"利益: {profit:,} 円")
    st.markdown(f"### {status}")
