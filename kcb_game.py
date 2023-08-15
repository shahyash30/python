Q = [ ["what is your name", "y","a","s","h",1],
      ["what is your age", "20","21","22","23",2],
      ["where do u live ", "hyd","mum","del","chennai",1],
      ["which is national bird of india ","peacock","lion","tiger","horse",1],
      ["how far is sum from earth","far", "veryfar ","so far","much far",4],
      ["seplling of chrome ","chrome ","crome","croma","chroma",1],
      ["what is vs code","idle","compiler","browser","extension",2],
      ["an umbrella is used for","rain","summer","winter","nothing",1],
      ["chair is used for ","sitting ","dancing","standing ","swimming",1],
      ["we need food to ","die","fill stomach","stay hydrated","dont need",2],
      ["what is your mother tongue ","gujarati","tel","marathi","english",1]
     ]

levels = [10,20,50,100,200,500,1000,2000,5000,10000,50000]   
money = 0

for i  in range(0,len(Q)):
    question = Q[i]
    print(f"give the answer for {Q[i][0]} :")
    print(f"a.{Q[i][1]}             b.{Q[i][2]}")
    print(f"c.{Q[i][3]}             d.{Q[i][4]}")

    reply = int(input("Enter your answer in (1-4):"))
    if(reply == question[-1]):
        print(f"You won Rs.{levels[i]}")
    elif(i==3):
        money == 100
    elif(i==6):
        money == 1000
    else:
        print(f"wrong ans, you won Rs.{levels[i-1]}")
        break


