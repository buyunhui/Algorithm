#ifndef __CONCRETE_SA_H
#define __CONCRETE_SA_H

#include "Strategy.h"

class ConcreteStrategyA : public Strategy
{
public:
    ConcreteStrategyA();
    ~ConcreteStrategyA();

    void algorithmInterface();
};

#endif
