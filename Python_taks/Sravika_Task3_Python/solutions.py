#Q1. Find the Frequency of Each Word in a Sentence
def word_frequency(s):
    S=s.split()
    freq={}
    for word in S:
        if word in freq:
            freq[word]+=1 
        else:
            freq[word]=1
    return freq    

#Q2. Find the Frequency of Each Character in a Word
def character_freq(s):
    freq={}
    for ch in s:
        if ch in freq:
            freq[ch]=freq[ch]+1 
        else:
            freq[ch]=1 
    return freq

#3. Find the First Non-Repeating Character in a Word
def non_repeating(w):
    freq={}
    for ch in w:
        if ch in freq:
            freq[ch]+=1 
        else:
            freq[ch]=1 
    for c in freq:
        if freq[c]==1:
            return c
            break
    else:
        return "None"

#Q4. Check Whether Two Strings Are Anagrams
def anagram(s1,s2):
    if sorted(s1)==sorted(s2):
        return "True"
    else:
        return "False"

#Q5. Find the First Repeating Character in a String
def repeating_char(s):
    freq={}
    for ch in s:
        if ch in freq:
            freq[ch]+=1 
        else:
            freq[ch]=1
    print(freq)
    for ch in freq:
        if freq[ch]==2:
            return ch 
            break
    else:
        return "None"

#6.Move All Zeros to the End of a List
def zeroes_to_end(l):
    non_zeroes=[]
    zeroes=[]
    for num in l:
        if num==0:
            zeroes.append(num)
        else:
            non_zeroes.append(num) 
    return non_zeroes+zeroes

#Q7. Find the Second Highest Distinct Number in a List
def second_distinct(n):
    l=[]
    for num in n:
        if num not in l:
            l.append(num)
    
    s=sorted(l,reverse=True)
    if len(s)>1:
        return s[1]
    else:
        return "None"

#Q8. Remove Duplicates Without Changing the Original Order
def unique(l):
    unique=[]
    for num in l:
        if num not in unique:
            unique.append(num)
    return unique

#Q9. Find the Missing Number from 1 to N
def missing_number(l,N): 
    n=len(l)+1 
    total_sum=n*(n+1)//2 
    actual_sum=sum(l)
    return (total_sum-actual_sum)

#Q10. Find Two Numbers Whose Sum Equals a Target
def two_sum(nums,target):
    l=[]
    for i in nums:
        for j in nums:
            if i==j:
               continue 
            else:
                if i+j==target:
                    l.append([i,j])
                    break 
    if len(l)>0:
       return l[0]
    else:
       return "None"

#Q11. Find the Number Closest to Zero
def closest_to_zero(l):
    s=sorted(l)
    for num in s:
       if num>0:
           return num
           break

#12. Find Common Elements Between Two Lists
def common_elements(l1,l2):
    l=[]
    for num in l1:
        if num in l2:
            l.append(num)
    return l

#Q13. Rotate a List to the Right by K Positions
def rotate_right(l, k):
    k = k % len(l)   # handle cases where k > len(l)
    return l[-k:] + l[:-k]


#Q14. Find the Maximum Sum of Two Consecutive Elements
def consecutive(nums):
    if len(nums) < 2:
        return None  # Not enough elements for consecutive pairs
    
    max_sum = nums[0] + nums[1]  # initialize with first pair
    for i in range(1, len(nums) - 1):
        current_sum = nums[i] + nums[i + 1]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum

    

#Q15. Find All Pairs of Numbers Whose Sum Equals a Target
def find_pairs(nums, target):
    pairs = set()   # Step 1: store unique pairs

    # Step 2: check all pairs
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                # Step 3: sort each pair so smaller number comes first
                if nums[i] < nums[j]:
                    pair = (nums[i], nums[j])
                else:
                    pair = (nums[j], nums[i])
                pairs.add(pair)

    # Step 4: convert set to list of lists
    result = []
    for p in pairs:
        result.append([p[0], p[1]])

    # Step 5: sort by first element ascending
    result.sort(key=lambda x: x[0])

    return result
    
def two(l,t):
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]+l[j]==t:
                return l[i],l[j]
print(two([2,7,11,15],9))