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
    }
    for (int i = n; i< n+window_size; i++){
        arr[i].frame_no = -1;
        arr[i].reciever_flag = 1;
        arr[i].sender_flag = 1;
    }
}

void GBN(struct frame arr[], int n, int window_size,int timer) {
    int i=0;
    for (int j=i; j<i+window_size; j++){
            cout<<"SENDER: Sending frame "<<j+1<<"\n";
        }
        Sleep(timer);
    while (i<n){
        arr[i].reciever_flag=RNG(0,1);
        Sleep(timer);
        while(arr[i].reciever_flag!=1){
            cout<<"SENDER: Acknowledgement not Recieved for frame "<<i+1<<"... Resending entire window\n";
            for (int j=i; j<i+window_size; j++){
                cout<<"SENDER: Resending frame "<<j+1<<"\n";
            }
            arr[i].reciever_flag=RNG(0,1);
        }
        cout<<"RECIEVER: Frame "<<i+1<<" Recieved... Sending Acknowledgement\n";
        arr[i].sender_flag=RNG(0,1);
        while(arr[i].sender_flag!=1){
            cout<<"SENDER: Acknowledgement not Recieved for frame "<<i+1<<"... Resending entire window\n";
            for (int j=i; j<i+window_size; j++){
                cout<<"SENDER: Resending Sending frame "<<j+1<<"\n";
            }
            Sleep(timer);
            arr[i].sender_flag=RNG(0,1);
            cout<<"RECIEVER: Duplicate data detected... Resending Acknowledgement\n";
        }
        cout<<"SENDER: Acknowledgement recieved... frame "<<i+1<<" transmitted...\nSHIFTING WINDOW\n";
        i++;
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
    GBN(arr, n, window_size, timer);

    return 0;
}
