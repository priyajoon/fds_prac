#include<bits/stdc++.h>
using namespace std;

int partition(int arr[],int start,int end){
    int i,j,pivot;
    if(start<end){
        pivot=arr[start];
        i=start;
        j=end;
        while(i<j){
            while(arr[i]<=pivot){
                i++;

            }
            while(arr[j]>pivot){
                j--;
            }
            if(i<j){
                swap(arr[i],arr[j]);
            }
        }
    }
    swap(arr[start],arr[j]);
    return j;
}
 void quickSort(int arr[],int start,int end){
    int p;
    
    if(start<end){
        for(int i=0;i<end+1;i++){
            cout<<arr[i]<<" ";
        }
        cout<<endl;
        p=partition(arr,start,end);
        quickSort(arr,start,p-1);
        quickSort(arr,p+1,end);
    }
    
    
 }

 int main(){
    cout<<"*****by Quick Sort *****"<<endl;

    cout<<"best case"<<endl;
    cout<<"Enter number of students"<<endl;
    int n;
    cin>>n;
    cout<<"Enter percentage of marks obtained by students"<<endl;
    int a[n];
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    
    quickSort(a,0,n-1);
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
    
    quickSort(a2,0,n2-1);
    for(int i=0;i<n2;i++){
        cout<<a2[i]<<" ";
    }
    cout<<endl;
    cout<<"Top 5 scores"<<endl;
    for(int i=n2-5;i<n2;i++){
        cout<<a2[i]<<" ";
    }
    cout<<endl;

    return 0;
 }