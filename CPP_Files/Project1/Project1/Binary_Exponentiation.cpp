//https://cp-algorithms.com/algebra/binary-exp.html

#include<iostream>
using namespace std;
long long binpow(long long a, long long n)
{
	int res = 1;
	while (n > 0)
	{
		if (n & 1)
			res = res * a;
		a = a * a;
		n >>= 1; 
	}
	return res;
}

/*int main() {
	cout << binpow(3, 13) << endl;
	return 0;
}*/
