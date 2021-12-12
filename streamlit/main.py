import streamlit as st

st.markdown("""
セクション4

- 流れ
    - Pythonの型ヒント
    - GET,POSTメソッドに対応したAPI開発
    - バリデーション
- Python3.5から型に関する注釈をつけることが出てきた
- HTTPメソッドは、オペレータと呼ぶ
- URLを叩く ＝ HTTPのGetメソッドを使っている
- SwaggerUI
    - APIの仕様書をWebページ上で見やすく表示するツール
    - FastAPIは自動的にSwaggerUIを用いた、APIの仕様書ドキュメントを生成してくれる
        - 型ヒントをベースにドキュメントが生成される
            - 裏で型チェックにはPydanticが動いているから
    - ドキュメントの確認は`/docs` か`/redoc` で確認できる
- パスパラメータ

```python
@app.get("/countries/{country_name}")
async def country(country_name: int):
    return {"message" : country_name}
```

[Javaがオワコンではなく学ぶ価値がある8つの理由 | dawaan](https://dawaan.com/java-is-still-worth-learning-2020/)
""")

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

agree = st.checkbox('I agree')
if agree:
    st.write('Great!')

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)

color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)