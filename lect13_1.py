'''
import matplotlib.pyplot as plt

#선
plt.plot([2,3,6,7,10], [1,4,5,8,9], "-", label="PData(km)")

#plt.plot([2,3,6,7,10], [1,4,5,8,9], "-", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], "--", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], ";", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], "-.", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], ".", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], ".-", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], ".--", label="PData(km)")

plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="solid", linewidth=10, solid_capstyle="round", label="Value(m)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="solid", linewidth=10, solid_capstyle="round", label="Value(m)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="dashed", linewidth=10, solid_capstyle="round", label="Value(m)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="dotted", linewidth=10, solid_capstyle="round", label="Value(m)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="dashdot", linewidth=10, solid_capstyle="round", label="Value(m)")

# linestyle(0, (픽셀크기, 여백간격))
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle=(0, (1, 0)), label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle=(0, (4, 2)), label="PData(km)")

#색
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="r", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="b", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="g", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="red", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="line", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="#75FA8D", label="Value(m)")

#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="C1", label="Value(m)")

#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="C6", label="Value(m)")

#선 두께
plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="solid", linewidth=10, solid_capstyle="round", label="Value(m)")
# plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="dashed", linewidth=10, solid_capstyle="round", label="Value(m)"

plt.plot([2,3,6,7,10], [1,4,5,8,9], "bo-", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], "bo--", label="PData(km)")

plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="H", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], marker=11, label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="s", label="PData(km)")

# c=cyan d=diamond
plt.plot([2,3,6,7,10], [1,4,5,8,9], "cd", label="PData(km)")

plt.plot([2,3,6,7,10], [1,4,5,8,9], "bo-", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], "bo--", label="PData(km)")

plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="H", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="D", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="x", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="11", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="s", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="$test$", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="$y$", label="PData(km)")

#plt.fill_between(xdata[1:4], ydata[1:4], alpha=0.5)

#세로 축 채우기
#plt.fill_between(xdata[1:4], ydata[1:4], alpha=0.5)
#plt.fill_between(xdata[2:4], ydata[2:4], alpha=0.5)
#plt.fill_between(xdata[1:3], ydata[1:3], alpha=0.5)
#plt.fill_between(xdata[1:3], ydata[1:3], alpha=0.5)

#가로 축 채우기
#plt.fill_betweenx(ydata[1:3], xdata[1:3], alpha=0.3)
#plt.fill_betweenx(ydata[2:4], xdata[2:4], alpha=0.3)

# 두 선간의 영역 채우기
#plt.fill_between(xdata[1:4], ydata[1:4], y1data[1:4], alpha=0.5)
#plt.fill_between(xdata[1:3], ydata[1:3], y1data[1:3], alpha=0.5)
#plt.fill_between(xdata[:4], ydata[:4], y1data[:4], color="C2",alpha=0.5)

#영역 채우기
#plt.fill([2.9, 2.9, 7.1, 7.1],[2.5, 5.0, 8.1, 5.1], alpha=0.5)

plt.show()




#배경
plt.grid()

#plt.grid(axis="x")

#plt.grid(axis="y")

# 색상 설정
plt.grid(axis="y", color="g")
plt.grid(axis="y", color="b")

# 투명도 설정
plt.grid(axis="y", color="g", alpha=0.5)

# 선 종류 선택
plt.grid(axis="g", color="g", alpha=0.5, linestyle="-")
plt.grid(axis="y", color="g", alpha=0.5, linestyle="--")
plt.grid(axis="y", color="g", alpha=0.5, linestyle="-.")

#눈금표시

#plt.xticks()
#plt.yticks()

# 임의 데이터 지정
#plt.xticks([0,1,2,3,4,5,6,7,8,9,10])

# 라벨 지정
#plt.xticks([1,3,5,7,9,11])
#plt.yticks([2,4,6,8,16,12])

#plt.xticks([1,3,5,7,9,11], labels=["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"])
#plt.yticks([2,4,6,8,16,12], labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

# 라벨 지정
plt.xticks([1,2,3,4,5,6,7,8,9,10], labels=["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"])
plt.yticks([0,1,2,3,4,5,6,7,8,9,10,11], labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

# 눈금 안쪽/바깥쪽 지
plt.tick_params(axis="x", direction="in")
# 눈금 안쪽/바깥쪽 지
plt.tick_params(axis="x", direction="in")

#색 지정

#plt.bar(x_years, y_data, color="g")
#plt.bar(x_years, y_data, color="C7")
#plt.bar(x_years, y_data, color="#57ADCC")


#개별 색 지정

#plt.bar(x_years, y_data, color=clr)

#막대 너비 설정

#plt.bar(x_years, y_data, color=clr, width=2)
#plt.bar(x_years, y_data, color=clr, width=0.5)
#plt.bar(x_years, y_data, color=clr, width=2)

#막대 위치 선정 edge/center

#plt.bar(x_years, y_data, color=clr, align="edge", width=0.5)
#plt.bar(x_years, y_data, color=clr, align="edge", width=0.5)

#막대 테두리 설정

# 라인 색 선택
#plt.bar(x_years, y_data, color=clr, align="center", edgecolor="black", width=0.5)

# 테두리 라인 설정
#plt.bar(x_years, y_data, color=clr, align="center", edgecolor="black", linewidth=3, width=0.5)

# 축 지표 설정

plt.yticks(100, 200, 300, 400, 500, 600, 900)

#수평 그래프 그리기
#plt.barh(x_years, y_data)

'''








































