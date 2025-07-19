#splaying with dic and lt
# lt = [1,2,3,4,5,6,7,8,np.nan,10,11]
# # dic = {'deep':1,'ghetia':2}
# # s = pd.Series(lt, index=[9,9,9,9,9], name='deep') #note here we can have same index to multiple elements
# s = pd.Series(lt, index=[9,9,9,9,9,9,9,9,9,9,9], name='deep') #if you see the code we are replacing the index alues but what does python do is 
# # print(s) #it finds the index values passed in list to map it with dic keys if found then data is prsent if not then NaN.

#####
val = list(s[s.apply(lambda x: type(x) == int)])
final_m = sum(val)/len(s)

def filtered(s, final_m):
    if isinstance(s,float) and s > final_m:
        return True
    else:
        return False
    
print(s[s.apply(lambda x: filtered(x, final_m))])

########
def filtering(s):
    if s[0] in 'ae':
        return True
    else:
        return False
    
val = s[s.index.isin(list('aeiou')) & s.apply(filtering)]
print(val)

###########
val = s[(s!=0) & (s%3==0)] #bracket are really important keep in mind

########
val = s[(s.index == s) | (s.apply(lambda x: isinstance(x,bool)))]
print(val)