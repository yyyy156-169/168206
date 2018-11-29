class table :  
        graph = {}  
        graph["乐谱"] = {}  
        graph["乐谱"]["唱片"] = 5  
        graph["乐谱"]["海报"] = 0  
        graph["唱片"] = {}  
        graph["唱片"]["吉他"] = 15  
        graph["唱片"]["架子鼓"] = 20  
        graph["海报"] = {}  
        graph["海报"]["吉他"] = 30  
        graph["海报"]["架子鼓"] = 35  
        graph["架子鼓"] = {}  
        graph["架子鼓"]["钢琴"] = 10  
        graph["吉他"] = {}  
        graph["吉他"]["钢琴"] = 20 
        graph["钢琴"] = {}  
        infinity = float("inf")  
        costs = {}  
        costs["唱片"] = 5  
        costs["海报"] = 0  
        costs["吉他"] = infinity  
        costs["架子鼓"] = infinity   
        costs["钢琴"] = infinity    
        parents = {}  
        parents["唱片"] = "乐谱"  
        parents["海报"] = "乐谱"  
        parents["吉他"] = None  
        parents["架子鼓"] = None  
        parents["钢琴"] = None  
        processed = []   
  
   def find_lowest_cost_node(costs):	  
      lowest_cost = float('inf')  
      lowest_cost_node = None	  
      for node in costs:			  
         if not node in processed:				  
                if costs[node] < lowest_cost:				  
                  lowest_cost = costs[node]				  
                  lowest_cost_node = node	  
      return lowest_cost_node   
     
  def find_less_path():	  
      node = "钢琴"	  
      less_path = ["钢琴"]	  
      while table.parents[node] != "乐谱":		  
          less_path.append(table.parents[node])		  
          node = table.parents[node]	  
      less_path.append("乐谱")	  
      return less_path  
    
  def find():  
      node = find_lowest_cost_node(table.costs)	  
      while node is not None:				  
          cost =table.costs[node]			  
          neighbors =table. graph[node]			  
         for n in neighbors :			  
  	     new_cost = cost + neighbors[n]			  
             if new_cost <table. costs[n]:				  
                 table.costs[n] = new_cost				  
                 table.parents[n] = node		  
          print(node)  
          processed.append(node)		  
          node = find_lowest_cost_node(table.costs)	  
      less_path = find_less_path()	  
      less_path.reverse()	  
      print(less_path)		  
 find() 
