//selection sort
//name = priya
//roll no. 7241

#include<bits/stdc++.h>
using namespace std;


void selection_sort(float arr[],int n){
    int comp=0,swaps=0;
    for(int i=0;i<n-1;i++){
        float minn=arr[i];
        int index=i;
        for(int j=i+1;j<n;j++){
            comp++;
            if(arr[j]<minn){
                index=j;
                minn=arr[j];
            }
        }
        comp++;
        if(index!=i){
            int a=arr[index];
            arr[index]=arr[i];
            arr[i]=a;
            swaps++;
        }
        cout<<"Pass "<<i+1<<":"<<endl;
        for(int j=0;j<n;j++){
            cout<<arr[j]<<" ";
        }
        cout<<endl;

    }
    cout<<"Comparisons in selection sort: "<<comp<<endl;
    cout<<"Swaps in selection sort: "<<swaps<<endl;
}


int main(){
    cout<<"First test:"<<endl;
    cout<<"Enter number of students: ";
    int n;
    cin>>n;
    float arr[n];
    cout<<"Enter their percentages: ";
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    selection_sort(arr,n);

    cout<<"Top 5 Scores: ";
    for(int i=n-1;i>=n-5;i--){
        cout<<arr[i]<<" ";
    }
    cout<<endl;

    cout<<"Second test:"<<endl;
    cout<<"Enter number of students: ";
    cin>>n;
    float arr1[n];
    cout<<"Enter their percentages: ";
    for(int i=0;i<n;i++){
        cin>>arr1[i];
    }
    selection_sort(arr1,n);

    cout<<"Top 5 Scores: ";
    for(int i=n-1;i>=n-5;i--){
        cout<<arr1[i]<<" ";
    }
    cout<<endl;
} 