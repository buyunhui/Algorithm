


#include <iostream>
using namespace std;


//��ʽһ���̰߳�ȫ�����������ݵ�ʱ�����׳�Ϊ����ƿ��
class Singleton
{
public:
static Singleton *GetInstance()
{
if (m_Instance == NULL )
{
//Lock(); // C++û��ֱ�ӵ�Lock��������ʹ���������Lock������Boost���˴���Ϊ��˵��
if (m_Instance == NULL )
{
m_Instance = new Singleton ();
}
//UnLock(); // C++û��ֱ�ӵ�Lock��������ʹ���������Lock������Boost���˴���Ϊ��˵��
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


//��ʽ��,�̰߳�ȫ�����ܸ�
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


//��ʽ��,Ҳ������Զ���˵ʡȥ���ͷ��ڴ�Ŀ���
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


//��ʽ�ģ��Զ��ͷ��ڴ棬�����ص�
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