def cryptology(sellected,entry):
    famework = { " ":".",   "A":"M$3d!","B":"Z1s9+","C":"NsG93"
                ,"D":"B?4*T","E":"V#4AX","F":"C!2+E","G":"L%3P^"
                ,"H":"AR1-4","I":"K4$#!","J":"JT7+/","K":"J585%"
                ,"L":"SL43+","M":"F46^^","N":"K566&","O":"G16#6"
                ,"P":"W74QE","Q":"Z^24D","R":"C47F7","S":"B+47H"
                ,"T":"W43+R","U":"E8E4L","V":"W?*4E","W":"M'4K+"
                ,"X":"RQ4&'","Y":"TQ4.3","Z":"P3<>3","Ç":"OP8aİ"
                ,"Ğ":"I?5?H","İ":"U52^W","Ö":"Y&0%+","$":"_?4Şj"
                ,"Ü":"JC2+X","Ş":"VA5/*","0":"i/7*s","1":"d7t4*"
                ,"2":"d41d7","3":"A14/*","4":"V211*","5":"41A/*"
                ,"6":"V75/*","7":"d11/*","8":"gA/1*","9":"V0,/*"
                ,"/":"05A/*","*":"st#0!","-":"a516!","+":"!'44w"
                ,",":"?ğ0oj","!":"gs055","'":"^BX0D","^":"441$!"
                ,"%":"?=(1R","&":"as615","(":"2k1lo",")":"ıf2fh"
                ,"=":"d52ks","?":"dfg25","_":"ft2f5","{":"zs55s"
                ,"}":"r455t","[":"s5t5f","]":"h,857","<":"df5dt"
                ,">":"b5d44",".":"vbb12",":":"MFG72",";":"MK24*"
                ,"|":"LD5R5","`":"+5i5ü","q":"e5d4%","w":"f5şLĞ"
                ,"e":"s1dv4","r":"adv28","t":"ch3n7","y":"gg4=?"
                ,"u":"jh5d+","ı":"+85h)","o":"158ü?","p":"6i8şK"
                ,"ğ":"5d9j/","ü":"q496%","a":"j79/*","s":"H7Y//"
                ,"d":"M87/6","f":"Kj87/","g":"FT74+","h":"Ç:8İi"
                ,"j":"5J,d7","k":"kF+,5","l":"mf0)5","ş":"5;0ğp"
                ,"i":"50:?,","z":"5şj09","x":"52,-9","c":"012şp"
                ,"v":"0eı4u","b":"0144-","n":"3e4r4","m":"Wff46"
                ,"ö":"4r443","ç":":j4gf","é":"5454ş","@":"d1!d1"
                ,"#":"?=4ol"}
    famework2 = {}
    for x,y in famework.items():
        famework2[y] = x
    def encrtiption(text3):
        key = ""
        text_len = len(text3)
        for shred_text in range(0,text_len):
            key += str(famework.get(text3[shred_text]))
        
        return key
    def decription(keyword):
        point = 0
        text2 = ""
        while point < len(keyword):
            if "." in keyword[point:point+4]:
                point +=1
                text2 += " "
            else:
                text2 += str(famework2.get(keyword[point:point+5]))
                point += 5
    
        return text2
    
    
    selection = sellected
    
    if selection == "1":
        text_entry = entry
        return decription(text_entry)
    elif selection == "2":
        text_entry = entry
        return encrtiption(text_entry)
    
print("**************MENU**************")
print("1-ENCRİPTİON")
print("2-DENCRİPTİON")
print("********************************")
select = input("WHAT DO YOU WANT TO DO:")
print("********************************")
if select=="1":
    istext = input("Enter the text to be encrypted:")
    print("********************************")
    str(istext)
    text=cryptology("2",istext)
    print("ENCRİPTİON:\n",text)
else:
    istext = input("Enter the text to be decrypted:") 
    print("********************************")
    str(istext)
    text=cryptology("1",istext)
    print("DENCRİPTİON:\n",text)
