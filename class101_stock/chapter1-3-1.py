# 어제 5000원 매수하고 오늘 3000원 추가 매수했다.
# 총 매입 금액은 얼마인가?
stockPrice1 = 5000
stockPrice2 = 3000
print("총 매입 금액 : %s" % (stockPrice1 + stockPrice2))
totalStockPrice = stockPrice1 + stockPrice2
print("총 매입 금액 : %s" % totalStockPrice)

# 어제 6000원 매수하고 오늘 2000원 매도 했다.
# 총 매입 금액은 얼마인가?
stockPrice1 = 6000
stockPrice2 = 2000
totalStockPrice = stockPrice1 - stockPrice2
print("총 매입 금액 : %s" % totalStockPrice)

# 삼성전자 55400원에 5종목을 매수한다.
stockName = "삼성전자"
stockPrice = 55400
stockQuantity = 5
totalStockPrice = stockPrice * stockQuantity
print("%s 종목의 총 매입 금액 : %s" % (stockName, totalStockPrice))

# 예수금이 100만원 있다. LG 상사 14800원에 매수할 수 있는 수량은?
# 그리고 남은 예수금은 ?
account = 1000000
lgStockPrice = 14800
quantity1 = account / lgStockPrice # 소수점 제거 전
quantity2 = account // lgStockPrice # 소수점 제거 후
print("예수금 : %s, 현재가 : %s, 수량(소수점포함) : %s, 수량2(소수점제외) : %s" % (account, lgStockPrice, quantity1, quantity2))
restAccount = account % lgStockPrice
print("남은 예수금 : %s" % restAccount);


# 과제 : LG 상사 종목의 2020년 6월 18일자 종가의 등락률을 구해라 (종가 - 전일종가) / 전일종가 X 100
# 소수점 둘째자리 이하 절사
def myRound(targetRate) : 
    return round(targetRate * 100) / 100
    
stockName = "LG 상사"
tradeDate = "2020-06-18"
closingPrice = 16850
yesterdayClosingPrice = 14950
rate = (closingPrice - yesterdayClosingPrice) / yesterdayClosingPrice * 100
print("%s 의 %s 종목의 등락률 : %s" % (tradeDate, stockName, myRound(rate)))

