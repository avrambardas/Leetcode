class Solution(object):
    def convert(self, s, numRows):
        
        if numRows < 2:
            return s
        
        word = list(s)
        index_len = 2*numRows-2
        index_nums =[]
        new_word = []
        counter = 0
        viewed = set()
        index_nums.append(counter)
        # create initial indexes
        while counter < len(word):
            counter += index_len
            index_nums.append(counter)
            viewed.add(counter)
        
        for i in range(numRows):
            for num in index_nums:
                if num < len(word):
                    new_word.append(word[num])
            
            # create the following indexes (+/- the previous indexes)
            new_index_nums = []
            for index in index_nums:
                num1 = index-1
                num2 = index+1
                if num1 > 0 and num1 not in viewed:
                    new_index_nums.append(num1)
                    viewed.add(num1)
                if num2 > 0  and num2 not in viewed:
                    new_index_nums.append(num2)
                    viewed.add(num2)
                new_index_nums = sorted(new_index_nums)
            index_nums = new_index_nums
        
        return("".join(new_word))
