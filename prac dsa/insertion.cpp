#include<bits/stdc++.h>
using namespace std;

void insertion_sort(float arr[],int n){
    int count=0,shifts=0;

    for(int i=1;i<n;i++){
        float x=arr[i];
        int j;
        for(j=i-1;j>=0;j--){
            count++;
            if(arr[j]>x){
                arr[j+1]=arr[j];
                shifts++;
            }
            else{
                break;
            }
        }
        arr[j+1]=x;
        if(j+1!=i){
            shifts++;
        }
        cout<<"Pass "<<i<<":"<<endl;
        for(int j=0;j<n;j++){
            cout<<arr[j]<<" ";
        }
        cout<<endl;
    }

    cout<<"Comparisons in insertion sort: "<<count<<endl;
    cout<<"Shifts in insertion sort: "<<shifts<<endl;

}

int main(){
    cout<<"Best test case:"<<endl;
    cout<<"Enter number of students: ";
    int n;
    cin>>n;
    float arr[n];
    cout<<"Enter their percentages: ";
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    insertion_sort(arr,n);
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;

    cout<<"Top 5 Scores: ";
    for(int i=n-1;i>=n-5;i--){
        cout<<arr[i]<<" ";
    }
    cout<<endl;

    cout<<"worst test case:"<<endl;
    cout<<"Enter number of students: ";
    cin>>n;
    float arr1[n];
    cout<<"Enter their percentages: ";
    for(int i=0;i<n;i++){
        cin>>arr1[i];
    }
    insertion_sort(arr1,n);
    for(int i=0;i<n;i++){
        cout<<arr1[i]<<" ";
    }
    cout<<endl;

    cout<<"Top 5 Scores: ";
    for(int i=n-1;i>=n-5;i--){
        cout<<arr1[i]<<" ";
    }
    cout<<endl;
}
