# 분류 모델 웹앱 만들기

import streamlit as st

# 1. 기계학습 모델 파일 로드


# 2. 모델 설명
 st.title('_______')
col1, col2,col3 = st.columns( ____ )      # 몇 개의 컬럼으로 나눌까?
with col1:
      st.subheader('모델 설명 ')
      st.write(' - 기계학습 알고리즘 : 로지스틱 회귀 ')
      st.write(' - 학습 데이터 출처 : https://data.kma.go.kr/data/weatherIssue/slthtList.do?pgmNo=690)
      st.write(' - 훈련    데이터 : 700건')
      st.write(' - 테스트 데이터 : 300건')
      st.write(' - 모델 정확도 : ')

# 3. 데이터시각화


# 4. 모델 활용
st.subheader('모델 활용')
st.write('--다음 수치들을 입력하세요.인공지능이 폭염 여부를 판단해드립니다.--')

a=st.number_input('최고 기온 입력')
b=st.number_input('최저 기온 입력')
c=st.number_input('평균 상대 습도 입력')
d=st.selectbox('자외선 지수 선택(메우높음:0,높음:1,낮음:2,매우 낮음:3',[0,1,2,3])

if st.button('폭염 예측')
  input_data=[[a,b,c,d]]
  p=model.predict(input_data)
  st.write('인공지능의 폭염 여부 예측은',p)
