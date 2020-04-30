# [1,2,null,null,3,4,null,null,5,null,null]
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1byte for flag indicating type of node
# 4byte for the node value
# [1byte flag][4byte data]

# 0x0 -> Null
# 0x1 -> Node
# 0x2 -> has left
# 0x4 -> has right

# Flag
# '000' -> null
# '001' -> node with no childrens
# '101' -> node with only right child
# '011' -> node with only left child
# '111' -> node with two childrens


class Codec:
    @staticmethod
    def encode_flag(node):
        flag = 0x0
        if node:
            flag |= 0x1
            if node.left: flag |= 0x2
            if node.right: flag |= 0x4
        return flag
    
    def serialize(self, root):
        # result = []
        # def encode(node):
        #     if not node: return result.append('null')
        #     result.append(str(node.val))
        #     encode(node.left)
        #     encode(node.right)
        # encode(root)
        # s = ','.join(result)
        out = io.BytesIO()
        def encode(node):
            flag = self.encode_flag(node)
            out.write(flag.to_bytes(1, 'little'))
            if not node: return
            out.write(node.val.to_bytes(4, 'little', signed=True))
            if node.left: encode(node.left)
            if node.right: encode(node.right)
        encode(root)
        out.seek(0)
        s = out.read()
        return s

    def deserialize(self, data):
        # deque = collections.deque(data.split(','))
        # def decode():
        #     node_str = deque.popleft()
        #     if node_str == 'null': return None
        #     node = TreeNode(int(node_str))
        #     node.left = decode()
        #     node.right = decode()
        #     return node
        stream = io.BytesIO(data)
        def decode():
            flag = int.from_bytes(stream.read(1), 'little')
            if ~flag & 0x1: return None
            node = TreeNode(int.from_bytes(stream.read(4), 'little', signed=True))
            node.left = None if ~flag & 0x2 else decode()
            node.right = None if ~flag & 0x4 else decode()
            return node
        root = decode()
        return root
            
            
            
            
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))