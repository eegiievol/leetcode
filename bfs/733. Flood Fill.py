# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

# You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

# Return the modified image after performing the flood fill.

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        directions = [(0,1), (1,0), (0,-1), (-1, 0)]
        visited = []
        color = image[sr][sc]
        rowlen, collen = len(image), len(image[0])
        q=deque()
        q.append((sr,sc))
        while q:
            popped = q.popleft()
            if popped in visited:
                continue
            visited.append(popped)
            row,col = popped
            image[row][col] = newColor
            for r,c in directions:
                if 0<=row+r<rowlen and 0<=col+c<collen and image[row+r][col+c]==color:
                    q.append((row+r, col+c))

        return image
     