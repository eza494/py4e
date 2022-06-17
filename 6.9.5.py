str = 'X-DSPAM-Confidence:0.8475'
numindex = str.find(':')
newstr = str[numindex+1:]
new = float(newstr)
