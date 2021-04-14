# 여러개의 데이터 동시에 다루기(list)

### 리스트
# 오늘 매수할 종목 10개
stockList = ["삼성전자", "LG화학", "카카오", "원풍물산", "싸이토젠", "현대차", "한익스프레스", "한국팩키지", "대림제지", "아이에이"]
print("오늘 매수할 종목 %s" % stockList)
print("\n")

# 매수할 종목 추가하기(append)
stockList.append("현대")
print("추가된 종목 %s" % stockList)
print("\n")

# 종목 삭제하기(del)
del stockList[0]
print("인덱스 0번째 삭제 : %s" % stockList)
print("\n")

### 딕셔너리
# 삼성전자 종목에 대한 여러가지 데이터를 동시에 담기
stockDic = {"현재가" : 60000, "등락율" : 2.42}
print("현재가와 등락율을 담은 딕셔너리 : " % stockDic);
print("현재가 : %s, 등락율 : %s" % (stockDic["현재가"], stockDic["등락율"]))

# 종목 별로 데이터 담아주기
productDictionary = {"삼성전자" : stockDic}
print("삼성전자에 현재가와 등락율 담아주기 : %s" % productDictionary);

# 더이터 추가하기
productDictionary["삼성전자"]["거래량"] = 230000
print("거래량 데이터 추가 : %s" % productDictionary);

# 데이터 삭제하기
del productDictionary["삼성전자"]["거래량"];
print("거래량 데이터 삭제 : %s" % productDictionary);

# 튜플, 속도 빠름 : 최초에 선언한 그대로 사용해야 한다. 데이터 추가/삭제 안됨.
stockList = ("삼성전자", "LG화학", "카카오", "원풍물산", "싸이토젠", "현대차", "한익스프레스", "한국팩키지", "대림제지", "아이에이");
print(stockList);
print(stockList[0]);

'''
MISSION
stock_list 변수에 있는 10개의 종목들을 HTS의 일봉차트에서 2020년 6월 3일의 일봉데이터의 시가, 고가, 저가, 거래량 등의 데이터를 가지고 각각 딕셔너리로 만들어라.
'''
amtList = [
    [51800, 55000, 51700, 49257814]
    , [399000, 401500, 395000, 474692]
    , [259500, 261500, 247500, 2303391]
    , [2740, 2740, 2660, 189652]
    , [11750, 12800, 11450, 523838]
    , [106000, 110000, 105500, 3118795]
    , [4880, 4925, 4785, 119770]
    , [2445, 2450, 2385, 287030]
    , [8350, 8350, 8125, 102795]
    , [502, 520, 495, 2450376]
];

i = 0;
for product in stockList :
    productDictionary[product]= {"시가" : amtList[i][0], "고가" : amtList[i][1], "저가" : amtList[i][2], "거래량" : amtList[i][3]};
    i += 1;
print(productDictionary);
