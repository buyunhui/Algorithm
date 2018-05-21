#ifndef CONCRETE_DECORATOR_H
#define CONCRETE_DECORATOR_H

#include "decorator.h"

/********** **********/


class Cream : public PersonDecorator
{
public:
    Cream(Person *beverage) : PersonDecorator(beverage) {}

    string Name() {
        return m_pBeverage->Name() + " Cream";
    }

    double Cost() {
        return m_pBeverage->Cost(10) + 3.5;
    }
};


class Mocha : public PersonDecorator
{
public:
    Mocha(Person *beverage) : PersonDecorator(beverage) {}

    string Name() {
        return m_pBeverage->Name() + " Mocha";
    }

    double Cost() {
        return m_pBeverage->Cost(9) + 2.0;
    }
};


class Syrup : public PersonDecorator
{
public:
    Syrup(Person *beverage) : PersonDecorator(beverage) {}

    string Name() {
        return m_pBeverage->Name() + " Syrup";
    }

    double Cost() {
        return m_pBeverage->Cost(10) + 3.0;
    }
};

#endif // CONCRETE_DECORATOR_H