class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for word in strs:
            character_count = [0]*26
            for character in word:
                # tally the characters
                character_count[ord(character) - ord("a")] += 1
            # use tally as a key to insert words
            if tuple(character_count) in map:
                map[tuple(character_count)].append(word)
            else:
                map[tuple(character_count)] = [word]
        return_list = []
        for key, value in map.items():
            return_list.append(value)
        
        return return_list

        