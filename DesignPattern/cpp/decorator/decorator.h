#ifndef DECORATOR_H
#define DECORATOR_H

#include "component.h"

// 调味品
class PersonDecorator : public Person
{
public :
    PersonDecorator(Person *beverage) : m_pBeverage(beverage) {}

    string Name() {
        return m_pBeverage->Name();
    }

    double Age(int cost) {
        return m_pBeverage->Cost(cost);
    }

protected :
    Person *m_pBeverage;
} ;

#endif // DECORATOR_H