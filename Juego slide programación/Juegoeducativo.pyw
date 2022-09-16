#py -m pip install -U pygame --user para instalar pygame en la terminal
import pygame, sys, random
from pygame.locals import *


ancho_casilla = 4  
alto_casilla = 4 
tamaño_casilla = 80
ancho_ventana = 800
alto_ventana = 600
FPS = 30
BLANK = None


negro ="black"
blanco ="white"
azul ="blue"
coral ="lightcoral"
verde ="green"
turquesa = "turquoise"
azuloscuro = "darkblue"


BGCOLOR = coral
TILECOLOR = turquesa
TEXTCOLOR = azuloscuro
COLORBORDE = azul
tamañodeletra = 20

colorboton = blanco
BUTTONTEXTCOLOR = negro
colormensaje = blanco

margenx = int((ancho_ventana - (tamaño_casilla * ancho_casilla + (ancho_casilla - 1))) / 2)
margeny = int((alto_ventana - (tamaño_casilla * alto_casilla + (alto_casilla - 1))) / 2)

ARRIBA ='up'
ABAJO ='down'
IZQUIERDA ='left'
RIGHT = 'right'

def main():
    global FPSCLOCK, DISPLAYSURF, letrabasica, RESET_SURF, RESET_RECT, NEW_SURF, NEW_RECT, SOLVE_SURF, SOLVE_RECT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((ancho_ventana, alto_ventana))
    pygame.display.set_caption("Puzzle de deslizamiento")
    letrabasica= pygame.font.Font('freesansbold.ttf', tamañodeletra)

   
    RESET_SURF, RESET_RECT = makeText("Reiniciar",    TEXTCOLOR, TILECOLOR, ancho_ventana - 120, alto_ventana - 90)
    NEW_SURF,   NEW_RECT   = makeText("Nuevo juego", TEXTCOLOR, TILECOLOR, ancho_ventana - 120, alto_ventana - 60)
    SOLVE_SURF, SOLVE_RECT = makeText("Solucionar",    TEXTCOLOR, TILECOLOR, ancho_ventana - 120, alto_ventana - 30)

    mainBoard, solutionSeq = generateNewPuzzle(80)
    resolvertabla = getStartingBoard() 
    allMoves = [] 

    while True: 
        slideTo = None 
        msg = "Haz click en la ficha para moverla o usa teclas WASD o las flechas de dirección." 
        if mainBoard == resolvertabla:
            msg = "Solucionado Felicitaciones"

        drawBoard(mainBoard, msg)

        checkForQuit()
        for event in pygame.event.get(): 
            if event.type == MOUSEBUTTONUP:
                spotx, spoty = getSpotClicked(mainBoard, event.pos[0], event.pos[1])

                if (spotx, spoty) == (None, None):
                    
                    if RESET_RECT.collidepoint(event.pos):
                        resetAnimation(mainBoard, allMoves)
                        allMoves = []
                    elif NEW_RECT.collidepoint(event.pos):
                        mainBoard, solutionSeq = generateNewPuzzle(80) 
                        allMoves = []
                    elif SOLVE_RECT.collidepoint(event.pos):
                        resetAnimation(mainBoard, solutionSeq + allMoves) 
                        allMoves = []
                else:
                    

                    blankx, blanky = getBlankPosition(mainBoard)
                    if spotx == blankx + 1 and spoty == blanky:
                        slideTo = IZQUIERDA
                    elif spotx == blankx - 1 and spoty == blanky:
                        slideTo = RIGHT
                    elif spotx == blankx and spoty == blanky + 1:
                        slideTo = ARRIBA
                    elif spotx == blankx and spoty == blanky - 1:
                        slideTo = ABAJO

            elif event.type == KEYUP:
                
                if event.key in (K_LEFT, K_a) and isValidMove(mainBoard, IZQUIERDA):
                    slideTo = IZQUIERDA
                elif event.key in (K_RIGHT, K_d) and isValidMove(mainBoard, RIGHT):
                    slideTo = RIGHT
                elif event.key in (K_UP, K_w) and isValidMove(mainBoard, ARRIBA):
                    slideTo = ARRIBA
                elif event.key in (K_DOWN, K_s) and isValidMove(mainBoard, ABAJO):
                    slideTo = ABAJO

        if slideTo:
            slideAnimation(mainBoard, slideTo, 'Click tile or press arrow keys to slide.', 8)
            makeMove(mainBoard, slideTo)
            allMoves.append(slideTo)
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def terminate():
    pygame.quit()
    sys.exit()


def checkForQuit():
    for event in pygame.event.get(QUIT):
        terminate() 
    for event in pygame.event.get(KEYUP): 
        if event.key == K_ESCAPE:
            terminate()
        pygame.event.post(event) 


def getStartingBoard():
    contador = 1
    board = []
    for x in range(ancho_casilla):
        column = []
        for y in range(alto_casilla):
            column.append(contador)
            contador += ancho_casilla
        board.append(column)
        contador -= ancho_casilla * (alto_casilla - 1) + ancho_casilla - 1

    board[ancho_casilla-1][alto_casilla-1] = BLANK
    return board


def getBlankPosition(board):
    for x in range(ancho_casilla):
        for y in range(alto_casilla):
            if board[x][y] == BLANK:
                return (x, y)


def makeMove(board, move):
    blankx, blanky = getBlankPosition(board)

    if move == ARRIBA:
        board[blankx][blanky], board[blankx][blanky + 1] = board[blankx][blanky + 1], board[blankx][blanky]
    elif move == ABAJO:
        board[blankx][blanky], board[blankx][blanky - 1] = board[blankx][blanky - 1], board[blankx][blanky]
    elif move == IZQUIERDA:
        board[blankx][blanky], board[blankx + 1][blanky] = board[blankx + 1][blanky], board[blankx][blanky]
    elif move == RIGHT:
        board[blankx][blanky], board[blankx - 1][blanky] = board[blankx - 1][blanky], board[blankx][blanky]


def isValidMove(board, move):
    blankx, blanky = getBlankPosition(board)
    return (move == ARRIBA and blanky != len(board[0]) - 1) or \
           (move == ABAJO and blanky != 0) or \
           (move == IZQUIERDA and blankx != len(board) - 1) or \
           (move == RIGHT and blankx != 0)


def getRandomMove(board, lastMove=None):
    validMoves = [ARRIBA, ABAJO, IZQUIERDA, RIGHT]

    if lastMove == ARRIBA or not isValidMove(board, ABAJO):
        validMoves.remove(ABAJO)
    if lastMove == ABAJO or not isValidMove(board, ARRIBA):
        validMoves.remove(ARRIBA)
    if lastMove == IZQUIERDA or not isValidMove(board, RIGHT):
        validMoves.remove(RIGHT)
    if lastMove == RIGHT or not isValidMove(board, IZQUIERDA):
        validMoves.remove(IZQUIERDA)

    return random.choice(validMoves)


def getLeftTopOfTile(tileX, tileY):
    left = margenx + (tileX * tamaño_casilla) + (tileX - 1)
    top = margeny + (tileY * tamaño_casilla) + (tileY - 1)
    return (left, top)


def getSpotClicked(board, x, y):
    for tileX in range(len(board)):
        for tileY in range(len(board[0])):
            left, top = getLeftTopOfTile(tileX, tileY)
            tileRect = pygame.Rect(left, top, tamaño_casilla, tamaño_casilla)
            if tileRect.collidepoint(x, y):
                return (tileX, tileY)
    return (None, None)


def drawTile(tilex, tiley, number, adjx=0, adjy=0):
    left, top = getLeftTopOfTile(tilex, tiley)
    pygame.draw.rect(DISPLAYSURF, TILECOLOR, (left + adjx, top + adjy, tamaño_casilla, tamaño_casilla))
    textSurf = letrabasica.render(str(number), True, TEXTCOLOR)
    textRect = textSurf.get_rect()
    textRect.center = left + int(tamaño_casilla / 2) + adjx, top + int(tamaño_casilla / 2) + adjy
    DISPLAYSURF.blit(textSurf, textRect)


def makeText(text, color, bgcolor, top, left):
    textSurf = letrabasica.render(text, True, color, bgcolor)
    textRect = textSurf.get_rect()
    textRect.topleft = (top, left)
    return (textSurf, textRect)


def drawBoard(board, message):
    DISPLAYSURF.fill(BGCOLOR)
    if message:
        textSurf, textRect = makeText(message, colormensaje, BGCOLOR, 5, 5)
        DISPLAYSURF.blit(textSurf, textRect)

    for tilex in range(len(board)):
        for tiley in range(len(board[0])):
            if board[tilex][tiley]:
                drawTile(tilex, tiley, board[tilex][tiley])

    left, top = getLeftTopOfTile(0, 0)
    width = ancho_casilla * tamaño_casilla
    height = alto_casilla * tamaño_casilla
    pygame.draw.rect(DISPLAYSURF, COLORBORDE, (left - 5, top - 5, width + 11, height + 11), 4)

    DISPLAYSURF.blit(RESET_SURF, RESET_RECT)
    DISPLAYSURF.blit(NEW_SURF, NEW_RECT)
    DISPLAYSURF.blit(SOLVE_SURF, SOLVE_RECT)


def slideAnimation(board, direction, message, animationSpeed):

    blankx, blanky = getBlankPosition(board)
    if direction == ARRIBA:
        movex = blankx
        movey = blanky + 1
    elif direction == ABAJO:
        movex = blankx
        movey = blanky - 1
    elif direction == IZQUIERDA:
        movex = blankx + 1
        movey = blanky
    elif direction == RIGHT:
        movex = blankx - 1
        movey = blanky


    drawBoard(board, message)
    baseSurf = DISPLAYSURF.copy()
    
    moveLeft, moveTop = getLeftTopOfTile(movex, movey)
    pygame.draw.rect(baseSurf, BGCOLOR, (moveLeft, moveTop, tamaño_casilla, tamaño_casilla))

    for i in range(0, tamaño_casilla, animationSpeed):
        
        checkForQuit()
        DISPLAYSURF.blit(baseSurf, (0, 0))
        if direction == ARRIBA:
            drawTile(movex, movey, board[movex][movey], 0, -i)
        if direction == ABAJO:
            drawTile(movex, movey, board[movex][movey], 0, i)
        if direction == IZQUIERDA:
            drawTile(movex, movey, board[movex][movey], -i, 0)
        if direction == RIGHT:
            drawTile(movex, movey, board[movex][movey], i, 0)

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def generateNewPuzzle(numSlides):
    sequence = []
    board = getStartingBoard()
    drawBoard(board, '')
    pygame.display.update()
    pygame.time.wait(500) 
    lastMove = None
    for i in range(numSlides):
        move = getRandomMove(board, lastMove)
        slideAnimation(board, move, 'Reorganizando las casillas para nuevo juego...', animationSpeed=int(tamaño_casilla / 3))
        makeMove(board, move)
        sequence.append(move)
        lastMove = move
    return (board, sequence)


def resetAnimation(board, allMoves):
    
    revAllMoves = allMoves[:] 
    revAllMoves.reverse()

    for move in revAllMoves:
        if move == ARRIBA:
            oppositeMove = ABAJO
        elif move == ABAJO:
            oppositeMove = ARRIBA
        elif move == RIGHT:
            oppositeMove = IZQUIERDA
        elif move == IZQUIERDA:
            oppositeMove = RIGHT
        slideAnimation(board, oppositeMove, '', animationSpeed=int(tamaño_casilla / 2))
        makeMove(board, oppositeMove)


if __name__ == '__main__':
    main()