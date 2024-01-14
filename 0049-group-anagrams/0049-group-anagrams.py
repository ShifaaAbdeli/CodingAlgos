class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_grpAnag = collections.defaultdict(list)
        for s in strs:
            dict_grpAnag[tuple(sorted(s))].append(s)
        return dict_grpAnag.values()
        