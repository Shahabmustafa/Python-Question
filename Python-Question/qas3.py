# (3) Matrix Transpose [2 pts.]


# The transpose of a square matrix M is an important tool that is used in solving systems of linear
# equations. It can be computed by swapping all of M’s rows and columns. For example:

                # ANSWER

X = [[1,2,3,4],  
      [4,5,6,7],  
     [7,8,9,10],
     [9,10,11,12]]  
  
result = [[0,0,0,0],  
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]  

  
# iterate through rows  
for i in range(len(X)):  
# iterate through coloums
   for j in range(len(result)):  
        result[j][i] = X[i][j]  
  
for r in result:  
   print(r)  