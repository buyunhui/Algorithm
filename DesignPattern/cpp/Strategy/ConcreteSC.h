#ifndef __CONCRETE_SC_H
#define __CONCRETE_SC_H

#include "Strategy.h"

class ConcreteStrategyC : public Strategy
{
public:
    ConcreteStrategyC();
    ~ConcreteStrategyC();

    void algorithmInterface();
};

#endif