// #include <iostream>

// void printMultiplicationTable(int number) {
//     for (int i = 1; i <= 10; ++i) {
//         std::cout << number << " x " << i 
//                   << " = " << number * i << '\n';
//     }
// }

// int main() {
//     int number{};

//     std::cout << "Enter a number: ";
//     std::cin >> number;

//     printMultiplicationTable(number);

//     return 0;
// }

#include<iostream>

void multiply(int number) {
    for(int i =1; i<=10; ++i){
        std::cout << number << "x" << i << "=" << number * i << "\n";
    }

}

int main(){
    int number{};

    std::cout << "Enter a number: ";
    std::cin >> number;

    multiply(number);
    return 0;
}



// #include <iostream>
// using namespace std;

// void multiply(int num) {
//     for (int i = 1; i <= 10; i++) {
//         cout << num << " x " << i << " = " << num * i << endl;
//     }
// }

// int main() {
//     int num = 2;
//     multiply(num);
//     return 0;
// }
