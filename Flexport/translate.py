def letterCombinations(digits):
    if digits == "":
            return []
    dic = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], 
            '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z'], '23':['mn']}
    res = []

    def backtracking(idx, path):
          #print(idx, path)
          if idx == len(digits):
                res.append(path.copy())
                return
          for i in range(idx+1, len(digits)+1):
                if digits[idx:i] in dic.keys():
                      path.append(digits[idx:i])
                      backtracking(i, path)
                      path.pop()
    
    backtracking(0, [])
    print(res)
    ans = set()
    
    def combine(idx, path, digit):
          if idx == len(digit):
                ans.add("".join(path))
                return
          for d in dic[digit[idx]]:
                path.append(d)
                combine(idx+1, path, digit)
                path.pop()
    for digit in res:
          combine(0, [], digit)
    return list(ans)

print(letterCombinations('23'))

    