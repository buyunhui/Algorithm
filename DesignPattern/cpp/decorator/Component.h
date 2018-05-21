//component.h
#ifndef COMPONENT_H
#define COMPONENT_H

#include <string>

using namespace std;

// 所有饮料的基类
class Person
{
public:
    virtual string Name() = 0;  // 名称
    virtual double Cost(int cost) = 0;  // 价钱
};

#endif // COMPONENT_H