#include<bits/stdc++.h>
using namespace std;

void radixsort(int array[],int n){
    int max=0;
   queue<int>q[10];
   for(int i=0;i<n;i++){
       
       if(array[i]>max){
          max=array[i];
       }
   }
   int z=1;
   while(max){
     z=z*10;
     int p=z/10;
     for(int i=0;i<n;i++){
         int x=array[i]/p;
         int r=x%10;
         q[r].push(array[i]);
        }
      int o=0;
     for(int i=0;i<10;i++ )
      {
         int l=q[i].size();
       for(int j=0;j<l;j++)
       {
          array[o]=q[i].front();
          cout<<q[i].front()<<" ";
          q[i].pop();
           o++;
       }
      }
      cout<<endl;
      max=max/10;
   }
}
int main(){
   cout<<"*****by Radix Sort *****"<<endl;

    cout<<"best case"<<endl;
    cout<<"Enter number of students"<<endl;
    int n;
    cin>>n;
    cout<<"Enter percentage of marks obtained by students"<<endl;
    int a[n];
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    
    radixsort(a,n);
    for(int i=0;i<n;i++){
        cout<<a[i]<<" ";
    }
    cout<<endl;
    cout<<"Top 5 scores"<<endl;
    for(int i=n-5;i<n;i++){
        cout<<a[i]<<" ";
    }
    cout<<endl;

    cout<<"worst case"<<endl;
    cout<<"Enter number of students"<<endl;
    int n2;
    cin>>n2;
    cout<<"Enter percentage of marks obtained by students"<<endl;
    int a2[n2];
    for(int i=0;i<n2;i++){
        cin>>a2[i];
    }
    
    radixsort(a2,n2);
    for(int i=0;i<n2;i++){
        cout<<a2[i]<<" ";
    }
    cout<<endl;
    cout<<"Top 5 scores"<<endl;
    for(int i=n2-5;i<n2;i++){
        cout<<a2[i]<<" ";
    }
    cout<<endl;

   
}
    
    
    
    
    
    
    
    
    
   




















