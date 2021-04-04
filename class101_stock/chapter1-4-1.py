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
