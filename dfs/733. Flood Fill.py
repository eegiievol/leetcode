# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

# You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

# Return the modified image after performing the flood fill.

 

# Example 1:


# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        direction = [(0,-1), (-1,0), (1,0), (0,1)]
        adj_list = defaultdict(list)
        
        for row in range(len(image)):
            for col in range(len(image[0])):
                for r,c in direction:                    
                    if 0<=row+r<len(image) and 0<=col+c<len(image[0]) and image[row][col]==image[row+r][col+c]:
                        adj_list[(row,col)].append((row+r, col+c))        
        
        visited = []
        q=deque()
        q.append(((sr,sc)))    
    
        while q:
            popped = q.popleft()
            image[popped[0]][popped[1]] = newColor
            visited.append(popped)
            for nei in adj_list[popped]:
                if nei not in visited:
                    q.append(nei)
        return image