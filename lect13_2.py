import matplotlib.pyplot as plt

# 산점도 그래프 그리기

""" x = 1
y = 1

plt.scatter(1, 1)
plt.scatter(x + 1,y + 1)
plt.scatter(x + 1,y + 2)
plt.scatter(x + 4,y + 1)
plt.scatter(x + 3,y + 1)
plt.scatter(x + 4,y + 3)



# 포인트 설정

#         {x}{y}{포인트크기}{색상설정}{투명}
plt.scatter(x+1.5, y+1.5, 100, "C1", alpha=0.5)
plt.scatter(x+2.5, y+1.5, 150, "red", alpha=0.5)
plt.scatter(x+3.5, y+1.5, 200, "blue", alpha=0.5)

# 컬러맵 설정

# plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="cividis")
# plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="Spectral")
# plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="viridis")
# plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="plasma")
# plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="inferno")
# plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="magma")
plt.colorbar() """

# 히스토그램 그리기
""" import numpy as np
rn = np.random.randint(1, 30, size = 20)
print(rn)

# plt.hist({data}, bins={구간수})
plt.hist(rn, bins=10, label="def")
plt.legend()
plt.show()

# 그래프 스타일 설정

# 라벨 설정
plt.hist(rn,  bins=10, label="def") 

# 투명도 설정
plt.hist(rn,  bins=10, label="def", alpha=0.5)

# 그래프 스타일 설정
plt.hist(rn,  bins=10, label="def", alpha=0.5, histtype="step")
plt.hist(rn,  bins=10, label="def", alpha=0.5, histtype="stepfield")
 """
#파이챠트 그리기

""" rate = [30, 40, 20, 10]
labels = ["Alpha", "Beta", "Gamma", "Delta"]

# plat.pie({data})
plt.pie(rate)

plt.show()

# 라벨 표시

plt.pie(rate, labels=labels)

# 퍼센트 표시

plt.pie(rate, labels=labels, autopct='%.1d%%')
plt.pie(rate, labels=labels, autopct='%.1f%%')

# 시작각도 설정

plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=0)
plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=90)
plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=270)

# 시작방향 설정

#                                                            시계방향으로 시작
plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=0, counterclock=False)
# plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=90, counterclock=False)
# plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=180, counterclock=False)

# 공백 설정

plt.pie(rate, labels=labels, autopct='%.1f%%', explode=[0, 0, 0, 0])
# plt.pie(rate, labels=labels, autopct='%.1f%%', explode=[1, 1, 1, 1])
# plt.pie(rate, labels=labels, autopct='%.1f%%', explode=[0.1, 0.1, 0.1, 0.1])

# 패널 스타일 설정

# 사용가능한 스타일 키
print(plt.style.available)

# plt.style.use("bmh")
# plt.style.use("ggplot")
# plt.style.use("classic")
# plt.style.use("Solarize_Light2")
# plt.style.use("dark_background")
# plt.style.use("fast")
 """
# 포맷 설정

"""

# 패널 사이즈 적용

plt.rcParams['figure.figsize'] = (6, 3)
# plt.rcParams['figure.figsize'] = (4, 3)

# 전체 폰트 사이즈 적용

plt.rcParams['font.size'] = 15

# 선 두께 설정

plt.rcParams['lines.linewidth'] = 5

# 선 스타일 설정

plt.rcParams['lines.linestyle'] = '--'

# 눈금 설정

# 위 눈금 설정
plt.rcParams['xtick.top'] = True

# 오른 눈금 설정
plt.rcParams['ytick.right'] = True

# 안쪽으로 눈금 설정
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

# 눈금 길이
plt.rcParams['ytick.major.size'] = 12

# 세부 눈금
plt.rcParams['xtick.minor.visible'] = True 

plt.plot([2, 3, 6, 7, 10], [1, 4, 5, 8, 9])
"""

# 객체 할용

""" fig, ax = plt.subplots()

ax = fig.add_axes([1, 1, 0, 0]) 

# 다중 패널 객체 생성

fig, ax = plt.subplots(1, 1)

# 다중 패널 그래프 출력

x = [1,4,5,8,9]
y1 = [2,3,6,7,10]

fig, ax = plt.subplots(2, 2)

ax[0][0].plot(x, y1)
# ~
ax[1][1].plot(x, y1)

# 축 공유

fig, ax = plt.subplots(2, 2, sharex=True)
fig, ax = plt.subplots(2, 2, sharey=True)
 """
# Y축 동시 출력

""" # 사용 데이터
x = [1,4,5,8,9]

y1 = [2,3,6,7,10]
y2 = [10,8,6,4,2]

fig, ax1 = plt.subplots()
ax1.set_xlabel("X-Data")
ax1.set_ylabel("Y1")
ax1.plot(x, y1)

ax2 = ax1.twinx()
ax2.set_ylabel("Y2")
ax2.plot(x, y2)

# ax1 / ax2 개별 색상 설정

ax1.plot(x, y1, color="C1")
ax2.plot(x, y2, color="C2")

# ax1 / ax2 개별 라벨 출력

ax1.plot(x, y1, color="C1", label="y1 Data")
ax1.legend(loc="upper right")

ax2.plot(x, y2, color="C2", label="y2 Data")
ax2.legend(loc="upper left")
 """
# 이종 그래프 출력

x = [1,4,5,8,9]
y1 = [2,3,6,7,10]
y2 = [2,3,6,7,10]

fig, ax1 = plt.subplots()

ax1.plot(x, y1, "-o", color="C1")
ax1.set_xlabel("X")
ax1.set_ylabel("Ydata")

ax2 = ax1.twinx()
ax2.bar(x, y2, color="C2")
ax2.set_ylabel("Y2data")

# 2종 그래프 라벨 출력
ax1.plot(x, y1, "-o", color="C1", label="XData")
ax2.bar(x, y2, color="C2", label="YData")


ax1.legend(loc="upper left")
ax2.legend(loc="upper right")







