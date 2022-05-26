
def twoSum(self, nums: list[int], target: int) -> list[int]:
    values = {} # Creamos el diccionario
    for idx, value in enumerate(nums):
        if target - value in values:
            return [values[target - value], idx]
        else:
            values[value] = idx
