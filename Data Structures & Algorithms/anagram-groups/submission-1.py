class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = 0
        output_list = []
        for a in range(len(strs)):
            if strs[a] != None:
                output_list.append([])
                output_list[count].append(strs[a])
                for b in range(a+1,len(strs)):
                    if strs[b] != None:
                        a_dict = dict()
                        b_dict = dict()
                        for i in strs[a]:
                            a_dict[i] = 0
                        for i in strs[a]:
                            a_dict[i] += 1
                        for j in strs[b]:
                            b_dict[j] = 0
                        for j in strs[b]:
                            b_dict[j] += 1
                        if a_dict == b_dict:
                            output_list[count].append(strs[b])
                            strs[b] = None
                strs[a] = None
                count += 1
        return output_list
