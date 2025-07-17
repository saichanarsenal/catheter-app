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
    num_neraton = st.number_input("ネラトンカテーテル（箱）", min_value=1, step=1)

num_bc = st.number_input("グリセリンBC（本）", min_value=0, step=1)
num_balloon = st.number_input("間欠バルーン（本）", min_value=0, step=1)

# 院別単価（カナリハと他院）
prices_kanariha = {
    "self": 2000,
    "neraton": 800,
    "bc": 860,
    "balloon": 8100
}

prices_other = {
    "self": 3200,
    "neraton": 3200,  # 箱あたり
    "bc": 1300,
    "balloon": 12000
}

# 支給上限額
limit_per_month = 4000 if usage_pattern == "セルフカテーテルのみ" else 10000
limit_total = limit_per_month * months

# 支給条件チェック（共通）
if usage_pattern == "セルフカテーテルのみ" and num_neraton > 0:
    result_kanariha = "❌ セルフカテーテルのみの場合、ネラトンは使用できません。"
    result_other = result_kanariha
elif usage_pattern == "ネラトンカテーテル使用（併用含む）" and num_neraton == 0:
    result_kanariha = "❌ ネラトンが0箱のため、支給対象外です。"
    result_other = result_kanariha
else:
    # カナリハ価格での原価計算
    cost_kanariha = (
        num_self * prices_kanariha["self"] +
        num_neraton * prices_kanariha["neraton"] +
        num_bc * prices_kanariha["bc"] +
        num_balloon * prices_kanariha["balloon"]
    )
    profit_kanariha = limit_total - cost_kanariha
    result_kanariha = "✅ カナリハなら支給可能" if profit_kanariha >= 0 else "❌ カナリハでは支給不可"

    # 他院価格での原価計算
    cost_other = (
        num_self * prices_other["self"] +
        num_neraton * prices_other["neraton"] +
        num_bc * prices_other["bc"] +
        num_balloon * prices_other["balloon"]
    )
    profit_other = limit_total - cost_other
    result_other = "✅ 他院でも支給可能" if profit_other >= 0 else "❌ 他院では支給不可"

# 結果表示
if st.button("結果を表示"):
    st.subheader("🧾 判定結果")
    st.write(f"使用パターン: {usage_pattern}")
    st.write(f"使用期間: {months}か月")
    st.write(f"支給限度額: {limit_total:,} 円")

    st.markdown("### 【カナリハの場合】")
    st.write(f"総原価: {cost_kanariha:,} 円")
    st.write(f"利益: {profit_kanariha:,} 円")
    st.markdown(f"**{result_kanariha}**")

    st.markdown("---")

    st.markdown("### 【他院の場合】")
    st.write(f"総原価: {cost_other:,} 円")
    st.write(f"利益: {profit_other:,} 円")
    st.markdown(f"**{result_other}**")
