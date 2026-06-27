class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first count the digit and the count and store in dictionary
        # then send the keys accordingly
        count_dict = {}
        for i in nums:
            count_dict[i] = count_dict.get(i, 0) + 1
        
        result = []

    # Find the top k elements

        for _ in range(k):
            max_key = max(count_dict, key=count_dict.get)
            result.append(max_key)
            del count_dict[max_key]  # remove it so we can find the next maximum

        return result
            