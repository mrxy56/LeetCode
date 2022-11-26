class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n, m = len(image), len(image[0])
        for i in range(n):
            for j in range(m // 2):
                image[i][j], image[i][m - 1 - j] = image[i][m - 1 - j], image[i][j]
        for i in range(n):
            for j in range(m):
                image[i][j] = 1 - image[i][j]
        return image