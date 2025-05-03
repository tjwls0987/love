import streamlit as st
import base64

# 1. 헬로키티 폰트 파일 로드 및 스타일 적용
def load_hellokitty_font():
    font_path = "./헬로키티체.ttf"  # 업로드한 폰트 파일 경로
    with open(font_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
        return f"""
        <style>
        @font-face {{
            font-family: 'HelloKitty';
            src: url(data:font/ttf;base64,{encoded}) format('truetype');
        }}
        .hellokitty {{
            font-family: 'HelloKitty', cursive;
            font-size: 20px;
            color: #ff6f91;
            line-height: 1.8;
            white-space: pre-wrap;
        }}
        </style>
        """

# 2. 페이지 설정 및 스타일 적용
st.set_page_config(page_title="편지 💌", page_icon="💌", layout="centered")
st.markdown(load_hellokitty_font(), unsafe_allow_html=True)

# 3. 제목 출력
st.markdown("<h2 class='hellokitty'>💌 너에게 보내는 편지 💌</h2>", unsafe_allow_html=True)

# 4. 버튼 클릭 시 편지와 유튜브 링크 출력
if st.button("응원메세지가 도착했습니다❤"):
    st.markdown(
        """
        <div class='hellokitty'>
        안녕, 이 편지를 읽고 있을 너에게.

        오늘도 수고 많았어. 누구보다 열심히 살아가고 있는 너를 응원해!
        때로는 지치고 외로울 수도 있지만, 너는 절대 혼자가 아니야.

        세상엔 너를 아끼는 마음이 분명히 존재해.
        앞으로도 계속 빛나는 네 길을 응원할게.

        - 너를 응원하는 마음으로부터 💌
        </div>
        """, unsafe_allow_html=True
    )

    st.markdown("[💖 응원 영상 보러가기](https://youtu.be/5gR8kqgv9oc?si=VqSPu9CrkV_e0LrG)", unsafe_allow_html=True)
