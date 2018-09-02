#pragma once
#ifndef _ASTAR_H_
#define _ASTAR_H_
#include "stdafx.h"


using std::vector;
using std::set;
using std::cout;
using std::cin;
using std::endl;

typedef unsigned char UINT8;
typedef unsigned int UINT32;

enum APointType {
	APT_UNKNOWN = 0, // 未知状态  
	APT_OPENED, // 开放列表中  
	APT_CLOSED, // 关闭列表中  
};

struct Point
{
	UINT8 ucX;
	UINT8 ucY;
	UINT8 pType;
	Point() {};
	~Point() {};
	Point(UINT8 _x, UINT8 _y, UINT8 _type) :ucX(_x),ucY (_y),pType(_type){};

};

bool operator==(const Point &l, const Point &r) ;

struct baseAstar
{
	Point point;
	UINT8 F;
	UINT8 G;
	UINT8 H;
	baseAstar() {};
	~baseAstar() {};
	baseAstar(Point _p) :point(_p),F(0),G(0),H(0){};
}; 

class Astar {
public:
	vector<Point*> getPath() { return m_path; };
	void findpath(const Point &begin, const Point &end);
	baseAstar getLeastPoint(const Point &p); //获取F最小的点
	bool isCanReach(const Point &p);
	set<baseAstar> getSurroundPoints(const Point &p) const;
	APointType getPointType(const Point &p) const;
	UINT8 calcH(const Point &begin, const Point &end);
	UINT8 calcF(const Point &p);
	UINT8 calcG(const Point &p);


	Astar() {};
	Astar(vector<vector<UINT8>> _maze) { m_maze = _maze; };
	~Astar() {};

private:
	vector<vector<UINT8>> m_maze;
	baseAstar *a_point;
	vector<Point *> m_path;
};
#endif

