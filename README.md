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