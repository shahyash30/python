q1 = [
    ["what is capital of India ","Telangana","Delhi","Andhra pradesh","Goa","none",2],
    ["what is capital of Delhi","Bhuvaneshwar","Goa","New Delhi","Tamil nadu","none",3],
    ["what is capital of Telangana","Mumbai","Banglore","Thiruvananthapuram","Hyderabad","none",4],
    ["what is capital of Tamil nadu","Hyderabad","Chennai","Banglore","Panji","none",2],
    ["what is capital of kerala","Thiruvananthapuram","Chennai","Srinagar","Ranchi","none",1],
    ["what is capital of Karnataka","Raipur","Goa","Hyderabad","Banglore","none",4],
    ["what is capital of Andhar pradesh","Amaravati","Panji","Dispur","Gangtok","none",1],
    ["what is capital of Maharastra","Punjab","Hyderbad","Mumbai","Gangtok","none",3],
    ["what is capital of Madhya pradesh","Tiruvananthapuram","Bhuvaneshwar","Banglore","Dispur","none",2],
    ["what is capital of Odissa","Ghandhi nagar","Bhuvaneshwar","Washington DC","Panji","none",2],
    ["what is capital of Punjab","Chatisghar","Srinagar","Jersy","Chandigarh","none",4],
    ["what is capital of Jammu and Kashmir","Srinagar","Panji","New Delhi","Shellong","none",1],
    ["what is capital of Arunachal pradesh","Shellong","Sikkim","Itanagar","Dispur","none",3],
    ["what is capital of sikkim","teja","Sikkim","Gangtok","Manipur","none",2],
    ["what is capital of Meghalaya","Hyderabad","Itanagar","Shellong","Dispur","none",3],

]
price = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
money = 0 
for i in range(0,len(q1)):
    question = q1[i]
    print(f"\n\n{question[0]}")
    print(f"a.{question[1]}    b.{question[2]}")
    print(f"c.{question[3]}    d.{question[4]}")
    reply = int(input("enter your answer between (1-4) or 0 to quit "))
    if(reply==0):
        money = price[i-1]
        break
    if(reply == question[-1]):
        print(f"correct answer, you won rs.{price[i]}")
        if(i==4):
            money = 10000
        elif(i==9):
            money = 320000
        elif(i==14):
            money = 10000000 

    else:
        print("wrong answer!")
        break
                
print(f"your take home money is {money}") 