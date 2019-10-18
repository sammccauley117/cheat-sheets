// <iostream> & <cstdio>
#include <iostream>
#include <cstdio>
using namespace std;
cout << "Yah" << endl;
int x; cout << "Enter a number: "; cin >> x;
int input;
printf("Enter a number: ");
scanf("%d", &input);
printf("%d * %d = %d\n\n", input, input, input*input);

// Formatters
d // Signed decimal integer
u // Unsigned decimal integer
f // Float
c // Char
s // String
p // Pointer

// <string>
#include <string>
using namespace std;
string str = "Big";
str += " Hoss";
str.length();
str.size(); // Same as length()
str.substr(index,length); // Starts at index (inclusive) and keeps going for length
str.substr(index); // Returns the rest of the string after index (inclusive)
str.erase(index,length); // Starts at index (inclusive) and erases length characters
str.find(x); // Returns first index of x (could be char or whole string)
str.rfind(x); // Same as find() but for last index
str.empty(); // Returns True if the length of the string is 0
stoi(str); // Returns an int parsed from string

// array
int arr1[5];
int arr2[] = {1,2,3,4,5};
int arr3[5] = {1,2,3};
arr.size(); // Returns the number of elements
arr.empty(); // Returns true if array is empty
int getLast(int arr[], int size) {
   return arr[size-1];
}

// <vector>
#include <vector>
using namespace std;
vector<int> myVector(n,x); // Vector of size n, all with value x
vector<int> myVector;
myVector.insert(index, val); // Inserts val at index
myVector.push_back(val);
myVector.pop_back();
myVector.size(); // Returns the number of elements
myVector.empty(); // Returns true if vector is empty
myVector.clear(); // Erases all entries
myVector.erase(myVector.begin() + index); // Deletes element at index
myVector.erase(myVector.begin() + start, myVector.begin() + stop); // Deletes elements from [start,stop)

// <map>
#include <map>
using namespace std;
map<char, int> myMap;
myMap.insert(pair<char,int>('a',0)); // Insert a key:value pair
myMap[key] = val; // Either insert or modify val at key
myMap.size(); // Returns number of items
myMap.empty(); // Returns True if no items are present
myMap.clear(); // Erases all entries
myMap.count('a'); // Returns 1 if 'a' is in the map, 0 otherwise
if (map[key]) // Works (use carefully)

// <queue>
#include <queue>
using namespace std;
queue<int> myQueue;
myQueue.push(val); // Push val to back of queue
myQueue.pop(); // Pop first element
myQueue.size(); // Returns number of items
myQueue.empty(); // Returns True if no items are present
myQueue.front(); // First item
myQueue.back(); // Last item

// <stack>
#include <stack>
using namespace std;
stack<int> myStack;
myStack.push(val); // Adds val to the top
myStack.pop(); // Removes the top
myStack.size(); // Returns number of items
myStack.empty(); // Returns True if no items are present
myStack.top(); // Top item

// <set>
#include <set>
using namespace std;
set<int> mySet;
mySet.insert(el); // Insert element
mySet.size(); // Returns number of items
mySet.empty(); // Returns True if no items are present
mySet.clear(); // Erases all entries
mySet.count(el); // Returns 1 if el is in the set, 0 otherwise

// Pointers
int var = 20; // Regular int
int *p;       // Pointer to an int
p = &var;     // Pointer now contains the address of var
p;  // The address
*p; // The value
int *width = new int;

// Iterator and Algorithms
map<string, int>::iterator it;
vector<int>::iterator it;
for (it = myMap.begin(); it != myMap.end(); it++)
  cout << it->first << " : " << it->second << endl;
for (it = myVector.begin(); it != myVector.end(); it++)
  cout << *it << endl;
reverse(myVector.begin(), myVector.end()); // Flips vector
reverse(myVector.begin(), myVector.begin() + n); // Reverses the first n elements [start,end)
sort(myVector.begin(), myVector.end()); // Sorts the vector
rotate(myVector.begin(), myVector.begin() + index, myVector.end()); // Rotates so that index is the first element
unique(myVector.begin(), myVector.end()); // Removes consecutive duplicates
replace(myVector.begin(), myVector.end(),x,y); // Replaces all occurances of x with y
max_element(myVector.begin(), myVector.end()); // Returns iterator to max element
min_element(myVector.begin(), myVector.end()); // Returns iterator to min element
count(myVector.begin(), myVector.end(), val); // Returns how many times val appeared

// Functions
void doSomething(int& num) {} // Pass by reference
void doSomething(int *num) {} // Pass by pointer
int* doSomething(int num)  {} // Return pointer
int& doSomething(int num)  {} // Return reference

// Struct
struct song {
  string title;
  string artist;
};
song favorite;
favorite.title("Heart of the Country");
favorite.artist("Paul McCartney");

// Classes
class nameOfClass{
public:  // Public Variables and Member Functions
  void setX(int x) { this->x = x; }
private: // Private Variables and Functions
  int x;
};

// Linked List
struct ListNode {
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(NULL) {}
};

ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    ListNode *n1;
    n1 = l1;
    while (n1 != NULL) {
        cout << n1->val << " ";
        n1 = n1->next;
    }
    return n1;
}
