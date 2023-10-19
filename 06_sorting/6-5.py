#퀵정렬 파이썬 - 비효율적이지만 간단

array =[5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    if len(array)<=1:
        return array
    pivot= array[0]
    tail=array[1:]

    left_slide= [x for x in tail if x < pivot]
    right_slide = [x for x in tail if x > pivot]
    return quick_sort(left_slide) + [pivot] +quick_sort(right_slide)

r=quick_sort(array)
print(r)

