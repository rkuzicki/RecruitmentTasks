data BinaryTree a = EmptyTree | Node Int (BinaryTree Int) (BinaryTree Int)
    deriving (Show)

treeInsert :: Int -> BinaryTree Int -> BinaryTree Int
treeInsert x EmptyTree = Node x EmptyTree EmptyTree
treeInsert x (Node p left right)
    | x <= p = Node p (treeInsert x left) right
    | x > p = Node p left (treeInsert x right)

inOrder :: BinaryTree Int -> [Int]
inOrder EmptyTree = []
inOrder (Node x left right) = inOrder left ++ [x] ++ inOrder right

treeSum :: BinaryTree Int -> Int
treeSum EmptyTree = 0
treeSum bt = foldl (+) 0 $ inOrder bt

find :: Int -> BinaryTree Int -> BinaryTree Int
find x EmptyTree = EmptyTree
find x (Node a left right)
    | x == a = Node x left right
    | x < a = find x left
    | x > a = find x right

testTree :: BinaryTree Int
testTree = treeInsert 3 (treeInsert 1 (treeInsert 9 (treeInsert 4 (treeInsert 0 (treeInsert 4 EmptyTree)))))

avg :: BinaryTree Int -> Float
avg bt = (fromIntegral $ treeSum bt) / (fromIntegral . length $ inOrder bt)

median :: BinaryTree Int -> Float
median bt
    | size == 0 = 0
    | odd size = fromIntegral $ arr !! mid
    | even size = fromIntegral (arr !! mid + arr !! (mid-1)) / 2
    where
        arr = inOrder bt
        size = length $ inOrder bt
        mid = length arr `div` 2
