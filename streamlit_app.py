import streamlit as st
import numpy as np

# データの仮定された特徴量重要度
feature_importances = {
    'Workload': 0.2,
    'Relationships': 0.15,
    'Health': 0.1,
    'Environment': 0.1,
    'Financial': 0.08,
    'Family': 0.07,
    'Work-life balance': 0.06,
    'Social': 0.05,
    'Personal Growth': 0.05,
    'Time Pressure': 0.1,
    'Uncertainty': 0.04
}

# 加重平均を計算する関数
def calculate_stress_level(answers, feature_importances):
    total_weight = sum(feature_importances.values())
    stress_level = sum(answers[feature] * weight for feature, weight in feature_importances.items()) / total_weight
    return stress_level

# Streamlitアプリケーションの作成
def main():
    st.title("Stress Level Calculator")

    # 回答データの入力
    st.subheader("Enter Your Answers:")
    answers = {}
    for feature in feature_importances.keys():
        answer = st.slider(f"{feature} (1: Very Bad, 5: Very Good)", 1, 5, 3)
        answers[feature] = answer

    # ストレスレベルの計算
    stress_level = calculate_stress_level(answers, feature_importances)

    # 結果の表示
    st.subheader("Your Stress Level:")
    st.write(f"Your stress level is: {stress_level:.2f}")

# アプリケーションの実行
if __name__ == "__main__":
    main()
