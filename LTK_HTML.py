import streamlit as st

class LTK_HTML:
    tab_menu = ['작업형 1형', '작업형 2형', '작업형 3형']
    def __init__(self):
        self.Job_info();

    def Main_Menu(self):
        pass;

    def Job_info(self):
        st.title('빅데이터분석기사 요약 정리')

        tab_menu_list = ['작업형 1형', '작업형 2형', '작업형 3형']
        Job1, Job2, Job3 = st.tabs(tab_menu_list);

        with Job1:
            self.Job_01(tab_menu_list[0]);
        with Job2:
            self.Job_02(tab_menu_list[1]);
        with Job3:
            self.Job_03(tab_menu_list[2]);

    str_job1_function_info_list = [
        """
        ##### 1. pandas
        ###### ● 데이터 처리와 분석을 위한 패키지 파일
            * Series: 1차원
            * DataFrame: 2차원
            * Pane: 3차원
        ```
        [예시]
        import pandas as pd
        ```
        """,
        """
        ##### 2. Dataframe
        ###### ● 2차원 자료구조로 표의 형태를 띄고 있다.
        ```
        [예시]
        import pandas as pd
        # 딕셔너리
        data = {
            'ID': [ faker, chobie, doran, madlife, deft, peanut],
            'Postion': [ mid, mid, top, sup, ad, jug],
            'Win Rate': [ 66.5, 66.3, 64.5, 56.7, 62.8, 60.8]
            'KDA Rate': ['9.14', '9.52', '8.63', '3.14', '9.24', '7.63']
            'Gold': ['9.14/m', '9.01/m','8.95/m','1.52/m','9.68/m','5.63/m']
        }
        print(data)
        ```
        ```
        [결과창]
        ID          Postion     Win Rate    KDA Rate    Gold
        faker       mid         66.5        9.14        9.14/m
        chobie      mid         66.3        9.52        9.01/m
        doran       top         64.5        8.63        8.95/m
        madlife     sup         56.7        3.14        1.52/m
        deft        ad          62.8        9.24        9.68/m
        peanut      jug         60.8        7.63        5.63/m
        ```
        """,
        """
    
        ##### 3. Dataframe['칼럼명']
        ###### ● 해당 데이터 프레임 안의 칼럼 안의 내용을 가지고 온다.
        ```
        [예시]
        csv = pd.read_csv("data.csv")
        ID = csv['ID']
        print(ID)
        ```
        ```
        [결과창]
        faker
        chobie
        doran
        madlife
        deft
        peanut
        ```
        """,
        """
        ##### 4. Dataframe[Dataframe['칼럼명'] == 조건]
        ###### ● 해당 데이터 프레임 안의 칼럼 안에서 조건에 해당 하는 행을 가지고 온다.
        ```
        [예시]
        csv = pd.read_csv("data.csv")
        Mid = csv[csv['Postion'] == 'mid']
        print(Mid)
        ```
        ```
        [결과창]
        faker       mid         66.5        9.14        9.14/m
        chobie      mid         66.3        9.52        9.01/m
        ```
        
        ##### 4. Dataframe[Dataframe['칼럼명'] == 조건]['필드명']
        ###### ● 해당 데이터 프레임 안의 칼럼 안에서 조건에 해당 하는 필드명 칼럼의 데이터 행을 가지고 온다.
        ```
        [예시]
        csv = pd.read_csv("data.csv")
        Mid_ID = csv[csv['Postion'] == 'mid']['ID']
        print(Mid_ID)
        ```
        ```
        [결과창]
        faker
        chobie
        ```
        """
    ]
    str_job1_import_function_info_list = [
        ''' 
        ##### 1. .read_csv()
        ###### ● csv 파일 [엑셀 파일]을 읽어 객체에 저장하는 함수
        ```
        csv = pd.read_csv("data.csv")
        ```
        ''',
        '''
        ##### 2. DataFrame.mean()
        ###### ● DataFrame 내의 평균을 도출 하는 함수
        ```
        [예시]
        csv = pd.read_csv("data.csv")
        Win_Rate_mean = csv['Win Rate'].mean()
        print(Win_Rate_mean)
        ```
        ```
        [결과창]
        62.9333333
        ```
        ''',
        '''
        ##### 3. DataFrame.std()
        ###### ● DataFrame 내의 분산을 도출 하는 함수
        ```
        [예시]
        csv = pd.read_csv("data.csv")
        Win_Rate_mean = csv['Win Rate'].std()
        print(Win_Rate_mean)
        ```
        ```
        [결과창]
        1.245639
        ```
        ''',
        '''
        ##### 4. DataFrame.sort_values(ascending= True or False)
        ###### ● DataFrame의 정렬
            * ○ ascending = True      #내림차순
            * ○ ascending = False     #오름차순
        ```
        [예시]
        csv = pd.read_csv("data.csv")
        Win_Rate_mean = csv['ID'].sort_values()
        print(Win_Rate_mean)
        ```
        ```
        [결과창]
        chobie
        deft
        doran
        faker
        madlife
        peanut
        ```
        ''',
        '''
        ##### 5. DataFrame.values_count()
        ###### ● DataFrame 내의 각 필드의 개수 [가장 많은 순으로 내림 차순 정렬]
        ```
        [예시]
        csv = pd.read_csv("data.csv")
        Win_Rate_mean = csv['Postion'].values_count()
        print(Win_Rate_mean)
        ```
        ```
        [결과창]
        Postion     count()
        mid         2
        top         1
        jug         1
        ad          1
        sup         1
        ```
        ''',
        '''
        ##### 6. DataFrame.head(숫자)
        ###### ● 위에서 부터 숫자의 행까지의 정보를 보여주는 함수
        ###### ● [Tip] 데이터 정렬 이후 .head()를 하게 될경우 [순위를 매겨진 데이터 or 정렬된 데이터] 의 일부를 가져 올수 있다.
        ###### ● [반대의 경우] .tail 아래에서 부터 가져오는 함수
        ```
        [예시]
        csv = pd.read_csv("data.csv")
        Win_Rate_mean = csv.head(2)
        print(Win_Rate_mean)
        ```
        ```
        [결과창]
        faker       mid         66.5        9.14        9.14/m
        chobie      mid         66.3        9.52        9.01/m
        ```
        ''',
    ]
    def Job_01(self, title):
        tab_menu_list = ['작업형1형 요약', '주요 함수 정리', '예제문제 풀이','문제모음집']
        info, function_info, quest, csv_web_link = st.tabs(tab_menu_list);
        with info:
            self.Job_label(tab_menu_list[0], 4);
            for job_info in self.str_job1_function_info_list:
                st.divider()
                st.write(job_info)
        with function_info:
            self.Job_label(tab_menu_list[1], 4);
            for job_info in self.str_job1_import_function_info_list:
                st.divider()
                st.write(job_info)
        with quest:
            pass;
        with csv_web_link:
            pass;

    str_job2_function_info = """
    #### 작업형2형 작업순서
    ##### 1. 
    """
    def Job_02(self, title):
        tab_menu_list = ['작업형2형 요약', '주요 함수 정리', '예제문제 풀이', '문제모음집']
        info, function_info, quest, csv_web_link = st.tabs(tab_menu_list);
        with info:
            pass;
        with function_info:
            pass;
        with quest:
            pass;
        with csv_web_link:
            pass;

    str_job3_info = ''' 
    ###### #### 검정 통계량 구하는 패키지
    ###### scipy
    ###### ├── 01 integrate 수치적분, 미분방정식
    ###### ├── 02 linalg (선형대수, 매트릭스 분해)
    ###### ├── 03 optimize (방정식 해 구하는 알고리즘, 함수 최적화)
    ###### ├── 04 signal (신호 관련)
    ###### ├── 05 sparse (희소 행렬, 희소 선형 시스템)
    ###### └── 06 stats (통계 분석) 
    #############################################################
    ###### #### scipy.stats 구조
    ###### scipy.stats
    ###### ├── 01 T-test
    ###### │   ├── ttest_1samp         (단일표본 t검정)
    ###### │   ├── ttest_ind           (독립표본 t검정)
    ###### │   └── ttest_rel           (대응표본 t검정) 
    ###### ├── 02 비모수 검정
    ###### │   ├── mannwhitneyu        (맨-휘트니 U 검정 - 중위수 , 윌콕슨 순위합 검정과 동일하다 볼 수 있음)
    ###### │   ├── ranksums            (윌콕슨 순위합 검정 - 중위수)
    ###### │   └── wilcoxon            (윌콕슨 부호 순위합 검정)
    ###### ├── 03 정규정 검정
    ###### │   ├── anderson            (Anderson-Darling , 데이터수가 상대적으로 많을 때)
    ###### │   ├── kstest              (Kolmogorov-Smirnov , 데이터수가 상대적으로 많을 때)
    ###### │   ├── mstats.normaltest
    ###### │   └── shapiro             (shapiro, 노말분포 가장 엄격하게 검정, 데이터수가 상대적으로 적을때)
    ###### ├── 04 등분산 검정
    ###### │   ├── bartlett
    ###### │   ├── fligner
    ###### │   └── levene
    ###### ├── 05 카이제곱검정
    ###### │   ├── chi2_contingency     (카이제곱독립검정, 독립성 검정)
    ###### │   ├── chisquare            (카이제곱검정 , 적합도 검정)
    ###### │   └── fisher_exact         (피셔 정확 검정 - 빈도수가 5개 이하 셀의 수가 전체 셀의 20%이상일 경우 사용 )
    ###### └── 06 ANOVA (일원분산분석)
    ######      └── f_oneway (분산 분석은  statmodels 모듈이 더 좋음! )
    '''
    def Job_03(self, title):
        tab_menu_list = ['작업형3형 요약', '주요 함수 정리', '예제문제 풀이', '문제모음집']
        info, function_info, quest, csv_web_link = st.tabs(tab_menu_list);
        with info:
            self.Job_label(tab_menu_list[0], 4);
            st.divider()
            st.write(self.str_job3_info)
            pass;
        with function_info:
            pass;
        with quest:
            pass;
        with csv_web_link:
            pass;
    def Job_label(self, title, text_size):
        if text_size == None:
            st.subheader(title)
        else:
            text_str = text_size * '#'
            st.write(text_str+" "+title)
        pass
