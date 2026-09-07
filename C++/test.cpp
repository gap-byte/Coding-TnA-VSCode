#include <iostream>
#include <string>

int main() {
    std::string name;
    
    std::cout << "Enter your name: ";
    std::cin >> name; // Takes user input, like input() in Python
    
    std::cout << "Welcome to C++, " << name << "!" << std::endl;
    return 0;
}
