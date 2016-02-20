text = "X-DSPAM-Confidence:    0.8475";
letter= text.find('0.8475')
str= text[23:]
final= float(str)
print final
