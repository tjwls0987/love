import tkinter as tk
import webbrowser

# 유튜브 링크 열기
def open_youtube():
    # 편지 텍스트 보여주기
    letter_text.config(state='normal')
    letter_text.insert(tk.END, "\n\n안녕, 이 편지를 읽고 있을 너에게.\n\n"
                               "오늘도 수고 많았어. 누구보다 열심히 살아가고 있는 너를 응원해!\n"
                               "때로는 지치고 외로울 수도 있지만, 너는 절대 혼자가 아니야.\n\n"
                               "세상엔 너를 아끼는 마음이 분명히 존재해.\n"
                               "앞으로도 계속 빛나는 네 길을 응원할게.\n\n"
                               "- 너를 응원하는 마음으로부터 💌")
    letter_text.config(state='disabled')

    # 유튜브 링크 열기
    youtube_url = "https://youtu.be/5gR8kqgv9oc?si=VqSPu9CrkV_e0LrG"  # 유튜브 영상 링크
    webbrowser.open(youtube_url)  # 기본 웹 브라우저에서 유튜브 링크를 열어줍니다.

# Tkinter 윈도우 설정
root = tk.Tk()
root.title("편지 💌")  # 윈도우의 제목
root.geometry("500x600")  # 윈도우의 크기
root.configure(bg="#fff9f0")  # 배경 색상

# 제목 라벨
title = tk.Label(root, text="💌 너에게 보내는 편지 💌", font=("헬로키티", 18, "bold"), bg="#fff9f0")
title.pack(pady=20)

# 편지 텍스트 박스
letter_text = tk.Text(root, width=50, height=20, font=("헬로키티", 12), wrap=tk.WORD, state='disabled')
letter_text.pack(pady=20)

# 버튼 클릭 시 편지와 유튜브 링크를 실행
open_button = tk.Button(root, text="응원메세지가 도착했습니다❤", font=("맑은 고딕", 14), command=open_youtube, bg="#ffcccc")
open_button.pack(pady=10)

# Tkinter 이벤트 루프 시작
root.mainloop()
