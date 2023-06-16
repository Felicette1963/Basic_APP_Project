import streamlit as st

class streamlit_HTML:
    Video_Wild_Fire_link = 'https://www.youtube.com/watch?v=40m1qT8D5Is'
    Vido_Wild_Fire_lyrics = '''
        Wrapped in biting wind
        
        살을 에는 듯한 바람에 휩싸여도
        
        Hearts will never bleed
        
        심장은 피를 흘리지 않지
        
        Frozen and banished
        
        얼어붙고 추방되어
        
        Out of grief
        
        슬픔에서 벗어나
        
        In their restless dreams
        
        쉴 틈 없는 꿈속에서
        
        They try so hard to breathe
        
        그들은 힘겹게 숨을 쉬려 하지
        
        Pulses flutter and sting
        
        맥박이 고동치며 아파와
        
        Within this bleakness
        
        이 황량함 속에서
        
        (Ah, ah)
        
        Pain will come with the blade
        
        고통은 칼날과 함께 찾아와
        
        Pain will wake up the despondent crowd
        
        고통이 절망한 군중을 일으킬 거야
        
        In this dormant world somehow
        
        이 잠든 세계에서 말이지
        
        Unsheathe a sword not to kill
        
        살육을 위해 검을 뽑는 게 아닌
        
        Unsheathe a sword to rend those clouds above the ground
        
        땅 위의 저 구름들을 가르기 위해 검을 뽑아
        
        Wake up, it's time to gather now
        
        일어나, 이젠 모일 시간이야
        
        The only warmth remains
        
        온기가 남아있는 곳은 오직
        
        In hands clasped so tight
        
        꽉 쥔 손 안밖에 없고
        
        The only fire exists
        
        불이 존재하는 곳은 오직
        
        In brave hearts
        
        용감한 자들의 마음뿐
        
        Seasons that refuse
        
        계절들은 거절했지
        
        To change over the years
        
        세월이 지나면서 바뀌기를
        
        Will find their way back
        
        그들은 제 갈 길을 찾아
        
        Back on track
        
        다시 궤도에 오를 거야
        
        (Oh, oh, oh)
        
        We've made a choice, go fight against your fate!
        
        우린 선택을 내렸어, 가서 네 운명에 맞서 싸워!
        
        Pain will come with the blade
        
        고통은 칼날과 함께 찾아와
        
        Pain will wake up the despondent crowd
        
        고통이 절망한 군중을 일으킬 거야
        
        In this dormant world somehow
        
        이 잠든 세계에서 말이지
        
        Unsheathe a sword not to kill
        
        살육을 위해 검을 뽑는 게 아닌
        
        Unsheathe a sword to rend those clouds above the ground
        
        땅 위의 저 구름들을 가르기 위해 검을 뽑아
        
        Wake up, it's time to gather now
        
        일어나, 이젠 모일 시간이야
        
        Forget about the rules written on weathered rock
        
        낡은 바위에 써져 있는 규칙 따윈 잊어버려
        
        There were chasers of light
        
        그들은 빛을 좇는 이들이었지
        
        Find the way or get lost
        
        길을 찾거나 헤매거나
        
        We have no way to know
        
        우린 알 길이 없지
        
        Where they all headed for
        
        그들이 다 어디로 떠나버렸는지
        
        See the light from afar
        
        멀리서 빛을 바라봐
        
        Just blaze through the thorns
        
        그냥 가시덤불을 빨리 뚫고 지나가
        
        We know it's right over there
        
        우린 그것이 거기에 있다는 걸 알지
        
        We have something to declare
        
        선언할 것이 있어
        
        Whatever is arriving, we'll be prepared
        
        무엇이 도착하든 간에 우린 준비되어 있을 거야
        
        We've made a choice, go fight against your fate!
        
        우린 선택을 내렸어, 가서 네 운명에 맞서 싸워!
        
        Pain will come with the blade
        
        고통은 칼날과 함께 찾아와
        
        Pain will wake up the despondent crowd
        
        고통이 절망한 군중을 일으킬 거야
        
        In this dormant world somehow
        
        이 잠든 세계에서 말이지
        
        Unsheathe a sword not to kill
        
        살육을 위해 검을 뽑는 게 아닌
        
        Unsheathe a sword to rend those clouds above the ground
        
        땅 위의 저 구름들을 가르기 위해 검을 뽑아
        
        Wake up to hear the cheering sound
        
        일어나서 저 환호소리를 들어
        
    '''
    Img_Path = "Image/"
    def __init__(self):
        self.streamlit_label("이미지와 동영상");
        self.stream_Img();
        self.streamlit_head("붕괴:스타레일 OST 목록");
        self.streamlit_Video(
            "Wild Fire",
            self.Video_Wild_Fire_link,
            self.Vido_Wild_Fire_lyrics
        );
        self.stream_Test_Text_size()
        self.stream_Layout();
        self.stream_Link()
        self.stream_sk();
        self.stream_componunt()
        self.stream_input()

    def streamlit_head(self, title_name):
        st.title(title_name)
    def streamlit_label(self, sub_title):
        st.divider()
        st.subheader(sub_title)

    def streamlit_Video(self, head, video_link, lyrics):
        st.subheader(head);
        st.video(video_link)
        st.write(lyrics)

    def stream_Img(self):
        st.image(self.Img_Path + "title.png", use_column_width=True)

    def stream_Test_Text_size(self):
        self.streamlit_label("글씨 크기");
        # 제목 마크 다운
        st.write("""
        # 가장 큰 제목 (h1 - headline1 - st.title)
        ## 그 다음 큰 제목 (h2 - headline2 - st.header)
        ### 그것보단 작은 제목 <- 대부분 여기까지만 씀 (h3 - headline3 - st.subheader)
        #### 좀 더 작은 제목 (h4)
        ##### 이건 없겠지? (h5)
        ###### 이것도 있나? (h6)
        ####### 이건 없어.
        """)
        self.streamlit_label("서식");
        text = """
        기울임 : *별표* 또는 _언더바_ 하나씩 써주면

        진하게(bold) : **별표**를 또는 __언더바__ 두개씩 써주면

        기울임 + 진하게(bold) : ***별표***를 또는 ___언더바___ 세개씩 써주면

        취소선 : ~물결표~

        밑줄 : <u>밑줄</u>

        형광펜 : <mark>형광펜</mark>
        """
        # st.write(text)
        # 태그를 허용하는 옵션
        st.markdown(text, unsafe_allow_html=True)

    def stream_Layout(self):
        st.write("""
            #### 순서가 없는 리스트
            * 별표를 여백 1칸 이상과 사용하면 순서가 없는 리스트
            * 별표를 여백 1칸 이상과 사용하면 순서가 없는 리스트
            * 별표를 여백 1칸 이상과 사용하면 순서가 없는 리스트
                * 들여쓰기1
                    * 들여쓰기2
                        * 들여쓰기3
            - (-)를 여백 1칸 이상과 사용하면 순서가 없는 리스트
            - (-)를 여백 1칸 이상과 사용하면 순서가 없는 리스트
            - (-)를 여백 1칸 이상과 사용하면 순서가 없는 리스트
                - 들여쓰기1
                    - 들여쓰기2
                        - 들여쓰기3
        """)
        st.write("""
            #### 순서가 있는 리스트
            1. 순서가
            2. 있는
            4. 리스트 - 숫자를 건너 뛰어도 무시하고 순서를 따름
                1. 들여쓰기1
                    1. 들여쓰기2 # 1로 시작하지 않으면 들여쓰기는 무시
                        1. 들여쓰기3
            1. 순서가
            1. 1로 넣어도
            1. 증가됨
            ### 가로줄
            ---
            (---)
            ___
            (___)
            ### 테이블(표)
            |이름|직업|
            |-----|---|
            |파이썬|백수|
            |자바|일잘러|
        """)

    def stream_Link(self):
        # 링크
        self.streamlit_label("링크")
        l1 = "https://naver.com"
        l2 = "https://cdn.pixabay.com/photo/2023/04/08/18/01/flower-7909902_640.jpg"
        st.write(f"""
            * [표시할 텍스트](https://naver.com)
            * [표시할 텍스트]({l1})
            * ![이미지에 대한 설명](https://cdn.pixabay.com/photo/2023/04/08/18/01/flower-7909902_640.jpg)
            * ![이미지에 대한 설명]({l2})
            * [![이미지에 대한 설명](https://cdn.pixabay.com/photo/2023/04/08/18/01/flower-7909902_640.jpg)](https://naver.com)
        """)

    def stream_sk(self):
        # 인용
        self.streamlit_label("인용")
        st.write(f"""
            > 무언가 멋진 말 - 유명한 사람


            > 진입장벽은 수익이다 - 어느 코딩 강사

            책이나, 사람말 인용할 때...
            > 인용 첫줄
            > > 인용문 안에 인용임

            #### 코드
            `코드를 나타낼 때 주로 쓰이는 묶음 표시 (한줄)`
            ```
            여러 줄로 코드를 나타내고
            줄바꿈도 반영하고 싶으면...
            print("파이썬!")
            ```
            ```python
            print("파이썬!")
            ```
        """)

    def stream_componunt(self):
        self.streamlit_label("컴포넌트")
        # 위-아래로 한 줄로만....
        st.write("👨🏿‍🔬")
        cols = st.columns(2)  # 컬럼 리스트
        cols[0].write("👨🏿‍🔬")
        cols[1].write("👨🏿‍🔬")
        cols = st.columns(3)
        # 🐦 -> n등분 -> 3등분
        cols[0].write("🐦")
        cols[1].write("🐦")
        cols[-1].write("🐦")
        cols = cols[0].columns(3)  # 열의 열인 거임
        cols[0].write("🐦")
        cols[1].write("🐦")
        cols[-1].write("🐦")

        col1, col2 = st.columns(2)  # 리스트 언패킹
        col1.write("왼쪽 열")
        col2.write("오른쪽 열")

        with col1:  # col1을 기준으로 streamlit을 써주겠다
            # 블록 (:) 을 열면 -> 이 안에서는 streamlit 기능 실행시 col1에 종속
            st.write("왼쪽")
        with col2:  # col2을 기준으로 streamlit을 써주겠다
            # 블록 (:) 을 열면 -> 이 안에서는 streamlit 기능 실행시 col2에 종속
            st.write("오른쪽")

        # tabs = st.tabs(["김치찌개", "된장찌개", "로제마라어묵찌개"])
        tab_menus = ["김치찌개", "된장찌개", "로제마라어묵찌개"]
        tab1, tab2, tab3 = st.tabs(tab_menus)
        img1 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ4MFBhxEu7tdtEmSpJ-DEzVl9si8NYOiYmbruRyOr7vYS8ZMLSpu60YsPo5WtmB5xg_F0&usqp=CAU"
        tab1.image(img1)
        with tab2:
            img2 = "https://imagescdn.gettyimagesbank.com/500/201708/jv10940386.jpg"
            st.image(img2)
        tab3.write("이런 건 없어요... 상상도 마라요")

        exp = st.expander("Surprise!!!", expanded=False)
        exp.image(
            "https://i.namu.wiki/i/5lWwYGj-VC8ZqJxug7Exm5-7rHE97fdZui3DWEAjm0zdLiBCbcdw4mLyGhcbZ_KecZOQr4rtwNJSFs63Rsdd_Q.webp")
        # with exp: ...

    def stream_input(self):
        # 입력
        self.streamlit_label("입력")
        name = st.text_input("나의 이름은")  # 변수로 받을 수 있음
        name2 = st.text_input("너의 이름은")  # 변수로 받을 수 있음
        # st.text_input("")
        # st.write(name)
        # st.write(name2)
        st.write(f"신랑 {name}과 신부 {name2}는...")
        # number = st.number_input("당신의 나이는?")
        age = st.number_input("당신의 나이는?", step=1)
        st.write(f"나의 나이는 {age}세")
        height = st.number_input("당신의 키는?", step=0.1)
        st.write(f"나의 키는 {height}cm")

        st.divider()
        mode = st.checkbox("강사님 잔소리모드")  # bool (T/F)
        col1, col2, col3 = st.columns(3)
        r = col1.radio("잔소리 내용 선택", ["취업", "코딩", "지각"])
        s = col2.slider("잔소리 강도 선택", min_value=1, max_value=10)
        b = col3.selectbox("잔소리 말투 선택", ["친절하게", "반말", "모욕적"])
        if mode:
            # r -> 취업, 코딩, 지각
            format = None
            if b == "친절하게":
                format = lambda x: f"여러분~ {x}"
            elif b == "반말":
                format = lambda x: f"야! {x}"
            elif b == "모욕적":
                format = lambda x: f"XXXXXX! {x}"
            if r == "취업":
                for i in range(s):
                    st.write(format("8월에는 자소서 넣어야겠죠?"))
            elif r == "코딩":
                st.write(format("저보다 파이썬 잘해요?"))
            elif r == "지각":
                st.write(format("9시랑 9시 1분은 다른 거에요."))