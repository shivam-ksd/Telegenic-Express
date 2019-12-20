#include<bits/stdc++.h>
using namespace std;
int main(){
	int t;
	cin>>t;
	while(t--){
		long n;
		cin>>n;
		float sum=0;
		for(int i=0;i<n;i++){
			long p,q,d;
			cin>>p>>q>>d;
			float r=(p+(p*d*1.0)/100)
			sum=sum+q*(abs(p-(r-(r*d*1.0)/100)));
			cout<<sum<<endl;
		}
	}
}