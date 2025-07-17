import streamlit as st

def check_feasibility(catheter_type, unit, quantity):
    if catheter_type == 'セルフ':
        unit_price = 2000
        max_price = 4000
    elif catheter_type == 'ネラトン':
        unit_price = 10
        max_price = 10000
    else:
        return "無効なカテーテルタイプです"

    if unit == '箱':
        if catheter_type == 'ネラトン':
            quantity *= 50
        else:
            return "セルフには箱指定はできません"

    cost = quantity * unit_price
    profit = max_price - cost

    result = "可能" if profit >= 0 else "不可能"
    return {
        "使用カテーテル": catheter_type,
        "数量（本）": quantity,
        "総原価（円）": cost,
        "点数収入（円）": max_price,
        "利益（円）": profit,
        "結果": result
    }

st.title("💉 自己導尿カテーテル支給シミュレーター")

catheter_type = st.selectbox("カテーテルの種類を選んでください", ["セルフ", "ネラトン"])
unit_input = st.selectbox("入力方法を選んでください", ["1日あたりの導尿回数", "月あたりの本数", "月あたりの箱数"])

if unit_input == "1日あたりの導尿回数":
    daily_count = st.number_input("1日の導尿回数", min_value=1, max_value=20, step=1)
    quantity = daily_count * 30
    unit = "本"
elif unit_input == "月あたりの本数":
    quantity = st.number_input("1ヶ月の本数", min_value=1, step=1)
    unit = "本"
else:
    quantity = st.number_input("1ヶ月の箱数（50本/箱）", min_value=1, step=1)
    unit = "箱"

if st.button("結果を表示"):
    result = check_feasibility(catheter_type, unit, int(quantity))
    if isinstance(result, dict):
        st.subheader("🧾 支給判定")
        for key, value in result.items():
            st.write(f"**{key}**: {value}")
    else:
        st.error(result)
