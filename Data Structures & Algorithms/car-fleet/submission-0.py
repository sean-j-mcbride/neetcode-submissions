class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        stack = []
        car_fleets = 0

        for i in range(len(position)):
            arr.append((position[i], speed[i]))
        
        arr.sort(key=lambda tup: tup[0], reverse=True)

        for elt in arr:
            curr_time = (target - elt[0]) / elt[1]
            if stack:
                if curr_time > stack[-1]:
                    stack.append(curr_time)
            else:
                stack.append(curr_time)
        return len(stack)



