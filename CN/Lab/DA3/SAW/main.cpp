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

void input(struct frame arr[], int n) {
    for (int i = 0; i < n; i++) {
        arr[i].frame_no = i + 1;
        arr[i].reciever_flag = 0;
        arr[i].sender_flag = 0;
    }
}

void SAW(struct frame arr[], int n, int timer) {
    int frame_status = -1;
    int ACK_status = -1;
    for (int i = 0; i < n; i++) {
        cout << "SENDER: Sending frame " << i + 1 << "..." << endl;
        Sleep(timer);
        frame_status = RNG(0, 1);
        ACK_status = RNG(0, 1);
        while (frame_status != 1) {
            Sleep(timer);
            cout << "SENDER: Acknowledgement not recieved from reciever end...\t Resending frame\n";
            Sleep(timer);
            frame_status = RNG(0, 1);
        }
        cout << "RECIEVER: Frame recieved...\t Sending Acknowledgement\n";
        arr[i].reciever_flag = 1;
        while (ACK_status != 1) {
            cout << "SENDER: Acknowledgement not recieved from reciever end...\t Resending frame\n";
            Sleep(timer);
            cout << "RECIEVER: Duplicate frame recieved...\t Sending Acknowledgement again\n";
            Sleep(timer);
            ACK_status = RNG(0, 1);
        }
        arr[i].sender_flag = 1;

        cout << "SENDER: Acknowledgement recieved for frame " << i + 1 << "\nTransmission completed for frame" << i + 1 << "\n\n";
    }
}

int main() {
    init();
    int n;
    int timer = 100;
    cout << "Enter Number of frames: ";
    cin >> n;
    cout << "\n";
    struct frame arr[100];
    input(arr, n);
    SAW(arr, n, timer);

    return 0;
}
