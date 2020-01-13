## 1114. Print in Order
- Description: Define three different functions. Using multi-threading thinking to make sure the three different functions will be excuted in a fixed order
- Link: https://leetcode.com/problems/print-in-order/
- Analysis: Basic concurrency questions. Can be solved by Semaphore to make the excution order fixed.

## Original question
```java
class Foo {
    
    Semaphore s1,s2;

    public Foo() {
    }

    public void first(Runnable printFirst) throws InterruptedException {
        
        // printFirst.run() outputs "first". Do not change or remove this line.
        printFirst.run();
    }

    public void second(Runnable printSecond) throws InterruptedException {
        // printSecond.run() outputs "second". Do not change or remove this line.
        printSecond.run();
    }

    public void third(Runnable printThird) throws InterruptedException {
        // printThird.run() outputs "third". Do not change or remove this line.
        printThird.run();
    }
}
```

## Solution
```java
import java.util.concurrent.Semaphore;
class Foo {
    
    Semaphore s1,s2;

    public Foo() {
        s1 = new Semaphore(0);
        s2 = new Semaphore(0);
    }

    public void first(Runnable printFirst) throws InterruptedException {
        
        // printFirst.run() outputs "first". Do not change or remove this line.
        printFirst.run();
        s1.release();
    }

    public void second(Runnable printSecond) throws InterruptedException {
        s1.acquire();
        // printSecond.run() outputs "second". Do not change or remove this line.
        printSecond.run();
        s2.release();
    }

    public void third(Runnable printThird) throws InterruptedException {
        s2.acquire();
        // printThird.run() outputs "third". Do not change or remove this line.
        printThird.run();
    }
}
```