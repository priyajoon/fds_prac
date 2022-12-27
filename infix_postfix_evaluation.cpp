#include <bits/stdc++.h>
using namespace std;
 
int  precedence(char c)
{
    if (c == '/' || c == '*')
        return 2;
    else if (c == '+' || c == '-')
        return 1;
    else
        return -1;
}
 
string infixToPostfix(string s)
{
    stack<char> st; 
                    
    string result;
 
    for (int i = 0; i < s.length(); i++) {
        char c = s[i];
 
        if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z' )
            || (c >= '0' && c <= '9'))
            result += c;

        else if (c == '(')
            st.push('(');
 
        else if (c == ')') {
            while (st.top() != '(') {
                result += st.top();
                st.pop();
            }
            st.pop();
        }
 
        else {
            while (!st.empty() &&  precedence(s[i]) <=  precedence(st.top())) {
                result += st.top();
                st.pop();
            }
            st.push(c);
        }
    }

    while (!st.empty()) {
        result += st.top();
        st.pop();
    }
 
    return result;
}

int evaluatePostfixExpression(string exp) {
    // Defining an stack of integer type.
    stack<int> st;
    string expression=infixToPostfix(exp);
    // Traversing in the expression from left 
    // to right. 
    for (int i = 0; i < expression.length(); i++){
        char c = expression[i];

        // If 'c' is a digit (operand)
        if (c >= '0' && c <= '9'){
            // Convert 'c' in integer and
            // push it into the stack.
            int temp = (int)(c - '0');
            st.push(temp);
        }
        // Otherwise it is an operator.
        else{
            // Pop element from the stack.
            int op1 = st.top();
            st.pop();
            // Pop another element from the stack. 
            int op2 = st.top();
            st.pop();

            // Use the switch case to deal with
            // the operand accordingly.
            switch(c){
                case '+':
                    st.push(op2 + op1);
                    break;
                case '-':
                    st.push(op2 - op1);
                    break;
                case '*':
                    st.push(op2 * op1);
                    break;    
                case '/':
                    st.push(op2 / op1);
                    break;
            }
        }
    }
    
    // Return the element at the top 
    // of the stack.
    return st.top();
}

 
int main()
{
    string exp ;
    cout<<"enter the infix expression : ";
    cin>>exp;
    cout<<"postfix expression is : ";
    // Function call
    cout<<infixToPostfix(exp)<<endl;
    string post=exp;
    cout<<"eveluation"<<endl;
    cout<<evaluatePostfixExpression(post)<<endl;
    return 0;
}