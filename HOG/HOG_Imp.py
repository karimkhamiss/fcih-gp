import cv2
import numpy as np
import numpy.ma as ma
from PIL import Image




#Class Pixel Used As node
class Pixel:
    def __init__(self,magnitude,angle):
        self.magnitude=magnitude
        self.angle=angle

#////////////////////////////////////////////////////////////////////////////////////////////#
#////////////////////////////////////////////////////////////////////////////////////////////#

#calculate Magnitude and Angle for all pixels in Matrix
def cal(image):
    # dimentions of Matrix
    height = image.shape[0]  # col
    width = image.shape[1]  # row

    # matrix of objects
    pixelsList = []
    img = np.float32(image) / 255.0
    # Calculate gradient
    gx = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=1)
    gy = cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=1)
    mag, angle = cv2.cartToPolar(gx, gy, angleInDegrees=True)

    #print 'Mangnitude>>',mag
    #print 'Angle >>',angle

    # loop in Matrix
    # insert angle and Magnitude
    for row in range(0, height):  #col
        for col in range(0, width):
            Magnitude=mag[row][col]
            Angle=angle[row][col]
            pixel = Pixel(Magnitude, Angle)
            #print "angle>>",pixel.angle
            #print "mangnitude",pixel.magnitude
            pixelsList.append(pixel)

    # Convert List To Matrix with nodes(objects of class pixel)
    # each pixel is object of class pixel
    pixelsList = np.array(ma.getdata(pixelsList)).reshape(width, height)
    #print pixelsList[1][1]
    return pixelsList
#img=pre_processing('0.png')
#cal(img)

#////////////////////////////////////////////////////////////////////////////////////////////#
#////////////////////////////////////////////////////////////////////////////////////////////#


def Dividing(cell_size,block_size,matrixList):
    sx, sy = matrixList.shape   #rows and cols
    cx, cy = cell_size
    bx, by = block_size #bx = no of cells in rews and cols
    n_cellsx = int(np.floor(sx // cx))  # number of cells in x
    n_cellsy = int(np.floor(sy // cy))  # number of cells in y
    n_blocksx = (n_cellsx - bx) + 1
    n_blocksy = (n_cellsy - by) + 1
    cellsinrow = []
    cells=[] #cells
    blocks=[] #blocs
    Img_Row=cx #No Of Rows in Block
    Img_Col=cy #No Of Columns in Block
    #print "Img_Row>>",Img_Row," Img_Col>>",Img_Col  #Print No Of Rows and Columns
    for r in range(0, matrixList.shape[0] ,Img_Row):
        for c in range(0, matrixList.shape[1] ,Img_Col):
            cellsinrow.append( matrixList[r:r + Img_Row, c:c + Img_Col])
        cells.append(cellsinrow)
        cellsinrow=[]

    cells = np.array(cells)#.reshape(1, len(cells))
    for x in range(0 ,n_blocksx):
        for y in range(0 ,n_blocksy):
            block = cells[x:x + bx , y:y + by ]
            blocks.append(block)

    return  cells , blocks

#////////////////////////////////////////////////////////////////////////////////////////////#
#////////////////////////////////////////////////////////////////////////////////////////////#


def blockNormaliztion(blocklist):

    #calcultate vector lenght
    value = 0.0
    for index in range(0,len(blocklist)):
        value=value+np.power(blocklist[index], 2)
    vectorlen=np.sqrt(value)

    #to divide all values of histogram in vector length
    for index in range(0, len(blocklist)):
        if vectorlen==0.0 and blocklist[index]==0.0:   #don't want the result to be infinity
            blocklist[index]=0.0
        else:
            blocklist[index]= float("{0:.4f}".format(blocklist[index]/vectorlen).rstrip('0'))#divide to find value after normalization


    return blocklist

#////////////////////////////////////////////////////////////////////////////////////////////#
#////////////////////////////////////////////////////////////////////////////////////////////#


def drawHis(blocksList) :
    ang1,ang2,ang3,ang4,ang5,ang6,ang7,ang8,ang9=10,30,50,70,90,110,130,150,170
    #each angle with its magnitude
    dicList=[]
    blockdicList = []
    imagevector=[]
    count=0
    finalDic = {'ang1': 0, 'ang2': 0, 'ang3': 0, 'ang4': 0, 'ang5': 0, 'ang6': 0, 'ang7': 0, 'ang8': 0, 'ang9': 0}
    for block in blocksList:
        bins = {'ang1': 0, 'ang2': 0, 'ang3': 0, 'ang4': 0, 'ang5': 0, 'ang6': 0, 'ang7': 0, 'ang8': 0, 'ang9': 0}

        for cells in block:
            blockvector = []
            for cell in cells:
                row = cell.shape[0]
                col = cell.shape[1]
                for x in range(0, row):
                    for y in range(0, col):

                        if cell[x, y].angle <= ang1:
                            bins['ang1'] = bins['ang1'] + cell[x, y].magnitude

                        elif cell[x, y].angle == ang2:
                            bins['ang2'] = bins['ang2'] + cell[x, y].magnitude

                        elif cell[x, y].angle == ang3:
                            bins['ang3'] = bins['ang3'] + cell[x, y].magnitude

                        elif cell[x, y].angle == ang4:
                            bins['ang4'] = bins['ang4'] + cell[x, y].magnitude

                        elif cell[x, y].angle == ang5:
                            bins['ang5'] = bins['ang5'] + cell[x, y].magnitude

                        elif cell[x, y].angle == ang6:
                            bins['ang6'] = bins['ang6'] + cell[x, y].magnitude

                        elif cell[x, y].angle == ang7:
                            bins['ang7'] = bins['ang7'] + cell[x, y].magnitude

                        elif cell[x, y].angle == ang8:
                            bins['ang8'] = bins['ang8'] + cell[x, y].magnitude

                        elif cell[x, y].angle >= ang9:
                            bins['ang9'] += bins['ang9'] + cell[x, y].magnitude

                        elif cell[x, y].angle < ang2 and cell[x, y].angle > ang1:
                            bins['ang2'] += bins['ang2'] + cell[x, y].magnitude * (ang1 - cell[x, y].angle) / 20
                            bins['ang1'] += bins['ang1'] + cell[x, y].magnitude * (cell[x, y].angle - ang2) / 20

                        elif cell[x, y].angle < ang3 and cell[x, y].angle > ang2:
                            bins['ang3'] += bins['ang3'] + cell[x, y].magnitude * (ang2 - cell[x, y].angle) / 20
                            bins['ang2'] += bins['ang2'] + cell[x, y].magnitude * (cell[x, y].angle - ang3) / 20

                        elif cell[x, y].angle < ang4 and cell[x, y].angle > ang3:
                            bins['ang4'] += bins['ang4'] + cell[x, y].magnitude * (ang3 - cell[x, y].angle) / 20
                            bins['ang3'] += bins['ang3'] + cell[x, y].magnitude * (cell[x, y].angle - ang4) / 20

                        elif cell[x, y].angle < ang5 and cell[x, y].angle > ang4:
                            bins['ang5'] += bins['ang5'] + cell[x, y].magnitude * (ang4 - cell[x, y].angle) / 20
                            bins['ang4'] += bins['ang4'] + cell[x, y].magnitude * (cell[x, y].angle - ang5) / 20

                        elif cell[x, y].angle < ang6 and cell[x, y].angle > ang5:
                            bins['ang6'] += bins['ang6'] + cell[x, y].magnitude * (ang5 - cell[x, y].angle) / 20
                            bins['ang5'] += bins['ang5'] + cell[x, y].magnitude * (cell[x, y].angle - ang6) / 20

                        elif cell[x, y].angle < ang7 and cell[x, y].angle > ang6:
                            bins['ang7'] += bins['ang7'] + cell[x, y].magnitude * (ang6 - cell[x, y].angle) / 20
                            bins['ang6'] += bins['ang6'] + cell[x, y].magnitude * (cell[x, y].angle - ang7) / 20

                        elif cell[x, y].angle < ang8 and cell[x, y].angle > ang7:
                            bins['ang8'] += bins['ang8'] + cell[x, y].magnitude * (ang7 - cell[x, y].angle) / 20
                            bins['ang7'] += bins['ang7'] + cell[x, y].magnitude * (cell[x, y].angle - ang8) / 20

                        elif cell[x, y].angle < ang9 and cell[x, y].angle > ang8:
                            bins['ang9'] = bins['ang9'] + cell[x, y].magnitude * (ang8 - cell[x, y].angle) / 20
                            bins['ang8'] = bins['ang8'] + cell[x, y].magnitude * (cell[x, y].angle - ang9) / 20

            #bn.blockNormaliztion(bins)
            #blockdicList.append(bn.blockNormaliztion(bins))

                for index in range(1, 10):
                    blockvector.append(bins['ang' + str(index)])

            blockvector=blockNormaliztion(blockvector)    #normalize block vector
            for index in range(0, len(blockvector)):
                imagevector.append(blockvector[index])

    return  imagevector


#////////////////////////////////////////////////////////////////////////////////////////////#
#////////////////////////////////////////////////////////////////////////////////////////////#


def Hogfun(img , Cell_Size , Block_Size):
    matrixList = cal(img)
    cells, blockList = Dividing(Cell_Size,Block_Size, matrixList)
    imagevector = drawHis(blockList)

    return imagevector


