# include<iostream>
using namespace std;
int main()
{
    int num1 = 4, num2 = 5;
    cout<<"Enter the value of number 1: \n";// '<<' is called insertion operator

    cin>>num1;

    cout << "Enter the value of number 2: \n"; // '>>' is called exraction operator

    cin>>num2;

    cout<<"The sum is "<<num1+num2<<endl;
    cout<<"The difference is "<<num1-num2<<endl;
    cout<<"The product is "<<num1*num2<<endl;
    cout<<"The quotient is "<<num1/num2<<endl;
    cout<<"The remainder is "<<num1%num2<<endl;
    // cout<<"The value of num1++ is "<<num1++<<endl;
    // cout<<"The value of num1-- is "<<num1--<<endl;
    // cout<<"The value of --num1 is "<<--num1<<endl;
    // cout<<"The value of ++num1 is "<<++num1<<endl;

    
// *Comparison operator examples:
//"the value of a==b is"<<(a==b);
//"the value of a>b is"<<(a>b);
//"the value of a<b is"<<(a<b);
//"the value of a<=b is"<<(a<=b);
//"the value of a>=b is"<<(a>=b);
//!"the value of a!=b is"<<(a!=b);(the change of not equal to sign is because of font ligaures its actually exclamation mark and =.)

//!logical operator (a==b) && (a>b); [If both of these is true then the statement will be true otherwise it will be false] this is a logical and operator (a==b)
//!logical or operator (a==b) || (a>b) [If one of these is true then the operator will be true]

    return 0;
}