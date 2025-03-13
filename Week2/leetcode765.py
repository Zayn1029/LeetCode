class Solution:
    def minSwapsCouples(self, row):
        n = len(row)
        pos = {}
        for i in range(n):
            pos[row[i]] = i
        
        swaps = 0

        for i in range(0, n, 2):
            person = row[i]
            partner = person + 1 if person % 2 == 0 else person - 1
            

            if row[i + 1] != partner:
                partner_pos = pos[partner]           
                row[i + 1], row[partner_pos] = row[partner_pos], row[i + 1]                
                pos[row[i + 1]] = i + 1
                pos[row[partner_pos]] = partner_pos
                
                swaps += 1
        
        return swaps

