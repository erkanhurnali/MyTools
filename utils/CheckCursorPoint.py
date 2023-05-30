import datetime
import math

class CheckCursorPoint():
    def __init__(
        self,
        currentX=int,
        currentY=int,
        currenTime=datetime,
        radius: int = 50,


    ) -> None:
        self.currentX = currentX
        self.currentY = currentY
        self.oldX = currentX
        self.oldY = currentY
        if datetime.timedelta.total_seconds(currenTime - datetime.datetime.now()) > 3.0:
            self.oldX = self.currentX
            self.oldY = self.currentY

        currentPoint = [currentX, currentY]
        oldPoint = [self.oldX, self.oldY]
        distanseBetweenTwoPoints = math.dist(currentPoint, oldPoint)
        absoluteDifferance = abs(distanseBetweenTwoPoints)
        return absoluteDifferance > radius

        # pass

    def checkCursor(
        # self,
        oldX: int = None,
        oldY: int = None,

    ) -> bool:
        # if (oldX is None) and (oldY is None):
        #     oldX = currentX
        #     oldY = currentY
        # currentPoint = [currentX, currentY]
        # oldPoint = [oldX, oldY]
        # distanseBetweenTwoPoints = math.dist(currentPoint, oldPoint)
        # absoluteDifferance = abs(distanseBetweenTwoPoints)
        # return absoluteDifferance > radius
        pass
