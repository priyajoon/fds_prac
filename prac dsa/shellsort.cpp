#include<bits/stdc++.h>
using namespace std;


void shell_sort(float arr[],int n){
    int shifts=0,count=0;
    int x=n/2;
    int pass_num=1;
    while(x){
        for(int i=x;i<n;i++){
            float y=arr[i];
            int j;
            for(j=i-x;j>=0;j-=x){
                count++;
                if(y<arr[j]){
                    arr[j+x]=arr[j];shifts++;
                }
                else{
                    break;
                }
            }
            arr[j+x]=y;
            if(j+x!=i){
                shifts++;
            }
        }
        cout<<"Pass"<<pass_num<<":"<<endl;
        for(int i=0;i<n;i++){
            cout<<arr[i]<<" ";
        }
        cout<<endl;
        x=x/2;
        pass_num++;
    }

    cout<<"number of Comparisons in shell sort: "<<count<<endl;
    cout<<"number of Shifts in shell sort: "<<shifts<<endl;

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
    shell_sort(arr,n);
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
    shell_sort(arr1,n);
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