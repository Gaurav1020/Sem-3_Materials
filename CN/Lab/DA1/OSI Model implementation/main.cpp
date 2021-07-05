#include <iostream>
#include <cstring>
#include <ctype.h>
#include <stdlib.h>
using namespace std;
//String to character array function
void char_array(string s, char* outstr){
    int n = s.length();
    for (int i = 0; i < n; i++){
            outstr[i] = s[i];}}
//class for array functions
class ArrayFunc {
    public:
    char* message = (char*)calloc(100,sizeof(char));
    int counter;
    //Constructor to assign message the value of input
    ArrayFunc(char* outstr){
        char *temp=outstr;
        int n=0;
        while(*temp!=0) {
            n++;
            temp++;}
        counter=n;
        for (int i=0; i < n; i++){
            message[i] = outstr[i];}}
    int counters(){
        return counter;}
    void add_to_begin(char element){
        counter=counter+1;
        for(int i=counter-1;i>0;i--) {
            message[i]=message[i-1];}
        message[0]=element;}
    void add_to_end(char element){
        counter=counter+1;
        message[counter-1]=element;}
    void trim_end() {
        message[counter-1]=0;
        counter=counter-1;}
    void trim_begin() {
        for(int i=0;i<counter-1;i++) {
            message[i]=message[i+1];}
        message[counter-1]=0;
        counter=counter-1;}};
int main()
{
    char *char_arr;
    char_arr=(char*)calloc(100,sizeof(char));
    string s;
    cout<< "Enter the message to send (**without white spaces**):\n";
    cin>>s;
    //Assigning String value to the character array
    char_array(s , char_arr);
    //Assigning made char array to class char array to perform functions on and keep track of array length counter.
    ArrayFunc a(char_arr);
    cout<<"Legend:\n5-->Application Layer(7-Application Layer,6-Presentation Layer,5-Session Layer)\n4--> Transport Layer\n3-->Network Layer\n2-->Data-Link Layer\n1-->Physical Layer";
    //SENDERS SIDE HEAD AND TAILS
    int choice=0;
    cout<<"\n\n\n------------------------Sender's Side------------------------\n\n";
    cout<<"\n\nDo you want to add Application Layer\n(1->yes,0->no): ";
    while(choice==0 || choice==1){
        cin>>choice;
        switch(choice){
            case 0:
                cout<<"Application layer not added";
                choice=-1;
                break;
            case 1:
                a.add_to_begin('5');
                cout<<a.message;
                choice=-1;
                break;
            default:
                cout<<"Enter Valid Value\n(1->yes,0->no): ";
                choice=0;
                break;}}
    choice=0;
    cout<<"\n\nDo you want to add Transport Layer\n(1->yes,0->no): ";
    while(choice==0 || choice==1){
        cin>>choice;
        switch(choice){
            case 0:
                cout<<"Transport layer not added";
                choice=-1;
                break;
            case 1:
                a.add_to_begin('4');
                cout<<a.message;
                choice=-1;
                break;
            default:
                cout<<"Enter Valid Value\n(1->yes,0->no): ";
                choice=0;
                break;}}
    choice=0;
    cout<<"\n\nDo you want to add Network Layer\n(1->yes,0->no): ";
    while(choice==0 || choice==1){
        cin>>choice;
        switch(choice){
            case 0:
                cout<<"Network layer not added";
                choice=-1;
                break;
            case 1:
                a.add_to_begin('3');
                cout<<a.message;
                choice=-1;
                break;
            default:
                cout<<"Enter Valid Value\n(1->yes,0->no): ";
                choice=0;
                break;}}
    choice=0;
    cout<<"\n\nDo you want to add Data-Link Layer\n(1->yes,0->no): ";
    while(choice==0 || choice==1){
        cin>>choice;
        switch(choice){
            case 0:
                cout<<"Data-Link layer not added";
                choice=-1;
                break;
            case 1:
                a.add_to_begin('2');
                a.add_to_end('2');
                cout<<a.message;
                choice=-1;
                break;
            default:
                cout<<"Enter Valid Value\n(1->yes,0->no): ";
                choice=0;
                break;}}
    choice=0;
    cout<<"\n\nDo you want to add Physical Layer\n(1->yes,0->no): ";
    while(choice==0 || choice==1){
        cin>>choice;
        switch(choice){
            case 0:
                cout<<"Physical layer not added";
                choice=-1;
                break;
            case 1:
                a.add_to_begin('1');
                cout<<a.message;
                choice=-1;
                break;
            default:
                cout<<"Enter Valid Value\n(1->yes,0->no): ";
                choice=0;
                break;}}
    choice=0;
    cout<<"\n\n\n------------------------Receiver's Side------------------------\n\n";
    cout<<"Message Received: "<<a.message<<"\n\n";
    while(a.message[0]=='1' || a.message[0]=='2' || a.message[0]=='3' || a.message[0]=='4' || a.message[0]=='5' || a.message[0]=='6' || a.message[0]=='7')
    switch(a.message[0]) {
        case '1':
            a.trim_begin();
            cout<<"Physical Layer found and processed.\n"<<"Remaining encoded message is: "<<a.message<<"\n\n";
            break;
        case '2':
            a.trim_begin();
            a.trim_end();
            cout<<"Data-Link Layer found and processed.\n"<<"Remaining encoded message is: "<<a.message<<"\n\n";
            break;
        case '3':
            a.trim_begin();
            cout<<"Network Layer found and processed.\n"<<"Remaining encoded message is: "<<a.message<<"\n\n";
            break;
        case '4':
            a.trim_begin();
            cout<<"Transport Layer found and processed.\n"<<"Remaining encoded message is: "<<a.message<<"\n\n";
            break;
        case '5':
            a.trim_begin();
            cout<<"Application Layer found and processed.\n"<<"Remaining encoded message is: "<<a.message<<"\n\n";
            break;
        default:
            cout<<"Error encountered";
            break;}
    cout<<"\n\n\nThe Received message is: "<<a.message;
    return 0;}
