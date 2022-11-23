# read integers from heights.txt
# find maximum area of rectangle


def main():
    # read integers from heights.txt
    heights = []
    with open('heights.txt', 'r') as f:
        for line in f:
            heights.append(int(line))
    # find maximum area of rectangle
    max_area = 0
    beg = 0
    end = len(heights) - 1
    while beg < end:
        area = min(heights[beg], heights[end]) * (end - beg)
        if area > max_area:
            max_area = area
        if heights[beg] < heights[end]:
            beg += 1
        else:
            end -= 1
    # for i in range(len(heights)):
    #     for j in range(i, len(heights)):
    #         area = (j - i + 1) * min(heights[i:j+1])
    #         if area > max_area:
    #             max_area = area
    print(max_area) #   795173218  # ignore one digit

# main guard
if __name__ == '__main__':
    main()
