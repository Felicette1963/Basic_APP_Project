import streamlit as st

class streamlit_HTML:
    Video_link = 'https://www.youtube.com/watch?v=40m1qT8D5Is'
    Vido_lyrics = '''
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
    Img_Path
    def __init__(self):
        self.streamlit_head();
        self.streamlit_Video();
    def streamlit_head(self):
        st.title("나의 파이썬 웹 페이지")

    def streamlit_Video(self):
        st.video(self.Video_link)
        st.subheader("붕괴 스타레일 들불 ost");
        st.write(self.Vido_lyrics)

    def stream_Img(self):
