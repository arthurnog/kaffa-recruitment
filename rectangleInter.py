def intersect(A,B):
    #A and B are two arays with 4 numbers
    #A[0] = x1; A[1] = y1; A[2] = x2; A[3] = y2
    #So, for the rectangles to be intersected they must respect the following
    #sentence
    if ((B[0]>=A[0] and B[0]<=A[2]) or (B[2]>=A[0] and B[2]<=A[2])) and ((B[1]>=A[1] and B[1]<=A[3]) or (B[3]>=A[1] and B[3]<=A[3])):
        print("the rectangles are intersected")
        return True
    else:
        print("the rectangles are not intersected")
        return False


points = input()

points = points.replace('(','')
points = points.replace(')','')
points = points.replace(',','')
points = points.replace(';','')

A = [int(s) for s in points.split() if s.isdigit()]

points = input()

points = points.replace('(','')
points = points.replace(')','')
points = points.replace(',','')
points = points.replace(';','')

B = [int(s) for s in points.split() if s.isdigit()]

intersect(A,B)

