def cal_total(exp):
    total=0
    for item in exp:
        total= total+item
    return total

R_exp_list=[200,300,400]
T_exp_list=[300,400,500]

R_total=cal_total(R_exp_list)
T_total=cal_total(T_exp_list)
print("R total expenses:",R_total)
print("T total expenses:",T_total)






