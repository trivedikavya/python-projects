<h1> PYTHON PROJECTS OUTPUT</h1> 
<H2> 1] CHAT-BOT </H2> <br>
<img src="Screenshot (15).png" alt="Chatbot img" >
<a href="https://github.com/trivedikavya/python-projects/blob/main/chatbot.py">CODE LINK</a>
<H2> 2] ATM </H2> <br>
<img src=" " alt="ATM img" >
<a href="https://github.com/trivedikavya/python-projects/blob/main/chatbot.py">CODE LINK</a>

#### Python

```python
from collections import deque, defaultdict

class Solution:
    def bottomView(self, root):
        res = []
        if not root:
            return res
        
        bottom_view_map = defaultdict(int)
        q = deque([(root, 0)])
        
        while q:
            node, hd = q.popleft()
            bottom_view_map[hd] = node.data
            
            if node.left:
                q.append((node.left, hd - 1))
            if node.right:
                q.append((node.right, hd + 1))
        
        for key in sorted(bottom_view_map.keys()):
            res.append(bottom_view_map[key])
        
        return res
```

