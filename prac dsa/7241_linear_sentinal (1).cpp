//name=priya
//roll no. 7241
#include <bits/stdc++.h>
using namespace std;
int main()
{
    cout<<"*******LINEAR SEARCH******"<<endl;
    int n, key;
    cout << "Total strength of students:- " << endl;
    cin >> n;
    
    int array[n + 1];
    bool v = false;
    cout << "Students who attended the session are :- ";
    for (int i = 0; i < n; i++)
    {
        cin >> array[i];
    }
    cout << "enter roll no. to search:- " << endl;
    cin >> key;

    // x will store the index of the key
    int x = 0;
    for (int i = 0; i < n; i++)
    {
        if (array[i] == key)
        {
            v = true;
            x = i;
            break;
        }
    }
    if (v)
    {
        cout << " By Linear search " << endl;
        cout << "Found at " << x << " index " << endl;
    }
    else
    {
        cout << " By Linear search " << endl;
        cout << "key not found" << endl;
    }

    cout<<"********SENTINEL SEARCH*********"<<endl;
    int last = array[n];
    array[n] = key;
    int i = 0;

    while (array[i] != key)
        i++;

    if ((i < n) || (array[n - 1] == key))
    {
        cout << " By sentinel search " << endl;
        cout << "Found at " << i << " index " << endl;
        ;
    }
    else
    {
        cout << " By sentinel search " << endl;
        cout << "key not found" << endl;
        ;
    }
}