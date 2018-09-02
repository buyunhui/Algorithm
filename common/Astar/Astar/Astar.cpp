// Astar.cpp: 定义控制台应用程序的入口点。
//

#include "Astar.h"

bool operator==(const Point &l, const Point &r)
{
	if (l.ucX == r.ucX && l.ucY == r.ucY)
	{
		return true;
	}

	return false;
}


void Astar::findpath(const Point &begin, const Point &end)
{
}

baseAstar Astar::getLeastPoint(const Point &p) 
{

}

bool isCanReach(const Point &p)
{
}

set<baseAstar> Astar::getSurroundPoints(const Point &p) const
{

}

APointType Astar::getPointType(const Point &p) const
{

}

UINT8 Astar::calcH(const Point &begin, const Point &end)
{

}

UINT8 Astar::calcF(const Point &p)
{

}

UINT8 Astar::calcG(const Point &p)
{

}

int main()
{
    return 0;
}

