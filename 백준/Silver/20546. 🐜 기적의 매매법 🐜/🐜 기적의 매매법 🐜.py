import sys
input = sys.stdin.readline

cash = int(input().strip())
prices = list(map(int,input().split()))

bnp_cash = cash
bnp_stock = 0
for p in prices:
    if bnp_cash>=p:
        buy = bnp_cash//p
        bnp_stock += buy
        bnp_cash -= buy*p
bnp_total = bnp_cash+bnp_stock *prices[-1]

timing_cash = cash
timing_stock = 0
up_cnt = 0
down_cnt = 0
for i in range(len(prices)):
    if i>0:
        if prices[i]>prices[i-1]:
            up_cnt +=1
            down_cnt = 0
        elif prices[i]<prices[i-1]:
            down_cnt+=1
            up_cnt =0
        else:
            up_cnt = 0
            down_cnt = 0
    if up_cnt>=3 and timing_stock >0:
        timing_cash += timing_stock*prices[i]
        timing_stock = 0
    elif down_cnt>=3 and timing_cash>= prices[i]:
        buy = timing_cash//prices[i]
        timing_stock += buy
        timing_cash -= buy*prices[i]
timing_total = timing_cash + timing_stock*prices[-1]

if bnp_total > timing_total:
    print("BNP")
elif bnp_total < timing_total:
    print("TIMING")
else:
    print("SAMESAME")