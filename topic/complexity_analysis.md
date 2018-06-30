Complexity Analysis
======

## Case #1

- time: `O(N)`
- REF: https://en.wikipedia.org/wiki/1/2_%2B_1/4_%2B_1/8_%2B_1/16_%2B_%E2%8B%AF

`N/2 + N/4 + N/8 + ... = N`

```java
int count = 0;
for (int i = N; i > 0; i /= 2) {
  for (int j = 0; j < i; j++) {
    count += 1;
  }
}
```

## Case #2

If X will always be a better choice for **large inputs**,
then we say that **an algorithm X is asymptotically more efficient than Y**.
