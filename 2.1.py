text = "X-DSPAM-Confidence:    0.8475";
chp = text.find(' ')
print(float(text[chp:].lstrip()))