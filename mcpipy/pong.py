from mine import *
from board2d import Board2D
from time import sleep
import input
import random

paddleHeight = 5
width = 60
statusY = 40
statusSize = 11
boardHeight = statusY + statusSize

maxLeftSpeed = 1
maxRightSpeed = 0.5

leftPaddleY = statusY // 2
rightPaddleY = statusY // 2
rightPaddleX = width - 2
leftPaddleX = 1
leftScore = 0
rightScore = 0

mc = Minecraft()
board = Board2D(mc, width, boardHeight, distance=30)

lastMove = -1
redraw = True

while True:
    board.line(0, statusY, 0, 0, block.WOOL_BLACK)
    board.line(width-1, 0, width-1, statusY, block.WOOL_BLACK)
    board.text(width//4, statusY+2, str(leftScore), foreground=block.WOOL_BLACK, background=block.AIR, center=True)                
    board.text(width-width//4, statusY+2, str(rightScore), foreground=block.WOOL_BLACK, background=block.AIR, center=True)            
    ballX = width // 2
    ballY = statusY // 2
    vX = 0.75 * random.choice([-1,1])
    vY = 0.75 * random.choice([-1,1])
    board.draw()
    if leftScore >= 2 or rightScore >= 2:
        break

    while True:
        if input.isPressedNow(input.UP) and leftPaddleY < statusY-1:
            leftPaddleY += maxLeftSpeed
        if input.isPressedNow(input.DOWN) and leftPaddleY > 0:
            leftPaddleY -= maxLeftSpeed
        if vX > 0:
            if rightPaddleY < ballY:
                rightPaddleY += maxRightSpeed
            elif rightPaddleY > ballY:
                rightPaddleY -= maxRightSpeed

        ballX = ballX + vX
        ballY = ballY + vY
        
        if ballY <= 0.5:
            vY = abs(vY)
        elif ballY >= statusY-0.5:
            vY = -abs(vY)
        board.setBlocks(1,1,width-2,statusY-1, block.STAINED_GLASS_LIGHT_BLUE) 
        board.line(0, statusY, width-1, statusY, block.WOOL_BLACK)
        board.line(0, 0, width-1, 0, block.WOOL_BLACK)
        board.setBlocks(leftPaddleX, leftPaddleY-paddleHeight//2, leftPaddleX, leftPaddleY+paddleHeight//2, block.WOOL_WHITE)
        board.setBlocks(rightPaddleX, rightPaddleY-paddleHeight//2, rightPaddleX, rightPaddleY+paddleHeight//2, block.WOOL_WHITE)
        board.setBlock(ballX, ballY, block.PUMPKIN_ACTIVE)
        board.draw()
        
        if ballX <= leftPaddleX + 0.5:
            if abs(ballY-leftPaddleY) <= paddleHeight * 0.5:
                vX = abs(vX)
            else:
                rightScore += 1
                break

        if ballX >= rightPaddleX - 0.5:
            if abs(ballY-rightPaddleY) <= paddleHeight * 0.5:
                vX = abs(vX)
            else:
                leftScore += 1
                break

        sleep(.1)
