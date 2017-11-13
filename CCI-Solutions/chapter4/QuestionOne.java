import java.lang.*;

class Node {
    int data;
    Node left_child;
    Node right_child;

    public Node(int data, Node left_child, Node right_child)
    {
        this.data = data;
        this.left_child = left_child;
	    this.right_child = right_child;
    }
    public Node()
    {
	    this.data = 0;
	    this.left_child = null;
	    this.right_child = null;
    }
}

/**
* Question 4.1
* Implement a function to check if a tree is balanced For the 
* purposes of this question, a balanced tree is defined to be 
* a tree such that no two leaf nodes differ in distance from 
* the root by more than one
*/
public class QuestionOne {
    
    /**
 	* findHeightBFS
 	*
 	* @param (root) (root node of tree)
  	* @param (height) (distance from root)
 	* @return (integer indicating the height of the tree)
 	*/
    static int findHeightBFS(Node root, int height)
    {
        int left, right;
        if(root.left_child == null && root.right_child==null)
	    {
		    return height;
	    }
	    if(root.left_child != null) {
		    left = findHeightBFS(root.left_child, height++);
	    }
	    else {
		    left = 0;
	    }
	    if(root.right_child != null) {
		    right = findHeightBFS(root.right_child, height++);
	    }
	    else {
		    right = 0;
	    }
	    return Math.max(left, right);
    }

    /**
 	* checkIfBalanced
 	* Description: checks if binary tree is balanced 
 	* i.e. all nodes have the same distance from root
 	* Traverse the graph using DFS but check height from
 	* each node with BFS
 	*
 	* @param (root) (root node of tree)
 	* @return (a boolean indicating whether a tree is balanced)
 	* Time Complexity: O(n^2)
 	* Space Complexity: O(4^n)
 	*/
	static boolean checkIfBalanced(Node root)
	{
		if(root.left_child == null && root.right_child == null)
		{
			return true;
		}
		if(root.left_child != null){
			checkIfBalanced(root.left_child);
		}
		if(root.right_child != null){
			checkIfBalanced(root.right_child);
		}
		return root.left_child!=null && root.right_child!=null 
			&& findHeightBFS(root.left_child, 0) == findHeightBFS(root.right_child, 0);
	}


	public static void main(String [] args)
	{
		// Some tests
		Node bt1 = new Node(0, new Node(0,new Node(), new Node()), new Node(0,new Node(), new Node()));
		Node bt2 = new Node(0, new Node(0,new Node(), null), new Node());

		assert QuestionOne.checkIfBalanced(bt1) == true;
		assert QuestionOne.checkIfBalanced(bt2) == false;
	}
}



