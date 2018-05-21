#ifndef CONCRETE_COMPONENT_H
#define CONCRETE_COMPONENT_H

#include "component.h"

/********** **********/

//女生
class girl : public Person
{
public:
    string Name() {
        return "���ƻ�";
    }

    double Cost(int cost) {
        return cost;
    }
};

// 深度烘培咖啡�?
class boy : public Person
{
public:
    string Name() {
        return "男士";
    }

    double Cost(int cost) {
        return cost;
    }
};

#endif // CONCRETE_COMPONENT_H