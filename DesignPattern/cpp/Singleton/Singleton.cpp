


#include <iostream>
using namespace std;


//方式一，线程安全，但当大数据的时候容易成为性能瓶颈
class Singleton
{
public:
static Singleton *GetInstance()
{
if (m_Instance == NULL )
{
//Lock(); // C++没有直接的Lock操作，请使用其它库的Lock，比如Boost，此处仅为了说明
if (m_Instance == NULL )
{
m_Instance = new Singleton ();
}
//UnLock(); // C++没有直接的Lock操作，请使用其它库的Lock，比如Boost，此处仅为了说明
}
return m_Instance;
}


static void DestoryInstance()
{
if (m_Instance != NULL )
{
delete m_Instance;
m_Instance = NULL ;
}
}


int GetTest()
{
return m_Test;
}


private:
Singleton(){ m_Test = 0; }
static Singleton *m_Instance;
int m_Test;
};


Singleton *Singleton ::m_Instance = NULL;


//方式二,线程安全，性能高
class Singleton1
{
public:
static Singleton1 *GetInstance()
{
return const_cast <Singleton1 *>(m_Instance);
}


static void DestoryInstance()
{
if (m_Instance != NULL )
{
delete m_Instance;
m_Instance = NULL ;
}
}


int GetTest()
{
return m_Test;
}


private:
Singleton1(){ m_Test = 10; }
static const Singleton1 *m_Instance;
int m_Test;
};


const Singleton1 *Singleton1 ::m_Instance = new Singleton1();


//方式三,也不错，相对二来说省去了释放内存的开销
class Singleton2
{
public:
static Singleton2 *GetInstance()
{
static Singleton2 m_Instance;
return &m_Instance;
}


int GetTest()
{
return m_Test++;
}


private:
Singleton2(){ m_Test = 10; };
int m_Test;
};


//方式四，自动释放内存，很有特点
class Singleton3
{
public:
static Singleton3 *GetInstance()
{
return m_Instance;
}


int GetTest()
{
return m_Test;
}


private:
Singleton3(){ m_Test = 10; }
static Singleton3 *m_Instance;
int m_Test;


// This is important
class GC
{
public :
~GC()
{
// We can destory all the resouce here, eg:db connector, file handle and so on
if (m_Instance != NULL )
{
cout<< "Here is the test" <<endl;
delete m_Instance;
m_Instance = NULL ;
}
}
};
static GC gc;
};


Singleton3 *Singleton3 ::m_Instance = new Singleton3();
Singleton3::GC Singleton3 ::gc;






int main()
{
    Singleton *singletonObj = Singleton ::GetInstance();
    cout<<singletonObj->GetTest()<<endl;
    Singleton ::DestoryInstance();


return 0;
}