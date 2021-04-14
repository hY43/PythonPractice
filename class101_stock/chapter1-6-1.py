def mesu_check() :
    print("매수할지 정하는 함수");


mesu_check
print("괄호를 안 붙이면 활성화 안 됨");

mesu_check();
print("괄호를 붙이면 활성화 됨");

def mesu_check(price=0) :
    print("현재 받은 가격 : %s" % price);
    
mesu_check();
mesu_check(price=10000);
mesu_check(20000);

def mesu_check(stock_name=None, price=0) :
    if price > 5000 :
        print("매수 가능, 종목명 : %s, 종목가격 : %s" % (stock_name, price));

mesu_check(stock_name="삼성전자", price=30000);
mesu_check("LG화학", 40000);

def mesu_check(stock_name=None, price=0) :
    if price > 5000 :
        print("매수 가능, 종목명 : %s, 종목가격 : %s" % (stock_name, price));
    elif price < 100000 :
        print("매수 가능, 종목명 : %s, 종목가격 : %s" % (stock_name, price));
    else :
        print("좀 더 보류, 종목명 : %s, 종목가격 : %s" % (stock_name, price));
        
mesu_check(stock_name="원풍물산", price=2000);
mesu_check(stock_name="카카오", price=10000);
mesu_check(stock_name="삼성전자", price=500000);

def mesu_check(stock_name=None, price=0) :
    if price < 3000 :
        return 0;
    elif price < 100000 :
        return 1;
    else :
        return 2;
        
result = mesu_check(stock_name="원풍물산", price=2000);
print("매수 가능 여부 : %s" % result);

stock_dict = {"삼성전자":{"일시":20200603, "시가":51800, "고가":55000, "저가":51700, "종가":54500, "대비":3100, "대비율":6.03, "거래량":49257814, "거래대금":2655435}
, "LG화학":{"일시":20200603, "시가":399000, "고가":401500, "저가":395000, "종가":400500, "대비":5500, "대비율":1.39, "거래량":474692, "거래대금":189208}, "카카오":{"일시":20200603, "시가":259500, "고가":261500, "저가":247500, "종가":249500, "대비":-10000, "대비율":-3.85, "거래량":2302391, "거래대금":579420}
, "원풍물산":{"일시":20200603, "시가":2740, "고가":2740, "저가":2660, "종가":2685, "대비":-35, "대비율":-1.29, "거래량":189652, "거래대금":508}, "싸이토젠":{"일시":20200603, "시가":11750, "고가":12800, "저가":11450, "종가":11850, "대비":250, "대비율":2.16, "거래량":523838, "거래대금":6315}
,"현대차":{"일시":20200603, "시가":106000, "고가":110000, "저가":105500, "종가":108500, "대비":6000, "대비율":5.85, "거래량":3118795, "거래대금":335572}
, "한익스프레스":{"일시":20200603, "시가":4880, "고가":4925, "저가":4785, "종가":4800, "대비":-65, "대비율":-1.34, "거래량":119770, "거래대금":579}
, "한국팩키지":{"일시":20200603, "시가":2445, "고가":2450, "저가":2385, "종가":2385, "대비":-45, "대비율":-1.85, "거래량":287030, "거래대금":690}
, "대림제지":{"일시":20200603, "시가":1670, "고가":1670, "저가":1625, "종가":1630, "대비":-35, "대비율":-2.10, "거래량":513975, "거래대금":845}
, "아이에이":{"일시":20200603, "시가":502, "고가":520, "저가":495, "종가":510, "대비":8, "대비율":1.59, "거래량":2450376, "거래대금":1237}
};

def mesu_check(stock_name=None, price=0) :
    if price < 3000 :
        return True, stock_name, price;
    else :
        return False, None, None;
        
for name in stock_dict.keys() :
    price = stock_dict[name]["종가"];
    
    mesu_go, mesu_name, mesu_price = mesu_check(stock_name=name, price=price);
    if mesu_go is True :
        print("매수하자 : %s, 종목명 : %s, 가격 : %s" % (mesu_go, mesu_name, mesu_price));
    ##else :
    ##    print("매수하지 말자 : %s, 종목명 : %s, 가격 : %s" % (mesu_go, mesu_name, mesu_price));