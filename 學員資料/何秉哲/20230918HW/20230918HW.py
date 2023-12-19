# 90(含)~100分為「優」
# 80(含)~89分為「甲」
# 70(含)~79分為「乙」
# 60(含)~69分為「丙」
# 0(含)~59分為「丁」
import pyinputplus as pyip

score = pyip.inputInt("請輸入學生分數:", min=0, max=100)
if score >= 90:
    print("優")
elif score >= 80:
    print("甲")
elif score >= 70:
    print("乙")
elif score >= 60:
    print("丙")
else:
    print("丁")
