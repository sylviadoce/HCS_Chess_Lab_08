#Author: Sahil Agrawal

from Piece import Piece

class King(Piece):
    '''King subclass'''
    def calcListDirections(self):
        '''returns the list of directions and the number of spaces it can go in each direction'''
        numSpaces = 1
        listDir = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]

        return listDir,1



class Bishop(Piece):
    '''Bishop subclass'''
    def calcListDirections(self):
        '''returns the list of directions and the number of spaces it can go in each direction'''
        numSpaces = 10
        listDir = [[1,1],[1,-1],[-1,1],[-1,-1]]

        return listDir,10


