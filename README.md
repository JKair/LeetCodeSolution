LeetCodeSolution
=================
外国的一个算法网站，据说做完之后会有面试能力buff，面试成功率增加，哈，于是有事没事做做题，目测用python完成，涉及到树的可能使用C++，目前还在努力完成中，有时间就保持做题更新。

###记录

从easy做到hard
--------------
1. Excel Sheet Column Number：
这道题主要是思路的转换，一开始做的时候没转换过来，其实把这道题当成进制转换来做就可以了

1. Implement strStr()：
这道题可以很简单一行就解决，也可以做得有深度点，本来使用kmp，看到鸟哥的微博知道sunday或者bm更高效更容易理解，于是学习了sunday，当做练手了

1. pow(x,n):
快速幂AC

1. Remove Element:
总觉得这道题并不严谨，没有判定多个值一样的问题，处理是很简单的。直接删除然后返回长度

1. Plus One:
一开始没看懂在讲什么，后来才明白，给定一个数组然后+1，比如[1,9] + 1 = [2,0]，注意类型转换就可以了

1. Find Peak Element:
这个只是要返回最大值的下标而已，很简单，只要排序然后查找顺序就好。

1. Sort Colors:
数字代表颜色，然后小的放在前面，大的放在后面，解法很多，最常规的思路就是记录个数还有排序了。我使用的是另外一种，有点类似快排的思想，以1为基准，比1小的滚去左边，比1大的，滚去右边，完毕。

1. Add Two Numbers:
两个数相加，其实这道题就是一个大数相加问题而已，大一已经写过好几次的了，不过之前是字符串处理，现在变成树了，太久没写C++，有点不熟，浪费了点时间，不过解决起来的思路其实不难，就是我们小学所做的那种思路就可以解决此问题

1. Search Insert Position:
这道题的意思是给你一个数，你找一下在哪里插入，很简单，最简单就是把数加入数组，然后排个序，然后看一下下标就好了。另外也可以使用二分法，节省时间

1. Jump Game:
一开始不知道是什么意思，后来才理解了，原来只是一步一步走下去，没跨过一个下标就减一，但是每个下标又有新步数，最后看能不能走到最后。解题思路很简单，每一次都拿到最大步数，如果能走到最后return true，不能走到最后，就是在中途步数为0了就再见。

1. Swap Nodes in Pairs:
一开始我就弄错题意啊，悲剧啊！后来才弄清楚了，原来只是相邻交换而已。很容易，C++直接AC。

1. Linked List Cycle:
英语果然是硬伤啊，它要我们判断一下有没有环路，很简单的，就是直接两个指针，一个跑得快一个跑得慢，如果有环路的话，快的那个肯定会跑回来找到慢的那个的，不需要额外的记录了

1. Same Tree：
遍历结构而已，很简单，递归思想！

1. Symmetric Tree ：
这道题也很简单，算是Same Tree的变形，只要拆分成两棵树，两棵树镜像对称，那就只要一棵树的左等于另一棵树的右就可以解决问题了。依然是递归解决

1. Binary Tree Level Order Traversal：
其实就是分深度而已，使用一个参数去控制，搞定。依旧是递归解决

1. Maximum Depth of Binary Tree：
其实就是一个打擂和遍历而已。

1. Minimum Depth of Binary Tree：
这个和max不大一样，但是总体处理起来还是差不多的。解题过程中有点陷入思维误区，因为要的是最小深度，把left和right赋值为0了，之后永远是0。后来把right和left的值赋值为int_max之后才解决。思路也是递归算而已，算左子树的最小深度，再算右子树的深度，然后每次往下走就深度+1，最后得出左子树和右子树谁小就可以了。有点像分治。

1. Path Sum ：
这道题就是计算有没有路径的值等于sum而已，其实就是遍历，只要一边遍历一遍把根节点的值加上上一个节点的值就可以了，注意一个点，要算的是到叶子节点的地方，不是找一条路径等于就好！

1. Path SumII：
这道题是path sum的变形，要记录路径，所以思路换一下，不改变节点的值了，改变sum的值

1. Merge Intervals：
这个只是区间合并而已，不是太难，先排好序，然后只要前一个元素的结尾大于后一个元素的结尾，那就可以比对一下结尾是谁大，因为存在包含情况，所以核心就是比对结尾了。比如存在这种情况:[1,5] [2,4]，注意细节处理就可以AC了

1. Insert Interval:
这道题其实本身也不难的，只要找出需要处理的区间就好了，然后一开始懒惰，没有多加思考，以为O(n)肯定不会超时，结果还是超了，郁闷至极，以为是出现在apppend上，结果去除了各种排序。还是不行，到最后，直接砍掉不需要循环的地方，AC 

1. Remove Duplicates from Sorted List：
删除前后一样的节点，很简单。只要判断前后节点一样，那么就让当前节点等于下一个节点，相当于缩短链表。

1. Maximum Subarray:
一开始我是直接穷举记录的，超空间了。第二次穷举但是不记录，超时了，原因是我使用了两次循环，O(n^2)超时超成狗，然后就换成现在这种思路，后来我发现，其实你每次加加加加，如果加完之后小于0了，或者变小了，那就证明没有之前那个好，那我只要两个变量，一个始终记录最好的情况，另外一个一直往前加就好了，但是有一个情况，如果加完这次，小于0了，那证明这次加是坏情况，前面的全部舍弃了，再从下一个数开始往后加，如此，题解

1. Spiral Matrix:
我的解法只是纯粹的事件模拟而已，没技术含量，晚点再找一些更有技术含量的解法吧。

1. Reverse Words in a String:
倒转字符串，很简单，就是只要split处理，然后要注意的一个细节就是，要还给人家一个空格，而且注意，因为存在两个单词之间有五千万个空格这种坑爹的情况，所以如果切割之后为""切勿加上空格。

1. First Missing Positive:
我没有想到很好的方法，先写着一种比较垃圾的。

1. Binary Tree Zigzag Level Order Traversal：
这个其实就是(Maximum Depth of Binary Tree)[https://github.com/JKair/LeetCodeSolution/blob/master/1.Easy/Maximum%20Depth%20of%20Binary%20Tree.cpp]的变形来的，一开始脑筋没转过来，一直想怎么让深度为双数的倒转过来。其实只要全部数据遍历完毕在用vector来倒转就好了- -。哎，越简单越是想不到。我的错