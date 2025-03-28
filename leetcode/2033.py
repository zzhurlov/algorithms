class Solution:
    def minOperations(self, grid, x: int) -> int:
        data = []
        for arr in grid:
            for i in arr:
                data.append(i)
        data.sort()

        ost = data[0] % x

        for i in data:
            if i % x != ost:
                return -1

        # мы здесь ищем среднее число к которому мы будем приходить
        average = sum(data) // len(data)

        target = None

        for i in range(len(data) - 1):
            if data[i] == average:
                target = data[i]
                break

            if data[i] < average < data[i + 1]:
                if average - data[i] > data[i + 1] - average:
                    target = data[i + 1]
                else:
                    target = data[i]
                break

        sm = 0

        for i in data:
            sm += abs(target - i) // x

        return sm


print(
    Solution.minOperations(
        Solution,
        [
            [980, 476, 644, 56],
            [644, 140, 812, 308],
            [812, 812, 896, 560],
            [728, 476, 56, 812],
        ],
        84,
    )
)
