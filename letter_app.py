import streamlit as st
import webbrowser

# Streamlit 앱 UI
st.set_page_config(page_title="편지 💌", page_icon="💌", layout="centered")
st.markdown(
    "<h2 style='text-align: center; color: #ff6f61;'>💌 너에게 보내는 편지 💌</h2>", unsafe_allow_html=True
)

# 버튼 클릭 시 편지 내용과 유튜브 링크 출력
if st.button("응원메세지가 도착했습니다❤"):
    st.write(
        """
        안녕, 이 편지를 읽고 있을 너에게.  
        
        오늘도 수고 많았어. 누구보다 열심히 살아가고 있는 너를 응원해!  
        때로는 지치고 외로울 수도 있지만, 너는 절대 혼자가 아니야.  
        
        세상엔 너를 아끼는 마음이 분명히 존재해.  
        앞으로도 계속 빛나는 네 길을 응원할게.  
        
        - 너를 응원하는 마음으로부터 💌
        """
    )

    youtube_url = "https://youtu.be/5gR8kqgv9oc?si=VqSPu9CrkV_e0LrG"
    st.markdown(f"[💖 응원 영상 보러가기]({youtube_url})", unsafe_allow_html=True)
