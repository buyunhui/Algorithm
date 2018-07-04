#include "Context.h"
#include "ConcreteSA.h"
#include "ConcreteSB.h"
#include "ConcreteSC.h"

int main()
{
    Context *c = new Context();
    Strategy *sa = new ConcreteStrategyA();
    Strategy *sb = new ConcreteStrategyB();
    Strategy *sc = new ConcreteStrategyC();
    c->setStrategy(sa);
    c->contextInterface();
    c->setStrategy(sb);
    c->contextInterface();
    c->setStrategy(sc);
    c->contextInterface();
    return 0;
}