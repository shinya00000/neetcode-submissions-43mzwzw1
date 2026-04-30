class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = len(position)
        max_time = 0
        group_count = 0
        car_dict = []
        for i in range(cars):
            car_dict.append([position[i], speed[i]])
        car_dict.sort(reverse=True)
        print(car_dict)
        for i in range(cars):
            cur_time = (target - car_dict[i][0])/car_dict[i][1]
            if cur_time > max_time:
                max_time = cur_time
                group_count += 1
        return group_count