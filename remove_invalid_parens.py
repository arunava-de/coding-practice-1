# def is_valid(s):

#     S = [] 

#     for i in range(len(s)):
#         if s[i]==")":
#             if S!=[]:
#                 return False
#             else:
#                 S.pop()
#         else:
#             S.append(s[i])

#     return S==[] 
    
class Solution(object):

    def __init__(self):
        self.valid_exps = None 
        self.min_removed = None 

    def reset(self):
        self.valid_exps = set()
        self.min_removed = float('inf') # Keeps track of global minima of parentheses removed 

    def recur(self, s, idx, lc, rc, curr, rem):

        if idx==len(s):
            if lc==rc: # Valid expression 
                if rem<=self.min_removed:
                    cand = "".join(curr)

                    if rem<self.min_removed: # We clear all previous solutions since new minima found 
                        self.valid_exps = set()
                        self.min_removed = rem 

                    self.valid_exps.add(cand)
        else:
            if s[idx]!="(" and s[idx]!=")":
                curr.append(s[idx])
                self.recur(s, idx+1, lc, rc, curr, rem)
                curr.pop()
            else:
                # For both opening and closing, we can choose to include or ignore
                self.recur(s, idx+1, lc, rc, curr, rem+1)

                curr.append(s[idx])

                if s[idx]=='(':
                    self.recur(s, idx+1, lc+1, rc, curr, rem)
                elif rc<lc:
                    self.recur(s, idx+1, lc, rc+1, curr, rem)
                
                curr.pop()

    def removeInvalidParentheses(self, s):

        self.reset()

        self.recur(s, 0, 0, 0, [], 0)

        return self.valid_exps
