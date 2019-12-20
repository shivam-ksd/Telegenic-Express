#include<bits/stdc++.h>
using namespace std;
int main(){
	int t;
	cin>>t;
	while(t--){
	long n;
	cin>>n;
	for(int i=0;i<n;i++)
		cin>>arr1[i];
	for(int i=0;i<n;i++)
		cin>>arr2[i];

	for(int i=0;i<n;i++){
	if(arr2[i]>=arr1[i])
		count1++;
	else
		break;
	}
	for(int i=0;i<n;i++)
		if(arr2[n-i-1]>=arr1[i])
			count2++;
		else
			break;

	}
	if(count1==n && count2==n)
		cout<<"both"<<endl;
	else{
	if(count1==n)
		cout<<"front"<<endl;
	else{
	if(count2==n)
		cout<<"back"<<endl;
	else
		cout<<"none"<<endl;
		}

		}
}