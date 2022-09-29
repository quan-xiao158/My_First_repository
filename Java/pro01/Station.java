import java.util.concurrent.Semaphore;

/**
 * 
 * ��վֻ�ܽ�20��
 */


public class Station {
    Semaphore people = new Semaphore(20);

    /**
     * ��վ
     */
    void customIn() {
        new Thread() {

            int id=1;
            @Override
            public void run() 
            {
                while (true) 
                {
                    try {

                        people.acquire();// ��ȡ�߳�
                        sleep(1000);
                        if (people.availablePermits() <= 0) //�鿴������Դ����
                        {
                            System.out.println("��Ʊ������"+(id+1)+"�ų˿������Ŷ�");
                        }
                        else   System.out.println((id)+"�ų˿ͽ��빺Ʊ����Ʊ");
                        } catch (Exception e) {// �����߳������쳣
                        e.printStackTrace();
                        
                    }
                    id++;
                }
            }
        }.start();
    }

    /**
     * ��վ
     */
    void customOut() {
        new Thread() {
            @Override
            public void run() {
                while (true) {
                    try {
                        sleep(3300);
                        people.release();
                        System.out.println("�г˿�����Ʊ�˳�����");
                        System.out.println("�Ŷӳ˿ͽ��빺Ʊ��");
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            }
            
        }.start();
    }

    public static void main(String[] args) {
        Station station = new Station();
        station.customIn();
        station.customOut();

    }
}
