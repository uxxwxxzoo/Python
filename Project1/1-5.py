money = 10000
print("10000원의 금액이 적립되어 있습니다.")

prompt = """
다음 메뉴에 해당하는 번호를 입력하세요
1. 아메리카노 1500
2. 카페라떼 2000
3. 에스프레소 1800
4. 주문을 끝냅니다.
"""

order = 1 
while money >= 1500 and 1<= order <=3:
    print(prompt)
    order = int(input())

    if order == 1:
        money = money - 1500
        print("손님께서는 아메리카노를 주문하셨습니다.")
        print("잔돈은 {0} 입니다.".format(money))
    elif order == 2:
        money = money - 2000
        print("손님께서는 카페라떼를 주문하셨습니다.")
        print("잔돈은 {0} 입니다.".format(money))
    elif order == 3:
        money = money - 1800
        print("손님께서는 에스프레소를 주문하셨습니다.")
        print("잔돈은 {0} 입니다.".format(money))

if money <= 1500:
    print("잔액이 부족합니다.")
else:
    print("이용해 주셔서 감사합니다.")

