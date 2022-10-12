# 버블 정렬
def bubbleSort(arr) :
    for i in range(len(arr)) :
        for j in range(0, len(arr) -i -1) :
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)

# 삽입 정렬
def insertSort(arr) :
    for i in range(1, len(arr)) :
        for j in range(i, 0, -1) :
            if arr[j - 1] > arr[j] :
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
    print(arr)

# 퀵 정렬
def quickSort(arr) :
    if len(arr) <= 1 : return arr

    pivot = arr[len(arr) // 2]
    lessArr, equalArr, greatArr = [], [], []

    for i in arr :
        if i < pivot :
            lessArr.append(i)
        elif i > pivot :
            greatArr.append(i)
        else :
            equalArr.append(i)

    return quickSort(lessArr) + equalArr + quickSort(greatArr)

# 프로그램 구현
def main() :
    
    # 리스트 길이 직접 설정
    while True :
        arrLen = int(input('리스트 길이 입력(10 이하) : '))
        if arrLen <= 10 : break
        else : continue

    # 리스트 입력받기
    arr = []
    while (len(arr) < arrLen) :
        arr.append(int(input('%d중 %d번째 값 입력 : ' %(arrLen, len(arr)+1))))

        # 중복 찾기
        if not len(arr) == len(set(arr)) :
            print('리스트에 중복 값이 있습니다. 다시 입력하세요.')
            arr = []
    
    print()
    print(arr)
    
    # 메뉴 선택하기
    print()
    print('-' *3, '정렬 방법 선택', '-' *3)
    print('1. 버블 정렬 \n2. 삽입 정렬 \n3. 퀵 정렬 \n4. 종료')
    selWay = int(input(': '))

    if not selWay == 0 :
        array = arr[:]
        print()
        print('-' *6, '정렬 결과', '-' *6)
        if selWay == 1 : bubbleSort(array)
        elif selWay == 2 : insertSort(array)
        elif selWay == 3 : print(quickSort(array))
    else : print('종료')

main()