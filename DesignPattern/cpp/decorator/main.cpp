#include "ConcreteComponent.h"
#include "ConcreteComponent.h"
#include <iostream>


int main()
{
    using namespace std;
    
    Person *p = new girl();
    cout<< p->Name()<<endl;
    return 0;
}