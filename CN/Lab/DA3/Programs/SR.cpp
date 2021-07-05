#include <iostream>

#include<stdio.h>

#include<stdlib.h>

#include<unistd.h>

#include <time.h>

#include <windows.h>

using namespace std;

struct frame {
    int frame_no;
    int reciever_flag; //activates when frame recieved by reciever
    int sender_flag; //activates when ACK recieved by sender
    int dup;
};

int RNG(int lower, int upper) {
    int num = (rand() % (upper - lower + 1)) + lower;
    return num;
}

void init() {
    srand(time(NULL));
}

void input(struct frame arr[], int n, int window_size) {
    for (int i = 0; i < n; i++) {
        arr[i].frame_no = i + 1;
        arr[i].reciever_flag = 0;
        arr[i].sender_flag = 0;
        arr[i].dup=0;
    }
    for (int i = n; i< n+window_size; i++){
        arr[i].frame_no = -1;
        arr[i].reciever_flag = 1;
        arr[i].sender_flag = 1;
    }
}

int check_empty (struct frame arr[]) {
    if (arr[0].frame_no==-1){
        return 0; //0 means empty
    }
    else {
        return 1; //1 means not empty
    }
}

struct frame Dequeue(struct frame arr[]){
    struct frame temp;
    if (arr[0].frame_no != -1){
        temp=arr[0];
    }
    int i=0;
    while (arr[i].frame_no != -1){
        arr[i]=arr[i+1];
        i++;
    }
    return temp;
};

void Enqueue(struct frame buffer[], struct frame temp){
    int i=0;
    int j=0;

    while (buffer[i].frame_no != -1){
        i++;
    }
    buffer[i]=temp;
}

void SR(struct frame arr[], int n, int window_size,int timer) {
    int i=0;
    int counter=0;
    struct frame buffer[100];
    struct frame ready[window_size+1];
    input(ready, 0, window_size+1);
    struct frame temp;
    input(buffer, 0, 100);
    for (int j=0; j<window_size; j++){
            cout<<"SENDER: Sending frame "<<j+1<<"\n";
            ready[j]=arr[j];
            counter++;
        }
        Sleep(timer);
    while (check_empty(ready) || check_empty(buffer) || i<n){
        if (!check_empty(ready)){
            if(check_empty(buffer)){
                Enqueue(ready, Dequeue(buffer));
            }
            else if(counter!=n && !check_empty(buffer)){
                Enqueue(ready, arr[counter]);
                counter++;
            }

        }

        ready[0].reciever_flag=RNG(0,1);
        Sleep(timer);
        if (ready[0].reciever_flag){
            if (ready[0].dup==1){
                cout<<"RECIEVER: Duplicate data found for frame "<<ready[0].frame_no<<"... Resending Acknowledgement\n";

            }
            else {
                cout<<"RECIEVER: Frame "<<ready[0].frame_no<<" Recieved... Sending Acknowledgement\n";
                ready[0].dup=1;
            }
            temp=Dequeue(ready);
            if(check_empty(buffer)){
                Enqueue(ready, Dequeue(buffer));
            }
            else if(counter!=n && !check_empty(buffer)){
                Enqueue(ready, arr[counter]);
                counter++;
            }
            Sleep(timer);
            temp.sender_flag=RNG(0,1);
            if (temp.sender_flag){
                cout<<"SENDER: Acknowledgement for frame "<<temp.frame_no<<" Recieved... Transmission Completed\n";
            }
            else{
                cout<<"SENDER: Acknowledgement for frame "<<temp.frame_no<<" Not recieved... Queuing frame for retransmission.\n";
                Enqueue(buffer, temp);
            }
        }
        else {
            cout<<"RECIEVER: Corrupted data recieved for frame "<<ready[0].frame_no<<"... Sending Negative ACK.\n";
            Enqueue(buffer, Dequeue(ready));
            if(check_empty(buffer)){
                Enqueue(ready, Dequeue(buffer));
            }
            else if(counter!=n && !check_empty(buffer)){
                Enqueue(ready, arr[counter]);
                counter++;
            }

        }
        i++;
    }
}

void display(struct frame arr[], int n){
    for (int i=0; i<n; i++){
        cout<<arr[i].frame_no<<"\t";
    }
}

int main() {
    init();
    int timer = 100;
    int n;
    int window_size;
    cout << "Enter Window Size: ";
    cin>> window_size;
    cout << "\n";
    cout << "Enter Number of frames: ";
    cin >> n;
    cout << "\n";
    struct frame arr[100];
    input(arr, n, window_size);
    SR(arr, n, window_size, timer);

    return 0;
}
