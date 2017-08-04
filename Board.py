height = 32
width  = 32
class Board():
      def __init__(self):
	  self.dummy=0;
	  self.board      = self.identity();
	  self.boardColor = self.identityColor();
	  	  
      def freeze(self,shape,canvas,matrix):
          i = 0
	  points = shape.points
          for j in points:
	      self.board[points[i][0]][points[i][1]]      = 1
	      self.boardColor[points[i][0]][points[i][1]] = shape.color
	      i+=1
          self.rowCompleteCheck(canvas,matrix)
	  matrix.Clear()
	  self.draw(canvas)
	  canvas = matrix.SwapOnVSync(canvas)

      def identity(self):
          return [ [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

	           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],]

      def identityColor(self):
    	return [[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
        	[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
             	[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
            	[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
             	[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
             	[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
             	[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
             	[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
             	[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
             	[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
             	[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
             	[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
             	[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
             	[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
             	[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
             	[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
             	[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
             	[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
             	[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
             	[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
             	[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
             	[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
             	[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
             	[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
             	[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
             	[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
             	[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
             	[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
             	[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
             	[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
             	[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
             	[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]]
  	
      def rowCompleteCheck(self,canvas,matrix):


          while True:
		_i = self.getFirstCompleteIndex()
	        if _i > -1:
	           matrix.Clear()
		   self.shiftAndClear(_i)
	           self.draw(canvas)
		   canvas = matrix.SwapOnVSync(canvas)
	        else:
	           break
	                   	
      def getFirstCompleteIndex(self):
	  _sum = self.sumX()
	  _val = -1
	  for j in range(0,height):
	      if _sum[j][0] > height - 1:
	         _val = j
                 break

	  return _val
          
      def draw(self,canvas):
          for j in range(0,height):
	      for k in range(0,height):
	          _c = self.boardColor[j][k]
	          if _c != []:
	             canvas.SetPixel(j,k,_c[0],_c[1],_c[2]);
             
      def shiftAndClear(self, _x):
	   for j in range(0,height):
	       _a = self.board[j]
	       _b = self.boardColor[j]
	       del _a[_x]
	       del _b[_x]
	       _a.insert(height - 2,0)
               _b.insert(height - 2,[])
	       self.board[j]      = _a
	       self.boardColor[j] = _b

      def sumX(self):
          _b = self.board
          return [ [ _b[0][0] + _b[1][0] + _b[2][0] + _b[3][0] + _b[4][0] + _b[5][0] + _b[6][0] + _b[7][0] + _b[8][0] + _b[9][0] + _b[10][0] + _b[11][0] + _b[12][0] + _b[13][0] + _b[14][0] + _b[15][0] + _b[16][0] + _b[17][0] + _b[18][0] + _b[19][0] + _b[20][0] + _b[21][0] + _b[22][0] + _b[23][0] + _b[24][0] + _b[25][0] + _b[26][0] + _b[27][0] + _b[28][0] + _b[29][0] + _b[30][0] + _b[31][0]],
                 [ _b[0][1] + _b[1][1] + _b[2][1] + _b[3][1] + _b[4][1] + _b[5][1] + _b[6][1] + _b[7][1] + _b[8][1] + _b[9][1] + _b[10][1] + _b[11][1] + _b[12][1] + _b[13][1] + _b[14][1] + _b[15][1] + _b[16][1] + _b[17][1] + _b[18][1] + _b[19][1] + _b[20][1] + _b[21][1] + _b[22][1] + _b[23][1] + _b[24][1] + _b[25][1] + _b[26][1] + _b[27][1] + _b[28][1] + _b[29][1] + _b[30][1] + _b[31][1]],
                 [ _b[0][2] + _b[1][2] + _b[2][2] + _b[3][2] + _b[4][2] + _b[5][2] + _b[6][2] + _b[7][2] + _b[8][2] + _b[9][2] + _b[10][2] + _b[11][2] + _b[12][2] + _b[13][2] + _b[14][2] + _b[15][2] + _b[16][2] + _b[17][2] + _b[18][2] + _b[19][2] + _b[20][2] + _b[21][2] + _b[22][2] + _b[23][2] + _b[24][2] + _b[25][2] + _b[26][2] + _b[27][2] + _b[28][2] + _b[29][2] + _b[30][2] + _b[31][2]],
                 [ _b[0][3] + _b[1][3] + _b[2][3] + _b[3][3] + _b[4][3] + _b[5][3] + _b[6][3] + _b[7][3] + _b[8][3] + _b[9][3] + _b[10][3] + _b[11][3] + _b[12][3] + _b[13][3] + _b[14][3] + _b[15][3] + _b[16][3] + _b[17][3] + _b[18][3] + _b[19][3] + _b[20][3] + _b[21][3] + _b[22][3] + _b[23][3] + _b[24][3] + _b[25][3] + _b[26][3] + _b[27][3] + _b[28][3] + _b[29][3] + _b[30][3] + _b[31][3]],
                 [ _b[0][4] + _b[1][4] + _b[2][4] + _b[3][4] + _b[4][4] + _b[5][4] + _b[6][4] + _b[7][4] + _b[8][4] + _b[9][4] + _b[10][4] + _b[11][4] + _b[12][4] + _b[13][4] + _b[14][4] + _b[15][4] + _b[16][4] + _b[17][4] + _b[18][4] + _b[19][4] + _b[20][4] + _b[21][4] + _b[22][4] + _b[23][4] + _b[24][4] + _b[25][4] + _b[26][4] + _b[27][4] + _b[28][4] + _b[29][4] + _b[30][4] + _b[31][4]],
                 [ _b[0][5] + _b[1][5] + _b[2][5] + _b[3][5] + _b[4][5] + _b[5][5] + _b[6][5] + _b[7][5] + _b[8][5] + _b[9][5] + _b[10][5] + _b[11][5] + _b[12][5] + _b[13][5] + _b[14][5] + _b[15][5] + _b[16][5] + _b[17][5] + _b[18][5] + _b[19][5] + _b[20][5] + _b[21][5] + _b[22][5] + _b[23][5] + _b[24][5] + _b[25][5] + _b[26][5] + _b[27][5] + _b[28][5] + _b[29][5] + _b[30][5] + _b[31][5]],
                 [ _b[0][6] + _b[1][6] + _b[2][6] + _b[3][6] + _b[4][6] + _b[5][6] + _b[6][6] + _b[7][6] + _b[8][6] + _b[9][6] + _b[10][6] + _b[11][6] + _b[12][6] + _b[13][6] + _b[14][6] + _b[15][6] + _b[16][6] + _b[17][6] + _b[18][6] + _b[19][6] + _b[20][6] + _b[21][6] + _b[22][6] + _b[23][6] + _b[24][6] + _b[25][6] + _b[26][6] + _b[27][6] + _b[28][6] + _b[29][2] + _b[30][6] + _b[31][6]],
                 [ _b[0][7] + _b[1][7] + _b[2][7] + _b[3][7] + _b[4][7] + _b[5][7] + _b[6][7] + _b[7][7] + _b[8][7] + _b[9][7] + _b[10][7] + _b[11][7] + _b[12][7] + _b[13][7] + _b[14][7] + _b[15][7] + _b[16][7] + _b[17][7] + _b[18][7] + _b[19][7] + _b[20][7] + _b[21][7] + _b[22][7] + _b[23][7] + _b[24][7] + _b[25][7] + _b[26][7] + _b[27][7] + _b[28][7] + _b[29][2] + _b[30][7] + _b[31][7]],

                 [ _b[0][8] + _b[1][8] + _b[2][8] + _b[3][8] + _b[4][8] + _b[5][8] + _b[6][8] + _b[7][8] + _b[8][8] + _b[9][8] + _b[10][8] + _b[11][8] + _b[12][8] + _b[13][8] + _b[14][8] + _b[15][8] + _b[16][8] + _b[17][8] + _b[18][8] + _b[19][8] + _b[20][8] + _b[21][8] + _b[22][8] + _b[23][8] + _b[24][8] + _b[25][8] + _b[26][8] + _b[27][8] + _b[28][8] + _b[29][2] + _b[30][8] + _b[31][8]],
                 [ _b[0][9] + _b[1][9] + _b[2][9] + _b[3][9] + _b[4][9] + _b[5][9] + _b[6][9] + _b[7][9] + _b[8][9] + _b[9][9] + _b[10][9] + _b[11][9] + _b[12][9] + _b[13][9] + _b[14][9] + _b[15][9] + _b[16][9] + _b[17][9] + _b[18][9] + _b[19][9] + _b[20][9] + _b[21][9] + _b[22][9] + _b[23][9] + _b[24][9] + _b[25][9] + _b[26][9] + _b[27][9] + _b[28][9] + _b[29][2] + _b[30][9] + _b[31][9]],
                 [ _b[0][10] + _b[1][10] + _b[2][10] + _b[3][10] + _b[4][10] + _b[5][10] + _b[6][10] + _b[7][10] + _b[8][10] + _b[9][10] + _b[10][10] + _b[11][10] + _b[12][10] + _b[13][10] + _b[14][10] + _b[15][10] + _b[16][10] + _b[17][10] + _b[18][10] + _b[19][10] + _b[20][10] + _b[21][10] + _b[22][10] + _b[23][10] + _b[24][10] + _b[25][10] + _b[26][10] + _b[27][10] + _b[28][10] + _b[29][10] + _b[30][10] + _b[31][10]],
                 [ _b[0][11] + _b[1][11] + _b[2][11] + _b[3][11] + _b[4][11] + _b[5][11] + _b[6][11] + _b[7][11] + _b[8][11] + _b[9][11] + _b[10][11] + _b[11][11] + _b[12][11] + _b[13][11] + _b[14][11] + _b[15][11] + _b[16][11] + _b[17][11] + _b[18][11] + _b[19][11] + _b[20][11] + _b[21][11] + _b[22][11] + _b[23][11] + _b[24][11] + _b[25][11] + _b[26][11] + _b[27][11] + _b[28][11] + _b[29][11] + _b[30][11] + _b[31][11]],
                 [ _b[0][12] + _b[1][12] + _b[2][12] + _b[3][12] + _b[4][12] + _b[5][12] + _b[6][12] + _b[7][12] + _b[8][12] + _b[9][12] + _b[10][12] + _b[11][12] + _b[12][12] + _b[13][12] + _b[14][12] + _b[15][12] + _b[16][12] + _b[17][12] + _b[18][12] + _b[19][12] + _b[20][12] + _b[21][12] + _b[22][12] + _b[23][12] + _b[24][12] + _b[25][12] + _b[26][12] + _b[27][12] + _b[28][12] + _b[29][12] + _b[30][12] + _b[31][12]],
                 [ _b[0][13] + _b[1][13] + _b[2][13] + _b[3][13] + _b[4][13] + _b[5][13] + _b[6][13] + _b[7][13] + _b[8][13] + _b[9][13] + _b[10][13] + _b[11][13] + _b[12][13] + _b[13][13] + _b[14][13] + _b[15][13] + _b[16][13] + _b[17][13] + _b[18][13] + _b[19][13] + _b[20][13] + _b[21][13] + _b[22][13] + _b[23][13] + _b[24][13] + _b[25][13] + _b[26][13] + _b[27][13] + _b[28][13] + _b[29][13] + _b[30][13] + _b[31][13]],
                 [ _b[0][14] + _b[1][14] + _b[2][14] + _b[3][14] + _b[4][14] + _b[5][14] + _b[6][14] + _b[7][14] + _b[8][14] + _b[9][14] + _b[10][14] + _b[11][14] + _b[12][14] + _b[13][14] + _b[14][14] + _b[15][14] + _b[16][14] + _b[17][14] + _b[18][14] + _b[19][14] + _b[20][14] + _b[21][14] + _b[22][14] + _b[23][14] + _b[24][14] + _b[25][14] + _b[26][14] + _b[27][14] + _b[28][14] + _b[29][14] + _b[30][14] + _b[31][14]],
                 [ _b[0][15] + _b[1][15] + _b[2][15] + _b[3][15] + _b[4][15] + _b[5][15] + _b[6][15] + _b[7][15] + _b[8][15] + _b[9][15] + _b[10][15] + _b[11][15] + _b[12][15] + _b[13][15] + _b[14][15] + _b[15][15] + _b[16][15] + _b[17][15] + _b[18][15] + _b[19][15] + _b[20][15] + _b[21][15] + _b[22][15] + _b[23][15] + _b[24][15] + _b[25][15] + _b[26][15] + _b[27][15] + _b[28][15] + _b[29][15] + _b[30][15] + _b[31][15]],

                 [ _b[0][16] + _b[1][16] + _b[2][16] + _b[3][16] + _b[4][16] + _b[5][16] + _b[6][16] + _b[7][16] + _b[8][16] + _b[9][16] + _b[10][16] + _b[11][16] + _b[12][16] + _b[13][16] + _b[14][16] + _b[15][16] + _b[16][16] + _b[17][16] + _b[18][16] + _b[19][16] + _b[20][16] + _b[21][16] + _b[22][16] + _b[23][16] + _b[24][16] + _b[25][16] + _b[26][16] + _b[27][16] + _b[28][16] + _b[29][16] + _b[30][16] + _b[31][16]],
                 [ _b[0][17] + _b[1][17] + _b[2][17] + _b[3][17] + _b[4][17] + _b[5][17] + _b[6][17] + _b[7][17] + _b[8][17] + _b[9][17] + _b[10][17] + _b[11][17] + _b[12][17] + _b[13][17] + _b[14][17] + _b[15][17] + _b[16][17] + _b[17][17] + _b[18][17] + _b[19][17] + _b[20][17] + _b[21][17] + _b[22][17] + _b[23][17] + _b[24][17] + _b[25][17] + _b[26][17] + _b[27][17] + _b[28][17] + _b[29][17] + _b[30][17] + _b[31][17]],
                 [ _b[0][18] + _b[1][18] + _b[2][18] + _b[3][18] + _b[4][18] + _b[5][18] + _b[6][18] + _b[7][18] + _b[8][18] + _b[9][18] + _b[10][18] + _b[11][18] + _b[12][18] + _b[13][18] + _b[14][18] + _b[15][18] + _b[16][18] + _b[17][18] + _b[18][18] + _b[19][18] + _b[20][18] + _b[21][18] + _b[22][18] + _b[23][18] + _b[24][18] + _b[25][18] + _b[26][18] + _b[27][18] + _b[28][18] + _b[29][18] + _b[30][18] + _b[31][18]],
                 [ _b[0][19] + _b[1][19] + _b[2][19] + _b[3][19] + _b[4][19] + _b[5][19] + _b[6][19] + _b[7][19] + _b[8][19] + _b[9][19] + _b[10][19] + _b[11][19] + _b[12][19] + _b[13][19] + _b[14][19] + _b[15][19] + _b[16][19] + _b[17][19] + _b[18][19] + _b[19][19] + _b[20][19] + _b[21][19] + _b[22][19] + _b[23][19] + _b[24][19] + _b[25][19] + _b[26][19] + _b[27][19] + _b[28][19] + _b[29][19] + _b[30][19] + _b[31][19]],
                 [ _b[0][20] + _b[1][20] + _b[2][20] + _b[3][20] + _b[4][20] + _b[5][20] + _b[6][20] + _b[7][20] + _b[8][20] + _b[9][20] + _b[10][20] + _b[11][20] + _b[12][20] + _b[13][20] + _b[14][20] + _b[15][20] + _b[16][20] + _b[17][20] + _b[18][20] + _b[19][20] + _b[20][20] + _b[21][20] + _b[22][20] + _b[23][20] + _b[24][20] + _b[25][20] + _b[26][20] + _b[27][20] + _b[28][20] + _b[29][20] + _b[30][20] + _b[31][20]],
                 [ _b[0][21] + _b[1][21] + _b[2][21] + _b[3][21] + _b[4][21] + _b[5][21] + _b[6][21] + _b[7][21] + _b[8][21] + _b[9][21] + _b[10][21] + _b[11][21] + _b[12][21] + _b[13][21] + _b[14][21] + _b[15][21] + _b[16][21] + _b[17][21] + _b[18][21] + _b[19][21] + _b[20][21] + _b[21][21] + _b[22][21] + _b[23][21] + _b[24][21] + _b[25][21] + _b[26][21] + _b[27][21] + _b[28][21] + _b[29][21] + _b[30][21] + _b[31][21]],
                 [ _b[0][22] + _b[1][22] + _b[2][22] + _b[3][22] + _b[4][22] + _b[5][22] + _b[6][22] + _b[7][22] + _b[8][22] + _b[9][22] + _b[10][22] + _b[11][22] + _b[12][22] + _b[13][22] + _b[14][22] + _b[15][22] + _b[16][22] + _b[17][22] + _b[18][22] + _b[19][22] + _b[20][22] + _b[21][22] + _b[22][22] + _b[23][22] + _b[24][22] + _b[25][22] + _b[26][22] + _b[27][22] + _b[28][22] + _b[29][22] + _b[30][22] + _b[31][22]],
                 [ _b[0][23] + _b[1][23] + _b[2][23] + _b[3][23] + _b[4][23] + _b[5][23] + _b[6][23] + _b[7][23] + _b[8][23] + _b[9][23] + _b[10][23] + _b[11][23] + _b[12][23] + _b[13][23] + _b[14][23] + _b[15][23] + _b[16][23] + _b[17][23] + _b[18][23] + _b[19][23] + _b[20][23] + _b[21][23] + _b[22][23] + _b[23][23] + _b[24][23] + _b[25][23] + _b[26][23] + _b[27][23] + _b[28][23] + _b[29][23] + _b[30][23] + _b[31][23]],

                 [ _b[0][24] + _b[1][24] + _b[2][24] + _b[3][24] + _b[4][24] + _b[5][24] + _b[6][24] + _b[7][24] + _b[8][24] + _b[9][24] + _b[10][24] + _b[11][24] + _b[12][24] + _b[13][24] + _b[14][24] + _b[15][24] + _b[16][24] + _b[17][24] + _b[18][24] + _b[19][24] + _b[20][24] + _b[21][24] + _b[22][24] + _b[23][24] + _b[24][24] + _b[25][24] + _b[26][24] + _b[27][24] + _b[28][24] + _b[29][24] + _b[30][24] + _b[31][24]],
                 [ _b[0][25] + _b[1][25] + _b[2][25] + _b[3][25] + _b[4][25] + _b[5][25] + _b[6][25] + _b[7][25] + _b[8][25] + _b[9][25] + _b[10][25] + _b[11][25] + _b[12][25] + _b[13][25] + _b[14][25] + _b[15][25] + _b[16][25] + _b[17][25] + _b[18][25] + _b[19][25] + _b[20][25] + _b[21][25] + _b[22][25] + _b[23][25] + _b[24][25] + _b[25][25] + _b[26][25] + _b[27][25] + _b[28][25] + _b[29][25] + _b[30][25] + _b[31][25]],
                 [ _b[0][26] + _b[1][26] + _b[2][26] + _b[3][26] + _b[4][26] + _b[5][26] + _b[6][26] + _b[7][26] + _b[8][26] + _b[9][26] + _b[10][26] + _b[11][26] + _b[12][26] + _b[13][26] + _b[14][26] + _b[15][26] + _b[16][26] + _b[17][26] + _b[18][26] + _b[19][26] + _b[20][26] + _b[21][26] + _b[22][26] + _b[23][26] + _b[24][26] + _b[25][26] + _b[26][26] + _b[27][26] + _b[28][26] + _b[29][26] + _b[30][26] + _b[31][26]],
                 [ _b[0][27] + _b[1][27] + _b[2][27] + _b[3][27] + _b[4][27] + _b[5][27] + _b[6][27] + _b[7][27] + _b[8][27] + _b[9][27] + _b[10][27] + _b[11][27] + _b[12][27] + _b[13][27] + _b[14][27] + _b[15][27] + _b[16][27] + _b[17][27] + _b[18][27] + _b[19][27] + _b[20][27] + _b[21][27] + _b[22][27] + _b[23][27] + _b[24][27] + _b[25][27] + _b[26][27] + _b[27][27] + _b[28][27] + _b[29][27] + _b[30][27] + _b[31][27]],
                 [ _b[0][28] + _b[1][28] + _b[2][28] + _b[3][28] + _b[4][28] + _b[5][28] + _b[6][28] + _b[7][28] + _b[8][28] + _b[9][28] + _b[10][28] + _b[11][28] + _b[12][28] + _b[13][28] + _b[14][28] + _b[15][28] + _b[16][28] + _b[17][28] + _b[18][28] + _b[19][28] + _b[20][28] + _b[21][28] + _b[22][28] + _b[23][28] + _b[24][28] + _b[25][28] + _b[26][28] + _b[27][28] + _b[28][28] + _b[29][28] + _b[30][28] + _b[31][28]],
                 [ _b[0][29] + _b[1][29] + _b[2][29] + _b[3][29] + _b[4][29] + _b[5][29] + _b[6][29] + _b[7][29] + _b[8][29] + _b[9][29] + _b[10][29] + _b[11][29] + _b[12][29] + _b[13][29] + _b[14][29] + _b[15][29] + _b[16][29] + _b[17][29] + _b[18][29] + _b[19][29] + _b[20][29] + _b[21][29] + _b[22][29] + _b[23][29] + _b[24][29] + _b[25][29] + _b[26][29] + _b[27][29] + _b[28][29] + _b[29][29] + _b[30][29] + _b[31][29]],
                 [ _b[0][30] + _b[1][30] + _b[2][30] + _b[3][30] + _b[4][30] + _b[5][30] + _b[6][30] + _b[7][30] + _b[8][30] + _b[9][30] + _b[10][30] + _b[11][30] + _b[12][30] + _b[13][30] + _b[14][30] + _b[15][30] + _b[16][30] + _b[17][30] + _b[18][30] + _b[19][30] + _b[20][30] + _b[21][30] + _b[22][30] + _b[23][30] + _b[24][30] + _b[25][30] + _b[26][30] + _b[27][30] + _b[28][30] + _b[29][30] + _b[30][30] + _b[31][30]],
                 [ _b[0][31] + _b[1][31] + _b[2][31] + _b[3][31] + _b[4][31] + _b[5][31] + _b[6][31] + _b[7][31] + _b[8][31] + _b[9][31] + _b[10][31] + _b[11][31] + _b[12][31] + _b[13][31] + _b[14][31] + _b[15][31] + _b[16][31] + _b[17][31] + _b[18][31] + _b[19][31] + _b[20][31] + _b[21][31] + _b[22][31] + _b[23][31] + _b[24][31] + _b[25][31] + _b[26][31] + _b[27][31] + _b[28][31] + _b[29][31] + _b[30][31] + _b[31][31]],

                 ]

      def checkPointsCollision(self,_x,_y):
	  _failed = {'top':False,'bottom':False,'side':False,'other':False}
	  if _y < 0:
	     _failed['bottom'] = True
	  else:
	     if _y > height - 1:
	        _failed['top'] = True
	    #    if _v > 0:
	    #       _failed['other'] = True
	     elif _x > width - 1 or _x < 0:
	        _failed['side'] = True
	     else:
	        _v = self.board[_x][_y]
	        if _v > 0:
                   _failed['other'] = True
	  return _failed          	

#      def sumR(self):
#          _b = self.board
#          return [ [ _b[0][0] + _b[0][1] + _b[0][2] + _b[0][3] + _b[0][4] + _b[0][5] + _b[0][6] + _b[0][7]],
#         	   [ _b[1][0] + _b[1][1] + _b[1][2] + _b[1][3] + _b[1][4] + _b[1][5] + _b[1][6] + _b[1][7]],
#       	           [ _b[2][0] + _b[2][1] + _b[2][2] + _b[2][3] + _b[2][4] + _b[2][5] + _b[2][6] + _b[2][7]],
#       	           [ _b[3][0] + _b[3][1] + _b[3][2] + _b[3][3] + _b[3][4] + _b[3][5] + _b[3][6] + _b[3][7]],
#       	           [ _b[4][0] + _b[4][1] + _b[4][2] + _b[4][3] + _b[4][4] + _b[4][5] + _b[4][6] + _b[4][7]],
#        	   [ _b[5][0] + _b[5][1] + _b[5][2] + _b[5][3] + _b[5][4] + _b[5][5] + _b[5][6] + _b[5][7]],
#         	   [ _b[6][0] + _b[6][1] + _b[6][2] + _b[6][3] + _b[6][4] + _b[6][5] + _b[6][6] + _b[6][7]],
#         	   [ _b[7][0] + _b[7][1] + _b[7][2] + _b[7][3] + _b[7][4] + _b[7][5] + _b[7][6] + _b[7][7]], ]	  	
