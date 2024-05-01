import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# データの読み込み
@st.cache
def load_data():
    # ダミーデータを読み込む例
    data = pd.read_csv("StressLevelDataset_filtered.xlsx")
import pandas as pd
from sklearn.ensemble import RandomForestRegressor


# 特徴量の重要度を計算する関数
def calculate_feature_importance(data):
    X = data.drop(columns=["target_column"])  # 特徴量
    y = data["target_column"]  # ターゲット変数

    # ランダムフォレストモデルを初期化して学習
    model = RandomForestRegressor()
    model.fit(X, y)

    # 特徴量の重要度を取得
    feature_importance = model.feature_importances_

    return feature_importance

# 倍率を計算する関数
def calculate_multiplier(feature_importance, user_input):
    multiplier = 1
    for i, importance in enumerate(feature_importance):
        multiplier *= user_input[i] ** importance
    return multiplier

def main():
    st.title("Feature Importance Multiplier Calculator")

    # データの読み込み
    data = load_data()

    # 特徴量の重要度を計算
    feature_importance = calculate_feature_importance(data)

    # ユーザーが設定する特徴量の値
    user_input = []
    for i in range(len(feature_importance)):
        user_input.append(st.slider(f"Feature {i+1}", min_value=0.0, max_value=10.0, value=5.0))

    # 倍率を計算
    multiplier = calculate_multiplier(feature_importance, user_input)

    # 結果を表示
    st.write(f"Multiplier: {multiplier}")

if __name__ == "__main__":
    main()
