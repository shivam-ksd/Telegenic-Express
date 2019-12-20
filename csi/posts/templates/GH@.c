#include<bits/stdc++.h>
using namespace std;
int main(){
	long t;
	cin>>t;
	while(t--){
		long n;
		cin>>n;
		long count[n]={0};
		long sum[n]={0};
		long arr[n];
		for(int i=1;i<=n;i++){
			cin>>arr[i];
			sum[i]=sum[i-1]+arr[i];
		}
		for(int i=1;i<=n;i++){
			for(int j=i+1;j<=n;j++){
				long p=sum[j]-sum[i]-arr[j];
				if(arr[j]>=p)
					count[j]++;
				if(arr[i]>=p)
						count[i]++;

			}
			cout<<count[i]<<endl;
		}


	}
}