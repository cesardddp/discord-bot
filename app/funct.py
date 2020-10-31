palavroes = ["PUTA","KRL","CACETE","BUCETA","FUDER","PUNHETA","PIKA","PIKASSO","CU","BOLSONARO"]

def pal_check(msg):
    listmsg =msg.split(" ")
    for i in listmsg:
        if i in palavroes:
            return 1
        
    return 0