import streamlit as st

# 模擬分類資料
keywords = {
    "蘋果": ["蘋果", "富士", "青森蜜"],
    "小白菜": ["小白菜", "有機小白菜", "蚵白菜"]
    # ... 加上更多
}

def identify(product_name):
    for variety, keys in keywords.items():
        if any(k in product_name for k in keys):
            return variety
    return "無法判斷"

# Streamlit 介面
st.title("蔬果品名分類器")
user_input = st.text_input("請輸入品名：")

if user_input:
    result = identify(user_input)
    st.success(f"判斷結果：{result}")
