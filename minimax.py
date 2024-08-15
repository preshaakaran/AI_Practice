import math


def minimax(curDepth, nodeIndex, isMax, scores, targetDepth):
    # Base case: targetDepth reached
    if curDepth == targetDepth:
        return scores[nodeIndex]

    if isMax:
        # For maximizing player, choose the maximum value among children
        maxEval = -math.inf
        leftChildIndex = nodeIndex * 2
        rightChildIndex = nodeIndex * 2 + 1
        maxEval = max(maxEval, minimax(
            curDepth + 1, leftChildIndex, False, scores, targetDepth))
        maxEval = max(maxEval, minimax(
            curDepth + 1, rightChildIndex, False, scores, targetDepth))
        return maxEval
    else:
        # For minimizing player, choose the minimum value among children
        minEval = math.inf
        leftChildIndex = nodeIndex * 2
        rightChildIndex = nodeIndex * 2 + 1
        minEval = min(minEval, minimax(
            curDepth + 1, leftChildIndex, True, scores, targetDepth))
        minEval = min(minEval, minimax(
            curDepth + 1, rightChildIndex, True, scores, targetDepth))
        return minEval

# Driver code
scores = [10, 9, 14, 18, 5, 4, 50, 3]
treeDepth = int(math.log(len(scores), 2))
print("The optimal value is:", end=" ")
print(minimax(0, 0, True, scores, treeDepth))