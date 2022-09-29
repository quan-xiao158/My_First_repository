import java.util.concurrent.Semaphore;

/**
 * 
 * 车站只能进20人
 */


public class Station {
    Semaphore people = new Semaphore(20);

    /**
     * 进站
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

                        people.acquire();// 获取线程
                        sleep(1000);
                        if (people.availablePermits() <= 0) //查看可用资源数量
                        {
                            System.out.println("售票厅已满"+(id+1)+"号乘客在外排队");
                        }
                        else   System.out.println((id)+"号乘客进入购票厅买票");
                        } catch (Exception e) {// 捕获线程阻塞异常
                        e.printStackTrace();
                        
                    }
                    id++;
                }
            }
        }.start();
    }

    /**
     * 出站
     */
    void customOut() {
        new Thread() {
            @Override
            public void run() {
                while (true) {
                    try {
                        sleep(3300);
                        people.release();
                        System.out.println("有乘客买完票了出来了");
                        System.out.println("排队乘客进入购票厅");
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
