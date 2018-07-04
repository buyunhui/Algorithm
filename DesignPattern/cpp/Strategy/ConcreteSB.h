#ifndef __CONCRETE_SB_H
#define __CONCRETE_SB_H

#include "Strategy.h"

class ConcreteStrategyB : public Strategy
{
public:
    ConcreteStrategyB();
    ~ConcreteStrategyB();

    void algorithmInterface();
};

#endif