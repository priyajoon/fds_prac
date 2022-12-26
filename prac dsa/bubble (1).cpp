#include<bits/stdc++.h>
using namespace std;

void bubble_sort(float arr[],int n){
    int count=0,swaps=0;
    for(int i=0;i<n-1;i++){
        int swaps1=0;
        for(int j=0;j<n-1-i;j++){
            count++;
            if(arr[j]>arr[j+1]){
                swaps1++;
                int a=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=a;
            }
        }
        swaps+=swaps1;
        cout<<"Pass "<<i+1<<":"<<endl;
        for(int j=0;j<n;j++){
            cout<<arr[j]<<" ";
        }
        cout<<endl;
        count++;
        if(!swaps1){
            break;
        }
    }
    cout<<"Comparisons in bubble sort: "<<count<<endl;
    cout<<"Swaps in bubble sort: "<<swaps<<endl;

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
    bubble_sort(arr,n);
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;

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
    bubble_sort(arr1,n);
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
