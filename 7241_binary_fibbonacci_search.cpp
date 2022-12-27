//Name: Priya
//Roll NO: 7241


#include <bits/stdc++.h>
using namespace std;

//Function for the binary search of the index

void binarysearch(int ar[],int n,int key)
{
   int check=0;
   int lo=0,hi=n-1;
   while((hi-lo)>1)
   {
    check++;
      int mid=(hi+lo)/2;
      if(ar[mid]<=key)
          lo=mid;
      else
          hi=mid-1;
   }
   if(ar[hi]==key) {
      cout<<"Element found in binary search at index "<< hi << endl;
      cout<<"NUmber ofIterations: "<<check<<endl;
   }
   else if (ar[lo]==key){
       cout<<"Element is in binary search at index "<< lo << endl;
       cout<<"Number of Iterations - "<<check<<endl;
       
   }
   else
      cout<<"Element not found in Binary search "<<endl; 
}

//Function for the fibbonacci search 


void fibo(int arr[],int n,int key)
{

      if(key>arr[n-1])
        {cout<<"Wrong element !!!"<<endl;
       return;          }
	  int fib=1;
	  int fib1=1;
	  int fib2=0;
	  while(fib<n)
	  {
	    fib2=fib1;
	    fib1=fib;
	    fib=fib1+fib2;
	  } 
      cout<<"fib2"<<" "<<"fib1"<<" "<<"fib"<<" "<<"offset"<<" "<<"index"<<" "<<"arr[index]"<<endl;  
	  int offset=0;
	  int index=fib2+offset;
          int check_fibo=0;
          bool value=false;
	  while(fib2>0)
	  {
            cout<<fib2<<"   "<<fib1<<"    "<<fib<<"      "<<offset<<"     "<<index<<"    "<<arr[index]<<endl;  
              check_fibo++;
            if(fib2==0)
            {
               if(arr[index-1]==key)
                  {
                   value=true;
                   cout<<"element is found at index : "<<index<<endl;
                   break;
                  }
                else break;

            }
	     if(arr[index-1]<key)
	     {
	       fib=fib1;
	       fib1=fib2;
	       fib2=fib-fib1;
	       offset=index;
	       index=fib2+offset;
	     }
	    else if(arr[index-1]==key)
	   {
              value=true;
	      cout<<"Index at fibonacci search : "<<index<<endl;
	      cout << "Actual Index: " << index-1 << endl;
              cout<<"No of Iterations : "<<check_fibo<<endl;
	      break;
	   }
	   else if(arr[index-1]>key)
	   { 
          
	     fib=fib2;
	     fib1=fib1-fib;
	     fib2=fib-fib1;
	     index=offset+fib2;
	   }
	   
	  }
     if(!value) cout<<"element not found!!"<<endl;
}

//Taking information from the user


int main()
{
  int key,n;
  cout << "Enter the no of students: ";
  cin>>n;
  int arr[n+1];
  cout << "Enter the roll no of the students: ";
  for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
  cout<<"Enter the Roll no to search- ";
  cin>>key;
  cout<<"-----FIBONACCI SEARCH------"<<endl;
  
  fibo(arr,n,key);
  cout<<"------BINARY SEARCH-----"<<endl;

  binarysearch(arr,n,key);
  

}








    
/*#include<bits/stdc++.h>
using namespace std;

int fib_search(int a[],int n,int key){
    int fib2=0;
    int fib1=1;
    int fib=fib1+fib2;
    while(fib<n){
        fib2=fib1;
        fib1=fib;
        fib=fib1+fib2;
    }
    cout<<"fib2"<<" "<<"fib1"<<" "<<"fib"<<" "<<"offset"<<" "<<"index"<<" "<<"arr[index]"<<endl; 
    int offset=0;
    int i=0;
    while(fib>1){
        cout<<fib2<<"   "<<fib1<<"    "<<fib<<"      "<<offset<<"     "<<i<<"    "<<a[i]<<endl; 
        i=min(offset+fib2,n-1);
        if(a[i]<key){
            //1 step down
            fib=fib1;
            fib1=fib2;
            fib2=fib-fib1;
            offset=i;
        }
        else if(a[i]>key){
            //2 step down
            fib=fib2;
            fib1=fib1-fib2;
            fib2=fib-fib1;
        }
        else{
            return i;
        }
    }
    if(fib1 && a[offset+1]==key){
        return offset+1;
    }
    return -1;
}

int main(){
int n;
    cout<<"enter number of students"<<endl;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++){
        cout<<"enter array element = ";
        cin>>a[i];
    }
    cout<<endl;
    cout<<"enter key to search"<<endl;
    int key;
    cin>>key;
    //int ans=linear_search(a,n,key);
    int ans=fib_search(a,n,key);
    if(ans==-1){
        cout<<"key not found"<<endl;
    }
    else{
        cout<<"key found at "<<ans<<endl;
    }
    //sentinal_search(a,n,key);
    return 0;
}*/